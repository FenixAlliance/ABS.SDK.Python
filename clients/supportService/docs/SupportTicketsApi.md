# openapi_client.SupportTicketsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_support_service_support_tickets_count_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_count_get) | **GET** /api/v2/SupportService/SupportTickets/Count | 
[**api_v2_support_service_support_tickets_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_get) | **GET** /api/v2/SupportService/SupportTickets | 
[**api_v2_support_service_support_tickets_post**](SupportTicketsApi.md#api_v2_support_service_support_tickets_post) | **POST** /api/v2/SupportService/SupportTickets | 
[**api_v2_support_service_support_tickets_support_ticket_id_conversations_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_conversations_get) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations | 
[**api_v2_support_service_support_tickets_support_ticket_id_conversations_post**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_conversations_post) | **POST** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations | 
[**api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete) | **DELETE** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId} | 
[**api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId} | 
[**api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId}/Messages | 
[**api_v2_support_service_support_tickets_support_ticket_id_delete**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_delete) | **DELETE** /api/v2/SupportService/SupportTickets/{supportTicketId} | 
[**api_v2_support_service_support_tickets_support_ticket_id_get**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_get) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId} | 
[**api_v2_support_service_support_tickets_support_ticket_id_put**](SupportTicketsApi.md#api_v2_support_service_support_tickets_support_ticket_id_put) | **PUT** /api/v2/SupportService/SupportTickets/{supportTicketId} | 


# **api_v2_support_service_support_tickets_count_get**
> Int32Envelope api_v2_support_service_support_tickets_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_get**
> SupportTicketDtoListEnvelope api_v2_support_service_support_tickets_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_dto_list_envelope import SupportTicketDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketDtoListEnvelope**](SupportTicketDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_post**
> EmptyEnvelope api_v2_support_service_support_tickets_post(support_ticket_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_create_dto import SupportTicketCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_create_dto = openapi_client.SupportTicketCreateDto() # SupportTicketCreateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_post(support_ticket_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_create_dto** | [**SupportTicketCreateDto**](SupportTicketCreateDto.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_support_service_support_tickets_support_ticket_id_conversations_get**
> SupportTicketConversationDtoListEnvelope api_v2_support_service_support_tickets_support_ticket_id_conversations_get(support_ticket_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_conversation_dto_list_envelope import SupportTicketConversationDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_conversations_get(support_ticket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketConversationDtoListEnvelope**](SupportTicketConversationDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_conversations_post**
> EmptyEnvelope api_v2_support_service_support_tickets_support_ticket_id_conversations_post(support_ticket_id, support_ticket_conversation_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_conversation_create_dto import SupportTicketConversationCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_create_dto = openapi_client.SupportTicketConversationCreateDto() # SupportTicketConversationCreateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_conversations_post(support_ticket_id, support_ticket_conversation_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_create_dto** | [**SupportTicketConversationCreateDto**](SupportTicketConversationCreateDto.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete**
> EmptyEnvelope api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete(support_ticket_id, support_ticket_conversation_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete(support_ticket_id, support_ticket_conversation_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get**
> SupportTicketConversationDtoEnvelope api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get(support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_conversation_dto_envelope import SupportTicketConversationDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get(support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketConversationDtoEnvelope**](SupportTicketConversationDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get**
> PrivateMessageDtoListEnvelope api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get(support_ticket_conversation_id, support_ticket_id, page_number=page_number, page_size=page_size, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.private_message_dto_list_envelope import PrivateMessageDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get(support_ticket_conversation_id, support_ticket_id, page_number=page_number, page_size=page_size, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_conversations_support_ticket_conversation_id_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_conversation_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PrivateMessageDtoListEnvelope**](PrivateMessageDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_delete**
> EmptyEnvelope api_v2_support_service_support_tickets_support_ticket_id_delete(support_ticket_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_delete(support_ticket_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_get**
> SupportTicketDtoEnvelope api_v2_support_service_support_tickets_support_ticket_id_get(support_ticket_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_dto_envelope import SupportTicketDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_get(support_ticket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketDtoEnvelope**](SupportTicketDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_tickets_support_ticket_id_put**
> EmptyEnvelope api_v2_support_service_support_tickets_support_ticket_id_put(support_ticket_id, support_ticket_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_update_dto import SupportTicketUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_update_dto = openapi_client.SupportTicketUpdateDto() # SupportTicketUpdateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_tickets_support_ticket_id_put(support_ticket_id, support_ticket_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->api_v2_support_service_support_tickets_support_ticket_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_id** | **str**|  | 
 **support_ticket_update_dto** | [**SupportTicketUpdateDto**](SupportTicketUpdateDto.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

