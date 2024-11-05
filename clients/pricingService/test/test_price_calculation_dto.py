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

from openapi_client.models.price_calculation_dto import PriceCalculationDto

class TestPriceCalculationDto(unittest.TestCase):
    """PriceCalculationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceCalculationDto:
        """Test PriceCalculationDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceCalculationDto`
        """
        model = PriceCalculationDto()
        if include_optional:
            return PriceCalculationDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                item_id = '',
                unit_id = '',
                unit_group_id = '',
                price_id = '',
                price_list_id = '',
                discount_id = '',
                discount_list_id = '',
                tenant_id = '',
                enrollment_id = '',
                rounding_policy_id = '',
                effective_discount_percent = 1.337,
                currency_id = '',
                total_base_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_discounts_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_surcharges_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_shipping_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_shipping_tax_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_tax_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), )
            )
        else:
            return PriceCalculationDto(
        )
        """

    def testPriceCalculationDto(self):
        """Test PriceCalculationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()