# openapi_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_service_projects_count_get**](ProjectsApi.md#api_v2_projects_service_projects_count_get) | **GET** /api/v2/ProjectsService/Projects/Count | 
[**api_v2_projects_service_projects_get**](ProjectsApi.md#api_v2_projects_service_projects_get) | **GET** /api/v2/ProjectsService/Projects | 
[**api_v2_projects_service_projects_post**](ProjectsApi.md#api_v2_projects_service_projects_post) | **POST** /api/v2/ProjectsService/Projects | 
[**api_v2_projects_service_projects_project_id_delete**](ProjectsApi.md#api_v2_projects_service_projects_project_id_delete) | **DELETE** /api/v2/ProjectsService/Projects/{projectId} | 
[**api_v2_projects_service_projects_project_id_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_get) | **GET** /api/v2/ProjectsService/Projects/{projectId} | 
[**api_v2_projects_service_projects_project_id_periods_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_periods_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Periods | 
[**api_v2_projects_service_projects_project_id_periods_project_period_id_delete**](ProjectsApi.md#api_v2_projects_service_projects_project_id_periods_project_period_id_delete) | **DELETE** /api/v2/ProjectsService/Projects/{projectId}/Periods/{projectPeriodId} | 
[**api_v2_projects_service_projects_project_id_periods_project_period_id_put**](ProjectsApi.md#api_v2_projects_service_projects_project_id_periods_project_period_id_put) | **PUT** /api/v2/ProjectsService/Projects/{projectId}/Periods/{projectPeriodId} | 
[**api_v2_projects_service_projects_project_id_put**](ProjectsApi.md#api_v2_projects_service_projects_project_id_put) | **PUT** /api/v2/ProjectsService/Projects/{projectId} | 
[**api_v2_projects_service_projects_project_id_task_categories_count_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_task_categories_count_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TaskCategories/Count | 
[**api_v2_projects_service_projects_project_id_task_categories_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_task_categories_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TaskCategories | 
[**api_v2_projects_service_projects_project_id_tasks_count_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_tasks_count_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Tasks/Count | 
[**api_v2_projects_service_projects_project_id_tasks_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_tasks_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Tasks | 
[**api_v2_projects_service_projects_project_id_tasks_post**](ProjectsApi.md#api_v2_projects_service_projects_project_id_tasks_post) | **POST** /api/v2/ProjectsService/Projects/{projectId}/Tasks | 
[**api_v2_projects_service_projects_project_id_tasks_project_task_id_delete**](ProjectsApi.md#api_v2_projects_service_projects_project_id_tasks_project_task_id_delete) | **DELETE** /api/v2/ProjectsService/Projects/{projectId}/Tasks/{projectTaskId} | 
[**api_v2_projects_service_projects_project_id_tasks_project_task_id_put**](ProjectsApi.md#api_v2_projects_service_projects_project_id_tasks_project_task_id_put) | **PUT** /api/v2/ProjectsService/Projects/{projectId}/Tasks/{projectTaskId} | 
[**api_v2_projects_service_projects_project_id_time_logs_count_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_time_logs_count_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TimeLogs/Count | 
[**api_v2_projects_service_projects_project_id_time_logs_get**](ProjectsApi.md#api_v2_projects_service_projects_project_id_time_logs_get) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TimeLogs | 


# **api_v2_projects_service_projects_count_get**
> Int32Envelope api_v2_projects_service_projects_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_count_get: %s\n" % e)
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

# **api_v2_projects_service_projects_get**
> ProjectDtoListEnvelope api_v2_projects_service_projects_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_dto_list_envelope import ProjectDtoListEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectDtoListEnvelope**](ProjectDtoListEnvelope.md)

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

# **api_v2_projects_service_projects_post**
> EmptyEnvelope api_v2_projects_service_projects_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_create_dto=project_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_create_dto import ProjectCreateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_create_dto = openapi_client.ProjectCreateDto() # ProjectCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_create_dto=project_create_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_create_dto** | [**ProjectCreateDto**](ProjectCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_delete**
> EmptyEnvelope api_v2_projects_service_projects_project_id_delete(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_delete(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_get**
> ProjectDtoEnvelope api_v2_projects_service_projects_project_id_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_dto_envelope import ProjectDtoEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectDtoEnvelope**](ProjectDtoEnvelope.md)

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

# **api_v2_projects_service_projects_project_id_periods_get**
> EmptyEnvelope api_v2_projects_service_projects_project_id_periods_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_period_create_dto=project_period_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_period_create_dto import ProjectPeriodCreateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_period_create_dto = openapi_client.ProjectPeriodCreateDto() # ProjectPeriodCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_periods_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_period_create_dto=project_period_create_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_periods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_periods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_period_create_dto** | [**ProjectPeriodCreateDto**](ProjectPeriodCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_periods_project_period_id_delete**
> EmptyEnvelope api_v2_projects_service_projects_project_id_periods_project_period_id_delete(project_id, project_period_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_periods_project_period_id_delete(project_id, project_period_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_periods_project_period_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_periods_project_period_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_periods_project_period_id_put**
> EmptyEnvelope api_v2_projects_service_projects_project_id_periods_project_period_id_put(project_id, project_period_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_period_update_dto=project_period_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_period_update_dto import ProjectPeriodUpdateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_period_update_dto = openapi_client.ProjectPeriodUpdateDto() # ProjectPeriodUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_periods_project_period_id_put(project_id, project_period_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_period_update_dto=project_period_update_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_periods_project_period_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_periods_project_period_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_period_update_dto** | [**ProjectPeriodUpdateDto**](ProjectPeriodUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_put**
> EmptyEnvelope api_v2_projects_service_projects_project_id_put(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_update_dto=project_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_update_dto import ProjectUpdateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_update_dto = openapi_client.ProjectUpdateDto() # ProjectUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_put(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_update_dto=project_update_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_update_dto** | [**ProjectUpdateDto**](ProjectUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_task_categories_count_get**
> Int32Envelope api_v2_projects_service_projects_project_id_task_categories_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_task_categories_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_task_categories_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_task_categories_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

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

# **api_v2_projects_service_projects_project_id_task_categories_get**
> TaskCategoryDtoListEnvelope api_v2_projects_service_projects_project_id_task_categories_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_dto_list_envelope import TaskCategoryDtoListEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_task_categories_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_task_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_task_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskCategoryDtoListEnvelope**](TaskCategoryDtoListEnvelope.md)

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

# **api_v2_projects_service_projects_project_id_tasks_count_get**
> Int32Envelope api_v2_projects_service_projects_project_id_tasks_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_tasks_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_tasks_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_tasks_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

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

# **api_v2_projects_service_projects_project_id_tasks_get**
> ProjectTaskDtoListEnvelope api_v2_projects_service_projects_project_id_tasks_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_task_dto_list_envelope import ProjectTaskDtoListEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_tasks_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTaskDtoListEnvelope**](ProjectTaskDtoListEnvelope.md)

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

# **api_v2_projects_service_projects_project_id_tasks_post**
> EmptyEnvelope api_v2_projects_service_projects_project_id_tasks_post(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_task_create_dto=project_task_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_task_create_dto import ProjectTaskCreateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_task_create_dto = openapi_client.ProjectTaskCreateDto() # ProjectTaskCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_tasks_post(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_task_create_dto=project_task_create_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_task_create_dto** | [**ProjectTaskCreateDto**](ProjectTaskCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_tasks_project_task_id_delete**
> EmptyEnvelope api_v2_projects_service_projects_project_id_tasks_project_task_id_delete(tenant_id, project_id, project_task_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_id = 'project_id_example' # str | 
    project_task_id = 'project_task_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_tasks_project_task_id_delete(tenant_id, project_id, project_task_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_tasks_project_task_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_tasks_project_task_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_id** | **str**|  | 
 **project_task_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_tasks_project_task_id_put**
> EmptyEnvelope api_v2_projects_service_projects_project_id_tasks_project_task_id_put(project_id, project_task_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_task_update_dto=project_task_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.project_task_update_dto import ProjectTaskUpdateDto
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_task_id = 'project_task_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_task_update_dto = openapi_client.ProjectTaskUpdateDto() # ProjectTaskUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_tasks_project_task_id_put(project_id, project_task_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_task_update_dto=project_task_update_dto)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_tasks_project_task_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_tasks_project_task_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_task_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_task_update_dto** | [**ProjectTaskUpdateDto**](ProjectTaskUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_service_projects_project_id_time_logs_count_get**
> Int32Envelope api_v2_projects_service_projects_project_id_time_logs_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_time_logs_count_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_time_logs_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_time_logs_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

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

# **api_v2_projects_service_projects_project_id_time_logs_get**
> ProjectTimeLogDtoListEnvelope api_v2_projects_service_projects_project_id_time_logs_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_projects_project_id_time_logs_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectsApi->api_v2_projects_service_projects_project_id_time_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_service_projects_project_id_time_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

