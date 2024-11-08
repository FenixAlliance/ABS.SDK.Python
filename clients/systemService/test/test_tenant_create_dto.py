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

from openapi_client.models.tenant_create_dto import TenantCreateDto

class TestTenantCreateDto(unittest.TestCase):
    """TenantCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantCreateDto:
        """Test TenantCreateDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantCreateDto`
        """
        model = TenantCreateDto()
        if include_optional:
            return TenantCreateDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                duns = '',
                name = '',
                legal_name = '',
                email = '',
                phone = '',
                web_url = '',
                about = '',
                handler = '',
                currency_id = '',
                language_id = '',
                timezone_id = '',
                city_id = '',
                state_id = '',
                country_id = '',
                tax_id = '',
                avatar_url = ''
            )
        else:
            return TenantCreateDto(
        )
        """

    def testTenantCreateDto(self):
        """Test TenantCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
