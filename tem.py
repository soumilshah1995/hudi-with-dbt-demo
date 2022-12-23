try:
    import os
    import logging
    import uuid
    from datetime import datetime, timezone
    from random import randint
    import datetime
    from faker import Faker
    import random

except Exception as e:
    raise Exception("Error: {} ".format(e))


def generate_data():
    states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN",
              "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA",
              "WA", "WV", "WI", "WY")
    shipping_types = ("Free", "3-Day", "2-Day")

    product_categories = ("Garden", "Kitchen", "Office", "Household")
    referrals = ("Other", "Friend/Colleague", "Repeat Customer", "Online Ad")

    data_array = []

    for i in range(0, 1000):
        item_id = random.randint(1, 100)
        state = states[random.randint(0, len(states) - 1)]
        shipping_type = shipping_types[random.randint(0, len(shipping_types) - 1)]
        product_category = product_categories[random.randint(0, len(product_categories) - 1)]
        quantity = random.randint(1, 4)
        referral = referrals[random.randint(0, len(referrals) - 1)]
        price = random.randint(1, 100)
        order_date = datetime.date(2016, random.randint(1, 12), random.randint(1, 28)).isoformat()
        invoiceid = random.randint(1, 20000)
        data_order = (invoiceid, item_id, product_category, price, quantity, order_date, state, shipping_type, referral)

        data_array.append(
            data_order
        )
    columns = ["invoiceid", "itemid", "category", "price", "quantity", "orderdate", "destinationstate",
                   "shippingtype", "referral"]

    return data_array, columns


data_array, columns = generate_data()

