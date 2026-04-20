# openapi_client.AntiforgeryApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_and_store_tokens**](AntiforgeryApi.md#get_and_store_tokens) | **GET** /api/v2/SystemService/Antiforgery/GetAndStoreTokens | Get and store antiforgery tokens
[**is_request_valid_async**](AntiforgeryApi.md#is_request_valid_async) | **GET** /api/v2/SystemService/Antiforgery/IsRequestValid | Validate antiforgery request


# **get_and_store_tokens**
> get_and_store_tokens(api_version=api_version, x_api_version=x_api_version)

Get and store antiforgery tokens

Generates antiforgery tokens and stores them in the current HTTP context.

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
    api_instance = openapi_client.AntiforgeryApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get and store antiforgery tokens
        api_instance.get_and_store_tokens(api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling AntiforgeryApi->get_and_store_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **is_request_valid_async**
> is_request_valid_async(api_version=api_version, x_api_version=x_api_version)

Validate antiforgery request

Validates whether the current HTTP request contains a valid antiforgery token.

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
    api_instance = openapi_client.AntiforgeryApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Validate antiforgery request
        api_instance.is_request_valid_async(api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling AntiforgeryApi->is_request_valid_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

