# coding: utf-8

"""
    SecurityService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.security_permission_create_dto import SecurityPermissionCreateDto

class TestSecurityPermissionCreateDto(unittest.TestCase):
    """SecurityPermissionCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityPermissionCreateDto:
        """Test SecurityPermissionCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityPermissionCreateDto`
        """
        model = SecurityPermissionCreateDto()
        if include_optional:
            return SecurityPermissionCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
                tenant_id = '0',
                description = ''
            )
        else:
            return SecurityPermissionCreateDto(
                name = '0',
                tenant_id = '0',
        )
        """

    def testSecurityPermissionCreateDto(self):
        """Test SecurityPermissionCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
