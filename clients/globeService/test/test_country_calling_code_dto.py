# coding: utf-8

"""
    GlobeService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.country_calling_code_dto import CountryCallingCodeDto

class TestCountryCallingCodeDto(unittest.TestCase):
    """CountryCallingCodeDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CountryCallingCodeDto:
        """Test CountryCallingCodeDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CountryCallingCodeDto`
        """
        model = CountryCallingCodeDto()
        if include_optional:
            return CountryCallingCodeDto(
                id = 56,
                calling_code = '',
                country_id = ''
            )
        else:
            return CountryCallingCodeDto(
        )
        """

    def testCountryCallingCodeDto(self):
        """Test CountryCallingCodeDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()