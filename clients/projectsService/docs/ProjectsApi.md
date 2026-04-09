# openapi_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_async**](ProjectsApi.md#create_project_async) | **POST** /api/v2/ProjectsService/Projects | Creates a new project
[**create_project_period_async**](ProjectsApi.md#create_project_period_async) | **POST** /api/v2/ProjectsService/Projects/{projectId}/Periods | Creates a project period
[**create_project_task_async**](ProjectsApi.md#create_project_task_async) | **POST** /api/v2/ProjectsService/Projects/{projectId}/Tasks | Creates a project task
[**delete_project_async**](ProjectsApi.md#delete_project_async) | **DELETE** /api/v2/ProjectsService/Projects/{projectId} | Deletes a project
[**delete_project_period_async**](ProjectsApi.md#delete_project_period_async) | **DELETE** /api/v2/ProjectsService/Projects/{projectId}/Periods/{projectPeriodId} | Deletes a project period
[**delete_project_task_async**](ProjectsApi.md#delete_project_task_async) | **DELETE** /api/v2/ProjectsService/Projects/{projectId}/Tasks/{projectTaskId} | Deletes a project task
[**get_project_by_id_async**](ProjectsApi.md#get_project_by_id_async) | **GET** /api/v2/ProjectsService/Projects/{projectId} | Gets a project by ID
[**get_project_periods_async**](ProjectsApi.md#get_project_periods_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Periods | Retrieves project periods
[**get_project_task_categories_async**](ProjectsApi.md#get_project_task_categories_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TaskCategories | Retrieves project task categories
[**get_project_task_categories_count_async**](ProjectsApi.md#get_project_task_categories_count_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TaskCategories/Count | Counts project task categories
[**get_project_tasks_async**](ProjectsApi.md#get_project_tasks_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Tasks | Retrieves project tasks
[**get_project_tasks_count_async**](ProjectsApi.md#get_project_tasks_count_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/Tasks/Count | Counts project tasks
[**get_project_time_logs_async**](ProjectsApi.md#get_project_time_logs_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TimeLogs | Retrieves project time logs
[**get_project_time_logs_count_async**](ProjectsApi.md#get_project_time_logs_count_async) | **GET** /api/v2/ProjectsService/Projects/{projectId}/TimeLogs/Count | Counts project time logs
[**get_projects_by_tenant_id_async**](ProjectsApi.md#get_projects_by_tenant_id_async) | **GET** /api/v2/ProjectsService/Projects | Retrieves all projects
[**get_projects_count_by_tenant_id_async**](ProjectsApi.md#get_projects_count_by_tenant_id_async) | **GET** /api/v2/ProjectsService/Projects/Count | Counts projects
[**update_project_async**](ProjectsApi.md#update_project_async) | **PUT** /api/v2/ProjectsService/Projects/{projectId} | Updates a project
[**update_project_period_async**](ProjectsApi.md#update_project_period_async) | **PUT** /api/v2/ProjectsService/Projects/{projectId}/Periods/{projectPeriodId} | Updates a project period
[**update_project_task_async**](ProjectsApi.md#update_project_task_async) | **PUT** /api/v2/ProjectsService/Projects/{projectId}/Tasks/{projectTaskId} | Updates a project task


# **create_project_async**
> EmptyEnvelope create_project_async(tenant_id, project_create_dto=project_create_dto)

Creates a new project

Creates a new project for the current tenant.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_create_dto = openapi_client.ProjectCreateDto() # ProjectCreateDto |  (optional)

    try:
        # Creates a new project
        api_response = api_instance.create_project_async(tenant_id, project_create_dto=project_create_dto)
        print("The response of ProjectsApi->create_project_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_create_dto** | [**ProjectCreateDto**](ProjectCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_period_async**
> EmptyEnvelope create_project_period_async(project_id, tenant_id, project_period_create_dto=project_period_create_dto)

Creates a project period

Creates a new period for the specified project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    project_period_create_dto = openapi_client.ProjectPeriodCreateDto() # ProjectPeriodCreateDto |  (optional)

    try:
        # Creates a project period
        api_response = api_instance.create_project_period_async(project_id, tenant_id, project_period_create_dto=project_period_create_dto)
        print("The response of ProjectsApi->create_project_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **project_period_create_dto** | [**ProjectPeriodCreateDto**](ProjectPeriodCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_task_async**
> EmptyEnvelope create_project_task_async(project_id, tenant_id, project_task_create_dto=project_task_create_dto)

Creates a project task

Creates a new task for the specified project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    project_task_create_dto = openapi_client.ProjectTaskCreateDto() # ProjectTaskCreateDto |  (optional)

    try:
        # Creates a project task
        api_response = api_instance.create_project_task_async(project_id, tenant_id, project_task_create_dto=project_task_create_dto)
        print("The response of ProjectsApi->create_project_task_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_task_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **project_task_create_dto** | [**ProjectTaskCreateDto**](ProjectTaskCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_async**
> EmptyEnvelope delete_project_async(project_id, tenant_id)

Deletes a project

Deletes the specified project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Deletes a project
        api_response = api_instance.delete_project_async(project_id, tenant_id)
        print("The response of ProjectsApi->delete_project_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_period_async**
> EmptyEnvelope delete_project_period_async(project_id, project_period_id, tenant_id)

Deletes a project period

Deletes the specified period from a project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Deletes a project period
        api_response = api_instance.delete_project_period_async(project_id, project_period_id, tenant_id)
        print("The response of ProjectsApi->delete_project_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_task_async**
> EmptyEnvelope delete_project_task_async(tenant_id, project_id, project_task_id)

Deletes a project task

Deletes the specified task from a project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_id = 'project_id_example' # str | 
    project_task_id = 'project_task_id_example' # str | 

    try:
        # Deletes a project task
        api_response = api_instance.delete_project_task_async(tenant_id, project_id, project_task_id)
        print("The response of ProjectsApi->delete_project_task_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_task_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_id** | **str**|  | 
 **project_task_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id_async**
> ProjectDtoEnvelope get_project_by_id_async(project_id, tenant_id)

Gets a project by ID

Retrieves the details of a project using its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a project by ID
        api_response = api_instance.get_project_by_id_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**ProjectDtoEnvelope**](ProjectDtoEnvelope.md)

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

# **get_project_periods_async**
> ProjectPeriodDtoListEnvelope get_project_periods_async(project_id, tenant_id)

Retrieves project periods

Gets all periods for a specific project.

### Example


```python
import openapi_client
from openapi_client.models.project_period_dto_list_envelope import ProjectPeriodDtoListEnvelope
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves project periods
        api_response = api_instance.get_project_periods_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_periods_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_periods_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**ProjectPeriodDtoListEnvelope**](ProjectPeriodDtoListEnvelope.md)

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

# **get_project_task_categories_async**
> TaskCategoryDtoListEnvelope get_project_task_categories_async(project_id, tenant_id)

Retrieves project task categories

Gets all task categories for a specific project with OData support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves project task categories
        api_response = api_instance.get_project_task_categories_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_task_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_task_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **get_project_task_categories_count_async**
> Int32Envelope get_project_task_categories_count_async(project_id, tenant_id)

Counts project task categories

Gets the count of task categories for a specific project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts project task categories
        api_response = api_instance.get_project_task_categories_count_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_task_categories_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_task_categories_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **get_project_tasks_async**
> ProjectTaskDtoListEnvelope get_project_tasks_async(project_id, tenant_id)

Retrieves project tasks

Gets all tasks for a specific project with OData support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves project tasks
        api_response = api_instance.get_project_tasks_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_tasks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_tasks_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**ProjectTaskDtoListEnvelope**](ProjectTaskDtoListEnvelope.md)

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

# **get_project_tasks_count_async**
> Int32Envelope get_project_tasks_count_async(project_id, tenant_id)

Counts project tasks

Gets the count of tasks for a specific project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts project tasks
        api_response = api_instance.get_project_tasks_count_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_tasks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_tasks_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **get_project_time_logs_async**
> ProjectTimeLogDtoListEnvelope get_project_time_logs_async(project_id, tenant_id)

Retrieves project time logs

Gets all time log entries for a specific project with OData support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves project time logs
        api_response = api_instance.get_project_time_logs_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_time_logs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_time_logs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

# **get_project_time_logs_count_async**
> Int32Envelope get_project_time_logs_count_async(project_id, tenant_id)

Counts project time logs

Gets the count of time log entries for a specific project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts project time logs
        api_response = api_instance.get_project_time_logs_count_async(project_id, tenant_id)
        print("The response of ProjectsApi->get_project_time_logs_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_time_logs_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **get_projects_by_tenant_id_async**
> ProjectDtoListEnvelope get_projects_by_tenant_id_async(tenant_id)

Retrieves all projects

Gets all projects for the current tenant with OData support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves all projects
        api_response = api_instance.get_projects_by_tenant_id_async(tenant_id)
        print("The response of ProjectsApi->get_projects_by_tenant_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_by_tenant_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ProjectDtoListEnvelope**](ProjectDtoListEnvelope.md)

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

# **get_projects_count_by_tenant_id_async**
> Int32Envelope get_projects_count_by_tenant_id_async(tenant_id)

Counts projects

Gets the count of projects for the current tenant.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts projects
        api_response = api_instance.get_projects_count_by_tenant_id_async(tenant_id)
        print("The response of ProjectsApi->get_projects_count_by_tenant_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_count_by_tenant_id_async: %s\n" % e)
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

# **update_project_async**
> EmptyEnvelope update_project_async(project_id, tenant_id, project_update_dto=project_update_dto)

Updates a project

Updates the specified project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    project_update_dto = openapi_client.ProjectUpdateDto() # ProjectUpdateDto |  (optional)

    try:
        # Updates a project
        api_response = api_instance.update_project_async(project_id, tenant_id, project_update_dto=project_update_dto)
        print("The response of ProjectsApi->update_project_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **project_update_dto** | [**ProjectUpdateDto**](ProjectUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_period_async**
> EmptyEnvelope update_project_period_async(project_id, project_period_id, tenant_id, project_period_update_dto=project_period_update_dto)

Updates a project period

Updates the specified period for a project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    project_period_update_dto = openapi_client.ProjectPeriodUpdateDto() # ProjectPeriodUpdateDto |  (optional)

    try:
        # Updates a project period
        api_response = api_instance.update_project_period_async(project_id, project_period_id, tenant_id, project_period_update_dto=project_period_update_dto)
        print("The response of ProjectsApi->update_project_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **project_period_update_dto** | [**ProjectPeriodUpdateDto**](ProjectPeriodUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_task_async**
> EmptyEnvelope update_project_task_async(project_id, project_task_id, tenant_id, project_task_update_dto=project_task_update_dto)

Updates a project task

Updates the specified task in a project.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_task_id = 'project_task_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    project_task_update_dto = openapi_client.ProjectTaskUpdateDto() # ProjectTaskUpdateDto |  (optional)

    try:
        # Updates a project task
        api_response = api_instance.update_project_task_async(project_id, project_task_id, tenant_id, project_task_update_dto=project_task_update_dto)
        print("The response of ProjectsApi->update_project_task_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_task_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_task_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **project_task_update_dto** | [**ProjectTaskUpdateDto**](ProjectTaskUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

