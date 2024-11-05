# coding: utf-8

"""
    CrmService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope

class TestContactDtoListEnvelope(unittest.TestCase):
    """ContactDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactDtoListEnvelope:
        """Test ContactDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactDtoListEnvelope`
        """
        model = ContactDtoListEnvelope()
        if include_optional:
            return ContactDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.contact_dto.ContactDto(
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
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ContactDtoListEnvelope(
        )
        """

    def testContactDtoListEnvelope(self):
        """Test ContactDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()