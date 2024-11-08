# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.1.4089
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://fenixalliance.com.co/Support](https://fenixalliance.com.co/Support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AntiforgeryApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_instance.api_v2_system_service_antiforgery_get_and_store_tokens_get(api_version=api_version, x_api_version=x_api_version)
    except ApiException as e:
        print("Exception when calling AntiforgeryApi->api_v2_system_service_antiforgery_get_and_store_tokens_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AntiforgeryApi* | [**api_v2_system_service_antiforgery_get_and_store_tokens_get**](docs/AntiforgeryApi.md#api_v2_system_service_antiforgery_get_and_store_tokens_get) | **GET** /api/v2/SystemService/Antiforgery/GetAndStoreTokens | 
*AntiforgeryApi* | [**api_v2_system_service_antiforgery_is_request_valid_get**](docs/AntiforgeryApi.md#api_v2_system_service_antiforgery_is_request_valid_get) | **GET** /api/v2/SystemService/Antiforgery/IsRequestValid | 
*LicensesApi* | [**api_licensing_licenses_generate_post**](docs/LicensesApi.md#api_licensing_licenses_generate_post) | **POST** /api/Licensing/Licenses/Generate | 
*LicensesApi* | [**api_licensing_licenses_validate_attributes_get**](docs/LicensesApi.md#api_licensing_licenses_validate_attributes_get) | **GET** /api/Licensing/Licenses/Validate/Attributes | 
*LicensesApi* | [**api_licensing_licenses_validate_errors_get**](docs/LicensesApi.md#api_licensing_licenses_validate_errors_get) | **GET** /api/Licensing/Licenses/Validate/Errors | 
*LicensesApi* | [**api_licensing_licenses_validate_get**](docs/LicensesApi.md#api_licensing_licenses_validate_get) | **GET** /api/Licensing/Licenses/Validate | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_get) | **GET** /api/v2/SystemService/Licensing/Licenses | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_license_id_assignments_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_license_id_assignments_get) | **GET** /api/v2/SystemService/Licensing/Licenses/{licenseId}/Assignments | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_license_id_attributes_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_license_id_attributes_get) | **GET** /api/v2/SystemService/Licensing/Licenses/{licenseId}/Attributes | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_license_id_features_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_license_id_features_get) | **GET** /api/v2/SystemService/Licensing/Licenses/{licenseId}/Features | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_license_id_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_license_id_get) | **GET** /api/v2/SystemService/Licensing/Licenses/{licenseId} | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_license_id_quota_get**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_license_id_quota_get) | **GET** /api/v2/SystemService/Licensing/Licenses/{licenseId}/Quota | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_redeem_post**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_redeem_post) | **POST** /api/v2/SystemService/Licensing/Licenses/Redeem | 
*LicensingApi* | [**api_v2_system_service_licensing_licenses_validate_post**](docs/LicensingApi.md#api_v2_system_service_licensing_licenses_validate_post) | **POST** /api/v2/SystemService/Licensing/Licenses/Validate | 
*MigrationsApi* | [**api_v2_system_service_migrations_get**](docs/MigrationsApi.md#api_v2_system_service_migrations_get) | **GET** /api/v2/SystemService/Migrations | 
*MigrationsApi* | [**api_v2_system_service_migrations_migrate_post**](docs/MigrationsApi.md#api_v2_system_service_migrations_migrate_post) | **POST** /api/v2/SystemService/Migrations/Migrate | 
*ModulesApi* | [**get_all_modules**](docs/ModulesApi.md#get_all_modules) | **GET** /api/v2/StudioService/Modules | Get all modules available on this suite server instance.
*ModulesApi* | [**get_available_modules**](docs/ModulesApi.md#get_available_modules) | **GET** /api/v2/StudioService/Modules/Data | Get all modules available to a tenant user.
*TenantsApi* | [**create_tenant**](docs/TenantsApi.md#create_tenant) | **POST** /api/v2/SystemService/Tenants | Create a new tenant.
*TenantsApi* | [**delete_tenant**](docs/TenantsApi.md#delete_tenant) | **DELETE** /api/v2/SystemService/Tenants/{tenantId} | Delete a specific tenant by ID.
*TenantsApi* | [**get_all_extended_tenants**](docs/TenantsApi.md#get_all_extended_tenants) | **GET** /api/v2/SystemService/Tenants/Extended | Get all extended tenants available on this suite server instance.
*TenantsApi* | [**get_all_tenants**](docs/TenantsApi.md#get_all_tenants) | **GET** /api/v2/SystemService/Tenants | Get all tenants available on this suite server instance.
*TenantsApi* | [**get_extended_tenants_count**](docs/TenantsApi.md#get_extended_tenants_count) | **GET** /api/v2/SystemService/Tenants/Extended/Count | Get the total count of extended tenants available on this suite server instance.
*TenantsApi* | [**get_tenant**](docs/TenantsApi.md#get_tenant) | **GET** /api/v2/SystemService/Tenants/{tenantId} | Get a specific tenant by ID.
*TenantsApi* | [**get_tenants_count**](docs/TenantsApi.md#get_tenants_count) | **GET** /api/v2/SystemService/Tenants/Count | Get the total count of tenants available on this suite server instance.
*TenantsApi* | [**update_tenant**](docs/TenantsApi.md#update_tenant) | **PUT** /api/v2/SystemService/Tenants/{tenantId} | Update a specific tenant by ID.
*UsersApi* | [**api_v2_system_service_users_count_get**](docs/UsersApi.md#api_v2_system_service_users_count_get) | **GET** /api/v2/SystemService/Users/Count | 
*UsersApi* | [**api_v2_system_service_users_extended_count_get**](docs/UsersApi.md#api_v2_system_service_users_extended_count_get) | **GET** /api/v2/SystemService/Users/Extended/Count | 
*UsersApi* | [**api_v2_system_service_users_extended_get**](docs/UsersApi.md#api_v2_system_service_users_extended_get) | **GET** /api/v2/SystemService/Users/Extended | 
*UsersApi* | [**api_v2_system_service_users_get**](docs/UsersApi.md#api_v2_system_service_users_get) | **GET** /api/v2/SystemService/Users | 
*UsersApi* | [**api_v2_system_service_users_post**](docs/UsersApi.md#api_v2_system_service_users_post) | **POST** /api/v2/SystemService/Users | 
*UsersApi* | [**api_v2_system_service_users_user_id_delete**](docs/UsersApi.md#api_v2_system_service_users_user_id_delete) | **DELETE** /api/v2/SystemService/Users/{userId} | 
*UsersApi* | [**api_v2_system_service_users_user_id_extended_get**](docs/UsersApi.md#api_v2_system_service_users_user_id_extended_get) | **GET** /api/v2/SystemService/Users/{userId}/Extended | 
*UsersApi* | [**api_v2_system_service_users_user_id_put**](docs/UsersApi.md#api_v2_system_service_users_user_id_put) | **PUT** /api/v2/SystemService/Users/{userId} | 
*UsersApi* | [**get_user_async**](docs/UsersApi.md#get_user_async) | **GET** /api/v2/SystemService/Users/{userId} | 


## Documentation For Models

 - [AccountHolderCreateDto](docs/AccountHolderCreateDto.md)
 - [AdditionalAttribute](docs/AdditionalAttribute.md)
 - [BooleanEnvelope](docs/BooleanEnvelope.md)
 - [CartDto](docs/CartDto.md)
 - [EmptyEnvelope](docs/EmptyEnvelope.md)
 - [ErrorEnvelope](docs/ErrorEnvelope.md)
 - [ExtendedTenantDto](docs/ExtendedTenantDto.md)
 - [ExtendedTenantDtoListEnvelope](docs/ExtendedTenantDtoListEnvelope.md)
 - [ExtendedUserDto](docs/ExtendedUserDto.md)
 - [ExtendedUserDtoEnvelope](docs/ExtendedUserDtoEnvelope.md)
 - [ExtendedUserDtoListEnvelope](docs/ExtendedUserDtoListEnvelope.md)
 - [GeneralValidationFailure](docs/GeneralValidationFailure.md)
 - [GeneralValidationFailureListEnvelope](docs/GeneralValidationFailureListEnvelope.md)
 - [ISwaggerContact](docs/ISwaggerContact.md)
 - [ISwaggerEndpoint](docs/ISwaggerEndpoint.md)
 - [ISwaggerLicense](docs/ISwaggerLicense.md)
 - [ISwaggerSpec](docs/ISwaggerSpec.md)
 - [Int32Envelope](docs/Int32Envelope.md)
 - [LicenseAttributesListEnvelope](docs/LicenseAttributesListEnvelope.md)
 - [LicenseFeature](docs/LicenseFeature.md)
 - [LicenseKey](docs/LicenseKey.md)
 - [LicenseKeyRequest](docs/LicenseKeyRequest.md)
 - [LicenseValidationError](docs/LicenseValidationError.md)
 - [LicenseValidationErrorListEnvelope](docs/LicenseValidationErrorListEnvelope.md)
 - [LicenseValidationRequest](docs/LicenseValidationRequest.md)
 - [Module](docs/Module.md)
 - [ModuleListEnvelope](docs/ModuleListEnvelope.md)
 - [SocialProfileDto](docs/SocialProfileDto.md)
 - [StringEnvelope](docs/StringEnvelope.md)
 - [StringListEnvelope](docs/StringListEnvelope.md)
 - [StudioModule](docs/StudioModule.md)
 - [StudioModuleListEnvelope](docs/StudioModuleListEnvelope.md)
 - [SuiteLicenseAssignmentDto](docs/SuiteLicenseAssignmentDto.md)
 - [SuiteLicenseAssignmentDtoListEnvelope](docs/SuiteLicenseAssignmentDtoListEnvelope.md)
 - [SuiteLicenseDto](docs/SuiteLicenseDto.md)
 - [SuiteLicenseDtoEnvelope](docs/SuiteLicenseDtoEnvelope.md)
 - [SuiteLicenseDtoListEnvelope](docs/SuiteLicenseDtoListEnvelope.md)
 - [TenantCreateDto](docs/TenantCreateDto.md)
 - [TenantDto](docs/TenantDto.md)
 - [TenantDtoEnvelope](docs/TenantDtoEnvelope.md)
 - [TenantDtoListEnvelope](docs/TenantDtoListEnvelope.md)
 - [TenantUpdateDto](docs/TenantUpdateDto.md)
 - [UserDto](docs/UserDto.md)
 - [UserDtoEnvelope](docs/UserDtoEnvelope.md)
 - [UserDtoListEnvelope](docs/UserDtoListEnvelope.md)
 - [UserSettingsDto](docs/UserSettingsDto.md)
 - [WalletDto](docs/WalletDto.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@fenix-alliance.com


