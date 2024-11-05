# coding: utf-8

"""
    WalletsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.location_dto_list_envelope import LocationDtoListEnvelope

class TestLocationDtoListEnvelope(unittest.TestCase):
    """LocationDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocationDtoListEnvelope:
        """Test LocationDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationDtoListEnvelope`
        """
        model = LocationDtoListEnvelope()
        if include_optional:
            return LocationDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.location_dto.LocationDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        title = '', 
                        business = '', 
                        email = '', 
                        phone = '', 
                        fax = '', 
                        address1 = '', 
                        address2 = '', 
                        address3 = '', 
                        unit = '', 
                        city_id = '', 
                        state_id = '', 
                        postal_code = '', 
                        country_id = '', 
                        longitude = 1.337, 
                        latitude = 1.337, 
                        is_routable = True, 
                        is_global_primary = True, 
                        is_country_primary = True, 
                        can_generate_labels = True, 
                        is_default_sender_address = True, 
                        is_default_return_address = True, 
                        is_default_supping_location = True, )
                    ]
            )
        else:
            return LocationDtoListEnvelope(
        )
        """

    def testLocationDtoListEnvelope(self):
        """Test LocationDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()