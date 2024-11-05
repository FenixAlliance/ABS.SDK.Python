# coding: utf-8

"""
    QuotesService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.quote_dto import QuoteDto

class TestQuoteDto(unittest.TestCase):
    """QuoteDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDto:
        """Test QuoteDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDto`
        """
        model = QuoteDto()
        if include_optional:
            return QuoteDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed = True,
                type = '',
                title = '',
                user_id = '',
                tenant_id = '',
                currency_id = '',
                description = '',
                price_list_id = '',
                enrollment_id = '',
                individual_id = '',
                organization_id = '',
                receiver_tenant_id = '',
                first_name = '',
                last_name = '',
                company_name = '',
                billing_email = '',
                address_line1 = '',
                address_line2 = '',
                postal_code = '',
                country_id = '',
                state_id = '',
                city_id = '',
                customer_notes = '',
                forex_rate = 1.337,
                total = 1.337,
                total_taxes = 1.337,
                total_tax_base = 1.337,
                total_discounts = 1.337,
                total_surcharges = 1.337,
                total_global_discounts = 1.337,
                total_global_surcharges = 1.337,
                total_taxes_in_usd = 1.337,
                total_amount_in_usd = 1.337,
                total_profit_in_usd = 1.337,
                total_tax_base_in_usd = 1.337,
                total_discounts_in_usd = 1.337,
                total_surcharges_in_usd = 1.337,
                total_detail_amount_in_usd = 1.337,
                total_global_discounts_in_usd = 1.337,
                total_global_surcharges_in_usd = 1.337,
                total_withholding_taxes_in_usd = 1.337,
                total_shipping_cost_in_usd = 1.337,
                total_shipping_taxes_in_usd = 1.337,
                currency = openapi_client.models.currency.Currency(
                    code = '', 
                    country = '', ),
                total_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_tax_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_tax_base_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_discounts_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_surcharges_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_global_discounts_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_global_surcharges_amount_in_usd = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_tax_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_tax_base_amount = openapi_client.models.money.Money(
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
                total_global_discounts_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                total_global_surcharges_amount = openapi_client.models.money.Money(
                    amount = 1.337, 
                    currency = openapi_client.models.currency.Currency(
                        code = '', 
                        country = '', ), ),
                cart_id = '',
                effective_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                effective_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                quote_status = 0,
                freight_terms = 0,
                cost_calculation_method = 0,
                custom_discounts_amount = 1.337
            )
        else:
            return QuoteDto(
        )
        """

    def testQuoteDto(self):
        """Test QuoteDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
