# openapi_client.CheckerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_authenticated**](CheckerApi.md#is_authenticated) | **GET** /api/v2/Auth/Checker/IsAuthenticated | Check if user is authenticated


# **is_authenticated**
> bool is_authenticated(api_version=api_version, x_api_version=x_api_version)

Check if user is authenticated

Returns whether the current user is authenticated.

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
    api_instance = openapi_client.CheckerApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if user is authenticated
        api_response = api_instance.is_authenticated(api_version=api_version, x_api_version=x_api_version)
        print("The response of CheckerApi->is_authenticated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckerApi->is_authenticated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**bool**

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

