# openapi_client.TaskCategoriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_tenant_task_categories_async**](TaskCategoriesApi.md#count_tenant_task_categories_async) | **GET** /api/v2/ProjectsService/TaskCategories/Count | Counts task categories
[**create_task_category_async**](TaskCategoriesApi.md#create_task_category_async) | **POST** /api/v2/ProjectsService/TaskCategories | Creates a new task category
[**delete_task_category_async**](TaskCategoriesApi.md#delete_task_category_async) | **DELETE** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | Deletes a task category
[**get_task_category_by_id_async**](TaskCategoriesApi.md#get_task_category_by_id_async) | **GET** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | Gets a task category by ID
[**get_task_category_task_types_async**](TaskCategoriesApi.md#get_task_category_task_types_async) | **GET** /api/v2/ProjectsService/TaskCategories/{taskCategoryId}/Types | Retrieves task types for a category
[**get_tenant_task_categories_async**](TaskCategoriesApi.md#get_tenant_task_categories_async) | **GET** /api/v2/ProjectsService/TaskCategories | Retrieves all task categories
[**update_task_category_async**](TaskCategoriesApi.md#update_task_category_async) | **PUT** /api/v2/ProjectsService/TaskCategories/{taskCategoryId} | Updates a task category


# **count_tenant_task_categories_async**
> Int32Envelope count_tenant_task_categories_async(tenant_id)

Counts task categories

Gets the count of task categories for the current tenant.

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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts task categories
        api_response = api_instance.count_tenant_task_categories_async(tenant_id)
        print("The response of TaskCategoriesApi->count_tenant_task_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->count_tenant_task_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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

# **create_task_category_async**
> TaskCategoryDto create_task_category_async(tenant_id, task_category_create_dto=task_category_create_dto)

Creates a new task category

Creates a new task category for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.task_category_create_dto import TaskCategoryCreateDto
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    task_category_create_dto = openapi_client.TaskCategoryCreateDto() # TaskCategoryCreateDto |  (optional)

    try:
        # Creates a new task category
        api_response = api_instance.create_task_category_async(tenant_id, task_category_create_dto=task_category_create_dto)
        print("The response of TaskCategoriesApi->create_task_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->create_task_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **task_category_create_dto** | [**TaskCategoryCreateDto**](TaskCategoryCreateDto.md)|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **delete_task_category_async**
> TaskCategoryDto delete_task_category_async(task_category_id, tenant_id)

Deletes a task category

Deletes the specified task category.

### Example


```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Deletes a task category
        api_response = api_instance.delete_task_category_async(task_category_id, tenant_id)
        print("The response of TaskCategoriesApi->delete_task_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->delete_task_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **get_task_category_by_id_async**
> TaskCategoryDto get_task_category_by_id_async(task_category_id, tenant_id)

Gets a task category by ID

Retrieves the details of a task category using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a task category by ID
        api_response = api_instance.get_task_category_by_id_async(task_category_id, tenant_id)
        print("The response of TaskCategoriesApi->get_task_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->get_task_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **get_task_category_task_types_async**
> TaskCategoryDto get_task_category_task_types_async(task_category_id, tenant_id)

Retrieves task types for a category

Gets all task types belonging to the specified task category.

### Example


```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves task types for a category
        api_response = api_instance.get_task_category_task_types_async(task_category_id, tenant_id)
        print("The response of TaskCategoriesApi->get_task_category_task_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->get_task_category_task_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

# **get_tenant_task_categories_async**
> TaskCategoryDtoListEnvelope get_tenant_task_categories_async(tenant_id)

Retrieves all task categories

Gets all task categories for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.task_category_dto_list_envelope import TaskCategoryDtoListEnvelope
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves all task categories
        api_response = api_instance.get_tenant_task_categories_async(tenant_id)
        print("The response of TaskCategoriesApi->get_tenant_task_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->get_tenant_task_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**TaskCategoryDtoListEnvelope**](TaskCategoryDtoListEnvelope.md)

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

# **update_task_category_async**
> TaskCategoryDto update_task_category_async(task_category_id, tenant_id, task_category_update_dto=task_category_update_dto)

Updates a task category

Updates the specified task category.

### Example


```python
import openapi_client
from openapi_client.models.task_category_dto import TaskCategoryDto
from openapi_client.models.task_category_update_dto import TaskCategoryUpdateDto
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
    api_instance = openapi_client.TaskCategoriesApi(api_client)
    task_category_id = 'task_category_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    task_category_update_dto = openapi_client.TaskCategoryUpdateDto() # TaskCategoryUpdateDto |  (optional)

    try:
        # Updates a task category
        api_response = api_instance.update_task_category_async(task_category_id, tenant_id, task_category_update_dto=task_category_update_dto)
        print("The response of TaskCategoriesApi->update_task_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskCategoriesApi->update_task_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **task_category_update_dto** | [**TaskCategoryUpdateDto**](TaskCategoryUpdateDto.md)|  | [optional] 

### Return type

[**TaskCategoryDto**](TaskCategoryDto.md)

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

