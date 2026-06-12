# openapi_client.TimeIntervalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_interval_async**](TimeIntervalsApi.md#create_time_interval_async) | **POST** /api/v2/HrmsService/TimeIntervals | Create a time interval
[**delete_time_interval_async**](TimeIntervalsApi.md#delete_time_interval_async) | **DELETE** /api/v2/HrmsService/TimeIntervals/{timeIntervalId} | Delete a time interval
[**get_time_interval_by_id_async**](TimeIntervalsApi.md#get_time_interval_by_id_async) | **GET** /api/v2/HrmsService/TimeIntervals/{timeIntervalId} | Get time interval by ID
[**get_time_intervals_async**](TimeIntervalsApi.md#get_time_intervals_async) | **GET** /api/v2/HrmsService/TimeIntervals | Get time intervals
[**get_time_intervals_count_async**](TimeIntervalsApi.md#get_time_intervals_count_async) | **GET** /api/v2/HrmsService/TimeIntervals/Count | Count time intervals
[**patch_time_interval_async**](TimeIntervalsApi.md#patch_time_interval_async) | **PATCH** /api/v2/HrmsService/TimeIntervals/{timeIntervalId} | Patch a time interval
[**update_time_interval_async**](TimeIntervalsApi.md#update_time_interval_async) | **PUT** /api/v2/HrmsService/TimeIntervals/{timeIntervalId} | Update a time interval


# **create_time_interval_async**
> EmptyEnvelope create_time_interval_async(tenant_id, api_version=api_version, x_api_version=x_api_version, time_interval_create_dto=time_interval_create_dto)

Create a time interval

Creates a new time interval for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.time_interval_create_dto import TimeIntervalCreateDto
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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    time_interval_create_dto = openapi_client.TimeIntervalCreateDto() # TimeIntervalCreateDto |  (optional)

    try:
        # Create a time interval
        api_response = api_instance.create_time_interval_async(tenant_id, api_version=api_version, x_api_version=x_api_version, time_interval_create_dto=time_interval_create_dto)
        print("The response of TimeIntervalsApi->create_time_interval_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->create_time_interval_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **time_interval_create_dto** | [**TimeIntervalCreateDto**](TimeIntervalCreateDto.md)|  | [optional] 

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

# **delete_time_interval_async**
> EmptyEnvelope delete_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version)

Delete a time interval

Deletes a time interval for the specified tenant.

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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_interval_id = 'time_interval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a time interval
        api_response = api_instance.delete_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TimeIntervalsApi->delete_time_interval_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->delete_time_interval_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_interval_id** | **str**|  | 
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

# **get_time_interval_by_id_async**
> TimeIntervalDtoEnvelope get_time_interval_by_id_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version)

Get time interval by ID

Retrieves a specific time interval by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.time_interval_dto_envelope import TimeIntervalDtoEnvelope
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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_interval_id = 'time_interval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get time interval by ID
        api_response = api_instance.get_time_interval_by_id_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TimeIntervalsApi->get_time_interval_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->get_time_interval_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_interval_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TimeIntervalDtoEnvelope**](TimeIntervalDtoEnvelope.md)

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

# **get_time_intervals_async**
> TimeIntervalDtoListEnvelope get_time_intervals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get time intervals

Retrieves time intervals for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.time_interval_dto_list_envelope import TimeIntervalDtoListEnvelope
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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get time intervals
        api_response = api_instance.get_time_intervals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TimeIntervalsApi->get_time_intervals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->get_time_intervals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TimeIntervalDtoListEnvelope**](TimeIntervalDtoListEnvelope.md)

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

# **get_time_intervals_count_async**
> Int32Envelope get_time_intervals_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count time intervals

Counts time intervals for the specified tenant.

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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count time intervals
        api_response = api_instance.get_time_intervals_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TimeIntervalsApi->get_time_intervals_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->get_time_intervals_count_async: %s\n" % e)
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

# **patch_time_interval_async**
> EmptyEnvelope patch_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a time interval

Partially updates an existing time interval for the specified tenant.

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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_interval_id = 'time_interval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a time interval
        api_response = api_instance.patch_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TimeIntervalsApi->patch_time_interval_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->patch_time_interval_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_interval_id** | **str**|  | 
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

# **update_time_interval_async**
> EmptyEnvelope update_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version, time_interval_update_dto=time_interval_update_dto)

Update a time interval

Updates an existing time interval for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.time_interval_update_dto import TimeIntervalUpdateDto
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
    api_instance = openapi_client.TimeIntervalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_interval_id = 'time_interval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    time_interval_update_dto = openapi_client.TimeIntervalUpdateDto() # TimeIntervalUpdateDto |  (optional)

    try:
        # Update a time interval
        api_response = api_instance.update_time_interval_async(tenant_id, time_interval_id, api_version=api_version, x_api_version=x_api_version, time_interval_update_dto=time_interval_update_dto)
        print("The response of TimeIntervalsApi->update_time_interval_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeIntervalsApi->update_time_interval_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_interval_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **time_interval_update_dto** | [**TimeIntervalUpdateDto**](TimeIntervalUpdateDto.md)|  | [optional] 

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

