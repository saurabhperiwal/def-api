import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def add_product(body):  # noqa: E501
    """Add a new product to the ecommerce store

     # noqa: E501

    :param body: Product object that needs to be added to the class
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
