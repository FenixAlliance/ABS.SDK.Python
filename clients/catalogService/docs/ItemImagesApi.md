# openapi_client.ItemImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_image_async**](ItemImagesApi.md#create_item_image_async) | **POST** /api/v2/CatalogService/ItemImages | Create a new item image
[**delete_item_image_async**](ItemImagesApi.md#delete_item_image_async) | **DELETE** /api/v2/CatalogService/ItemImages/{itemImageId} | Delete an item image
[**get_item_image_by_id_async**](ItemImagesApi.md#get_item_image_by_id_async) | **GET** /api/v2/CatalogService/ItemImages/{itemImageId} | Get item image by ID
[**get_item_images_async**](ItemImagesApi.md#get_item_images_async) | **GET** /api/v2/CatalogService/ItemImages | Get all item images
[**update_item_image_async**](ItemImagesApi.md#update_item_image_async) | **PUT** /api/v2/CatalogService/ItemImages/{itemImageId} | Update an item image


# **create_item_image_async**
> ItemImageDtoEnvelope create_item_image_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_image_create_dto=item_image_create_dto)

Create a new item image

Creates a new item image for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_image_create_dto import ItemImageCreateDto
from openapi_client.models.item_image_dto_envelope import ItemImageDtoEnvelope
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
    api_instance = openapi_client.ItemImagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_image_create_dto = openapi_client.ItemImageCreateDto() # ItemImageCreateDto |  (optional)

    try:
        # Create a new item image
        api_response = api_instance.create_item_image_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_image_create_dto=item_image_create_dto)
        print("The response of ItemImagesApi->create_item_image_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemImagesApi->create_item_image_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_image_create_dto** | [**ItemImageCreateDto**](ItemImageCreateDto.md)|  | [optional] 

### Return type

[**ItemImageDtoEnvelope**](ItemImageDtoEnvelope.md)

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

# **delete_item_image_async**
> delete_item_image_async(tenant_id, item_image_id, api_version=api_version, x_api_version=x_api_version)

Delete an item image

Deletes an item image for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ItemImagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item image
        api_instance.delete_item_image_async(tenant_id, item_image_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemImagesApi->delete_item_image_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_image_id** | **str**|  | 
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

# **get_item_image_by_id_async**
> ItemImageDtoEnvelope get_item_image_by_id_async(item_image_id, api_version=api_version, x_api_version=x_api_version)

Get item image by ID

Retrieves a specific item image by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_envelope import ItemImageDtoEnvelope
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
    api_instance = openapi_client.ItemImagesApi(api_client)
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item image by ID
        api_response = api_instance.get_item_image_by_id_async(item_image_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemImagesApi->get_item_image_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemImagesApi->get_item_image_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_image_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoEnvelope**](ItemImageDtoEnvelope.md)

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

# **get_item_images_async**
> ItemImageDtoListEnvelope get_item_images_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item images

Retrieves all item images for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_list_envelope import ItemImageDtoListEnvelope
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
    api_instance = openapi_client.ItemImagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item images
        api_response = api_instance.get_item_images_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemImagesApi->get_item_images_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemImagesApi->get_item_images_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoListEnvelope**](ItemImageDtoListEnvelope.md)

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

# **update_item_image_async**
> update_item_image_async(tenant_id, item_image_id, api_version=api_version, x_api_version=x_api_version, item_image_update_dto=item_image_update_dto)

Update an item image

Updates an existing item image for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_image_update_dto import ItemImageUpdateDto
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
    api_instance = openapi_client.ItemImagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_image_update_dto = openapi_client.ItemImageUpdateDto() # ItemImageUpdateDto |  (optional)

    try:
        # Update an item image
        api_instance.update_item_image_async(tenant_id, item_image_id, api_version=api_version, x_api_version=x_api_version, item_image_update_dto=item_image_update_dto)
    except Exception as e:
        print("Exception when calling ItemImagesApi->update_item_image_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_image_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_image_update_dto** | [**ItemImageUpdateDto**](ItemImageUpdateDto.md)|  | [optional] 

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

