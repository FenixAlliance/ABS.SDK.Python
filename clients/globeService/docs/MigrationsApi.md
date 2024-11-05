# openapi_client.MigrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_global_system_migrate_post**](MigrationsApi.md#api_v2_global_system_migrate_post) | **POST** /api/v2/Global/System/Migrate | 


# **api_v2_global_system_migrate_post**
> PaymentResponse api_v2_global_system_migrate_post(api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.payment_response import PaymentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MigrationsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_global_system_migrate_post(api_version=api_version, x_api_version=x_api_version)
        print("The response of MigrationsApi->api_v2_global_system_migrate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->api_v2_global_system_migrate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

