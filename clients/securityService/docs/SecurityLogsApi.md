# openapi_client.SecurityLogsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_logs_async**](SecurityLogsApi.md#get_security_logs_async) | **GET** /api/v2/SecurityService/SecurityLogs | Get business security logs
[**get_security_logs_count_async**](SecurityLogsApi.md#get_security_logs_count_async) | **GET** /api/v2/SecurityService/SecurityLogs/Count | Get business security logs count


# **get_security_logs_async**
> BusinessSecurityLogDtoListEnvelope get_security_logs_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get business security logs

Retrieves security logs for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.business_security_log_dto_list_envelope import BusinessSecurityLogDtoListEnvelope
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
    api_instance = openapi_client.SecurityLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business security logs
        api_response = api_instance.get_security_logs_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SecurityLogsApi->get_security_logs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityLogsApi->get_security_logs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessSecurityLogDtoListEnvelope**](BusinessSecurityLogDtoListEnvelope.md)

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

# **get_security_logs_count_async**
> Int32Envelope get_security_logs_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get business security logs count

Retrieves the count of security logs for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.SecurityLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business security logs count
        api_response = api_instance.get_security_logs_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SecurityLogsApi->get_security_logs_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityLogsApi->get_security_logs_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

