# openapi_client.SupportTicketPrioritiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_ticket_priority_async**](SupportTicketPrioritiesApi.md#create_support_ticket_priority_async) | **POST** /api/v2/SupportService/SupportTicketPriorities | Create a new support ticket priority
[**delete_support_ticket_priority_async**](SupportTicketPrioritiesApi.md#delete_support_ticket_priority_async) | **DELETE** /api/v2/SupportService/SupportTicketPriorities/{supportTicketPriorityId} | Delete a support ticket priority
[**get_support_ticket_priorities_async**](SupportTicketPrioritiesApi.md#get_support_ticket_priorities_async) | **GET** /api/v2/SupportService/SupportTicketPriorities | Retrieve a list of support ticket priorities
[**get_support_ticket_priorities_count_async**](SupportTicketPrioritiesApi.md#get_support_ticket_priorities_count_async) | **GET** /api/v2/SupportService/SupportTicketPriorities/Count | Get the count of support ticket priorities
[**get_support_ticket_priority_async**](SupportTicketPrioritiesApi.md#get_support_ticket_priority_async) | **GET** /api/v2/SupportService/SupportTicketPriorities/{supportTicketPriorityId} | Retrieve a support ticket priority by ID
[**update_support_ticket_priority_async**](SupportTicketPrioritiesApi.md#update_support_ticket_priority_async) | **PUT** /api/v2/SupportService/SupportTicketPriorities/{supportTicketPriorityId} | Update a support ticket priority


# **create_support_ticket_priority_async**
> EmptyEnvelope create_support_ticket_priority_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_priority_create_dto=support_ticket_priority_create_dto)

Create a new support ticket priority

Creates a new support ticket priority for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_priority_create_dto import SupportTicketPriorityCreateDto
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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_priority_create_dto = openapi_client.SupportTicketPriorityCreateDto() # SupportTicketPriorityCreateDto |  (optional)

    try:
        # Create a new support ticket priority
        api_response = api_instance.create_support_ticket_priority_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_priority_create_dto=support_ticket_priority_create_dto)
        print("The response of SupportTicketPrioritiesApi->create_support_ticket_priority_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->create_support_ticket_priority_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_priority_create_dto** | [**SupportTicketPriorityCreateDto**](SupportTicketPriorityCreateDto.md)|  | [optional] 

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

# **delete_support_ticket_priority_async**
> EmptyEnvelope delete_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version)

Delete a support ticket priority

Deletes a support ticket priority by its unique identifier.

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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_priority_id = 'support_ticket_priority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support ticket priority
        api_response = api_instance.delete_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketPrioritiesApi->delete_support_ticket_priority_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->delete_support_ticket_priority_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_priority_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_ticket_priorities_async**
> SupportTicketPriorityDtoListEnvelope get_support_ticket_priorities_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support ticket priorities

Retrieves a list of support ticket priorities for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.support_ticket_priority_dto_list_envelope import SupportTicketPriorityDtoListEnvelope
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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support ticket priorities
        api_response = api_instance.get_support_ticket_priorities_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketPrioritiesApi->get_support_ticket_priorities_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->get_support_ticket_priorities_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketPriorityDtoListEnvelope**](SupportTicketPriorityDtoListEnvelope.md)

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

# **get_support_ticket_priorities_count_async**
> Int32Envelope get_support_ticket_priorities_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support ticket priorities

Returns the total count of support ticket priorities for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support ticket priorities
        api_response = api_instance.get_support_ticket_priorities_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketPrioritiesApi->get_support_ticket_priorities_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->get_support_ticket_priorities_count_async: %s\n" % e)
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

# **get_support_ticket_priority_async**
> SupportTicketPriorityDtoEnvelope get_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support ticket priority by ID

Retrieves a single support ticket priority by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.support_ticket_priority_dto_envelope import SupportTicketPriorityDtoEnvelope
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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_priority_id = 'support_ticket_priority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support ticket priority by ID
        api_response = api_instance.get_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketPrioritiesApi->get_support_ticket_priority_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->get_support_ticket_priority_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_priority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketPriorityDtoEnvelope**](SupportTicketPriorityDtoEnvelope.md)

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

# **update_support_ticket_priority_async**
> EmptyEnvelope update_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version, support_ticket_priority_update_dto=support_ticket_priority_update_dto)

Update a support ticket priority

Updates an existing support ticket priority by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_priority_update_dto import SupportTicketPriorityUpdateDto
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
    api_instance = openapi_client.SupportTicketPrioritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_priority_id = 'support_ticket_priority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_priority_update_dto = openapi_client.SupportTicketPriorityUpdateDto() # SupportTicketPriorityUpdateDto |  (optional)

    try:
        # Update a support ticket priority
        api_response = api_instance.update_support_ticket_priority_async(tenant_id, support_ticket_priority_id, api_version=api_version, x_api_version=x_api_version, support_ticket_priority_update_dto=support_ticket_priority_update_dto)
        print("The response of SupportTicketPrioritiesApi->update_support_ticket_priority_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketPrioritiesApi->update_support_ticket_priority_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_priority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_priority_update_dto** | [**SupportTicketPriorityUpdateDto**](SupportTicketPriorityUpdateDto.md)|  | [optional] 

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

