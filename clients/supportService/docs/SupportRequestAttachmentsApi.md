# openapi_client.SupportRequestAttachmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_request_attachment_async**](SupportRequestAttachmentsApi.md#create_support_request_attachment_async) | **POST** /api/v2/SupportService/SupportRequestAttachments | Create a new support request attachment
[**delete_support_request_attachment_async**](SupportRequestAttachmentsApi.md#delete_support_request_attachment_async) | **DELETE** /api/v2/SupportService/SupportRequestAttachments/{supportRequestAttachmentId} | Delete a support request attachment
[**get_support_request_attachment_async**](SupportRequestAttachmentsApi.md#get_support_request_attachment_async) | **GET** /api/v2/SupportService/SupportRequestAttachments/{supportRequestAttachmentId} | Retrieve a support request attachment by ID
[**get_support_request_attachments_async**](SupportRequestAttachmentsApi.md#get_support_request_attachments_async) | **GET** /api/v2/SupportService/SupportRequestAttachments | Retrieve a list of support request attachments
[**get_support_request_attachments_count_async**](SupportRequestAttachmentsApi.md#get_support_request_attachments_count_async) | **GET** /api/v2/SupportService/SupportRequestAttachments/Count | Get the count of support request attachments
[**update_support_request_attachment_async**](SupportRequestAttachmentsApi.md#update_support_request_attachment_async) | **PUT** /api/v2/SupportService/SupportRequestAttachments/{supportRequestAttachmentId} | Update a support request attachment


# **create_support_request_attachment_async**
> EmptyEnvelope create_support_request_attachment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_create_dto=support_request_attachment_create_dto)

Create a new support request attachment

Creates a new support request attachment for the specified tenant.

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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_request_attachment_create_dto = openapi_client.SupportRequestAttachmentCreateDto() # SupportRequestAttachmentCreateDto |  (optional)

    try:
        # Create a new support request attachment
        api_response = api_instance.create_support_request_attachment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_create_dto=support_request_attachment_create_dto)
        print("The response of SupportRequestAttachmentsApi->create_support_request_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->create_support_request_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **delete_support_request_attachment_async**
> EmptyEnvelope delete_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version)

Delete a support request attachment

Deletes a support request attachment by its unique identifier.

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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_attachment_id = 'support_request_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support request attachment
        api_response = api_instance.delete_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestAttachmentsApi->delete_support_request_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->delete_support_request_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_attachment_id** | **str**|  | 
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

# **get_support_request_attachment_async**
> SupportRequestAttachmentDtoEnvelope get_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support request attachment by ID

Retrieves a single support request attachment by its unique identifier.

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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_attachment_id = 'support_request_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support request attachment by ID
        api_response = api_instance.get_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestAttachmentsApi->get_support_request_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->get_support_request_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_attachment_id** | **str**|  | 
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

# **get_support_request_attachments_async**
> SupportRequestAttachmentDtoListEnvelope get_support_request_attachments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support request attachments

Retrieves a list of support request attachments for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support request attachments
        api_response = api_instance.get_support_request_attachments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestAttachmentsApi->get_support_request_attachments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->get_support_request_attachments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_support_request_attachments_count_async**
> Int32Envelope get_support_request_attachments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support request attachments

Returns the total count of support request attachments for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support request attachments
        api_response = api_instance.get_support_request_attachments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportRequestAttachmentsApi->get_support_request_attachments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->get_support_request_attachments_count_async: %s\n" % e)
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

# **update_support_request_attachment_async**
> EmptyEnvelope update_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_update_dto=support_request_attachment_update_dto)

Update a support request attachment

Updates an existing support request attachment by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_request_attachment_update_dto import SupportRequestAttachmentUpdateDto
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
    api_instance = openapi_client.SupportRequestAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_request_attachment_id = 'support_request_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_request_attachment_update_dto = openapi_client.SupportRequestAttachmentUpdateDto() # SupportRequestAttachmentUpdateDto |  (optional)

    try:
        # Update a support request attachment
        api_response = api_instance.update_support_request_attachment_async(tenant_id, support_request_attachment_id, api_version=api_version, x_api_version=x_api_version, support_request_attachment_update_dto=support_request_attachment_update_dto)
        print("The response of SupportRequestAttachmentsApi->update_support_request_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportRequestAttachmentsApi->update_support_request_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_request_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_request_attachment_update_dto** | [**SupportRequestAttachmentUpdateDto**](SupportRequestAttachmentUpdateDto.md)|  | [optional] 

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

