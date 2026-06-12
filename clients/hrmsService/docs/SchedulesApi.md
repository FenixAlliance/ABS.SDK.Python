# openapi_client.SchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_async**](SchedulesApi.md#create_schedule_async) | **POST** /api/v2/HrmsService/Schedules | Create a schedule
[**delete_schedule_async**](SchedulesApi.md#delete_schedule_async) | **DELETE** /api/v2/HrmsService/Schedules/{scheduleId} | Delete a schedule
[**get_schedule_by_id_async**](SchedulesApi.md#get_schedule_by_id_async) | **GET** /api/v2/HrmsService/Schedules/{scheduleId} | Get schedule by ID
[**get_schedules_async**](SchedulesApi.md#get_schedules_async) | **GET** /api/v2/HrmsService/Schedules | Get schedules
[**get_schedules_count_async**](SchedulesApi.md#get_schedules_count_async) | **GET** /api/v2/HrmsService/Schedules/Count | Count schedules
[**patch_schedule_async**](SchedulesApi.md#patch_schedule_async) | **PATCH** /api/v2/HrmsService/Schedules/{scheduleId} | Patch a schedule
[**update_schedule_async**](SchedulesApi.md#update_schedule_async) | **PUT** /api/v2/HrmsService/Schedules/{scheduleId} | Update a schedule


# **create_schedule_async**
> EmptyEnvelope create_schedule_async(tenant_id, api_version=api_version, x_api_version=x_api_version, schedule_create_dto=schedule_create_dto)

Create a schedule

Creates a new schedule for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.schedule_create_dto import ScheduleCreateDto
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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    schedule_create_dto = openapi_client.ScheduleCreateDto() # ScheduleCreateDto |  (optional)

    try:
        # Create a schedule
        api_response = api_instance.create_schedule_async(tenant_id, api_version=api_version, x_api_version=x_api_version, schedule_create_dto=schedule_create_dto)
        print("The response of SchedulesApi->create_schedule_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->create_schedule_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **schedule_create_dto** | [**ScheduleCreateDto**](ScheduleCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_async**
> EmptyEnvelope delete_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version)

Delete a schedule

Deletes a schedule for the specified tenant.

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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    schedule_id = 'schedule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a schedule
        api_response = api_instance.delete_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SchedulesApi->delete_schedule_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->delete_schedule_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **schedule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_by_id_async**
> ScheduleDtoEnvelope get_schedule_by_id_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version)

Get schedule by ID

Retrieves a specific schedule by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.schedule_dto_envelope import ScheduleDtoEnvelope
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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    schedule_id = 'schedule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get schedule by ID
        api_response = api_instance.get_schedule_by_id_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SchedulesApi->get_schedule_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedule_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **schedule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ScheduleDtoEnvelope**](ScheduleDtoEnvelope.md)

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

# **get_schedules_async**
> ScheduleDtoListEnvelope get_schedules_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get schedules

Retrieves schedules for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.schedule_dto_list_envelope import ScheduleDtoListEnvelope
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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get schedules
        api_response = api_instance.get_schedules_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SchedulesApi->get_schedules_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedules_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ScheduleDtoListEnvelope**](ScheduleDtoListEnvelope.md)

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

# **get_schedules_count_async**
> Int32Envelope get_schedules_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count schedules

Counts schedules for the specified tenant.

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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count schedules
        api_response = api_instance.get_schedules_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SchedulesApi->get_schedules_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedules_count_async: %s\n" % e)
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

# **patch_schedule_async**
> EmptyEnvelope patch_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a schedule

Partially updates an existing schedule for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    schedule_id = 'schedule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a schedule
        api_response = api_instance.patch_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of SchedulesApi->patch_schedule_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->patch_schedule_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **schedule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule_async**
> EmptyEnvelope update_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version, schedule_update_dto=schedule_update_dto)

Update a schedule

Updates an existing schedule for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.schedule_update_dto import ScheduleUpdateDto
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
    api_instance = openapi_client.SchedulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    schedule_id = 'schedule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    schedule_update_dto = openapi_client.ScheduleUpdateDto() # ScheduleUpdateDto |  (optional)

    try:
        # Update a schedule
        api_response = api_instance.update_schedule_async(tenant_id, schedule_id, api_version=api_version, x_api_version=x_api_version, schedule_update_dto=schedule_update_dto)
        print("The response of SchedulesApi->update_schedule_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->update_schedule_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **schedule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **schedule_update_dto** | [**ScheduleUpdateDto**](ScheduleUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

