# openapi_client.ExchangeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_forex_service_exchange_history_get**](ExchangeApi.md#api_v2_forex_service_exchange_history_get) | **GET** /api/v2/ForexService/Exchange/History | 
[**api_v2_forex_service_exchange_latest_get**](ExchangeApi.md#api_v2_forex_service_exchange_latest_get) | **GET** /api/v2/ForexService/Exchange/Latest | 


# **api_v2_forex_service_exchange_history_get**
> MoneyEnvelope api_v2_forex_service_exchange_history_get(amount, source_currency_id, target_currency_id, var_date)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ExchangeApi(api_client)
    amount = 3.4 # float | 
    source_currency_id = 'source_currency_id_example' # str | 
    target_currency_id = 'target_currency_id_example' # str | 
    var_date = '2013-10-20' # date | 

    try:
        api_response = api_instance.api_v2_forex_service_exchange_history_get(amount, source_currency_id, target_currency_id, var_date)
        print("The response of ExchangeApi->api_v2_forex_service_exchange_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->api_v2_forex_service_exchange_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**|  | 
 **source_currency_id** | **str**|  | 
 **target_currency_id** | **str**|  | 
 **var_date** | **date**|  | 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **api_v2_forex_service_exchange_latest_get**
> MoneyEnvelope api_v2_forex_service_exchange_latest_get(amount, source_currency_id, target_currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ExchangeApi(api_client)
    amount = 3.4 # float | 
    source_currency_id = 'source_currency_id_example' # str | 
    target_currency_id = 'target_currency_id_example' # str | 

    try:
        api_response = api_instance.api_v2_forex_service_exchange_latest_get(amount, source_currency_id, target_currency_id)
        print("The response of ExchangeApi->api_v2_forex_service_exchange_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->api_v2_forex_service_exchange_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**|  | 
 **source_currency_id** | **str**|  | 
 **target_currency_id** | **str**|  | 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

