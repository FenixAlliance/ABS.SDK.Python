# openapi_client.ItemGoogleCategoriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_item_google_categories_async**](ItemGoogleCategoriesApi.md#get_all_item_google_categories_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/All | Get all Google item categories (all)
[**get_children_item_google_categories_by_id_async**](ItemGoogleCategoriesApi.md#get_children_item_google_categories_by_id_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/{itemCategoryId}/Children | Get children Google item categories by ID
[**get_item_google_categories_async**](ItemGoogleCategoriesApi.md#get_item_google_categories_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories | Get all Google item categories
[**get_item_google_categories_count_async**](ItemGoogleCategoriesApi.md#get_item_google_categories_count_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/Count | Get Google item categories count
[**get_item_google_categories_tree_async**](ItemGoogleCategoriesApi.md#get_item_google_categories_tree_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/tree | Get Google item categories tree
[**get_item_google_category_by_id_async**](ItemGoogleCategoriesApi.md#get_item_google_category_by_id_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/{itemCategoryId} | Get Google item category by ID
[**get_root_item_google_categories_async**](ItemGoogleCategoriesApi.md#get_root_item_google_categories_async) | **GET** /api/v2/CatalogService/ItemGoogleCategories/Primary | Get root Google item categories
[**map_item_google_categories_tree_async**](ItemGoogleCategoriesApi.md#map_item_google_categories_tree_async) | **POST** /api/v2/CatalogService/ItemGoogleCategories/tree | Map Google item categories tree


# **get_all_item_google_categories_async**
> ItemGoogleCategoryDtoListEnvelope get_all_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)

Get all Google item categories (all)

Retrieves all Google item categories (all) without OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all Google item categories (all)
        api_response = api_instance.get_all_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_all_item_google_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_all_item_google_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **get_children_item_google_categories_by_id_async**
> ItemGoogleCategoryDtoListEnvelope get_children_item_google_categories_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)

Get children Google item categories by ID

Retrieves children Google item categories for a given ID.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get children Google item categories by ID
        api_response = api_instance.get_children_item_google_categories_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_children_item_google_categories_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_children_item_google_categories_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **get_item_google_categories_async**
> ItemGoogleCategoryDtoListEnvelope get_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)

Get all Google item categories

Retrieves all Google item categories using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all Google item categories
        api_response = api_instance.get_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_item_google_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_item_google_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **get_item_google_categories_count_async**
> Int32Envelope get_item_google_categories_count_async(api_version=api_version, x_api_version=x_api_version)

Get Google item categories count

Retrieves the count of Google item categories using OData query options.

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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Google item categories count
        api_response = api_instance.get_item_google_categories_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_item_google_categories_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_item_google_categories_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_item_google_categories_tree_async**
> ItemGoogleCategoryDtoListEnvelope get_item_google_categories_tree_async(api_version=api_version, x_api_version=x_api_version)

Get Google item categories tree

Retrieves the Google item categories tree.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Google item categories tree
        api_response = api_instance.get_item_google_categories_tree_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_item_google_categories_tree_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_item_google_categories_tree_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **get_item_google_category_by_id_async**
> ItemGoogleCategoryDtoEnvelope get_item_google_category_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)

Get Google item category by ID

Retrieves a specific Google item category by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_envelope import ItemGoogleCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Google item category by ID
        api_response = api_instance.get_item_google_category_by_id_async(item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_item_google_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_item_google_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoEnvelope**](ItemGoogleCategoryDtoEnvelope.md)

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

# **get_root_item_google_categories_async**
> ItemGoogleCategoryDtoListEnvelope get_root_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)

Get root Google item categories

Retrieves root Google item categories.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get root Google item categories
        api_response = api_instance.get_root_item_google_categories_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->get_root_item_google_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->get_root_item_google_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **map_item_google_categories_tree_async**
> ItemGoogleCategoryDtoListEnvelope map_item_google_categories_tree_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Map Google item categories tree

Maps the Google item categories tree.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemGoogleCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Map Google item categories tree
        api_response = api_instance.map_item_google_categories_tree_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemGoogleCategoriesApi->map_item_google_categories_tree_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemGoogleCategoriesApi->map_item_google_categories_tree_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

