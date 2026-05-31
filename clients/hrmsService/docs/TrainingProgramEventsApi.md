# openapi_client.TrainingProgramEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_training_program_event_async**](TrainingProgramEventsApi.md#create_training_program_event_async) | **POST** /api/v2/HrmsService/TrainingProgramEvents | Create a training program event
[**delete_training_program_event_async**](TrainingProgramEventsApi.md#delete_training_program_event_async) | **DELETE** /api/v2/HrmsService/TrainingProgramEvents/{eventId} | Delete a training program event
[**get_training_program_event_by_id_async**](TrainingProgramEventsApi.md#get_training_program_event_by_id_async) | **GET** /api/v2/HrmsService/TrainingProgramEvents/{eventId} | Get training program event by ID
[**get_training_program_events_async**](TrainingProgramEventsApi.md#get_training_program_events_async) | **GET** /api/v2/HrmsService/TrainingProgramEvents | Get training program events
[**get_training_program_events_count_async**](TrainingProgramEventsApi.md#get_training_program_events_count_async) | **GET** /api/v2/HrmsService/TrainingProgramEvents/Count | Count training program events
[**update_training_program_event_async**](TrainingProgramEventsApi.md#update_training_program_event_async) | **PUT** /api/v2/HrmsService/TrainingProgramEvents/{eventId} | Update a training program event


# **create_training_program_event_async**
> EmptyEnvelope create_training_program_event_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_event_create_dto=training_program_event_create_dto)

Create a training program event

Creates a new training program event for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_event_create_dto import TrainingProgramEventCreateDto
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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_event_create_dto = openapi_client.TrainingProgramEventCreateDto() # TrainingProgramEventCreateDto |  (optional)

    try:
        # Create a training program event
        api_response = api_instance.create_training_program_event_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_event_create_dto=training_program_event_create_dto)
        print("The response of TrainingProgramEventsApi->create_training_program_event_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->create_training_program_event_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_event_create_dto** | [**TrainingProgramEventCreateDto**](TrainingProgramEventCreateDto.md)|  | [optional] 

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

# **delete_training_program_event_async**
> EmptyEnvelope delete_training_program_event_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version)

Delete a training program event

Deletes a training program event for the specified tenant.

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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    event_id = 'event_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a training program event
        api_response = api_instance.delete_training_program_event_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramEventsApi->delete_training_program_event_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->delete_training_program_event_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **event_id** | **str**|  | 
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

# **get_training_program_event_by_id_async**
> TrainingProgramEventDtoEnvelope get_training_program_event_by_id_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version)

Get training program event by ID

Retrieves a specific training program event by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.training_program_event_dto_envelope import TrainingProgramEventDtoEnvelope
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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    event_id = 'event_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training program event by ID
        api_response = api_instance.get_training_program_event_by_id_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramEventsApi->get_training_program_event_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->get_training_program_event_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **event_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramEventDtoEnvelope**](TrainingProgramEventDtoEnvelope.md)

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

# **get_training_program_events_async**
> TrainingProgramEventDtoListEnvelope get_training_program_events_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get training program events

Retrieves training program events for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.training_program_event_dto_list_envelope import TrainingProgramEventDtoListEnvelope
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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training program events
        api_response = api_instance.get_training_program_events_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramEventsApi->get_training_program_events_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->get_training_program_events_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramEventDtoListEnvelope**](TrainingProgramEventDtoListEnvelope.md)

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

# **get_training_program_events_count_async**
> Int32Envelope get_training_program_events_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count training program events

Counts training program events for the specified tenant.

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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count training program events
        api_response = api_instance.get_training_program_events_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramEventsApi->get_training_program_events_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->get_training_program_events_count_async: %s\n" % e)
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

# **update_training_program_event_async**
> EmptyEnvelope update_training_program_event_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version, training_program_event_update_dto=training_program_event_update_dto)

Update a training program event

Updates an existing training program event for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_event_update_dto import TrainingProgramEventUpdateDto
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
    api_instance = openapi_client.TrainingProgramEventsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    event_id = 'event_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_event_update_dto = openapi_client.TrainingProgramEventUpdateDto() # TrainingProgramEventUpdateDto |  (optional)

    try:
        # Update a training program event
        api_response = api_instance.update_training_program_event_async(tenant_id, event_id, api_version=api_version, x_api_version=x_api_version, training_program_event_update_dto=training_program_event_update_dto)
        print("The response of TrainingProgramEventsApi->update_training_program_event_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramEventsApi->update_training_program_event_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **event_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_event_update_dto** | [**TrainingProgramEventUpdateDto**](TrainingProgramEventUpdateDto.md)|  | [optional] 

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

