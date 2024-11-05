# openapi_client.CurrenciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_globe_service_currencies_currency_id_get**](CurrenciesApi.md#api_v2_globe_service_currencies_currency_id_get) | **GET** /api/v2/GlobeService/Currencies/{currencyId} | 
[**api_v2_globe_service_currencies_get**](CurrenciesApi.md#api_v2_globe_service_currencies_get) | **GET** /api/v2/GlobeService/Currencies | 


# **api_v2_globe_service_currencies_currency_id_get**
> CurrencyDtoEnvelope api_v2_globe_service_currencies_currency_id_get(currency_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.currency_dto_envelope import CurrencyDtoEnvelope
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
    api_instance = openapi_client.CurrenciesApi(api_client)
    currency_id = 'currency_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_globe_service_currencies_currency_id_get(currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CurrenciesApi->api_v2_globe_service_currencies_currency_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->api_v2_globe_service_currencies_currency_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CurrencyDtoEnvelope**](CurrencyDtoEnvelope.md)

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

# **api_v2_globe_service_currencies_get**
> CurrencyDtoListEnvelope api_v2_globe_service_currencies_get(api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.currency_dto_list_envelope import CurrencyDtoListEnvelope
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
    api_instance = openapi_client.CurrenciesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_globe_service_currencies_get(api_version=api_version, x_api_version=x_api_version)
        print("The response of CurrenciesApi->api_v2_globe_service_currencies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->api_v2_globe_service_currencies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CurrencyDtoListEnvelope**](CurrencyDtoListEnvelope.md)

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

