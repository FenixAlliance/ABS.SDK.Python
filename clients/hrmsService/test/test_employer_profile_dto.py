# coding: utf-8

"""
    HrmsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.employer_profile_dto import EmployerProfileDto

class TestEmployerProfileDto(unittest.TestCase):
    """EmployerProfileDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployerProfileDto:
        """Test EmployerProfileDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmployerProfileDto`
        """
        model = EmployerProfileDto()
        if include_optional:
            return EmployerProfileDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return EmployerProfileDto(
        )
        """

    def testEmployerProfileDto(self):
        """Test EmployerProfileDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
