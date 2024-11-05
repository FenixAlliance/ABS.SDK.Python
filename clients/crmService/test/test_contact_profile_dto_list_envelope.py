# coding: utf-8

"""
    CrmService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.contact_profile_dto_list_envelope import ContactProfileDtoListEnvelope

class TestContactProfileDtoListEnvelope(unittest.TestCase):
    """ContactProfileDtoListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactProfileDtoListEnvelope:
        """Test ContactProfileDtoListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactProfileDtoListEnvelope`
        """
        model = ContactProfileDtoListEnvelope()
        if include_optional:
            return ContactProfileDtoListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.contact_profile_dto.ContactProfileDto(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tenant_id = '', 
                        contact_id = '', 
                        enrollment_id = '', 
                        about = '', 
                        verified = True, 
                        submitted = True, 
                        avatar_url = '', 
                        qualified_name = '', 
                        verification_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data = '', 
                        data_label = '', 
                        data1 = '', 
                        data1_label = '', 
                        data2 = '', 
                        data2_label = '', 
                        data3 = '', 
                        data3_label = '', 
                        data4 = '', 
                        data4_label = '', 
                        data5 = '', 
                        data5_label = '', 
                        data6 = '', 
                        data6_label = '', 
                        data7 = '', 
                        data7_label = '', 
                        data8 = '', 
                        data8_label = '', 
                        data9 = '', 
                        data9_label = '', )
                    ]
            )
        else:
            return ContactProfileDtoListEnvelope(
        )
        """

    def testContactProfileDtoListEnvelope(self):
        """Test ContactProfileDtoListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()