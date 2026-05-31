# openapi_client.ApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/v2/Applications/{appId} | Get application by ID
[**get_granted_enrollment_permissions**](ApplicationsApi.md#get_granted_enrollment_permissions) | **GET** /api/v2/Applications/{appId}/GrantedRoles/{securityRoleId}/GrantedPermissions | Get granted permissions for an application role
[**get_granted_tenant_permissions**](ApplicationsApi.md#get_granted_tenant_permissions) | **GET** /api/v2/Applications/{appId}/GrantedPermissions | Get granted tenant permissions for an application
[**get_granted_tenant_roles**](ApplicationsApi.md#get_granted_tenant_roles) | **GET** /api/v2/Applications/{appId}/GrantedRoles | Get granted tenant roles for an application
[**get_required_permissions**](ApplicationsApi.md#get_required_permissions) | **GET** /api/v2/Applications/{appId}/RequiredPermissions | Get required permissions for an application


# **get_application**
> get_application(app_id, api_version=api_version, x_api_version=x_api_version)

Get application by ID

Retrieves an application by its unique identifier.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    app_id = 'app_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get application by ID
        api_instance.get_application(app_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_granted_enrollment_permissions**
> get_granted_enrollment_permissions(app_id, security_role_id, enrollment_id=enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get granted permissions for an application role

Retrieves the list of permissions granted through a specific security role for the specified application.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    app_id = 'app_id_example' # str | 
    security_role_id = 'security_role_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get granted permissions for an application role
        api_instance.get_granted_enrollment_permissions(app_id, security_role_id, enrollment_id=enrollment_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_granted_enrollment_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **security_role_id** | **str**|  | 
 **enrollment_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_granted_tenant_permissions**
> get_granted_tenant_permissions(app_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get granted tenant permissions for an application

Retrieves the list of permissions granted to the specified application within a tenant context.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    app_id = 'app_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get granted tenant permissions for an application
        api_instance.get_granted_tenant_permissions(app_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_granted_tenant_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_granted_tenant_roles**
> get_granted_tenant_roles(app_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get granted tenant roles for an application

Retrieves the list of security roles granted to the specified application within a tenant context.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    app_id = 'app_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get granted tenant roles for an application
        api_instance.get_granted_tenant_roles(app_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_granted_tenant_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_required_permissions**
> get_required_permissions(app_id, api_version=api_version, x_api_version=x_api_version)

Get required permissions for an application

Retrieves the list of permissions required by the specified application.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    app_id = 'app_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get required permissions for an application
        api_instance.get_required_permissions(app_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_required_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

