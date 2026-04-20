# openapi_client.ItemTagsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_tag_async**](ItemTagsApi.md#create_item_tag_async) | **POST** /api/v2/CatalogService/ItemTags | Create a new item tag
[**delete_item_tag_async**](ItemTagsApi.md#delete_item_tag_async) | **DELETE** /api/v2/CatalogService/ItemTags/{itemTagId} | Delete an item tag
[**get_item_tag_by_id_async**](ItemTagsApi.md#get_item_tag_by_id_async) | **GET** /api/v2/CatalogService/ItemTags/{itemTagId} | Get item tag by ID
[**get_item_tags_async**](ItemTagsApi.md#get_item_tags_async) | **GET** /api/v2/CatalogService/ItemTags | Get all item tags
[**update_item_tag_async**](ItemTagsApi.md#update_item_tag_async) | **PUT** /api/v2/CatalogService/ItemTags/{itemTagId} | Update an item tag


# **create_item_tag_async**
> ItemTagDtoEnvelope create_item_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_tag_create_dto=item_tag_create_dto)

Create a new item tag

Creates a new item tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_create_dto import ItemTagCreateDto
from openapi_client.models.item_tag_dto_envelope import ItemTagDtoEnvelope
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
    api_instance = openapi_client.ItemTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_tag_create_dto = openapi_client.ItemTagCreateDto() # ItemTagCreateDto |  (optional)

    try:
        # Create a new item tag
        api_response = api_instance.create_item_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_tag_create_dto=item_tag_create_dto)
        print("The response of ItemTagsApi->create_item_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTagsApi->create_item_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_tag_create_dto** | [**ItemTagCreateDto**](ItemTagCreateDto.md)|  | [optional] 

### Return type

[**ItemTagDtoEnvelope**](ItemTagDtoEnvelope.md)

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

# **delete_item_tag_async**
> delete_item_tag_async(tenant_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)

Delete an item tag

Deletes an item tag for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ItemTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item tag
        api_instance.delete_item_tag_async(tenant_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemTagsApi->delete_item_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **get_item_tag_by_id_async**
> ItemTagDtoEnvelope get_item_tag_by_id_async(item_tag_id, api_version=api_version, x_api_version=x_api_version)

Get item tag by ID

Retrieves a specific item tag by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_envelope import ItemTagDtoEnvelope
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
    api_instance = openapi_client.ItemTagsApi(api_client)
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item tag by ID
        api_response = api_instance.get_item_tag_by_id_async(item_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTagsApi->get_item_tag_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTagsApi->get_item_tag_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoEnvelope**](ItemTagDtoEnvelope.md)

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

# **get_item_tags_async**
> ItemTagDtoListEnvelope get_item_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item tags

Retrieves all item tags for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_list_envelope import ItemTagDtoListEnvelope
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
    api_instance = openapi_client.ItemTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item tags
        api_response = api_instance.get_item_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTagsApi->get_item_tags_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTagsApi->get_item_tags_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoListEnvelope**](ItemTagDtoListEnvelope.md)

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

# **update_item_tag_async**
> update_item_tag_async(tenant_id, item_tag_id, api_version=api_version, x_api_version=x_api_version, item_tag_update_dto=item_tag_update_dto)

Update an item tag

Updates an existing item tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_update_dto import ItemTagUpdateDto
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
    api_instance = openapi_client.ItemTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_tag_update_dto = openapi_client.ItemTagUpdateDto() # ItemTagUpdateDto |  (optional)

    try:
        # Update an item tag
        api_instance.update_item_tag_async(tenant_id, item_tag_id, api_version=api_version, x_api_version=x_api_version, item_tag_update_dto=item_tag_update_dto)
    except Exception as e:
        print("Exception when calling ItemTagsApi->update_item_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_tag_update_dto** | [**ItemTagUpdateDto**](ItemTagUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

