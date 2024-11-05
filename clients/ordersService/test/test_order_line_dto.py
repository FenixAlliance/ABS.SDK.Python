# coding: utf-8

"""
    OrdersService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.order_line_dto import OrderLineDto

class TestOrderLineDto(unittest.TestCase):
    """OrderLineDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderLineDto:
        """Test OrderLineDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderLineDto`
        """
        model = OrderLineDto()
        if include_optional:
            return OrderLineDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed = True,
                item_id = '',
                item_title = '',
                item_short_description = '',
                item_primary_image_url = '',
                shipping_policy_id = '',
                tenant_id = '',
                enrollment_id = '',
                currency_id = '',
                description = '',
                quantity = 1.337,
                free = True,
                free_reason = '',
                free_reason_code = '',
                data = '',
                data_label = '',
                data1 = '',
                data1_label = '',
                data2 = '',
                data2_label = '',
                data3 = '',
                data3_label = '',
                data4 = '',
                data4_label = '',
                data5 = '',
                data5_label = '',
                data6 = '',
                data6_label = '',
                data7 = '',
                data7_label = '',
                data8 = '',
                data8_label = '',
                data9 = '',
                data9_label = '',
                item_price_id = '',
                price_list_item_id = '',
                unit_id = '',
                unit_group_id = '',
                tax_calculation_method = 0,
                cost_calculation_method = 0,
                forex_rates_snapshot = '',
                forex_rate = 1.337,
                total_base_amount_in_usd = 1.337,
                total_profit_in_usd = 1.337,
                total_detail_amount_in_usd = 1.337,
                total_tax_base_in_usd = 1.337,
                total_discounts_in_usd = 1.337,
                total_taxes_in_usd = 1.337,
                total_withholding_taxes_in_usd = 1.337,
                total_shipping_cost_in_usd = 1.337,
                total_shipping_taxes_in_usd = 1.337,
                total_warranty_cost_in_usd = 1.337,
                total_return_cost_in_usd = 1.337,
                total_refund_cost_in_usd = 1.337,
                total_surcharges_in_usd = 1.337,
                total_amount_in_usd = 1.337,
                total_global_discounts_in_usd = 1.337,
                total_global_surcharges_in_usd = 1.337,
                custom_global_surcharges_amount = 1.337,
                custom_global_discounts_amount = 1.337,
                custom_base_amount = 1.337,
                custom_detail_amount = 1.337,
                custom_discounts_amount = 1.337,
                custom_tax_base = 1.337,
                custom_surcharges_amount = 1.337,
                custom_profit_amount = 1.337,
                custom_shipping_cost_amount = 1.337,
                custom_shipping_tax_amount = 1.337,
                custom_tax_amount = 1.337,
                custom_withholding_tax_amount = 1.337,
                custom_total_amount = 1.337,
                return_policy_id = '',
                refund_policy_id = '',
                warranty_policy_id = '',
                shipment_policy_id = '',
                shipping_location_id = '',
                location_id = '',
                quote_item_record_id = '',
                business_profile_record_id = '',
                parent_billing_item_record_id = '',
                order_id = ''
            )
        else:
            return OrderLineDto(
        )
        """

    def testOrderLineDto(self):
        """Test OrderLineDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
