# openapi_client.SupportTicketsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_ticket_async**](SupportTicketsApi.md#create_support_ticket_async) | **POST** /api/v2/SupportService/SupportTickets | Create a new support ticket
[**delete_support_ticket_async**](SupportTicketsApi.md#delete_support_ticket_async) | **DELETE** /api/v2/SupportService/SupportTickets/{supportTicketId} | Delete a support ticket
[**delete_support_ticket_conversation_async**](SupportTicketsApi.md#delete_support_ticket_conversation_async) | **DELETE** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId} | Delete a conversation from a support ticket
[**get_support_ticket_async**](SupportTicketsApi.md#get_support_ticket_async) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId} | Retrieve a support ticket by ID
[**get_support_ticket_conversation_async**](SupportTicketsApi.md#get_support_ticket_conversation_async) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId} | Retrieve a specific conversation for a support ticket
[**get_support_ticket_conversation_messages_async**](SupportTicketsApi.md#get_support_ticket_conversation_messages_async) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations/{supportTicketConversationId}/Messages | Retrieve messages for a support ticket conversation
[**get_support_ticket_conversations_async**](SupportTicketsApi.md#get_support_ticket_conversations_async) | **GET** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations | Retrieve conversations for a support ticket
[**get_support_tickets_async**](SupportTicketsApi.md#get_support_tickets_async) | **GET** /api/v2/SupportService/SupportTickets | Retrieve a list of support tickets
[**get_support_tickets_count_async**](SupportTicketsApi.md#get_support_tickets_count_async) | **GET** /api/v2/SupportService/SupportTickets/Count | Get the count of support tickets
[**relate_support_ticket_to_conversation_async**](SupportTicketsApi.md#relate_support_ticket_to_conversation_async) | **POST** /api/v2/SupportService/SupportTickets/{supportTicketId}/Conversations | Create a conversation for a support ticket
[**update_support_ticket_async**](SupportTicketsApi.md#update_support_ticket_async) | **PUT** /api/v2/SupportService/SupportTickets/{supportTicketId} | Update a support ticket


# **create_support_ticket_async**
> EmptyEnvelope create_support_ticket_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_create_dto=support_ticket_create_dto)

Create a new support ticket

Creates a new support ticket for the specified tenant.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_create_dto = openapi_client.SupportTicketCreateDto() # SupportTicketCreateDto |  (optional)

    try:
        # Create a new support ticket
        api_response = api_instance.create_support_ticket_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_ticket_create_dto=support_ticket_create_dto)
        print("The response of SupportTicketsApi->create_support_ticket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->create_support_ticket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_create_dto** | [**SupportTicketCreateDto**](SupportTicketCreateDto.md)|  | [optional] 

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

# **delete_support_ticket_async**
> EmptyEnvelope delete_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)

Delete a support ticket

Deletes a support ticket by its unique identifier.

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
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support ticket
        api_response = api_instance.delete_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->delete_support_ticket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->delete_support_ticket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
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

# **delete_support_ticket_conversation_async**
> EmptyEnvelope delete_support_ticket_conversation_async(tenant_id, support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)

Delete a conversation from a support ticket

Deletes a specific conversation from a support ticket.

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
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a conversation from a support ticket
        api_response = api_instance.delete_support_ticket_conversation_async(tenant_id, support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->delete_support_ticket_conversation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->delete_support_ticket_conversation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_id** | **str**|  | 
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

# **get_support_ticket_async**
> SupportTicketDtoEnvelope get_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support ticket by ID

Retrieves a single support ticket by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support ticket by ID
        api_response = api_instance.get_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_ticket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_ticket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketDtoEnvelope**](SupportTicketDtoEnvelope.md)

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

# **get_support_ticket_conversation_async**
> SupportTicketConversationDtoEnvelope get_support_ticket_conversation_async(tenant_id, support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a specific conversation for a support ticket

Retrieves a single conversation by its ID for a specific support ticket.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a specific conversation for a support ticket
        api_response = api_instance.get_support_ticket_conversation_async(tenant_id, support_ticket_id, support_ticket_conversation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_ticket_conversation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_ticket_conversation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketConversationDtoEnvelope**](SupportTicketConversationDtoEnvelope.md)

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

# **get_support_ticket_conversation_messages_async**
> PrivateMessageDtoListEnvelope get_support_ticket_conversation_messages_async(tenant_id, support_ticket_id, support_ticket_conversation_id, page_number=page_number, page_size=page_size, api_version=api_version, x_api_version=x_api_version)

Retrieve messages for a support ticket conversation

Retrieves the list of messages within a specific conversation of a support ticket.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    support_ticket_conversation_id = 'support_ticket_conversation_id_example' # str | 
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve messages for a support ticket conversation
        api_response = api_instance.get_support_ticket_conversation_messages_async(tenant_id, support_ticket_id, support_ticket_conversation_id, page_number=page_number, page_size=page_size, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_ticket_conversation_messages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_ticket_conversation_messages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **support_ticket_conversation_id** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PrivateMessageDtoListEnvelope**](PrivateMessageDtoListEnvelope.md)

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

# **get_support_ticket_conversations_async**
> SupportTicketConversationDtoListEnvelope get_support_ticket_conversations_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)

Retrieve conversations for a support ticket

Retrieves the list of conversations associated with a specific support ticket.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve conversations for a support ticket
        api_response = api_instance.get_support_ticket_conversations_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_ticket_conversations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_ticket_conversations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketConversationDtoListEnvelope**](SupportTicketConversationDtoListEnvelope.md)

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

# **get_support_tickets_async**
> SupportTicketDtoListEnvelope get_support_tickets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support tickets

Retrieves a list of support tickets for the specified tenant with OData query support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support tickets
        api_response = api_instance.get_support_tickets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_tickets_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_tickets_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketDtoListEnvelope**](SupportTicketDtoListEnvelope.md)

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

# **get_support_tickets_count_async**
> Int32Envelope get_support_tickets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support tickets

Returns the total count of support tickets for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support tickets
        api_response = api_instance.get_support_tickets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketsApi->get_support_tickets_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->get_support_tickets_count_async: %s\n" % e)
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

# **relate_support_ticket_to_conversation_async**
> EmptyEnvelope relate_support_ticket_to_conversation_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version, support_ticket_conversation_create_dto=support_ticket_conversation_create_dto)

Create a conversation for a support ticket

Creates a new conversation and associates it with the specified support ticket.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_conversation_create_dto = openapi_client.SupportTicketConversationCreateDto() # SupportTicketConversationCreateDto |  (optional)

    try:
        # Create a conversation for a support ticket
        api_response = api_instance.relate_support_ticket_to_conversation_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version, support_ticket_conversation_create_dto=support_ticket_conversation_create_dto)
        print("The response of SupportTicketsApi->relate_support_ticket_to_conversation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->relate_support_ticket_to_conversation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_conversation_create_dto** | [**SupportTicketConversationCreateDto**](SupportTicketConversationCreateDto.md)|  | [optional] 

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

# **update_support_ticket_async**
> EmptyEnvelope update_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version, support_ticket_update_dto=support_ticket_update_dto)

Update a support ticket

Updates an existing support ticket by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_ticket_id = 'support_ticket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_ticket_update_dto = openapi_client.SupportTicketUpdateDto() # SupportTicketUpdateDto |  (optional)

    try:
        # Update a support ticket
        api_response = api_instance.update_support_ticket_async(tenant_id, support_ticket_id, api_version=api_version, x_api_version=x_api_version, support_ticket_update_dto=support_ticket_update_dto)
        print("The response of SupportTicketsApi->update_support_ticket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketsApi->update_support_ticket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_ticket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_ticket_update_dto** | [**SupportTicketUpdateDto**](SupportTicketUpdateDto.md)|  | [optional] 

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

