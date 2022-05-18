# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add a new product to the ecommerce store
        """
        body = Product()
        response = self.client.open(
            '/v1/products',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
