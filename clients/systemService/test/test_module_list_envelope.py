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

from openapi_client.models.module_list_envelope import ModuleListEnvelope

class TestModuleListEnvelope(unittest.TestCase):
    """ModuleListEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleListEnvelope:
        """Test ModuleListEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleListEnvelope`
        """
        model = ModuleListEnvelope()
        if include_optional:
            return ModuleListEnvelope(
                is_success = True,
                error_message = '',
                correlation_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                activity_id = '',
                result = [
                    openapi_client.models.module.Module(
                        enable = True, 
                        active = True, 
                        order = 56, 
                        id = '', 
                        name = '', 
                        full_name = '', 
                        description = '', 
                        type = 0, 
                        configuration = '', 
                        author = '', 
                        author_url = '', 
                        license = '', 
                        require_license_acceptance = True, 
                        repository = '', 
                        path = '', 
                        icon = '', 
                        image = '', 
                        nu_spec_path = '', 
                        manifest = '', 
                        documentation = '', 
                        website = '', 
                        logo = '', 
                        swagger_spec = openapi_client.models.i_swagger_spec.ISwaggerSpec(
                            enable = True, 
                            name = '', 
                            title = '', 
                            version = '', 
                            description = '', 
                            terms_of_service = '', 
                            swagger_endpoint = openapi_client.models.i_swagger_endpoint.ISwaggerEndpoint(
                                enable = True, 
                                name = '', 
                                url = '', ), 
                            open_api_contact = openapi_client.models.i_swagger_contact.ISwaggerContact(
                                name = '', 
                                email = '', 
                                url = '', ), 
                            license = openapi_client.models.i_swagger_license.ISwaggerLicense(
                                name = '', 
                                url = '', ), ), 
                        swagger_specs = [
                            openapi_client.models.i_swagger_spec.ISwaggerSpec(
                                enable = True, 
                                name = '', 
                                title = '', 
                                version = '', 
                                description = '', 
                                terms_of_service = '', )
                            ], 
                        url = '', 
                        assembly_paths = [
                            ''
                            ], 
                        marked_for_deletion = True, 
                        version = '', )
                    ]
            )
        else:
            return ModuleListEnvelope(
        )
        """

    def testModuleListEnvelope(self):
        """Test ModuleListEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()