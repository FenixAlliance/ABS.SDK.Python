# openapi_client.ModulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_modules**](ModulesApi.md#get_all_modules) | **GET** /api/v2/StudioService/Modules | Get all modules available on this suite server instance.
[**get_available_modules**](ModulesApi.md#get_available_modules) | **GET** /api/v2/StudioService/Modules/Data | Get all modules available to a tenant user.


# **get_all_modules**
> StudioModuleListEnvelope get_all_modules(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all modules available on this suite server instance.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.studio_module_list_envelope import StudioModuleListEnvelope
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
    api_instance = openapi_client.ModulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all modules available on this suite server instance.
        api_response = api_instance.get_all_modules(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ModulesApi->get_all_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->get_all_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StudioModuleListEnvelope**](StudioModuleListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_available_modules**
> ModuleListEnvelope get_available_modules(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all modules available to a tenant user.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.module_list_envelope import ModuleListEnvelope
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
    api_instance = openapi_client.ModulesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all modules available to a tenant user.
        api_response = api_instance.get_available_modules(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ModulesApi->get_available_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->get_available_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ModuleListEnvelope**](ModuleListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

