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

from openapi_client.models.quote_create_dto import QuoteCreateDto

class TestQuoteCreateDto(unittest.TestCase):
    """QuoteCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteCreateDto:
        """Test QuoteCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteCreateDto`
        """
        model = QuoteCreateDto()
        if include_optional:
            return QuoteCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed = True,
                title = '',
                user_id = '',
                tenant_id = '',
                price_list_id = '',
                description = '',
                enrollment_id = '',
                individual_id = '',
                payment_term_id = '',
                organization_id = '',
                currency_id = '',
                forex_rate = 1.337,
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
                cart_id = '',
                deal_unit_id = '',
                receiver_tenant_id = '',
                effective_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                effective_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                quote_status = 0
            )
        else:
            return QuoteCreateDto(
        )
        """

    def testQuoteCreateDto(self):
        """Test QuoteCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()