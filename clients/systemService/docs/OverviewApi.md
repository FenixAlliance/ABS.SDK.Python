# openapi_client.OverviewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_overview**](OverviewApi.md#get_system_overview) | **GET** /api/v2/SystemService/Overview | Get system overview information


# **get_system_overview**
> SystemOverviewDtoEnvelope get_system_overview(api_version=api_version, x_api_version=x_api_version)

Get system overview information

Returns runtime, memory, and entity count information for the system

### Example


```python
import openapi_client
from openapi_client.models.system_overview_dto_envelope import SystemOverviewDtoEnvelope
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
    api_instance = openapi_client.OverviewApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get system overview information
        api_response = api_instance.get_system_overview(api_version=api_version, x_api_version=x_api_version)
        print("The response of OverviewApi->get_system_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverviewApi->get_system_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SystemOverviewDtoEnvelope**](SystemOverviewDtoEnvelope.md)

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

