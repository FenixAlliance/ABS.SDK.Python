# openapi_client.ItemAttachmentsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_attachment_async**](ItemAttachmentsApi.md#create_item_attachment_async) | **POST** /api/v2/CatalogService/ItemAttachments | Create a new item attachment
[**delete_item_attachment_async**](ItemAttachmentsApi.md#delete_item_attachment_async) | **DELETE** /api/v2/CatalogService/ItemAttachments/{itemAttachmentId} | Delete an item attachment
[**get_item_attachment_by_id_async**](ItemAttachmentsApi.md#get_item_attachment_by_id_async) | **GET** /api/v2/CatalogService/ItemAttachments/{itemAttachmentId} | Get item attachment by ID
[**get_item_attachments_async**](ItemAttachmentsApi.md#get_item_attachments_async) | **GET** /api/v2/CatalogService/ItemAttachments | Get all item attachments
[**update_item_attachment_async**](ItemAttachmentsApi.md#update_item_attachment_async) | **PUT** /api/v2/CatalogService/ItemAttachments/{itemAttachmentId} | Update an item attachment


# **create_item_attachment_async**
> ItemAttachmentDtoEnvelope create_item_attachment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attachment_create_dto=item_attachment_create_dto)

Create a new item attachment

Creates a new item attachment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_create_dto import ItemAttachmentCreateDto
from openapi_client.models.item_attachment_dto_envelope import ItemAttachmentDtoEnvelope
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attachment_create_dto = openapi_client.ItemAttachmentCreateDto() # ItemAttachmentCreateDto |  (optional)

    try:
        # Create a new item attachment
        api_response = api_instance.create_item_attachment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attachment_create_dto=item_attachment_create_dto)
        print("The response of ItemAttachmentsApi->create_item_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->create_item_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attachment_create_dto** | [**ItemAttachmentCreateDto**](ItemAttachmentCreateDto.md)|  | [optional] 

### Return type

[**ItemAttachmentDtoEnvelope**](ItemAttachmentDtoEnvelope.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_attachment_async**
> EmptyEnvelope delete_item_attachment_async(tenant_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)

Delete an item attachment

Deletes an item attachment for the specified tenant.

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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item attachment
        api_response = api_instance.delete_item_attachment_async(tenant_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttachmentsApi->delete_item_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->delete_item_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attachment_id** | **str**|  | 
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

# **get_item_attachment_by_id_async**
> ItemAttachmentDtoEnvelope get_item_attachment_by_id_async(item_attachment_id, api_version=api_version, x_api_version=x_api_version)

Get item attachment by ID

Retrieves a specific item attachment by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_dto_envelope import ItemAttachmentDtoEnvelope
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item attachment by ID
        api_response = api_instance.get_item_attachment_by_id_async(item_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttachmentsApi->get_item_attachment_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->get_item_attachment_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttachmentDtoEnvelope**](ItemAttachmentDtoEnvelope.md)

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

# **get_item_attachments_async**
> ItemAttachmentDtoListEnvelope get_item_attachments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item attachments

Retrieves all item attachments for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_dto_list_envelope import ItemAttachmentDtoListEnvelope
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item attachments
        api_response = api_instance.get_item_attachments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttachmentsApi->get_item_attachments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->get_item_attachments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttachmentDtoListEnvelope**](ItemAttachmentDtoListEnvelope.md)

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

# **update_item_attachment_async**
> EmptyEnvelope update_item_attachment_async(tenant_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version, item_attachment_update_dto=item_attachment_update_dto)

Update an item attachment

Updates an existing item attachment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_attachment_update_dto import ItemAttachmentUpdateDto
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
    api_instance = openapi_client.ItemAttachmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attachment_update_dto = openapi_client.ItemAttachmentUpdateDto() # ItemAttachmentUpdateDto |  (optional)

    try:
        # Update an item attachment
        api_response = api_instance.update_item_attachment_async(tenant_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version, item_attachment_update_dto=item_attachment_update_dto)
        print("The response of ItemAttachmentsApi->update_item_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttachmentsApi->update_item_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attachment_update_dto** | [**ItemAttachmentUpdateDto**](ItemAttachmentUpdateDto.md)|  | [optional] 

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

