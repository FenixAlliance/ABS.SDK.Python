# openapi_client.ItemReviewsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_review_async**](ItemReviewsApi.md#create_item_review_async) | **POST** /api/v2/CatalogService/ItemReviews | Create a new item review
[**delete_item_review_async**](ItemReviewsApi.md#delete_item_review_async) | **DELETE** /api/v2/CatalogService/ItemReviews/{itemReviewId} | Delete an item review
[**get_item_review_by_id_async**](ItemReviewsApi.md#get_item_review_by_id_async) | **GET** /api/v2/CatalogService/ItemReviews/{itemReviewId} | Get item review by ID
[**get_item_reviews_async**](ItemReviewsApi.md#get_item_reviews_async) | **GET** /api/v2/CatalogService/ItemReviews | Get all item reviews
[**update_item_review_async**](ItemReviewsApi.md#update_item_review_async) | **PUT** /api/v2/CatalogService/ItemReviews/{itemReviewId} | Update an item review


# **create_item_review_async**
> ItemReviewDtoEnvelope create_item_review_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_review_create_dto=item_review_create_dto)

Create a new item review

Creates a new item review for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_review_create_dto import ItemReviewCreateDto
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope
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
    api_instance = openapi_client.ItemReviewsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_review_create_dto = openapi_client.ItemReviewCreateDto() # ItemReviewCreateDto |  (optional)

    try:
        # Create a new item review
        api_response = api_instance.create_item_review_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_review_create_dto=item_review_create_dto)
        print("The response of ItemReviewsApi->create_item_review_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReviewsApi->create_item_review_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_review_create_dto** | [**ItemReviewCreateDto**](ItemReviewCreateDto.md)|  | [optional] 

### Return type

[**ItemReviewDtoEnvelope**](ItemReviewDtoEnvelope.md)

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

# **delete_item_review_async**
> delete_item_review_async(tenant_id, item_review_id, api_version=api_version, x_api_version=x_api_version)

Delete an item review

Deletes an item review for the specified tenant.

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
    api_instance = openapi_client.ItemReviewsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_review_id = 'item_review_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item review
        api_instance.delete_item_review_async(tenant_id, item_review_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemReviewsApi->delete_item_review_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_review_id** | **str**|  | 
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

# **get_item_review_by_id_async**
> ItemReviewDtoEnvelope get_item_review_by_id_async(item_review_id, api_version=api_version, x_api_version=x_api_version)

Get item review by ID

Retrieves a specific item review by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope
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
    api_instance = openapi_client.ItemReviewsApi(api_client)
    item_review_id = 'item_review_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item review by ID
        api_response = api_instance.get_item_review_by_id_async(item_review_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemReviewsApi->get_item_review_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReviewsApi->get_item_review_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_review_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReviewDtoEnvelope**](ItemReviewDtoEnvelope.md)

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

# **get_item_reviews_async**
> ItemReviewDtoListEnvelope get_item_reviews_async(item_id, api_version=api_version, x_api_version=x_api_version)

Get all item reviews

Retrieves all item reviews for the specified item using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_list_envelope import ItemReviewDtoListEnvelope
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
    api_instance = openapi_client.ItemReviewsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item reviews
        api_response = api_instance.get_item_reviews_async(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemReviewsApi->get_item_reviews_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReviewsApi->get_item_reviews_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReviewDtoListEnvelope**](ItemReviewDtoListEnvelope.md)

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

# **update_item_review_async**
> update_item_review_async(tenant_id, item_review_id, api_version=api_version, x_api_version=x_api_version, item_review_update_dto=item_review_update_dto)

Update an item review

Updates an existing item review for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_review_update_dto import ItemReviewUpdateDto
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
    api_instance = openapi_client.ItemReviewsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_review_id = 'item_review_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_review_update_dto = openapi_client.ItemReviewUpdateDto() # ItemReviewUpdateDto |  (optional)

    try:
        # Update an item review
        api_instance.update_item_review_async(tenant_id, item_review_id, api_version=api_version, x_api_version=x_api_version, item_review_update_dto=item_review_update_dto)
    except Exception as e:
        print("Exception when calling ItemReviewsApi->update_item_review_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_review_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_review_update_dto** | [**ItemReviewUpdateDto**](ItemReviewUpdateDto.md)|  | [optional] 

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

