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

from openapi_client.models.country_dto import CountryDto

class TestCountryDto(unittest.TestCase):
    """CountryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CountryDto:
        """Test CountryDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CountryDto`
        """
        model = CountryDto()
        if include_optional:
            return CountryDto(
                id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                iso3 = '',
                iso2 = '',
                name = '',
                native_name = '',
                flag_url = ''
            )
        else:
            return CountryDto(
        )
        """

    def testCountryDto(self):
        """Test CountryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
