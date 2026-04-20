# openapi_client.SupportTicketTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_ticket_type_async**](SupportTicketTypesApi.md#create_support_ticket_type_async) | **POST** /api/v2/SupportService/SupportTicketTypes | Create a new support ticket type
[**delete_support_ticket_type_async**](SupportTicketTypesApi.md#delete_support_ticket_type_async) | **DELETE** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | Delete a support ticket type
[**get_support_ticket_type_async**](SupportTicketTypesApi.md#get_support_ticket_type_async) | **GET** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | Retrieve a support ticket type by ID
[**get_support_ticket_types_async**](SupportTicketTypesApi.md#get_support_ticket_types_async) | **GET** /api/v2/SupportService/SupportTicketTypes | Retrieve a list of support ticket types
[**get_support_ticket_types_count_async**](SupportTicketTypesApi.md#get_support_ticket_types_count_async) | **GET** /api/v2/SupportService/SupportTicketTypes/Count | Get the count of support ticket types
[**update_support_ticket_type_async**](SupportTicketTypesApi.md#update_support_ticket_type_async) | **PUT** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | Update a support ticket type


# **create_support_ticket_type_async**
> EmptyEnvelope create_support_ticket_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_type_create_dto=support_ticket_type_create_dto)

Create a new support ticket type

Creates a new support ticket type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_type_create_dto import SupportTicketTypeCreateDto
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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_type_create_dto = openapi_client.SupportTicketTypeCreateDto() # SupportTicketTypeCreateDto |  (optional)

    try:
        # Create a new support ticket type
        api_response = api_instance.create_support_ticket_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_type_create_dto=support_ticket_type_create_dto)
        print("The response of SupportTicketTypesApi->create_support_ticket_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->create_support_ticket_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_type_create_dto** | [**SupportTicketTypeCreateDto**](SupportTicketTypeCreateDto.md)|  | [optional] 

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

# **delete_support_ticket_type_async**
> EmptyEnvelope delete_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a support ticket type

Deletes a support ticket type by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support ticket type
        api_response = api_instance.delete_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->delete_support_ticket_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->delete_support_ticket_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_type_id** | **str**|  | 
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

# **get_support_ticket_type_async**
> SupportTicketTypeDtoEnvelope get_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support ticket type by ID

Retrieves a single support ticket type by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.support_ticket_type_dto_envelope import SupportTicketTypeDtoEnvelope
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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support ticket type by ID
        api_response = api_instance.get_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->get_support_ticket_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->get_support_ticket_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketTypeDtoEnvelope**](SupportTicketTypeDtoEnvelope.md)

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

# **get_support_ticket_types_async**
> SupportTicketTypeDtoListEnvelope get_support_ticket_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support ticket types

Retrieves a list of support ticket types for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.support_ticket_type_dto_list_envelope import SupportTicketTypeDtoListEnvelope
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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support ticket types
        api_response = api_instance.get_support_ticket_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->get_support_ticket_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->get_support_ticket_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketTypeDtoListEnvelope**](SupportTicketTypeDtoListEnvelope.md)

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

# **get_support_ticket_types_count_async**
> Int32Envelope get_support_ticket_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support ticket types

Returns the total count of support ticket types for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support ticket types
        api_response = api_instance.get_support_ticket_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->get_support_ticket_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->get_support_ticket_types_count_async: %s\n" % e)
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

# **update_support_ticket_type_async**
> EmptyEnvelope update_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version, support_ticket_type_update_dto=support_ticket_type_update_dto)

Update a support ticket type

Updates an existing support ticket type by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_type_update_dto import SupportTicketTypeUpdateDto
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
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_type_update_dto = openapi_client.SupportTicketTypeUpdateDto() # SupportTicketTypeUpdateDto |  (optional)

    try:
        # Update a support ticket type
        api_response = api_instance.update_support_ticket_type_async(tenant_id, support_ticket_type_id, api_version=api_version, x_api_version=x_api_version, support_ticket_type_update_dto=support_ticket_type_update_dto)
        print("The response of SupportTicketTypesApi->update_support_ticket_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->update_support_ticket_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_type_update_dto** | [**SupportTicketTypeUpdateDto**](SupportTicketTypeUpdateDto.md)|  | [optional] 

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

