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

from openapi_client.models.suite_license_dto import SuiteLicenseDto

class TestSuiteLicenseDto(unittest.TestCase):
    """SuiteLicenseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SuiteLicenseDto:
        """Test SuiteLicenseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SuiteLicenseDto`
        """
        model = SuiteLicenseDto()
        if include_optional:
            return SuiteLicenseDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tenant_id = '',
                license_string = '',
                enrollment_id = '',
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                available_seats = 56,
                total_seats = 56
            )
        else:
            return SuiteLicenseDto(
        )
        """

    def testSuiteLicenseDto(self):
        """Test SuiteLicenseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
