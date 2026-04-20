# openapi_client.RolesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_permission_to_role_async**](RolesApi.md#assign_permission_to_role_async) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions/{securityPermissionId} | Assign a permission to a role
[**assign_role_to_business_application_async**](RolesApi.md#assign_role_to_business_application_async) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Applications/{applicationId} | Assign a role to a business application
[**assign_role_to_enrollment_async**](RolesApi.md#assign_role_to_enrollment_async) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments/{enrollmentId} | Assign a role to an enrollment
[**create_role_async**](RolesApi.md#create_role_async) | **POST** /api/v2/SecurityService/Roles | Create a new role
[**delete_role_async**](RolesApi.md#delete_role_async) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId} | Delete an existing role
[**get_applications_by_role_async**](RolesApi.md#get_applications_by_role_async) | **GET** /api/v2/SecurityService/Roles/{securityRoleId}/Applications | Get applications by role
[**get_enrollments_by_role_async**](RolesApi.md#get_enrollments_by_role_async) | **GET** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments | Get enrollments by role
[**get_role_async**](RolesApi.md#get_role_async) | **GET** /api/v2/SecurityService/Roles/{securityRoleId} | Get role by ID
[**get_role_permissions_async**](RolesApi.md#get_role_permissions_async) | **GET** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions | Get permissions by role
[**get_roles_async**](RolesApi.md#get_roles_async) | **GET** /api/v2/SecurityService/Roles | Get all roles
[**get_roles_by_enrollment_async**](RolesApi.md#get_roles_by_enrollment_async) | **GET** /api/v2/SecurityService/Roles/ByEnrollment/{enrollmentId} | Get roles by enrollment
[**get_roles_count_async**](RolesApi.md#get_roles_count_async) | **GET** /api/v2/SecurityService/Roles/Count | Get roles count
[**revoke_permission_from_role_async**](RolesApi.md#revoke_permission_from_role_async) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions/{securityPermissionId} | Revoke a permission from a role
[**revoke_role_from_business_application_async**](RolesApi.md#revoke_role_from_business_application_async) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Applications/{applicationId} | Revoke a role from a business application
[**revoke_role_from_enrollment_async**](RolesApi.md#revoke_role_from_enrollment_async) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments/{enrollmentId} | Revoke a role from an enrollment
[**update_role_async**](RolesApi.md#update_role_async) | **PUT** /api/v2/SecurityService/Roles/{securityRoleId} | Update an existing role


# **assign_permission_to_role_async**
> EmptyEnvelope assign_permission_to_role_async(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Assign a permission to a role

Assigns a security permission to a security role.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a permission to a role
        api_response = api_instance.assign_permission_to_role_async(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->assign_permission_to_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->assign_permission_to_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_role_to_business_application_async**
> EmptyEnvelope assign_role_to_business_application_async(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)

Assign a role to a business application

Assigns a security role to a business application.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a role to a business application
        api_response = api_instance.assign_role_to_business_application_async(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->assign_role_to_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->assign_role_to_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **assign_role_to_enrollment_async**
> EmptyEnvelope assign_role_to_enrollment_async(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Assign a role to an enrollment

Assigns a security role to a tenant enrollment.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assign a role to an enrollment
        api_response = api_instance.assign_role_to_enrollment_async(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->assign_role_to_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->assign_role_to_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **create_role_async**
> EmptyEnvelope create_role_async(tenant_id, security_role_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a new role

Creates a new security role for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_role_create_dto import SecurityRoleCreateDto
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_create_dto = openapi_client.SecurityRoleCreateDto() # SecurityRoleCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a new role
        api_response = api_instance.create_role_async(tenant_id, security_role_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->create_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_create_dto** | [**SecurityRoleCreateDto**](SecurityRoleCreateDto.md)|  | 
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

# **delete_role_async**
> EmptyEnvelope delete_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Delete an existing role

Deletes an existing security role for the specified tenant.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an existing role
        api_response = api_instance.delete_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->delete_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_applications_by_role_async**
> BusinessApplicationSimpleDtoListEnvelope get_applications_by_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Get applications by role

Retrieves all business applications that have a specific role granted.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get applications by role
        api_response = api_instance.get_applications_by_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_applications_by_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_applications_by_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **get_enrollments_by_role_async**
> TenantEnrollmentDtoListEnvelope get_enrollments_by_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Get enrollments by role

Retrieves all tenant enrollments that have a specific role.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get enrollments by role
        api_response = api_instance.get_enrollments_by_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_enrollments_by_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_enrollments_by_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **get_role_async**
> SecurityRoleDtoEnvelope get_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Get role by ID

Retrieves a specific security role by its ID.

### Example


```python
import openapi_client
from openapi_client.models.security_role_dto_envelope import SecurityRoleDtoEnvelope
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get role by ID
        api_response = api_instance.get_role_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityRoleDtoEnvelope**](SecurityRoleDtoEnvelope.md)

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

# **get_role_permissions_async**
> SecurityPermissionDtoListEnvelope get_role_permissions_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)

Get permissions by role

Retrieves all security permissions assigned to a specific role.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get permissions by role
        api_response = api_instance.get_role_permissions_async(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_role_permissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_permissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **get_roles_async**
> SecurityRoleDtoListEnvelope get_roles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all roles

Retrieves all security roles for the specified tenant.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all roles
        api_response = api_instance.get_roles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_roles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_roles_by_enrollment_async**
> SecurityRoleDtoListEnvelope get_roles_by_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get roles by enrollment

Retrieves all security roles granted to a specific enrollment.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get roles by enrollment
        api_response = api_instance.get_roles_by_enrollment_async(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_roles_by_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles_by_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
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

# **get_roles_count_async**
> Int32Envelope get_roles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get roles count

Retrieves the count of security roles for the specified tenant.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get roles count
        api_response = api_instance.get_roles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->get_roles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles_count_async: %s\n" % e)
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

# **revoke_permission_from_role_async**
> EmptyEnvelope revoke_permission_from_role_async(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)

Revoke a permission from a role

Revokes a security permission from a security role.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a permission from a role
        api_response = api_instance.revoke_permission_from_role_async(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->revoke_permission_from_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->revoke_permission_from_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **revoke_role_from_business_application_async**
> EmptyEnvelope revoke_role_from_business_application_async(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)

Revoke a role from a business application

Revokes a security role from a business application.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a role from a business application
        api_response = api_instance.revoke_role_from_business_application_async(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->revoke_role_from_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->revoke_role_from_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **revoke_role_from_enrollment_async**
> EmptyEnvelope revoke_role_from_enrollment_async(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Revoke a role from an enrollment

Revokes a security role from a tenant enrollment.

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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Revoke a role from an enrollment
        api_response = api_instance.revoke_role_from_enrollment_async(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->revoke_role_from_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->revoke_role_from_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **update_role_async**
> EmptyEnvelope update_role_async(tenant_id, security_role_id, security_role_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an existing role

Updates an existing security role for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_role_update_dto import SecurityRoleUpdateDto
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    security_role_update_dto = openapi_client.SecurityRoleUpdateDto() # SecurityRoleUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an existing role
        api_response = api_instance.update_role_async(tenant_id, security_role_id, security_role_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->update_role_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
 **security_role_update_dto** | [**SecurityRoleUpdateDto**](SecurityRoleUpdateDto.md)|  | 
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

