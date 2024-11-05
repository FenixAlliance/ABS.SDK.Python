# coding: utf-8

"""
    StorageService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope

class TestFileUploadDtoEnvelope(unittest.TestCase):
    """FileUploadDtoEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileUploadDtoEnvelope:
        """Test FileUploadDtoEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileUploadDtoEnvelope`
        """
        model = FileUploadDtoEnvelope()
        if include_optional:
            return FileUploadDtoEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = openapi_client.models.file_upload_dto.FileUploadDto(
                    id = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    notes = '', 
                    title = '', 
                    author = '', 
                    is_folder = True, 
                    hash = '', 
                    file_url = '', 
                    file_path = '', 
                    file_name = '', 
                    abstract = '', 
                    key_words = '', 
                    metadata = '', 
                    file_length = 56, 
                    content_type = '', 
                    parent_file_id = '', 
                    valid_response = True, 
                    user_id = '', 
                    tenant_id = '', 
                    enrollment_id = '', 
                    social_profile_id = '', 
                    folder_path = '', )
            )
        else:
            return FileUploadDtoEnvelope(
        )
        """

    def testFileUploadDtoEnvelope(self):
        """Test FileUploadDtoEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()