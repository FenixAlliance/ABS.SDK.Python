# coding: utf-8

"""
    PricingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.discount_list_update_dto import DiscountListUpdateDto

class TestDiscountListUpdateDto(unittest.TestCase):
    """DiscountListUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscountListUpdateDto:
        """Test DiscountListUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscountListUpdateDto`
        """
        model = DiscountListUpdateDto()
        if include_optional:
            return DiscountListUpdateDto(
                name = '',
                currency_id = '',
                tenant_id = '',
                enrolment_id = ''
            )
        else:
            return DiscountListUpdateDto(
        )
        """

    def testDiscountListUpdateDto(self):
        """Test DiscountListUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()