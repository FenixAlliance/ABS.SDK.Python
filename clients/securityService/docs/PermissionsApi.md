# openapi_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_security_service_permissions_get**](PermissionsApi.md#api_v2_security_service_permissions_get) | **GET** /api/v2/SecurityService/Permissions | 
[**api_v2_security_service_permissions_post**](PermissionsApi.md#api_v2_security_service_permissions_post) | **POST** /api/v2/SecurityService/Permissions | 
[**api_v2_security_service_permissions_security_permission_id_applications_application_id_delete**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_applications_application_id_delete) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Applications/{applicationId} | 
[**api_v2_security_service_permissions_security_permission_id_applications_application_id_post**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_applications_application_id_post) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Applications/{applicationId} | 
[**api_v2_security_service_permissions_security_permission_id_delete**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_delete) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId} | 
[**api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments/{enrollmentId} | 
[**api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments/{enrollmentId} | 
[**api_v2_security_service_permissions_security_permission_id_enrollments_get**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_enrollments_get) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId}/Enrollments | 
[**api_v2_security_service_permissions_security_permission_id_get**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_get) | **GET** /api/v2/SecurityService/Permissions/{securityPermissionId} | 
[**api_v2_security_service_permissions_security_permission_id_put**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_put) | **PUT** /api/v2/SecurityService/Permissions/{securityPermissionId} | 
[**api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete) | **DELETE** /api/v2/SecurityService/Permissions/{securityPermissionId}/Roles/{securityRoleId} | 
[**api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post**](PermissionsApi.md#api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post) | **POST** /api/v2/SecurityService/Permissions/{securityPermissionId}/Roles/{securityRoleId} | 


# **api_v2_security_service_permissions_get**
> SecurityRoleDtoListEnvelope api_v2_security_service_permissions_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.security_role_dto_list_envelope import SecurityRoleDtoListEnvelope
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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_post**
> EmptyEnvelope api_v2_security_service_permissions_post(tenant_id, security_permission_create_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_permission_create_dto import SecurityPermissionCreateDto
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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_create_dto = openapi_client.SecurityPermissionCreateDto() # SecurityPermissionCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_post(tenant_id, security_permission_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_applications_application_id_delete**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_applications_application_id_delete(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_applications_application_id_delete(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_applications_application_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_applications_application_id_delete: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_applications_application_id_post**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_applications_application_id_post(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_applications_application_id_post(tenant_id, security_permission_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_applications_application_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_applications_application_id_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_delete**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_delete(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_delete(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_delete: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_delete: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post(tenant_id, security_permission_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_enrollment_id_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_enrollments_get**
> TenantEnrolmentDtoListEnvelope api_v2_security_service_permissions_security_permission_id_enrollments_get(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.tenant_enrolment_dto_list_envelope import TenantEnrolmentDtoListEnvelope
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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_enrollments_get(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_enrollments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_permission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrolmentDtoListEnvelope**](TenantEnrolmentDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_get**
> SecurityRoleDtoListEnvelope api_v2_security_service_permissions_security_permission_id_get(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.security_role_dto_list_envelope import SecurityRoleDtoListEnvelope
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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_get(tenant_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_put**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_put(tenant_id, security_permission_id, security_permission_update_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_permission_update_dto import SecurityPermissionUpdateDto
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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_permission_update_dto = openapi_client.SecurityPermissionUpdateDto() # SecurityPermissionUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_put(tenant_id, security_permission_id, security_permission_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_put: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_roles_security_role_id_delete: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post**
> EmptyEnvelope api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.PermissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post(tenant_id, security_permission_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PermissionsApi->api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->api_v2_security_service_permissions_security_permission_id_roles_security_role_id_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

