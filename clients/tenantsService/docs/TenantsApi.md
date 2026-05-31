# openapi_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_license_async**](TenantsApi.md#assign_license_async) | **POST** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Licenses/{licenseId} | Assign a license to a specific enrollment
[**create_tenant_async**](TenantsApi.md#create_tenant_async) | **POST** /api/v2/TenantsService/Tenants | Create a new business tenant
[**de_select_tenant_async**](TenantsApi.md#de_select_tenant_async) | **POST** /api/v2/TenantsService/Tenants/Deselect | Deselect the user&#39;s default tenant
[**delete_tenant_async**](TenantsApi.md#delete_tenant_async) | **DELETE** /api/v2/TenantsService/Tenants | Delete a tenant
[**get_accessible_features_async**](TenantsApi.md#get_accessible_features_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Features | Get the list of features accessible to a specific enrollment
[**get_current_tenant_async**](TenantsApi.md#get_current_tenant_async) | **GET** /api/v2/TenantsService/Tenants/Current | Get the user&#39;s current default tenant
[**get_enrollment_license_by_id_async**](TenantsApi.md#get_enrollment_license_by_id_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Licenses/{licenseId} | Get a specific license for an enrollment
[**get_enrollment_licenses_async**](TenantsApi.md#get_enrollment_licenses_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Licenses | Get the list of licenses available to a specific enrollment
[**get_enrollment_permissions_async**](TenantsApi.md#get_enrollment_permissions_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Permissions | Get a specific tenant enrollment&#39;s permissions list
[**get_extended_tenant_async**](TenantsApi.md#get_extended_tenant_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Extended | Get an extended tenant&#39;s business profile
[**get_extended_tenant_enrollment_async**](TenantsApi.md#get_extended_tenant_enrollment_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Extended | Get a specific tenant enrollment
[**get_root_tenant_async**](TenantsApi.md#get_root_tenant_async) | **GET** /api/v2/TenantsService/Tenants/Root | Get the root tenant of the platform
[**get_tenant_async**](TenantsApi.md#get_tenant_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId} | Get a specific tenant by ID
[**get_tenant_avatar_async**](TenantsApi.md#get_tenant_avatar_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Avatar | Get a tenant&#39;s avatar
[**get_tenant_cart_async**](TenantsApi.md#get_tenant_cart_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Cart | Get a tenant&#39;s default cart
[**get_tenant_enrollment_async**](TenantsApi.md#get_tenant_enrollment_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId} | Get a specific tenant enrollment
[**get_tenant_enrollments_async**](TenantsApi.md#get_tenant_enrollments_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments | Get the list of user enrollments for a tenant
[**get_tenant_invitations_async**](TenantsApi.md#get_tenant_invitations_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Invitations | Get the list of invitations issued by a tenant
[**get_tenant_licenses_async**](TenantsApi.md#get_tenant_licenses_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Licenses | Get the list of licenses available to a tenant
[**get_tenant_notifications_async**](TenantsApi.md#get_tenant_notifications_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Notifications | Get the list of notifications for a tenant
[**get_tenant_notifications_count_async**](TenantsApi.md#get_tenant_notifications_count_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Notifications/Count | Get the count of notifications for a tenant
[**get_tenant_pending_invitations_async**](TenantsApi.md#get_tenant_pending_invitations_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Invitations/Pending | Get the list of invitations issued by a tenant that are pending
[**get_tenant_redeemed_invitations_async**](TenantsApi.md#get_tenant_redeemed_invitations_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Invitations/Redeemed | Get the list of invitations issued by a tenant that have been redeemed
[**get_tenant_revoked_invitations_async**](TenantsApi.md#get_tenant_revoked_invitations_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Invitations/Revoked | Get the list of invitations issued by a tenant that have been revoked
[**get_tenant_social_profile_async**](TenantsApi.md#get_tenant_social_profile_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/SocialProfile | Get a tenant&#39;s social profile
[**get_tenant_users_async**](TenantsApi.md#get_tenant_users_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Users | Get the list of users enrolled in a tenant
[**get_tenant_wallet_async**](TenantsApi.md#get_tenant_wallet_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Wallet | Get a tenant&#39;s billing profile (A.K.A. Wallet Account)
[**get_tenant_web_portals_async**](TenantsApi.md#get_tenant_web_portals_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/WebPortals | Get the list of web portals for a tenant
[**patch_tenant_async**](TenantsApi.md#patch_tenant_async) | **PATCH** /api/v2/TenantsService/Tenants/{tenantId} | Patch a tenant&#39;s profile
[**revoke_license_async**](TenantsApi.md#revoke_license_async) | **DELETE** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Licenses/{licenseId} | Revoke a license from a specific enrollment
[**select_tenant_async**](TenantsApi.md#select_tenant_async) | **POST** /api/v2/TenantsService/Tenants/{tenantId}/Select | Select a business tenant as the user&#39;s default tenant
[**update_avatar_async**](TenantsApi.md#update_avatar_async) | **POST** /api/v2/TenantsService/Tenants/{tenantId}/Avatar | Update a tenant&#39;s avatar
[**update_tenant_async**](TenantsApi.md#update_tenant_async) | **PUT** /api/v2/TenantsService/Tenants/{tenantId} | Update a tenant&#39;s profile
[**validate_enrollment_feature_access**](TenantsApi.md#validate_enrollment_feature_access) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/HasAccess | Validate the access to a specific feature for a specific enrollment
[**validate_enrollment_permissions_async**](TenantsApi.md#validate_enrollment_permissions_async) | **GET** /api/v2/TenantsService/Tenants/{tenantId}/Enrollments/{enrollmentId}/Permissions/Validate | Validate the existence of a list of roles and permissions for a specific enrollment


# **assign_license_async**
> SuiteLicenseDtoListEnvelope assign_license_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)

Assign a license to a specific enrollment

Assign a license to a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.suite_license_dto_list_envelope import SuiteLicenseDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    license_id = 'license_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a license to a specific enrollment
        api_response = api_instance.assign_license_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->assign_license_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->assign_license_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **license_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseDtoListEnvelope**](SuiteLicenseDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant_async**
> EmptyEnvelope create_tenant_async(api_version=api_version, x_api_version=x_api_version, tenant_create_dto=tenant_create_dto)

Create a new business tenant

Create a new business tenant

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_create_dto import TenantCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_create_dto = openapi_client.TenantCreateDto() # TenantCreateDto |  (optional)

    try:
        # Create a new business tenant
        api_response = api_instance.create_tenant_async(api_version=api_version, x_api_version=x_api_version, tenant_create_dto=tenant_create_dto)
        print("The response of TenantsApi->create_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_create_dto** | [**TenantCreateDto**](TenantCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **de_select_tenant_async**
> EmptyEnvelope de_select_tenant_async(api_version=api_version, x_api_version=x_api_version)

Deselect the user's default tenant

Deselect the user's default tenant

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deselect the user's default tenant
        api_response = api_instance.de_select_tenant_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->de_select_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->de_select_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_async**
> EmptyEnvelope delete_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant

Delete a business tenant

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant
        api_response = api_instance.delete_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->delete_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->delete_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accessible_features_async**
> SuiteLicenseFeatureDtoListEnvelope get_accessible_features_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get the list of features accessible to a specific enrollment

Get the list of features accessible to a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.suite_license_feature_dto_list_envelope import SuiteLicenseFeatureDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of features accessible to a specific enrollment
        api_response = api_instance.get_accessible_features_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_accessible_features_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_accessible_features_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseFeatureDtoListEnvelope**](SuiteLicenseFeatureDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_tenant_async**
> TenantDtoEnvelope get_current_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the user's current default tenant

Get the user's current default tenant

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the user's current default tenant
        api_response = api_instance.get_current_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_current_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_current_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_license_by_id_async**
> SuiteLicenseDtoListEnvelope get_enrollment_license_by_id_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)

Get a specific license for an enrollment

Get a specific license for an enrollment

### Example


```python
import openapi_client
from openapi_client.models.suite_license_dto_list_envelope import SuiteLicenseDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    license_id = 'license_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific license for an enrollment
        api_response = api_instance.get_enrollment_license_by_id_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_enrollment_license_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_enrollment_license_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **license_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseDtoListEnvelope**](SuiteLicenseDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_licenses_async**
> SuiteLicenseAssignmentDtoListEnvelope get_enrollment_licenses_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get the list of licenses available to a specific enrollment

Get the list of licenses available to a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.suite_license_assignment_dto_list_envelope import SuiteLicenseAssignmentDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of licenses available to a specific enrollment
        api_response = api_instance.get_enrollment_licenses_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_enrollment_licenses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_enrollment_licenses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseAssignmentDtoListEnvelope**](SuiteLicenseAssignmentDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_permissions_async**
> StringListEnvelope get_enrollment_permissions_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get a specific tenant enrollment's permissions list

Get a specific tenant enrollment's permissions list

### Example


```python
import openapi_client
from openapi_client.models.string_list_envelope import StringListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific tenant enrollment's permissions list
        api_response = api_instance.get_enrollment_permissions_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_enrollment_permissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_enrollment_permissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StringListEnvelope**](StringListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_tenant_async**
> ExtendedTenantDtoEnvelope get_extended_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get an extended tenant's business profile

Get an extended tenant's business profile

### Example


```python
import openapi_client
from openapi_client.models.extended_tenant_dto_envelope import ExtendedTenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get an extended tenant's business profile
        api_response = api_instance.get_extended_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_extended_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_extended_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedTenantDtoEnvelope**](ExtendedTenantDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_tenant_enrollment_async**
> ExtendedTenantEnrollmentDtoEnvelope get_extended_tenant_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get a specific tenant enrollment

Get a specific tenant enrollment

### Example


```python
import openapi_client
from openapi_client.models.extended_tenant_enrollment_dto_envelope import ExtendedTenantEnrollmentDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific tenant enrollment
        api_response = api_instance.get_extended_tenant_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_extended_tenant_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_extended_tenant_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedTenantEnrollmentDtoEnvelope**](ExtendedTenantEnrollmentDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_tenant_async**
> TenantDtoEnvelope get_root_tenant_async(api_version=api_version, x_api_version=x_api_version)

Get the root tenant of the platform

Get the root tenant of the platform

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the root tenant of the platform
        api_response = api_instance.get_root_tenant_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_root_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_root_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_async**
> TenantDtoEnvelope get_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a specific tenant by ID

Get a specific tenant by ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific tenant by ID
        api_response = api_instance.get_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_avatar_async**
> EmptyEnvelope get_tenant_avatar_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a tenant's avatar

Get a tenant's avatar

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tenant's avatar
        api_response = api_instance.get_tenant_avatar_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_cart_async**
> CartDtoEnvelope get_tenant_cart_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a tenant's default cart

Get a tenant's default cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tenant's default cart
        api_response = api_instance.get_tenant_cart_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_enrollment_async**
> TenantEnrollmentDtoEnvelope get_tenant_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get a specific tenant enrollment

Get a specific tenant enrollment

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_envelope import TenantEnrollmentDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific tenant enrollment
        api_response = api_instance.get_tenant_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoEnvelope**](TenantEnrollmentDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_enrollments_async**
> TenantEnrollmentDtoListEnvelope get_tenant_enrollments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of user enrollments for a tenant

Get the list of user enrollments for a tenant

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_list_envelope import TenantEnrollmentDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of user enrollments for a tenant
        api_response = api_instance.get_tenant_enrollments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_enrollments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_enrollments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoListEnvelope**](TenantEnrollmentDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_invitations_async**
> TenantInvitationDtoListEnvelope get_tenant_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of invitations issued by a tenant

Get the list of invitations issued by a tenant

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_list_envelope import TenantInvitationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of invitations issued by a tenant
        api_response = api_instance.get_tenant_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_invitations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_invitations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_licenses_async**
> SuiteLicenseDtoListEnvelope get_tenant_licenses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of licenses available to a tenant

Get the list of licenses available to a tenant

### Example


```python
import openapi_client
from openapi_client.models.suite_license_dto_list_envelope import SuiteLicenseDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of licenses available to a tenant
        api_response = api_instance.get_tenant_licenses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_licenses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_licenses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseDtoListEnvelope**](SuiteLicenseDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_notifications_async**
> NotificationDtoListEnvelope get_tenant_notifications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of notifications for a tenant

Get the list of notifications for a tenant

### Example


```python
import openapi_client
from openapi_client.models.notification_dto_list_envelope import NotificationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of notifications for a tenant
        api_response = api_instance.get_tenant_notifications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_notifications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_notifications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NotificationDtoListEnvelope**](NotificationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_notifications_count_async**
> Int32Envelope get_tenant_notifications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of notifications for a tenant

Get the count of notifications for a tenant

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of notifications for a tenant
        api_response = api_instance.get_tenant_notifications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_notifications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_notifications_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_pending_invitations_async**
> TenantInvitationDtoListEnvelope get_tenant_pending_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of invitations issued by a tenant that are pending

Get the list of invitations issued by a tenant that are pending

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_list_envelope import TenantInvitationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of invitations issued by a tenant that are pending
        api_response = api_instance.get_tenant_pending_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_pending_invitations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_pending_invitations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_redeemed_invitations_async**
> TenantInvitationDtoListEnvelope get_tenant_redeemed_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of invitations issued by a tenant that have been redeemed

Get the list of invitations issued by a tenant that have been redeemed

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_list_envelope import TenantInvitationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of invitations issued by a tenant that have been redeemed
        api_response = api_instance.get_tenant_redeemed_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_redeemed_invitations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_redeemed_invitations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_revoked_invitations_async**
> TenantInvitationDtoListEnvelope get_tenant_revoked_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of invitations issued by a tenant that have been revoked

Get the list of invitations issued by a tenant that have been revoked

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_list_envelope import TenantInvitationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of invitations issued by a tenant that have been revoked
        api_response = api_instance.get_tenant_revoked_invitations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_revoked_invitations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_revoked_invitations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_social_profile_async**
> SocialProfileDtoEnvelope get_tenant_social_profile_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a tenant's social profile

Get a tenant's social profile

### Example


```python
import openapi_client
from openapi_client.models.social_profile_dto_envelope import SocialProfileDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tenant's social profile
        api_response = api_instance.get_tenant_social_profile_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_social_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_social_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoEnvelope**](SocialProfileDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_users_async**
> UserDtoListEnvelope get_tenant_users_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of users enrolled in a tenant

Get the list of users enrolled in a tenant

### Example


```python
import openapi_client
from openapi_client.models.user_dto_list_envelope import UserDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of users enrolled in a tenant
        api_response = api_instance.get_tenant_users_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_users_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_users_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UserDtoListEnvelope**](UserDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_wallet_async**
> WalletDtoEnvelope get_tenant_wallet_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a tenant's billing profile (A.K.A. Wallet Account)

Get a tenant's billing profile (A.K.A. Wallet Account)

### Example


```python
import openapi_client
from openapi_client.models.wallet_dto_envelope import WalletDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tenant's billing profile (A.K.A. Wallet Account)
        api_response = api_instance.get_tenant_wallet_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_wallet_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_wallet_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletDtoEnvelope**](WalletDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_web_portals_async**
> WebPortalDtoListEnvelope get_tenant_web_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the list of web portals for a tenant

Get the list of web portals for a tenant

### Example


```python
import openapi_client
from openapi_client.models.web_portal_dto_list_envelope import WebPortalDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of web portals for a tenant
        api_response = api_instance.get_tenant_web_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant_web_portals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant_web_portals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPortalDtoListEnvelope**](WebPortalDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tenant_async**
> EmptyEnvelope patch_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a tenant's profile

Patch a tenant's profile

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a tenant's profile
        api_response = api_instance.patch_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TenantsApi->patch_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->patch_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_license_async**
> SuiteLicenseDtoListEnvelope revoke_license_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)

Revoke a license from a specific enrollment

Revoke a license from a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.suite_license_dto_list_envelope import SuiteLicenseDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    license_id = 'license_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a license from a specific enrollment
        api_response = api_instance.revoke_license_async(tenant_id, enrollment_id, license_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->revoke_license_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->revoke_license_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **license_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SuiteLicenseDtoListEnvelope**](SuiteLicenseDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_tenant_async**
> EmptyEnvelope select_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Select a business tenant as the user's default tenant

Select a business tenant as the user's default tenant

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Select a business tenant as the user's default tenant
        api_response = api_instance.select_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->select_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->select_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar_async**
> EmptyEnvelope update_avatar_async(tenant_id, api_version=api_version, x_api_version=x_api_version, avatar=avatar)

Update a tenant's avatar

Update a tenant's avatar

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    avatar = None # bytearray |  (optional)

    try:
        # Update a tenant's avatar
        api_response = api_instance.update_avatar_async(tenant_id, api_version=api_version, x_api_version=x_api_version, avatar=avatar)
        print("The response of TenantsApi->update_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **avatar** | **bytearray**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json, application/xml
 - **Accept**: image/png, application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_async**
> EmptyEnvelope update_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_update_dto=tenant_update_dto)

Update a tenant's profile

Update a tenant's profile

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_update_dto import TenantUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_update_dto = openapi_client.TenantUpdateDto() # TenantUpdateDto |  (optional)

    try:
        # Update a tenant's profile
        api_response = api_instance.update_tenant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_update_dto=tenant_update_dto)
        print("The response of TenantsApi->update_tenant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_update_dto** | [**TenantUpdateDto**](TenantUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_enrollment_feature_access**
> BooleanEnvelope validate_enrollment_feature_access(tenant_id, enrollment_id, feature=feature, api_version=api_version, x_api_version=x_api_version)

Validate the access to a specific feature for a specific enrollment

Validate the access to a specific feature for a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    feature = 'feature_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Validate the access to a specific feature for a specific enrollment
        api_response = api_instance.validate_enrollment_feature_access(tenant_id, enrollment_id, feature=feature, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->validate_enrollment_feature_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->validate_enrollment_feature_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **feature** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_enrollment_permissions_async**
> BooleanEnvelope validate_enrollment_permissions_async(tenant_id, enrollment_id, roles=roles, permissions=permissions, api_version=api_version, x_api_version=x_api_version)

Validate the existence of a list of roles and permissions for a specific enrollment

Validate the existence of a list of roles and permissions for a specific enrollment

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    roles = ['roles_example'] # List[str] |  (optional)
    permissions = ['permissions_example'] # List[str] |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Validate the existence of a list of roles and permissions for a specific enrollment
        api_response = api_instance.validate_enrollment_permissions_async(tenant_id, enrollment_id, roles=roles, permissions=permissions, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->validate_enrollment_permissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->validate_enrollment_permissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **roles** | [**List[str]**](str.md)|  | [optional] 
 **permissions** | [**List[str]**](str.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

