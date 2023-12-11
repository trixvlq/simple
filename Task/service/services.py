import stripe
from currency_converter import CurrencyConverter
from decouple import config


stripe.api_key = config('api_key')


def create_item_session(item, quantity=1, prefered_payment="USD"):
    products = stripe.Product.list()

    item = [i for i in products.auto_paging_iter() if i.name == item.name][0]

    c = CurrencyConverter()

    price = stripe.Price.retrieve(item['default_price'])

    converted_price = c.convert(price.unit_amount / 100, price.currency.upper(), prefered_payment)

    new_payment = stripe.Price.create(
        currency=prefered_payment,
        unit_amount=int(converted_price * 100),
        product=item['id']
    )

    line_items = [
        {'price': new_payment,
         'quantity': 1
         }
    ]

    result = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode="payment",
        success_url="http://127.0.0.1:8000/",
        cancel_url="http://127.0.0.1:8000/"
    )
    result.success_url = result.url
    return result


def create_items_session(items, prefered_payment, coupon):
    products = stripe.Product.list()
    coupons = stripe.Coupon.list()

    order_coupon = None

    bag = []

    for item in items:
        product = [i for i in products.auto_paging_iter() if i.name == item.item.name]
        line = [product, item.quantity]
        bag.append(line)

    for coup in coupons:
        order_coupon = [i for i in coupons.auto_paging_iter() if coupon == i.name]

    line_items = []

    c = CurrencyConverter()

    for item in bag:
        price = stripe.Price.retrieve(item[0][0]['default_price'])

        converted_price = c.convert(price.unit_amount / 100, price.currency.upper(), prefered_payment)

        new_payment = stripe.Price.create(
            currency=prefered_payment,
            unit_amount=int(converted_price * 100),
            product=item[0][0]['id']
        )

        line_items.append({'price': new_payment,
                           'quantity': item[1]
                           })
    if order_coupon:
        result = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode="payment",
            line_items=line_items,
            discounts=[{"coupon": order_coupon[0].id}],
            success_url="http://127.0.0.1:8000/",
            cancel_url="http://127.0.0.1:8000/",
        )
    else:
        result = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/",
            cancel_url="http://127.0.0.1:8000/"
        )

    return result
