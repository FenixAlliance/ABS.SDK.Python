# openapi_client.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_security_service_roles_get**](RolesApi.md#api_v2_security_service_roles_get) | **GET** /api/v2/SecurityService/Roles | 
[**api_v2_security_service_roles_post**](RolesApi.md#api_v2_security_service_roles_post) | **POST** /api/v2/SecurityService/Roles | 
[**api_v2_security_service_roles_security_role_id_applications_application_id_delete**](RolesApi.md#api_v2_security_service_roles_security_role_id_applications_application_id_delete) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Applications/{applicationId} | 
[**api_v2_security_service_roles_security_role_id_applications_application_id_post**](RolesApi.md#api_v2_security_service_roles_security_role_id_applications_application_id_post) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Applications/{applicationId} | 
[**api_v2_security_service_roles_security_role_id_delete**](RolesApi.md#api_v2_security_service_roles_security_role_id_delete) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId} | 
[**api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete**](RolesApi.md#api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments/{enrollmentId} | 
[**api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post**](RolesApi.md#api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments/{enrollmentId} | 
[**api_v2_security_service_roles_security_role_id_enrollments_get**](RolesApi.md#api_v2_security_service_roles_security_role_id_enrollments_get) | **GET** /api/v2/SecurityService/Roles/{securityRoleId}/Enrollments | 
[**api_v2_security_service_roles_security_role_id_get**](RolesApi.md#api_v2_security_service_roles_security_role_id_get) | **GET** /api/v2/SecurityService/Roles/{securityRoleId} | 
[**api_v2_security_service_roles_security_role_id_permissions_get**](RolesApi.md#api_v2_security_service_roles_security_role_id_permissions_get) | **GET** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions | 
[**api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete**](RolesApi.md#api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete) | **DELETE** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions/{securityPermissionId} | 
[**api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post**](RolesApi.md#api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post) | **POST** /api/v2/SecurityService/Roles/{securityRoleId}/Permissions/{securityPermissionId} | 
[**api_v2_security_service_roles_security_role_id_put**](RolesApi.md#api_v2_security_service_roles_security_role_id_put) | **PUT** /api/v2/SecurityService/Roles/{securityRoleId} | 


# **api_v2_security_service_roles_get**
> SecurityRoleDtoListEnvelope api_v2_security_service_roles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_get: %s\n" % e)
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

# **api_v2_security_service_roles_post**
> EmptyEnvelope api_v2_security_service_roles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, security_role_create_dto=security_role_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_role_create_dto import SecurityRoleCreateDto
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    security_role_create_dto = openapi_client.SecurityRoleCreateDto() # SecurityRoleCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, security_role_create_dto=security_role_create_dto)
        print("The response of RolesApi->api_v2_security_service_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **security_role_create_dto** | [**SecurityRoleCreateDto**](SecurityRoleCreateDto.md)|  | [optional] 

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

# **api_v2_security_service_roles_security_role_id_applications_application_id_delete**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_applications_application_id_delete(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_applications_application_id_delete(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_applications_application_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_applications_application_id_delete: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_applications_application_id_post**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_applications_application_id_post(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_applications_application_id_post(tenant_id, security_role_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_applications_application_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_applications_application_id_post: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_delete**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_delete(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_delete(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_delete: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_delete: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post(tenant_id, security_role_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_enrollments_enrollment_id_post: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_enrollments_get**
> TenantEnrolmentDtoListEnvelope api_v2_security_service_roles_security_role_id_enrollments_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_enrollments_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_enrollments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_enrollments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **api_v2_security_service_roles_security_role_id_get**
> SecurityRoleDtoListEnvelope api_v2_security_service_roles_security_role_id_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
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

# **api_v2_security_service_roles_security_role_id_permissions_get**
> SecurityPermissionDtoListEnvelope api_v2_security_service_roles_security_role_id_permissions_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.security_permission_dto_list_envelope import SecurityPermissionDtoListEnvelope
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_permissions_get(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_permissions_get: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_permissions_security_permission_id_delete: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    security_permission_id = 'security_permission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post(tenant_id, security_role_id, security_permission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_permissions_security_permission_id_post: %s\n" % e)
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

# **api_v2_security_service_roles_security_role_id_put**
> EmptyEnvelope api_v2_security_service_roles_security_role_id_put(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version, security_role_update_dto=security_role_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.security_role_update_dto import SecurityRoleUpdateDto
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
    api_instance = openapi_client.RolesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    security_role_update_dto = openapi_client.SecurityRoleUpdateDto() # SecurityRoleUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_security_service_roles_security_role_id_put(tenant_id, security_role_id, api_version=api_version, x_api_version=x_api_version, security_role_update_dto=security_role_update_dto)
        print("The response of RolesApi->api_v2_security_service_roles_security_role_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->api_v2_security_service_roles_security_role_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **security_role_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **security_role_update_dto** | [**SecurityRoleUpdateDto**](SecurityRoleUpdateDto.md)|  | [optional] 

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

