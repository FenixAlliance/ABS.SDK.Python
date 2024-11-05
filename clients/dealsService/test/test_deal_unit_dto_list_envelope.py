# coding: utf-8

"""
    DealsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deal_unit_dto_list_envelope import DealUnitDtoListEnvelope

class TestDealUnitDtoListEnvelope(unittest.TestCase):
    """DealUnitDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealUnitDtoListEnvelope:
        """Test DealUnitDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealUnitDtoListEnvelope`
        """
        model = DealUnitDtoListEnvelope()
        if include_optional:
            return DealUnitDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.deal_unit_dto.DealUnitDto(
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
                            amount = 1.337, ), 
                        total_tax_amount_in_usd = openapi_client.models.money.Money(
                            amount = 1.337, ), 
                        total_tax_base_amount_in_usd = , 
                        total_discounts_amount_in_usd = , 
                        total_surcharges_amount_in_usd = , 
                        total_global_discounts_amount_in_usd = , 
                        total_global_surcharges_amount_in_usd = , 
                        total_amount = , 
                        total_tax_amount = , 
                        total_tax_base_amount = , 
                        total_discounts_amount = , 
                        total_surcharges_amount = , 
                        total_global_discounts_amount = , 
                        total_global_surcharges_amount = , 
                        ordered = True, 
                        deal_unit_feed_id = '', 
                        deal_unit_flow_id = '', 
                        deal_unit_flow_stage_id = '', 
                        billing_location_id = '', 
                        shipping_location_id = '', 
                        partner_created = True, 
                        partner_collaboration = True, 
                        proposed_solution = '', 
                        current_situation = '', 
                        customer_need = '', 
                        won_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        lost_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        delivered_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expected_close_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deal_unit_status = 0, 
                        deal_unit_purchase_process = 0, 
                        deal_unit_forecast_category = 0, 
                        deal_unit_amounts_calculation = 0, 
                        lines_count = 56, 
                        custom_total_amount = 1.337, 
                        custom_detail_amount = 1.337, 
                        custom_profit_amount = 1.337, 
                        custom_shipping_cost_amount = 1.337, 
                        custom_withholding_tax_amount = 1.337, 
                        custom_surcharges_amount = 1.337, 
                        custom_discounts_amount = 1.337, 
                        custom_shipping_tax_amount = 1.337, )
                    ]
            )
        else:
            return DealUnitDtoListEnvelope(
        )
        """

    def testDealUnitDtoListEnvelope(self):
        """Test DealUnitDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
