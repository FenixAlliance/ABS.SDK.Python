# openapi_client.TrackingPixelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tracking_pixel_async**](TrackingPixelsApi.md#get_tracking_pixel_async) | **GET** /api/v2/MarketingService/TrackingPixels/{pixelId} | Get a tracking pixel


# **get_tracking_pixel_async**
> OrderDtoEnvelope get_tracking_pixel_async(pixel_id, api_version=api_version, x_api_version=x_api_version)

Get a tracking pixel

Retrieves a tracking pixel by its ID.

### Example


```python
import openapi_client
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
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
    api_instance = openapi_client.TrackingPixelsApi(api_client)
    pixel_id = 'pixel_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tracking pixel
        api_response = api_instance.get_tracking_pixel_async(pixel_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrackingPixelsApi->get_tracking_pixel_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPixelsApi->get_tracking_pixel_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pixel_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OrderDtoEnvelope**](OrderDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

