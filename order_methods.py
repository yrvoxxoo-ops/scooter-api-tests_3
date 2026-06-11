import requests

from configuration import URL_SERVICE


class OrderMethods:

    @staticmethod
    def create_order(payload):
        return requests.post(f"{URL_SERVICE}/api/v1/orders", json=payload)

    @staticmethod
    def get_orders():
        return requests.get(f"{URL_SERVICE}/api/v1/orders")