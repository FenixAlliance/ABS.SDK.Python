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

from openapi_client.models.studio_module import StudioModule

class TestStudioModule(unittest.TestCase):
    """StudioModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudioModule:
        """Test StudioModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudioModule`
        """
        model = StudioModule()
        if include_optional:
            return StudioModule(
                name = '',
                version = ''
            )
        else:
            return StudioModule(
        )
        """

    def testStudioModule(self):
        """Test StudioModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
