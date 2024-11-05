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

from openapi_client.models.currency_dto import CurrencyDto

class TestCurrencyDto(unittest.TestCase):
    """CurrencyDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrencyDto:
        """Test CurrencyDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CurrencyDto`
        """
        model = CurrencyDto()
        if include_optional:
            return CurrencyDto(
                id = '',
                code = '',
                name = '',
                symbol = '',
                country = openapi_client.models.country_dto.CountryDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    iso3 = '', 
                    iso2 = '', 
                    name = '', 
                    native_name = '', 
                    flag_url = '', )
            )
        else:
            return CurrencyDto(
        )
        """

    def testCurrencyDto(self):
        """Test CurrencyDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
