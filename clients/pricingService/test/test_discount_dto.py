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

from openapi_client.models.discount_dto import DiscountDto

class TestDiscountDto(unittest.TestCase):
    """DiscountDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscountDto:
        """Test DiscountDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscountDto`
        """
        model = DiscountDto()
        if include_optional:
            return DiscountDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                value = 1.337,
                percent = 1.337,
                item_id = '',
                tenant_id = '',
                enrolment_id = '',
                discount_list_id = '',
                end_quantity = 1.337,
                begin_quantity = 1.337
            )
        else:
            return DiscountDto(
        )
        """

    def testDiscountDto(self):
        """Test DiscountDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
