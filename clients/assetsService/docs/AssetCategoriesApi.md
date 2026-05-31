# openapi_client.AssetCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_category**](AssetCategoriesApi.md#create_asset_category) | **POST** /api/v2/AssetsService/AssetCategories | Creates a new asset category
[**delete_asset_category**](AssetCategoriesApi.md#delete_asset_category) | **DELETE** /api/v2/AssetsService/AssetCategories/{categoryId} | Deletes an asset category
[**get_asset_categories**](AssetCategoriesApi.md#get_asset_categories) | **GET** /api/v2/AssetsService/AssetCategories | Gets all asset categories for the current tenant
[**get_asset_categories_count**](AssetCategoriesApi.md#get_asset_categories_count) | **GET** /api/v2/AssetsService/AssetCategories/count | Gets the count of asset categories
[**get_asset_category**](AssetCategoriesApi.md#get_asset_category) | **GET** /api/v2/AssetsService/AssetCategories/{categoryId} | Gets a specific asset category
[**update_asset_category**](AssetCategoriesApi.md#update_asset_category) | **PUT** /api/v2/AssetsService/AssetCategories/{categoryId} | Updates an existing asset category


# **create_asset_category**
> AssetCategoryDtoEnvelope create_asset_category(tenant_id, asset_category_create_dto=asset_category_create_dto)

Creates a new asset category

Creates a new asset category for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_create_dto import AssetCategoryCreateDto
from openapi_client.models.asset_category_dto_envelope import AssetCategoryDtoEnvelope
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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_category_create_dto = openapi_client.AssetCategoryCreateDto() # AssetCategoryCreateDto |  (optional)

    try:
        # Creates a new asset category
        api_response = api_instance.create_asset_category(tenant_id, asset_category_create_dto=asset_category_create_dto)
        print("The response of AssetCategoriesApi->create_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->create_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_category_create_dto** | [**AssetCategoryCreateDto**](AssetCategoryCreateDto.md)|  | [optional] 

### Return type

[**AssetCategoryDtoEnvelope**](AssetCategoryDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_category**
> delete_asset_category(tenant_id, category_id)

Deletes an asset category

Deletes an asset category for the authenticated tenant.

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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Deletes an asset category
        api_instance.delete_asset_category(tenant_id, category_id)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->delete_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_categories**
> AssetCategoryDtoListEnvelope get_asset_categories(tenant_id)

Gets all asset categories for the current tenant

Retrieves all asset categories for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_dto_list_envelope import AssetCategoryDtoListEnvelope
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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets all asset categories for the current tenant
        api_response = api_instance.get_asset_categories(tenant_id)
        print("The response of AssetCategoriesApi->get_asset_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->get_asset_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**AssetCategoryDtoListEnvelope**](AssetCategoryDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_categories_count**
> Int32Envelope get_asset_categories_count(tenant_id)

Gets the count of asset categories

Returns the total number of asset categories for the authenticated tenant.

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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of asset categories
        api_response = api_instance.get_asset_categories_count(tenant_id)
        print("The response of AssetCategoriesApi->get_asset_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->get_asset_categories_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_category**
> AssetCategoryDtoEnvelope get_asset_category(tenant_id, category_id)

Gets a specific asset category

Retrieves a specific asset category by ID.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_dto_envelope import AssetCategoryDtoEnvelope
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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Gets a specific asset category
        api_response = api_instance.get_asset_category(tenant_id, category_id)
        print("The response of AssetCategoriesApi->get_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->get_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 

### Return type

[**AssetCategoryDtoEnvelope**](AssetCategoryDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_category**
> EmptyEnvelope update_asset_category(tenant_id, category_id, asset_category_update_dto=asset_category_update_dto)

Updates an existing asset category

Updates an existing asset category for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_update_dto import AssetCategoryUpdateDto
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
    api_instance = openapi_client.AssetCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    asset_category_update_dto = openapi_client.AssetCategoryUpdateDto() # AssetCategoryUpdateDto |  (optional)

    try:
        # Updates an existing asset category
        api_response = api_instance.update_asset_category(tenant_id, category_id, asset_category_update_dto=asset_category_update_dto)
        print("The response of AssetCategoriesApi->update_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetCategoriesApi->update_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **asset_category_update_dto** | [**AssetCategoryUpdateDto**](AssetCategoryUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

