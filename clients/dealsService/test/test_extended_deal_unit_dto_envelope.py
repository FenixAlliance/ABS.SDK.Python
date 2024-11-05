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

from openapi_client.models.extended_deal_unit_dto_envelope import ExtendedDealUnitDtoEnvelope

class TestExtendedDealUnitDtoEnvelope(unittest.TestCase):
    """ExtendedDealUnitDtoEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtendedDealUnitDtoEnvelope:
        """Test ExtendedDealUnitDtoEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendedDealUnitDtoEnvelope`
        """
        model = ExtendedDealUnitDtoEnvelope()
        if include_optional:
            return ExtendedDealUnitDtoEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = openapi_client.models.extended_deal_unit_dto.ExtendedDealUnitDto(
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
                    custom_shipping_tax_amount = 1.337, 
                    user = openapi_client.models.user_dto.UserDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        full_name = '', 
                        qualified_name = '', 
                        public_name = '', 
                        last_name = '', 
                        first_name = '', 
                        cover_url = '', 
                        avatar_url = '', 
                        git_hub_url = '', 
                        country_id = '', 
                        timezone_id = '', 
                        website_url = '', 
                        twitter_url = '', 
                        you_tube_url = '', 
                        linked_in_url = '', 
                        facebook_url = '', 
                        instagram_url = '', 
                        social_profile_id = '', 
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id_provider = '', 
                        language_id = '', 
                        gender = 0, 
                        city_id = '', 
                        state_id = '', 
                        email = '', 
                        about = '', 
                        job_title = '', 
                        social_feed_id = '', 
                        current_tenant_id = '', 
                        current_enrollment_id = '', 
                        status = '', 
                        cart_id = '', 
                        wallet_id = '', 
                        user_name = '', 
                        currency_id = '', 
                        phone_number = '', 
                        public_identifier = '', 
                        identity_provider = '', 
                        phone_number_confirmed = True, 
                        email_confirmed = True, 
                        availability = 0, 
                        lockout_enabled = True, 
                        lockout_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        enrollments_count = 56, 
                        site_theme = 0, ), 
                    tenant = openapi_client.models.tenant_dto.TenantDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        qualified_name = '', 
                        tax_id = '', 
                        about = '', 
                        wallet_id = '', 
                        social_feed_id = '', 
                        business_industry_id = '', 
                        business_segment_id = '', 
                        social_profile_id = '', 
                        language_id = '', 
                        name = '', 
                        duns = '', 
                        slogan = '', 
                        legal_name = '', 
                        cover_url = '', 
                        avatar_url = '', 
                        cart_id = '', 
                        currency_id = '', 
                        timezone_id = '', 
                        country_id = '', 
                        state_id = '', 
                        city_id = '', 
                        email = '', 
                        phone = '', 
                        web_url = '', 
                        facebook_url = '', 
                        twitter_url = '', 
                        git_hub_url = '', 
                        linked_in_url = '', 
                        instagram_url = '', 
                        you_tube_url = '', 
                        whats_app_number = '', 
                        support_phone_number = '', 
                        verified = True, 
                        business_name = '', 
                        business_legal_name = '', 
                        twitter_username = '', ), 
                    individual = openapi_client.models.contact_dto.ContactDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        qualified_name = '', 
                        tenant_id = '', 
                        type = 0, 
                        public_name = '', 
                        first_name = '', 
                        last_name = '', 
                        job_title = '', 
                        cover_url = '', 
                        avatar_url = '', 
                        country_id = '', 
                        timezone_id = '', 
                        language_id = '', 
                        social_profile_id = '', 
                        web_url = '', 
                        git_hub_url = '', 
                        twitch_url = '', 
                        reddit_url = '', 
                        tik_tok_url = '', 
                        website_url = '', 
                        twitter_url = '', 
                        facebook_url = '', 
                        you_tube_url = '', 
                        linked_in_url = '', 
                        instagram_url = '', 
                        github_username = '', 
                        duns = '', 
                        tax_id = '', 
                        email = '', 
                        about = '', 
                        street = '', 
                        cart_id = '', 
                        city_id = '', 
                        zip_code = '', 
                        state_id = '', 
                        wallet_id = '', 
                        fax_number = '', 
                        postal_code = '', 
                        currency_id = '', 
                        street_line1 = '', 
                        street_line2 = '', 
                        territory_id = '', 
                        mobile_phone = '', 
                        enrollment_id = '', 
                        annual_revenue = '', 
                        related_user_id = '', 
                        business_phone = '', 
                        owner_contact_id = '', 
                        related_tenant_id = '', 
                        activity_feed_id = '', 
                        parent_contact_id = '', 
                        identity_provider = '', 
                        partner_profile_id = '', 
                        primary_contact_id = '', 
                        active_directory_id = '', 
                        identity_provider_access_token = '', 
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    organization = openapi_client.models.contact_dto.ContactDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        qualified_name = '', 
                        tenant_id = '', 
                        type = 0, 
                        public_name = '', 
                        first_name = '', 
                        last_name = '', 
                        job_title = '', 
                        cover_url = '', 
                        avatar_url = '', 
                        country_id = '', 
                        timezone_id = '', 
                        language_id = '', 
                        social_profile_id = '', 
                        web_url = '', 
                        git_hub_url = '', 
                        twitch_url = '', 
                        reddit_url = '', 
                        tik_tok_url = '', 
                        website_url = '', 
                        twitter_url = '', 
                        facebook_url = '', 
                        you_tube_url = '', 
                        linked_in_url = '', 
                        instagram_url = '', 
                        github_username = '', 
                        duns = '', 
                        tax_id = '', 
                        email = '', 
                        about = '', 
                        street = '', 
                        cart_id = '', 
                        city_id = '', 
                        zip_code = '', 
                        state_id = '', 
                        wallet_id = '', 
                        fax_number = '', 
                        postal_code = '', 
                        currency_id = '', 
                        street_line1 = '', 
                        street_line2 = '', 
                        territory_id = '', 
                        mobile_phone = '', 
                        enrollment_id = '', 
                        annual_revenue = '', 
                        related_user_id = '', 
                        business_phone = '', 
                        owner_contact_id = '', 
                        related_tenant_id = '', 
                        activity_feed_id = '', 
                        parent_contact_id = '', 
                        identity_provider = '', 
                        partner_profile_id = '', 
                        primary_contact_id = '', 
                        active_directory_id = '', 
                        identity_provider_access_token = '', 
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    receiver_tenant = openapi_client.models.tenant_dto.TenantDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        qualified_name = '', 
                        tax_id = '', 
                        about = '', 
                        wallet_id = '', 
                        social_feed_id = '', 
                        business_industry_id = '', 
                        business_segment_id = '', 
                        social_profile_id = '', 
                        language_id = '', 
                        name = '', 
                        duns = '', 
                        slogan = '', 
                        legal_name = '', 
                        cover_url = '', 
                        avatar_url = '', 
                        cart_id = '', 
                        currency_id = '', 
                        timezone_id = '', 
                        country_id = '', 
                        state_id = '', 
                        city_id = '', 
                        email = '', 
                        phone = '', 
                        web_url = '', 
                        facebook_url = '', 
                        twitter_url = '', 
                        git_hub_url = '', 
                        linked_in_url = '', 
                        instagram_url = '', 
                        you_tube_url = '', 
                        whats_app_number = '', 
                        support_phone_number = '', 
                        verified = True, 
                        business_name = '', 
                        business_legal_name = '', 
                        twitter_username = '', ), 
                    enrollment = openapi_client.models.tenant_enrolment_dto.TenantEnrolmentDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tenant_id = '', 
                        user_id = '', 
                        is_root = True, 
                        is_owner = True, 
                        is_admin = True, 
                        is_disabled = True, ), )
            )
        else:
            return ExtendedDealUnitDtoEnvelope(
        )
        """

    def testExtendedDealUnitDtoEnvelope(self):
        """Test ExtendedDealUnitDtoEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()