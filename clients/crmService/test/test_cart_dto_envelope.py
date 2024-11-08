# coding: utf-8

"""
    CrmService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cart_dto_envelope import CartDtoEnvelope

class TestCartDtoEnvelope(unittest.TestCase):
    """CartDtoEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartDtoEnvelope:
        """Test CartDtoEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartDtoEnvelope`
        """
        model = CartDtoEnvelope()
        if include_optional:
            return CartDtoEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = openapi_client.models.cart_dto.CartDto(
                    id = '', 
                    ip = '', 
                    type = '', 
                    total = 1.337, 
                    taxes = 1.337, 
                    freight = 1.337, 
                    sub_total = 1.337, 
                    currency_id = '', 
                    country_id = '', 
                    item_cart_records_count = 56, 
                    item_to_compare_records_count = 56, )
            )
        else:
            return CartDtoEnvelope(
        )
        """

    def testCartDtoEnvelope(self):
        """Test CartDtoEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
