# coding: utf-8

"""
    MarketingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.email_signature_dto import EmailSignatureDto

class TestEmailSignatureDto(unittest.TestCase):
    """EmailSignatureDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailSignatureDto:
        """Test EmailSignatureDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailSignatureDto`
        """
        model = EmailSignatureDto()
        if include_optional:
            return EmailSignatureDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order = 56,
                slug = '',
                name = '',
                title = '',
                excerpt = '',
                password = '',
                description = '',
                highlight_image = '',
                canonical_url = '',
                seo_title = '',
                seo_key_words = '',
                seo_key_phrases = '',
                meta_description = '',
                twitter_image = '',
                twitter_title = '',
                twitter_description = '',
                facebook_image = '',
                facebook_title = '',
                facebook_description = '',
                featured_image_url = '',
                content = '',
                code = '',
                namespace = '',
                type_name = '',
                generated_code = '',
                compilation_path = '',
                html_content = '',
                c_sharp_content = '',
                razor_content = '',
                css_content = '',
                js_content = '',
                css_files = '',
                js_files = '',
                razor_generated_code = '',
                c_sharp_generated_code = '',
                template = True,
                default = True,
                enable = True,
                enable_comments = True,
                display_social_box = True,
                published = True,
                in_trash_can = True,
                system_locked = True,
                allow_ping_backs = True,
                allow_trackbacks = True,
                cornerstone_content = True,
                is_essential_content = True,
                allow_search_engine_indexing = True,
                tenant_id = '',
                web_portal_id = '',
                website_theme_id = '',
                enrollment_id = '',
                social_profile_id = '',
                parent_web_content_id = '',
                parent_web_content_version_id = ''
            )
        else:
            return EmailSignatureDto(
        )
        """

    def testEmailSignatureDto(self):
        """Test EmailSignatureDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
