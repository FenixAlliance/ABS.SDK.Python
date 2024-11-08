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

from openapi_client.models.item_price_update_dto import ItemPriceUpdateDto

class TestItemPriceUpdateDto(unittest.TestCase):
    """ItemPriceUpdateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemPriceUpdateDto:
        """Test ItemPriceUpdateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemPriceUpdateDto`
        """
        model = ItemPriceUpdateDto()
        if include_optional:
            return ItemPriceUpdateDto(
                price = 1.337,
                item_id = '',
                unit_id = '',
                percent = 1.337,
                unit_group_id = '',
                currency_id = '',
                discount_list_id = '',
                rounding_policy_id = ''
            )
        else:
            return ItemPriceUpdateDto(
        )
        """

    def testItemPriceUpdateDto(self):
        """Test ItemPriceUpdateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
