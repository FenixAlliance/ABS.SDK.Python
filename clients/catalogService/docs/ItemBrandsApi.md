# openapi_client.ItemBrandsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_brand_async**](ItemBrandsApi.md#create_item_brand_async) | **POST** /api/v2/CatalogService/ItemBrands | Create a new item brand
[**delete_item_brand_async**](ItemBrandsApi.md#delete_item_brand_async) | **DELETE** /api/v2/CatalogService/ItemBrands/{itemBrandId} | Delete an item brand
[**get_item_brand_by_id_async**](ItemBrandsApi.md#get_item_brand_by_id_async) | **GET** /api/v2/CatalogService/ItemBrands/{itemBrandId} | Get item brand by ID
[**get_item_brands_async**](ItemBrandsApi.md#get_item_brands_async) | **GET** /api/v2/CatalogService/ItemBrands | Get all item brands
[**update_item_brand_async**](ItemBrandsApi.md#update_item_brand_async) | **PUT** /api/v2/CatalogService/ItemBrands/{itemBrandId} | Update an item brand


# **create_item_brand_async**
> ItemBrandDtoEnvelope create_item_brand_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_brand_create_dto=item_brand_create_dto)

Create a new item brand

Creates a new item brand for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_create_dto import ItemBrandCreateDto
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
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
    api_instance = openapi_client.ItemBrandsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_brand_create_dto = openapi_client.ItemBrandCreateDto() # ItemBrandCreateDto |  (optional)

    try:
        # Create a new item brand
        api_response = api_instance.create_item_brand_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_brand_create_dto=item_brand_create_dto)
        print("The response of ItemBrandsApi->create_item_brand_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBrandsApi->create_item_brand_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_brand_create_dto** | [**ItemBrandCreateDto**](ItemBrandCreateDto.md)|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

# **delete_item_brand_async**
> delete_item_brand_async(tenant_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)

Delete an item brand

Deletes an item brand for the specified tenant.

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
    api_instance = openapi_client.ItemBrandsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item brand
        api_instance.delete_item_brand_async(tenant_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemBrandsApi->delete_item_brand_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_brand_id** | **str**|  | 
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

# **get_item_brand_by_id_async**
> ItemBrandDtoEnvelope get_item_brand_by_id_async(item_brand_id, api_version=api_version, x_api_version=x_api_version)

Get item brand by ID

Retrieves a specific item brand by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
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
    api_instance = openapi_client.ItemBrandsApi(api_client)
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item brand by ID
        api_response = api_instance.get_item_brand_by_id_async(item_brand_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemBrandsApi->get_item_brand_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBrandsApi->get_item_brand_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_brand_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

# **get_item_brands_async**
> ItemBrandDtoListEnvelope get_item_brands_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item brands

Retrieves all item brands for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_list_envelope import ItemBrandDtoListEnvelope
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
    api_instance = openapi_client.ItemBrandsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item brands
        api_response = api_instance.get_item_brands_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemBrandsApi->get_item_brands_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBrandsApi->get_item_brands_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoListEnvelope**](ItemBrandDtoListEnvelope.md)

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

# **update_item_brand_async**
> ItemBrandDtoEnvelope update_item_brand_async(tenant_id, item_brand_id, api_version=api_version, x_api_version=x_api_version, item_brand_update_dto=item_brand_update_dto)

Update an item brand

Updates an existing item brand for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
from openapi_client.models.item_brand_update_dto import ItemBrandUpdateDto
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
    api_instance = openapi_client.ItemBrandsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_brand_update_dto = openapi_client.ItemBrandUpdateDto() # ItemBrandUpdateDto |  (optional)

    try:
        # Update an item brand
        api_response = api_instance.update_item_brand_async(tenant_id, item_brand_id, api_version=api_version, x_api_version=x_api_version, item_brand_update_dto=item_brand_update_dto)
        print("The response of ItemBrandsApi->update_item_brand_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBrandsApi->update_item_brand_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_brand_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_brand_update_dto** | [**ItemBrandUpdateDto**](ItemBrandUpdateDto.md)|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

