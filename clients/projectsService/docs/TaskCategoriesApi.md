# openapi_client.TaskCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_service_task_categories_get**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_get) | **GET** /api/v2/ProjectsService/TaskCategories | 
[**api_v2_projects_service_task_categories_post**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_post) | **POST** /api/v2/ProjectsService/TaskCategories | 
[**api_v2_projects_service_task_categories_task_category_id_delete**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_task_category_id_delete) | **DELETE** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | 
[**api_v2_projects_service_task_categories_task_category_id_get**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_task_category_id_get) | **GET** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | 
[**api_v2_projects_service_task_categories_task_category_id_put**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_task_category_id_put) | **PUT** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | 
[**api_v2_projects_service_task_categories_task_category_id_types_get**](TaskCategoriesApi.md#api_v2_projects_service_task_categories_task_category_id_types_get) | **GET** /api/v2/ProjectsService/TaskCategories/{taskCategoryId}/Types | 


# **api_v2_projects_service_task_categories_get**
> TaskCategoryDtoListEnvelope api_v2_projects_service_task_categories_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_v2_projects_service_task_categories_post**
> TaskCategoryDto api_v2_projects_service_task_categories_post(tenant_id, api_version=api_version, x_api_version=x_api_version, task_category_create_dto=task_category_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_create_dto import TaskCategoryCreateDto
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    task_category_create_dto = openapi_client.TaskCategoryCreateDto() # TaskCategoryCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_post(tenant_id, api_version=api_version, x_api_version=x_api_version, task_category_create_dto=task_category_create_dto)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **task_category_create_dto** | [**TaskCategoryCreateDto**](TaskCategoryCreateDto.md)|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **api_v2_projects_service_task_categories_task_category_id_delete**
> TaskCategoryDto api_v2_projects_service_task_categories_task_category_id_delete(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_task_category_id_delete(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **api_v2_projects_service_task_categories_task_category_id_get**
> TaskCategoryDto api_v2_projects_service_task_categories_task_category_id_get(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_task_category_id_get(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **api_v2_projects_service_task_categories_task_category_id_put**
> TaskCategoryDto api_v2_projects_service_task_categories_task_category_id_put(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version, task_category_update_dto=task_category_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
from openapi_client.models.task_category_update_dto import TaskCategoryUpdateDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    task_category_update_dto = openapi_client.TaskCategoryUpdateDto() # TaskCategoryUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_task_category_id_put(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version, task_category_update_dto=task_category_update_dto)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **task_category_update_dto** | [**TaskCategoryUpdateDto**](TaskCategoryUpdateDto.md)|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **api_v2_projects_service_task_categories_task_category_id_types_get**
> TaskCategoryDto api_v2_projects_service_task_categories_task_category_id_types_get(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_projects_service_task_categories_task_category_id_types_get(task_category_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->api_v2_projects_service_task_categories_task_category_id_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

