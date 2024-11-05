# coding: utf-8

"""
    SystemService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.extended_user_dto import ExtendedUserDto

class TestExtendedUserDto(unittest.TestCase):
    """ExtendedUserDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtendedUserDto:
        """Test ExtendedUserDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendedUserDto`
        """
        model = ExtendedUserDto()
        if include_optional:
            return ExtendedUserDto(
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
                site_theme = 0,
                cart = openapi_client.models.cart_dto.CartDto(
                    id = '', 
                    ip = '', 
                    type = '', 
                    total = 1.337, 
                    taxes = 1.337, 
                    freight = 1.337, 
                    sub_total = 1.337, 
                    currency_id = '', 
                    country_id = '', 
                    item_cart_records_count = 56, 
                    item_to_compare_records_count = 56, ),
                wallet = openapi_client.models.wallet_dto.WalletDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    balance = 1.337, 
                    crypto_balance = 1.337, 
                    test_mode = True, 
                    verified = True, 
                    type = '', 
                    currency_id = '', 
                    forex_rate = 1.337, 
                    balance_in_usd = 1.337, 
                    main_net_ether_balance = 1.337, 
                    ethereum_address = '', 
                    ethereum_public_key = '', 
                    ethereum_private_key = '', 
                    rolling_reserve_percent = 1.337, ),
                social_profile = openapi_client.models.social_profile_dto.SocialProfileDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    about = '', 
                    cover = '', 
                    avatar = '', 
                    country_id = '', 
                    country_name = '', 
                    identity_id = '', 
                    follows_count = 56, 
                    messages_count = 56, 
                    followers_count = 56, 
                    notifications_count = 56, 
                    unread_notifications_count = 56, 
                    unread_messages_count = 56, 
                    type = 0, 
                    social_feed_id = '', 
                    twitter_url = '', 
                    facebook_url = '', 
                    linked_in_url = '', 
                    youtube_url = '', 
                    github_url = '', 
                    pinterest_url = '', 
                    dribble_url = '', 
                    domain = '', 
                    notes = '', ),
                settings = openapi_client.models.user_settings_dto.UserSettingsDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    page_size = 56, 
                    date_format = '', 
                    currency_format = '', 
                    date_time_format = '', 
                    site_theme = 0, )
            )
        else:
            return ExtendedUserDto(
        )
        """

    def testExtendedUserDto(self):
        """Test ExtendedUserDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
