# openapi_client.TaskTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_service_task_types_post**](TaskTypesApi.md#api_v2_projects_service_task_types_post) | **POST** /api/v2/ProjectsService/TaskTypes | 
[**api_v2_projects_service_task_types_task_type_id_delete**](TaskTypesApi.md#api_v2_projects_service_task_types_task_type_id_delete) | **DELETE** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | 
[**api_v2_projects_service_task_types_task_type_id_get**](TaskTypesApi.md#api_v2_projects_service_task_types_task_type_id_get) | **GET** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | 
[**api_v2_projects_service_task_types_task_type_id_put**](TaskTypesApi.md#api_v2_projects_service_task_types_task_type_id_put) | **PUT** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | 


# **api_v2_projects_service_task_types_post**
> TaskTypeDto api_v2_projects_service_task_types_post(tenant_id, api_version=api_version, x_api_version=x_api_version, task_type_create_dto=task_type_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_type_create_dto import TaskTypeCreateDto
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    task_type_create_dto = openapi_client.TaskTypeCreateDto() # TaskTypeCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_types_post(tenant_id, api_version=api_version, x_api_version=x_api_version, task_type_create_dto=task_type_create_dto)
        print("The response of TaskTypesApi->api_v2_projects_service_task_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->api_v2_projects_service_task_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **task_type_create_dto** | [**TaskTypeCreateDto**](TaskTypeCreateDto.md)|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **api_v2_projects_service_task_types_task_type_id_delete**
> TaskTypeDto api_v2_projects_service_task_types_task_type_id_delete(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_types_task_type_id_delete(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskTypesApi->api_v2_projects_service_task_types_task_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->api_v2_projects_service_task_types_task_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **api_v2_projects_service_task_types_task_type_id_get**
> TaskTypeDto api_v2_projects_service_task_types_task_type_id_get(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_types_task_type_id_get(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskTypesApi->api_v2_projects_service_task_types_task_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->api_v2_projects_service_task_types_task_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **api_v2_projects_service_task_types_task_type_id_put**
> TaskTypeDto api_v2_projects_service_task_types_task_type_id_put(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version, task_type_update_dto=task_type_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
from openapi_client.models.task_type_update_dto import TaskTypeUpdateDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    task_type_update_dto = openapi_client.TaskTypeUpdateDto() # TaskTypeUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_types_task_type_id_put(task_type_id, tenant_id, api_version=api_version, x_api_version=x_api_version, task_type_update_dto=task_type_update_dto)
        print("The response of TaskTypesApi->api_v2_projects_service_task_types_task_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->api_v2_projects_service_task_types_task_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **task_type_update_dto** | [**TaskTypeUpdateDto**](TaskTypeUpdateDto.md)|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

