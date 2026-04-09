# openapi_client.ItemCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_categories_async**](ItemCategoriesApi.md#count_item_categories_async) | **GET** /api/v2/CatalogService/ItemCategories/Count | Count item categories
[**create_item_category_async**](ItemCategoriesApi.md#create_item_category_async) | **POST** /api/v2/CatalogService/ItemCategories | Create a new item category
[**delete_item_category_async**](ItemCategoriesApi.md#delete_item_category_async) | **DELETE** /api/v2/CatalogService/ItemCategories/{itemCategoryId} | Delete an item category
[**get_item_categories_async**](ItemCategoriesApi.md#get_item_categories_async) | **GET** /api/v2/CatalogService/ItemCategories | Get all item categories
[**get_item_category_by_id_async**](ItemCategoriesApi.md#get_item_category_by_id_async) | **GET** /api/v2/CatalogService/ItemCategories/{itemCategoryId} | Get item category by ID
[**update_item_category_async**](ItemCategoriesApi.md#update_item_category_async) | **PUT** /api/v2/CatalogService/ItemCategories/{itemCategoryId} | Update an item category


# **count_item_categories_async**
> Int32Envelope count_item_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count item categories

Counts all item categories for the specified tenant.

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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item categories
        api_response = api_instance.count_item_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemCategoriesApi->count_item_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->count_item_categories_async: %s\n" % e)
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

# **create_item_category_async**
> ItemCategoryDtoEnvelope create_item_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_category_create_dto=item_category_create_dto)

Create a new item category

Creates a new item category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_category_create_dto import ItemCategoryCreateDto
from openapi_client.models.item_category_dto_envelope import ItemCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_category_create_dto = openapi_client.ItemCategoryCreateDto() # ItemCategoryCreateDto |  (optional)

    try:
        # Create a new item category
        api_response = api_instance.create_item_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_category_create_dto=item_category_create_dto)
        print("The response of ItemCategoriesApi->create_item_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->create_item_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_category_create_dto** | [**ItemCategoryCreateDto**](ItemCategoryCreateDto.md)|  | [optional] 

### Return type

[**ItemCategoryDtoEnvelope**](ItemCategoryDtoEnvelope.md)

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

# **delete_item_category_async**
> delete_item_category_async(tenant_id, item_category_id, api_version=api_version, x_api_version=x_api_version)

Delete an item category

Deletes an item category for the specified tenant.

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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item category
        api_instance.delete_item_category_async(tenant_id, item_category_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->delete_item_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_category_id** | **str**|  | 
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

# **get_item_categories_async**
> ItemCategoryDtoListEnvelope get_item_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item categories

Retrieves all item categories for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_list_envelope import ItemCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item categories
        api_response = api_instance.get_item_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemCategoriesApi->get_item_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->get_item_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoListEnvelope**](ItemCategoryDtoListEnvelope.md)

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

# **get_item_category_by_id_async**
> ItemCategoryDtoEnvelope get_item_category_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)

Get item category by ID

Retrieves a specific item category by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_envelope import ItemCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item category by ID
        api_response = api_instance.get_item_category_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemCategoriesApi->get_item_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->get_item_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoEnvelope**](ItemCategoryDtoEnvelope.md)

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

# **update_item_category_async**
> update_item_category_async(tenant_id, item_category_id, api_version=api_version, x_api_version=x_api_version, item_category_update_dto=item_category_update_dto)

Update an item category

Updates an existing item category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_category_update_dto import ItemCategoryUpdateDto
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
    api_instance = openapi_client.ItemCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_category_update_dto = openapi_client.ItemCategoryUpdateDto() # ItemCategoryUpdateDto |  (optional)

    try:
        # Update an item category
        api_instance.update_item_category_async(tenant_id, item_category_id, api_version=api_version, x_api_version=x_api_version, item_category_update_dto=item_category_update_dto)
    except Exception as e:
        print("Exception when calling ItemCategoriesApi->update_item_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_category_update_dto** | [**ItemCategoryUpdateDto**](ItemCategoryUpdateDto.md)|  | [optional] 

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

