# openapi_client.PermissionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_permission_to_business_application_async**](PermissionsApi.md#assign_permission_to_business_application_async) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Applications/{applicationId} | Assign a permission to a business application
[**assign_permission_to_enrollment_async**](PermissionsApi.md#assign_permission_to_enrollment_async) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments/{enrollmentId} | Assign a permission to an enrollment
[**assign_role_to_permission_async**](PermissionsApi.md#assign_role_to_permission_async) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Roles/{securityRoleId} | Assign a role to a permission
[**create_permission_async**](PermissionsApi.md#create_permission_async) | **POST** /api/v2/SecurityService/Permissions | Create a new permission
[**delete_permission_async**](PermissionsApi.md#delete_permission_async) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId} | Delete an existing permission
[**get_applications_by_permission_async**](PermissionsApi.md#get_applications_by_permission_async) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId}/Applications | Get applications by permission
[**get_enrollments_by_permission_async**](PermissionsApi.md#get_enrollments_by_permission_async) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments | Get enrollments by permission
[**get_permission_async**](PermissionsApi.md#get_permission_async) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId} | Get permission by ID
[**get_permissions_async**](PermissionsApi.md#get_permissions_async) | **GET** /api/v2/SecurityService/Permissions | Get all permissions
[**get_permissions_by_enrollment_async**](PermissionsApi.md#get_permissions_by_enrollment_async) | **GET** /api/v2/SecurityService/Permissions/ByEnrollment/{enrollmentId} | Get permissions by enrollment
[**get_permissions_count_async**](PermissionsApi.md#get_permissions_count_async) | **GET** /api/v2/SecurityService/Permissions/Count | Get permissions count
[**get_roles_by_permission_async**](PermissionsApi.md#get_roles_by_permission_async) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId}/Roles | Get roles by permission
[**revoke_permission_from_business_application_async**](PermissionsApi.md#revoke_permission_from_business_application_async) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Applications/{applicationId} | Revoke a permission from a business application
[**revoke_permission_from_enrollment_async**](PermissionsApi.md#revoke_permission_from_enrollment_async) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments/{enrollmentId} | Revoke a permission from an enrollment
[**revoke_role_from_permission_async**](PermissionsApi.md#revoke_role_from_permission_async) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Roles/{securityRoleId} | Revoke a role from a permission
[**update_permission_async**](PermissionsApi.md#update_permission_async) | **PUT** /api/v2/SecurityService/Permissions/{securityPermissionId} | Update an existing permission


# **assign_permission_to_business_application_async**
> EmptyEnvelope assign_permission_to_business_application_async(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)

Assign a permission to a business application

Assigns a security permission to a business application.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a permission to a business application
        api_response = api_instance.assign_permission_to_business_application_async(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->assign_permission_to_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->assign_permission_to_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_permission_to_enrollment_async**
> EmptyEnvelope assign_permission_to_enrollment_async(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Assign a permission to an enrollment

Assigns a security permission to a tenant enrollment.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a permission to an enrollment
        api_response = api_instance.assign_permission_to_enrollment_async(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->assign_permission_to_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->assign_permission_to_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_role_to_permission_async**
> EmptyEnvelope assign_role_to_permission_async(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Assign a role to a permission

Assigns a security role to a security permission.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a role to a permission
        api_response = api_instance.assign_role_to_permission_async(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->assign_role_to_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->assign_role_to_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permission_async**
> EmptyEnvelope create_permission_async(tenant_id, security_permission_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a new permission

Creates a new security permission for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_permission_create_dto import SecurityPermissionCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_create_dto = openapi_client.SecurityPermissionCreateDto() # SecurityPermissionCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a new permission
        api_response = api_instance.create_permission_async(tenant_id, security_permission_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->create_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->create_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_create_dto** | [**SecurityPermissionCreateDto**](SecurityPermissionCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_async**
> EmptyEnvelope delete_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Delete an existing permission

Deletes an existing security permission for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an existing permission
        api_response = api_instance.delete_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->delete_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->delete_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_by_permission_async**
> BusinessApplicationSimpleDtoListEnvelope get_applications_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Get applications by permission

Retrieves all business applications that have a specific permission granted.

### Example


```python
import openapi_client
from openapi_client.models.business_application_simple_dto_list_envelope import BusinessApplicationSimpleDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get applications by permission
        api_response = api_instance.get_applications_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_applications_by_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_applications_by_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessApplicationSimpleDtoListEnvelope**](BusinessApplicationSimpleDtoListEnvelope.md)

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

# **get_enrollments_by_permission_async**
> TenantEnrollmentDtoListEnvelope get_enrollments_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Get enrollments by permission

Retrieves all tenant enrollments that have a specific permission.

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_list_envelope import TenantEnrollmentDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get enrollments by permission
        api_response = api_instance.get_enrollments_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_enrollments_by_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_enrollments_by_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
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

# **get_permission_async**
> SecurityPermissionDtoEnvelope get_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Get permission by ID

Retrieves a specific security permission by its ID.

### Example


```python
import openapi_client
from openapi_client.models.security_permission_dto_envelope import SecurityPermissionDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get permission by ID
        api_response = api_instance.get_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityPermissionDtoEnvelope**](SecurityPermissionDtoEnvelope.md)

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

# **get_permissions_async**
> SecurityPermissionDtoListEnvelope get_permissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all permissions

Retrieves all security permissions for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.security_permission_dto_list_envelope import SecurityPermissionDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all permissions
        api_response = api_instance.get_permissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_permissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityPermissionDtoListEnvelope**](SecurityPermissionDtoListEnvelope.md)

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

# **get_permissions_by_enrollment_async**
> SecurityPermissionDtoListEnvelope get_permissions_by_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get permissions by enrollment

Retrieves all security permissions granted to a specific enrollment.

### Example


```python
import openapi_client
from openapi_client.models.security_permission_dto_list_envelope import SecurityPermissionDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get permissions by enrollment
        api_response = api_instance.get_permissions_by_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_permissions_by_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions_by_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityPermissionDtoListEnvelope**](SecurityPermissionDtoListEnvelope.md)

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

# **get_permissions_count_async**
> Int32Envelope get_permissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get permissions count

Retrieves the count of security permissions for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get permissions count
        api_response = api_instance.get_permissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_permissions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions_count_async: %s\n" % e)
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

# **get_roles_by_permission_async**
> SecurityRoleDtoListEnvelope get_roles_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Get roles by permission

Retrieves all security roles that have a specific permission granted.

### Example


```python
import openapi_client
from openapi_client.models.security_role_dto_list_envelope import SecurityRoleDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get roles by permission
        api_response = api_instance.get_roles_by_permission_async(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->get_roles_by_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_roles_by_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityRoleDtoListEnvelope**](SecurityRoleDtoListEnvelope.md)

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

# **revoke_permission_from_business_application_async**
> EmptyEnvelope revoke_permission_from_business_application_async(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)

Revoke a permission from a business application

Revokes a security permission from a business application.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a permission from a business application
        api_response = api_instance.revoke_permission_from_business_application_async(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->revoke_permission_from_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->revoke_permission_from_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_enrollment_async**
> EmptyEnvelope revoke_permission_from_enrollment_async(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Revoke a permission from an enrollment

Revokes a security permission from a tenant enrollment.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a permission from an enrollment
        api_response = api_instance.revoke_permission_from_enrollment_async(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->revoke_permission_from_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->revoke_permission_from_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_role_from_permission_async**
> EmptyEnvelope revoke_role_from_permission_async(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Revoke a role from a permission

Revokes a security role from a security permission.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a role from a permission
        api_response = api_instance.revoke_role_from_permission_async(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->revoke_role_from_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->revoke_role_from_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_async**
> EmptyEnvelope update_permission_async(tenant_id, security_permission_id, security_permission_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an existing permission

Updates an existing security permission for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_permission_update_dto import SecurityPermissionUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_permission_update_dto = openapi_client.SecurityPermissionUpdateDto() # SecurityPermissionUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an existing permission
        api_response = api_instance.update_permission_async(tenant_id, security_permission_id, security_permission_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->update_permission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->update_permission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **security_permission_update_dto** | [**SecurityPermissionUpdateDto**](SecurityPermissionUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

