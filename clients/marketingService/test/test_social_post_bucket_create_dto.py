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

from openapi_client.models.social_post_bucket_create_dto import SocialPostBucketCreateDto

class TestSocialPostBucketCreateDto(unittest.TestCase):
    """SocialPostBucketCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SocialPostBucketCreateDto:
        """Test SocialPostBucketCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SocialPostBucketCreateDto`
        """
        model = SocialPostBucketCreateDto()
        if include_optional:
            return SocialPostBucketCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                tenant_id = '',
                enrolment_id = ''
            )
        else:
            return SocialPostBucketCreateDto(
        )
        """

    def testSocialPostBucketCreateDto(self):
        """Test SocialPostBucketCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
