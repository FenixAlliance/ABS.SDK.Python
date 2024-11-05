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

from openapi_client.models.item_price_dto import ItemPriceDto

class TestItemPriceDto(unittest.TestCase):
    """ItemPriceDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemPriceDto:
        """Test ItemPriceDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemPriceDto`
        """
        model = ItemPriceDto()
        if include_optional:
            return ItemPriceDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                item_id = '',
                unit_id = '',
                currency_id = '',
                discount_id = '',
                unit_group_id = '',
                price_list_id = '',
                discount_list_id = '',
                rounding_policy_id = '',
                enrollment_id = '',
                tenant_id = '',
                price = 1.337,
                percent = 1.337
            )
        else:
            return ItemPriceDto(
        )
        """

    def testItemPriceDto(self):
        """Test ItemPriceDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
