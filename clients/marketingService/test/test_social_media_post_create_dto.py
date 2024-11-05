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

from openapi_client.models.social_media_post_create_dto import SocialMediaPostCreateDto

class TestSocialMediaPostCreateDto(unittest.TestCase):
    """SocialMediaPostCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SocialMediaPostCreateDto:
        """Test SocialMediaPostCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SocialMediaPostCreateDto`
        """
        model = SocialMediaPostCreateDto()
        if include_optional:
            return SocialMediaPostCreateDto(
                title = '',
                content = '',
                featured_image_url = '',
                tenant_id = '',
                social_post_bucket_id = '',
                enrolment_id = ''
            )
        else:
            return SocialMediaPostCreateDto(
        )
        """

    def testSocialMediaPostCreateDto(self):
        """Test SocialMediaPostCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()