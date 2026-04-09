# openapi_client.CompareApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_compare_table_async**](CompareApi.md#add_item_to_compare_table_async) | **POST** /api/v2/CartService/Compare | Add an item to the compare table
[**get_item_to_compare_record**](CompareApi.md#get_item_to_compare_record) | **GET** /api/v2/CartService/Compare/{recordId}/Details | Get compare record details
[**get_item_to_compare_records**](CompareApi.md#get_item_to_compare_records) | **GET** /api/v2/CartService/Compare/{cartId} | Get items to compare in a cart
[**remove_item_from_compare_table**](CompareApi.md#remove_item_from_compare_table) | **DELETE** /api/v2/CartService/Compare/{recordId} | Remove an item from the compare table


# **add_item_to_compare_table_async**
> ItemCartRecordDto add_item_to_compare_table_async(api_version=api_version, x_api_version=x_api_version, add_product_to_compare_request=add_product_to_compare_request)

Add an item to the compare table

Adds a product to the compare table for the specified cart with tracking.

### Example


```python
import openapi_client
from openapi_client.models.add_product_to_compare_request import AddProductToCompareRequest
from openapi_client.models.item_cart_record_dto import ItemCartRecordDto
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
    api_instance = openapi_client.CompareApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    add_product_to_compare_request = openapi_client.AddProductToCompareRequest() # AddProductToCompareRequest |  (optional)

    try:
        # Add an item to the compare table
        api_response = api_instance.add_item_to_compare_table_async(api_version=api_version, x_api_version=x_api_version, add_product_to_compare_request=add_product_to_compare_request)
        print("The response of CompareApi->add_item_to_compare_table_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->add_item_to_compare_table_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **add_product_to_compare_request** | [**AddProductToCompareRequest**](AddProductToCompareRequest.md)|  | [optional] 

### Return type

[**ItemCartRecordDto**](ItemCartRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_to_compare_record**
> ItemToCompareCartRecordDtoEnvelope get_item_to_compare_record(record_id, api_version=api_version, x_api_version=x_api_version)

Get compare record details

Retrieves the details of a specific item-to-compare cart record.

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto_envelope import ItemToCompareCartRecordDtoEnvelope
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
    api_instance = openapi_client.CompareApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get compare record details
        api_response = api_instance.get_item_to_compare_record(record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CompareApi->get_item_to_compare_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->get_item_to_compare_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDtoEnvelope**](ItemToCompareCartRecordDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_to_compare_records**
> ItemToCompareCartRecordDtoListEnvelope get_item_to_compare_records(cart_id, api_version=api_version, x_api_version=x_api_version)

Get items to compare in a cart

Retrieves all items added to the compare table for the specified cart.

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto_list_envelope import ItemToCompareCartRecordDtoListEnvelope
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
    api_instance = openapi_client.CompareApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get items to compare in a cart
        api_response = api_instance.get_item_to_compare_records(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CompareApi->get_item_to_compare_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->get_item_to_compare_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDtoListEnvelope**](ItemToCompareCartRecordDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_item_from_compare_table**
> ItemToCompareCartRecordDto remove_item_from_compare_table(record_id, api_version=api_version, x_api_version=x_api_version)

Remove an item from the compare table

Removes a specific record from the compare table by its record ID.

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto import ItemToCompareCartRecordDto
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
    api_instance = openapi_client.CompareApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove an item from the compare table
        api_response = api_instance.remove_item_from_compare_table(record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CompareApi->remove_item_from_compare_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->remove_item_from_compare_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDto**](ItemToCompareCartRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

