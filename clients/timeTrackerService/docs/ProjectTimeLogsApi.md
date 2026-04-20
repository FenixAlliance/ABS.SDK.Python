# openapi_client.ProjectTimeLogsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_project_period_time_logs_async**](ProjectTimeLogsApi.md#count_project_period_time_logs_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/Count | Get the count of project period time logs
[**create_project_time_log_async**](ProjectTimeLogsApi.md#create_project_time_log_async) | **POST** /api/v2/TimeTrackerService/ProjectTimeLogs | Create a new project time log
[**delete_project_time_log_async**](ProjectTimeLogsApi.md#delete_project_time_log_async) | **DELETE** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | Delete a project time log
[**get_project_period_time_logs_async**](ProjectTimeLogsApi.md#get_project_period_time_logs_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs | Retrieve project period time logs
[**get_project_time_log_by_id_async**](ProjectTimeLogsApi.md#get_project_time_log_by_id_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | Retrieve a project time log by ID
[**get_project_time_logs_async**](ProjectTimeLogsApi.md#get_project_time_logs_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/ForProject/{projectId} | Retrieve time logs for a project
[**get_project_time_logs_by_responsible_contact_async**](ProjectTimeLogsApi.md#get_project_time_logs_by_responsible_contact_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/ByResponsibleContact | Retrieve time logs by responsible contact
[**get_project_time_logs_created_by_contact_async**](ProjectTimeLogsApi.md#get_project_time_logs_created_by_contact_async) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/CreatedByContact | Retrieve time logs created by a contact
[**update_project_time_log_async**](ProjectTimeLogsApi.md#update_project_time_log_async) | **PUT** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | Update a project time log


# **count_project_period_time_logs_async**
> Int32Envelope count_project_period_time_logs_async(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)

Get the count of project period time logs

Returns the total count of time logs for a specific project period with OData query support.

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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of project period time logs
        api_response = api_instance.count_project_period_time_logs_async(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->count_project_period_time_logs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->count_project_period_time_logs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_period_id** | **str**|  | 
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

# **create_project_time_log_async**
> create_project_time_log_async(tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_create_dto=project_time_log_create_dto)

Create a new project time log

Creates a new project time log entry.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_create_dto import ProjectTimeLogCreateDto
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_time_log_create_dto = openapi_client.ProjectTimeLogCreateDto() # ProjectTimeLogCreateDto |  (optional)

    try:
        # Create a new project time log
        api_instance.create_project_time_log_async(tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_create_dto=project_time_log_create_dto)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->create_project_time_log_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_time_log_create_dto** | [**ProjectTimeLogCreateDto**](ProjectTimeLogCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_time_log_async**
> delete_project_time_log_async(tenant_id, time_log_id, api_version=api_version, x_api_version=x_api_version)

Delete a project time log

Deletes a project time log entry.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_log_id = 'time_log_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a project time log
        api_instance.delete_project_time_log_async(tenant_id, time_log_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->delete_project_time_log_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_log_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_period_time_logs_async**
> ProjectTimeLogDtoListEnvelope get_project_period_time_logs_async(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)

Retrieve project period time logs

Retrieves a list of time logs for a specific project period with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve project period time logs
        api_response = api_instance.get_project_period_time_logs_async(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->get_project_period_time_logs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->get_project_period_time_logs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **get_project_time_log_by_id_async**
> ProjectTimeLogDtoEnvelope get_project_time_log_by_id_async(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a project time log by ID

Retrieves a single project time log by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_dto_envelope import ProjectTimeLogDtoEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    time_log_id = 'time_log_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a project time log by ID
        api_response = api_instance.get_project_time_log_by_id_async(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->get_project_time_log_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->get_project_time_log_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_log_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoEnvelope**](ProjectTimeLogDtoEnvelope.md)

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
> ProjectTimeLogDtoListEnvelope get_project_time_logs_async(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve time logs for a project

Retrieves all time logs associated with the specified project.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve time logs for a project
        api_response = api_instance.get_project_time_logs_async(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->get_project_time_logs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->get_project_time_logs_async: %s\n" % e)
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

# **get_project_time_logs_by_responsible_contact_async**
> ProjectTimeLogDtoListEnvelope get_project_time_logs_by_responsible_contact_async(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve time logs by responsible contact

Retrieves time logs where the specified contact is the responsible party.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve time logs by responsible contact
        api_response = api_instance.get_project_time_logs_by_responsible_contact_async(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->get_project_time_logs_by_responsible_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->get_project_time_logs_by_responsible_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **get_project_time_logs_created_by_contact_async**
> ProjectTimeLogDtoListEnvelope get_project_time_logs_created_by_contact_async(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve time logs created by a contact

Retrieves time logs that were created by the specified contact.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve time logs created by a contact
        api_response = api_instance.get_project_time_logs_created_by_contact_async(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->get_project_time_logs_created_by_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->get_project_time_logs_created_by_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **update_project_time_log_async**
> update_project_time_log_async(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_update_dto=project_time_log_update_dto)

Update a project time log

Updates an existing project time log entry.

### Example


```python
import openapi_client
from openapi_client.models.project_time_log_update_dto import ProjectTimeLogUpdateDto
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    time_log_id = 'time_log_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_time_log_update_dto = openapi_client.ProjectTimeLogUpdateDto() # ProjectTimeLogUpdateDto |  (optional)

    try:
        # Update a project time log
        api_instance.update_project_time_log_async(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_update_dto=project_time_log_update_dto)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->update_project_time_log_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_log_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_time_log_update_dto** | [**ProjectTimeLogUpdateDto**](ProjectTimeLogUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

