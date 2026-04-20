# openapi_client.TaskTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_type_async**](TaskTypesApi.md#create_task_type_async) | **POST** /api/v2/ProjectsService/TaskTypes | Creates a new task type
[**delete_task_type_async**](TaskTypesApi.md#delete_task_type_async) | **DELETE** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | Deletes a task type
[**get_task_type_by_id_async**](TaskTypesApi.md#get_task_type_by_id_async) | **GET** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | Gets a task type by ID
[**update_task_type_async**](TaskTypesApi.md#update_task_type_async) | **PUT** /api/v2/ProjectsService/TaskTypes/{taskTypeId} | Updates a task type


# **create_task_type_async**
> TaskTypeDto create_task_type_async(tenant_id, task_type_create_dto=task_type_create_dto)

Creates a new task type

Creates a new task type for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.task_type_create_dto import TaskTypeCreateDto
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    task_type_create_dto = openapi_client.TaskTypeCreateDto() # TaskTypeCreateDto |  (optional)

    try:
        # Creates a new task type
        api_response = api_instance.create_task_type_async(tenant_id, task_type_create_dto=task_type_create_dto)
        print("The response of TaskTypesApi->create_task_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->create_task_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **task_type_create_dto** | [**TaskTypeCreateDto**](TaskTypeCreateDto.md)|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **delete_task_type_async**
> TaskTypeDto delete_task_type_async(task_type_id, tenant_id)

Deletes a task type

Deletes the specified task type.

### Example


```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Deletes a task type
        api_response = api_instance.delete_task_type_async(task_type_id, tenant_id)
        print("The response of TaskTypesApi->delete_task_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->delete_task_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **get_task_type_by_id_async**
> TaskTypeDto get_task_type_by_id_async(task_type_id, tenant_id)

Gets a task type by ID

Retrieves the details of a task type using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a task type by ID
        api_response = api_instance.get_task_type_by_id_async(task_type_id, tenant_id)
        print("The response of TaskTypesApi->get_task_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->get_task_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

# **update_task_type_async**
> TaskTypeDto update_task_type_async(task_type_id, tenant_id, task_type_update_dto=task_type_update_dto)

Updates a task type

Updates the specified task type.

### Example


```python
import openapi_client
from openapi_client.models.task_type_dto import TaskTypeDto
from openapi_client.models.task_type_update_dto import TaskTypeUpdateDto
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
    api_instance = openapi_client.TaskTypesApi(api_client)
    task_type_id = 'task_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    task_type_update_dto = openapi_client.TaskTypeUpdateDto() # TaskTypeUpdateDto |  (optional)

    try:
        # Updates a task type
        api_response = api_instance.update_task_type_async(task_type_id, tenant_id, task_type_update_dto=task_type_update_dto)
        print("The response of TaskTypesApi->update_task_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskTypesApi->update_task_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **task_type_update_dto** | [**TaskTypeUpdateDto**](TaskTypeUpdateDto.md)|  | [optional] 

### Return type

[**TaskTypeDto**](TaskTypeDto.md)

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

