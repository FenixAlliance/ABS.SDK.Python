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

from openapi_client.models.social_profile_dto import SocialProfileDto

class TestSocialProfileDto(unittest.TestCase):
    """SocialProfileDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SocialProfileDto:
        """Test SocialProfileDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SocialProfileDto`
        """
        model = SocialProfileDto()
        if include_optional:
            return SocialProfileDto(
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
                notes = ''
            )
        else:
            return SocialProfileDto(
        )
        """

    def testSocialProfileDto(self):
        """Test SocialProfileDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
