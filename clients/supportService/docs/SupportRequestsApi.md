# openapi_client.SupportRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_request_async**](SupportRequestsApi.md#create_support_request_async) | **POST** /api/v2/SupportService/SupportRequests | Create a new support request
[**delete_support_request_async**](SupportRequestsApi.md#delete_support_request_async) | **DELETE** /api/v2/SupportService/SupportRequests/{supportRequestId} | Delete a support request
[**get_support_request_async**](SupportRequestsApi.md#get_support_request_async) | **GET** /api/v2/SupportService/SupportRequests/{supportRequestId} | Retrieve a support request by ID
[**get_support_request_attachment_by_request**](SupportRequestsApi.md#get_support_request_attachment_by_request) | **GET** /api/v2/SupportService/SupportRequests/{supportRequestId}/Attachments/{attachmentId} | Retrieve a specific attachment for a support request
[**get_support_request_attachments_by_request**](SupportRequestsApi.md#get_support_request_attachments_by_request) | **GET** /api/v2/SupportService/SupportRequests/{supportRequestId}/Attachments | Retrieve attachments for a support request
[**get_support_request_attachments_count_by_request**](SupportRequestsApi.md#get_support_request_attachments_count_by_request) | **GET** /api/v2/SupportService/SupportRequests/{supportRequestId}/Attachments/Count | Get the count of attachments for a support request
[**get_support_request_tickets_async**](SupportRequestsApi.md#get_support_request_tickets_async) | **GET** /api/v2/SupportService/SupportRequests/{supportRequestId}/Tickets | Retrieve tickets for a support request
[**get_support_requests_async**](SupportRequestsApi.md#get_support_requests_async) | **GET** /api/v2/SupportService/SupportRequests | Retrieve a list of support requests
[**get_support_requests_count_async**](SupportRequestsApi.md#get_support_requests_count_async) | **GET** /api/v2/SupportService/SupportRequests/Count | Get the count of support requests
[**relate_support_request_to_attachment_async**](SupportRequestsApi.md#relate_support_request_to_attachment_async) | **POST** /api/v2/SupportService/SupportRequests/{supportRequestId}/Attachments | Add an attachment to a support request
[**update_support_request_async**](SupportRequestsApi.md#update_support_request_async) | **PUT** /api/v2/SupportService/SupportRequests/{supportRequestId} | Update a support request


# **create_support_request_async**
> EmptyEnvelope create_support_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_request_create_dto=support_request_create_dto)

Create a new support request

Creates a new support request for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_request_create_dto import SupportRequestCreateDto
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_request_create_dto = openapi_client.SupportRequestCreateDto() # SupportRequestCreateDto |  (optional)

    try:
        # Create a new support request
        api_response = api_instance.create_support_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_request_create_dto=support_request_create_dto)
        print("The response of SupportRequestsApi->create_support_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->create_support_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_request_create_dto** | [**SupportRequestCreateDto**](SupportRequestCreateDto.md)|  | [optional] 

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

# **delete_support_request_async**
> EmptyEnvelope delete_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)

Delete a support request

Deletes a support request by its unique identifier.

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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support request
        api_response = api_instance.delete_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->delete_support_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->delete_support_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
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

# **get_support_request_async**
> SupportRequestDtoEnvelope get_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support request by ID

Retrieves a single support request by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.support_request_dto_envelope import SupportRequestDtoEnvelope
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support request by ID
        api_response = api_instance.get_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportRequestDtoEnvelope**](SupportRequestDtoEnvelope.md)

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

# **get_support_request_attachment_by_request**
> SupportRequestAttachmentDtoEnvelope get_support_request_attachment_by_request(tenant_id, support_request_id, attachment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a specific attachment for a support request

Retrieves a single attachment by its ID for a specific support request.

### Example


```python
import openapi_client
from openapi_client.models.support_request_attachment_dto_envelope import SupportRequestAttachmentDtoEnvelope
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a specific attachment for a support request
        api_response = api_instance.get_support_request_attachment_by_request(tenant_id, support_request_id, attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_request_attachment_by_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_request_attachment_by_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
 **attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportRequestAttachmentDtoEnvelope**](SupportRequestAttachmentDtoEnvelope.md)

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

# **get_support_request_attachments_by_request**
> SupportRequestAttachmentDtoListEnvelope get_support_request_attachments_by_request(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve attachments for a support request

Retrieves the list of attachments associated with a specific support request.

### Example


```python
import openapi_client
from openapi_client.models.support_request_attachment_dto_list_envelope import SupportRequestAttachmentDtoListEnvelope
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve attachments for a support request
        api_response = api_instance.get_support_request_attachments_by_request(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_request_attachments_by_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_request_attachments_by_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportRequestAttachmentDtoListEnvelope**](SupportRequestAttachmentDtoListEnvelope.md)

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

# **get_support_request_attachments_count_by_request**
> Int32Envelope get_support_request_attachments_count_by_request(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)

Get the count of attachments for a support request

Returns the total count of attachments for a specific support request.

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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of attachments for a support request
        api_response = api_instance.get_support_request_attachments_count_by_request(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_request_attachments_count_by_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_request_attachments_count_by_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
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

# **get_support_request_tickets_async**
> SupportTicketDtoListEnvelope get_support_request_tickets_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve tickets for a support request

Retrieves the list of support tickets associated with a specific support request.

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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve tickets for a support request
        api_response = api_instance.get_support_request_tickets_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_request_tickets_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_request_tickets_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
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

# **get_support_requests_async**
> SupportRequestDtoListEnvelope get_support_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support requests

Retrieves a list of support requests for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.support_request_dto_list_envelope import SupportRequestDtoListEnvelope
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support requests
        api_response = api_instance.get_support_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportRequestDtoListEnvelope**](SupportRequestDtoListEnvelope.md)

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

# **get_support_requests_count_async**
> Int32Envelope get_support_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support requests

Returns the total count of support requests for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support requests
        api_response = api_instance.get_support_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestsApi->get_support_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->get_support_requests_count_async: %s\n" % e)
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

# **relate_support_request_to_attachment_async**
> EmptyEnvelope relate_support_request_to_attachment_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_create_dto=support_request_attachment_create_dto)

Add an attachment to a support request

Creates a new attachment and associates it with the specified support request.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_request_attachment_create_dto import SupportRequestAttachmentCreateDto
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_request_attachment_create_dto = openapi_client.SupportRequestAttachmentCreateDto() # SupportRequestAttachmentCreateDto |  (optional)

    try:
        # Add an attachment to a support request
        api_response = api_instance.relate_support_request_to_attachment_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_create_dto=support_request_attachment_create_dto)
        print("The response of SupportRequestsApi->relate_support_request_to_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->relate_support_request_to_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_request_attachment_create_dto** | [**SupportRequestAttachmentCreateDto**](SupportRequestAttachmentCreateDto.md)|  | [optional] 

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

# **update_support_request_async**
> EmptyEnvelope update_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version, support_request_update_dto=support_request_update_dto)

Update a support request

Updates an existing support request by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_request_update_dto import SupportRequestUpdateDto
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
    api_instance = openapi_client.SupportRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_id = 'support_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_request_update_dto = openapi_client.SupportRequestUpdateDto() # SupportRequestUpdateDto |  (optional)

    try:
        # Update a support request
        api_response = api_instance.update_support_request_async(tenant_id, support_request_id, api_version=api_version, x_api_version=x_api_version, support_request_update_dto=support_request_update_dto)
        print("The response of SupportRequestsApi->update_support_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestsApi->update_support_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_request_update_dto** | [**SupportRequestUpdateDto**](SupportRequestUpdateDto.md)|  | [optional] 

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

