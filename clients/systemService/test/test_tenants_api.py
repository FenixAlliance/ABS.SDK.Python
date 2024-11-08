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

from openapi_client.api.tenants_api import TenantsApi


class TestTenantsApi(unittest.TestCase):
    """TenantsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantsApi()

    def tearDown(self) -> None:
        pass

    def test_create_tenant(self) -> None:
        """Test case for create_tenant

        Create a new tenant.
        """
        pass

    def test_delete_tenant(self) -> None:
        """Test case for delete_tenant

        Delete a specific tenant by ID.
        """
        pass

    def test_get_all_extended_tenants(self) -> None:
        """Test case for get_all_extended_tenants

        Get all extended tenants available on this suite server instance.
        """
        pass

    def test_get_all_tenants(self) -> None:
        """Test case for get_all_tenants

        Get all tenants available on this suite server instance.
        """
        pass

    def test_get_extended_tenants_count(self) -> None:
        """Test case for get_extended_tenants_count

        Get the total count of extended tenants available on this suite server instance.
        """
        pass

    def test_get_tenant(self) -> None:
        """Test case for get_tenant

        Get a specific tenant by ID.
        """
        pass

    def test_get_tenants_count(self) -> None:
        """Test case for get_tenants_count

        Get the total count of tenants available on this suite server instance.
        """
        pass

    def test_update_tenant(self) -> None:
        """Test case for update_tenant

        Update a specific tenant by ID.
        """
        pass


if __name__ == '__main__':
    unittest.main()
