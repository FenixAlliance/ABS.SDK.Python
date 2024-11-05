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

from openapi_client.models.country_language_dto_list_envelope import CountryLanguageDtoListEnvelope

class TestCountryLanguageDtoListEnvelope(unittest.TestCase):
    """CountryLanguageDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CountryLanguageDtoListEnvelope:
        """Test CountryLanguageDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CountryLanguageDtoListEnvelope`
        """
        model = CountryLanguageDtoListEnvelope()
        if include_optional:
            return CountryLanguageDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.country_language_dto.CountryLanguageDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        iso639_1 = '', 
                        iso639_2 = '', 
                        enabled = True, 
                        name = '', 
                        language_native_name = '', )
                    ]
            )
        else:
            return CountryLanguageDtoListEnvelope(
        )
        """

    def testCountryLanguageDtoListEnvelope(self):
        """Test CountryLanguageDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()