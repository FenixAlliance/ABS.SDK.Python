# openapi_client.ExchangeApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_amount_async**](ExchangeApi.md#exchange_amount_async) | **GET** /api/v2/ForexService/Exchange/Latest | Exchange currency at latest rates
[**exchange_amount_historical_async**](ExchangeApi.md#exchange_amount_historical_async) | **GET** /api/v2/ForexService/Exchange/History | Exchange currency at historical rates


# **exchange_amount_async**
> MoneyEnvelope exchange_amount_async(amount, source_currency_id, target_currency_id)

Exchange currency at latest rates

Exchange an amount of money from one currency to another using the latest available exchange rates.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ExchangeApi(api_client)
    amount = 3.4 # float | 
    source_currency_id = 'source_currency_id_example' # str | 
    target_currency_id = 'target_currency_id_example' # str | 

    try:
        # Exchange currency at latest rates
        api_response = api_instance.exchange_amount_async(amount, source_currency_id, target_currency_id)
        print("The response of ExchangeApi->exchange_amount_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->exchange_amount_async: %s\n" % e)
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

# **exchange_amount_historical_async**
> MoneyEnvelope exchange_amount_historical_async(amount, source_currency_id, target_currency_id, var_date)

Exchange currency at historical rates

Exchange an amount of money from one currency to another using exchange rates from a specific historical date.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ExchangeApi(api_client)
    amount = 3.4 # float | 
    source_currency_id = 'source_currency_id_example' # str | 
    target_currency_id = 'target_currency_id_example' # str | 
    var_date = '2013-10-20' # date | 

    try:
        # Exchange currency at historical rates
        api_response = api_instance.exchange_amount_historical_async(amount, source_currency_id, target_currency_id, var_date)
        print("The response of ExchangeApi->exchange_amount_historical_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->exchange_amount_historical_async: %s\n" % e)
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

