# openapi_client.DeliveryNotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_delivery_note_async**](DeliveryNotesApi.md#create_delivery_note_async) | **POST** /api/v2/LogisticsService/DeliveryNotes | Create a delivery note
[**delete_delivery_note_async**](DeliveryNotesApi.md#delete_delivery_note_async) | **DELETE** /api/v2/LogisticsService/DeliveryNotes/{deliveryNoteId} | Delete a delivery note
[**get_delivery_note_by_id_async**](DeliveryNotesApi.md#get_delivery_note_by_id_async) | **GET** /api/v2/LogisticsService/DeliveryNotes/{deliveryNoteId} | Get delivery note by ID
[**get_delivery_notes_async**](DeliveryNotesApi.md#get_delivery_notes_async) | **GET** /api/v2/LogisticsService/DeliveryNotes | Get all delivery notes
[**get_delivery_notes_count_async**](DeliveryNotesApi.md#get_delivery_notes_count_async) | **GET** /api/v2/LogisticsService/DeliveryNotes/Count | Get delivery notes count
[**update_delivery_note_async**](DeliveryNotesApi.md#update_delivery_note_async) | **PUT** /api/v2/LogisticsService/DeliveryNotes/{deliveryNoteId} | Update a delivery note


# **create_delivery_note_async**
> EmptyEnvelope create_delivery_note_async(tenant_id, api_version=api_version, x_api_version=x_api_version, delivery_note_create_dto=delivery_note_create_dto)

Create a delivery note

Creates a new delivery note.

### Example


```python
import openapi_client
from openapi_client.models.delivery_note_create_dto import DeliveryNoteCreateDto
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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    delivery_note_create_dto = openapi_client.DeliveryNoteCreateDto() # DeliveryNoteCreateDto |  (optional)

    try:
        # Create a delivery note
        api_response = api_instance.create_delivery_note_async(tenant_id, api_version=api_version, x_api_version=x_api_version, delivery_note_create_dto=delivery_note_create_dto)
        print("The response of DeliveryNotesApi->create_delivery_note_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->create_delivery_note_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **delivery_note_create_dto** | [**DeliveryNoteCreateDto**](DeliveryNoteCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delivery_note_async**
> EmptyEnvelope delete_delivery_note_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version)

Delete a delivery note

Deletes a delivery note.

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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    delivery_note_id = 'delivery_note_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a delivery note
        api_response = api_instance.delete_delivery_note_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DeliveryNotesApi->delete_delivery_note_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->delete_delivery_note_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **delivery_note_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_note_by_id_async**
> DeliveryNoteDtoEnvelope get_delivery_note_by_id_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version)

Get delivery note by ID

Retrieves a specific delivery note.

### Example


```python
import openapi_client
from openapi_client.models.delivery_note_dto_envelope import DeliveryNoteDtoEnvelope
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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    delivery_note_id = 'delivery_note_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get delivery note by ID
        api_response = api_instance.get_delivery_note_by_id_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DeliveryNotesApi->get_delivery_note_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->get_delivery_note_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **delivery_note_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DeliveryNoteDtoEnvelope**](DeliveryNoteDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_notes_async**
> DeliveryNoteDtoListEnvelope get_delivery_notes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all delivery notes

Retrieves all delivery notes for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.delivery_note_dto_list_envelope import DeliveryNoteDtoListEnvelope
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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all delivery notes
        api_response = api_instance.get_delivery_notes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DeliveryNotesApi->get_delivery_notes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->get_delivery_notes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DeliveryNoteDtoListEnvelope**](DeliveryNoteDtoListEnvelope.md)

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

# **get_delivery_notes_count_async**
> Int32Envelope get_delivery_notes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get delivery notes count

Returns the count of delivery notes.

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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get delivery notes count
        api_response = api_instance.get_delivery_notes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DeliveryNotesApi->get_delivery_notes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->get_delivery_notes_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_note_async**
> EmptyEnvelope update_delivery_note_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version, delivery_note_update_dto=delivery_note_update_dto)

Update a delivery note

Updates an existing delivery note.

### Example


```python
import openapi_client
from openapi_client.models.delivery_note_update_dto import DeliveryNoteUpdateDto
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
    api_instance = openapi_client.DeliveryNotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    delivery_note_id = 'delivery_note_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    delivery_note_update_dto = openapi_client.DeliveryNoteUpdateDto() # DeliveryNoteUpdateDto |  (optional)

    try:
        # Update a delivery note
        api_response = api_instance.update_delivery_note_async(tenant_id, delivery_note_id, api_version=api_version, x_api_version=x_api_version, delivery_note_update_dto=delivery_note_update_dto)
        print("The response of DeliveryNotesApi->update_delivery_note_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryNotesApi->update_delivery_note_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **delivery_note_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **delivery_note_update_dto** | [**DeliveryNoteUpdateDto**](DeliveryNoteUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

