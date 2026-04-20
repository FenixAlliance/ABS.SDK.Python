# openapi_client.InventoryApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_details_async**](InventoryApi.md#get_inventory_details_async) | **GET** /api/v2/InventoryService/Inventory/{stockItemId}/Details | Get inventory details for a stock item


# **get_inventory_details_async**
> get_inventory_details_async(stock_item_id, api_version=api_version, x_api_version=x_api_version)

Get inventory details for a stock item

Retrieves the inventory details for a specific stock item by its ID.

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
    api_instance = openapi_client.InventoryApi(api_client)
    stock_item_id = 'stock_item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get inventory details for a stock item
        api_instance.get_inventory_details_async(stock_item_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

