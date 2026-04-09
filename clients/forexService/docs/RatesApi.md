# openapi_client.RatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_historical_currency_rate_async**](RatesApi.md#get_historical_currency_rate_async) | **GET** /api/v2/ForexService/Rates/History/{currencyId} | Get historical rate for a currency
[**get_historical_currency_rates_async**](RatesApi.md#get_historical_currency_rates_async) | **GET** /api/v2/ForexService/Rates/History | Get historical currency rates
[**get_latest_currency_rate_async**](RatesApi.md#get_latest_currency_rate_async) | **GET** /api/v2/ForexService/Rates/Latest/{currencyId} | Get latest rate for a currency
[**get_latest_currency_rates_model_async**](RatesApi.md#get_latest_currency_rates_model_async) | **GET** /api/v2/ForexService/Rates/Latest | Get latest currency rates


# **get_historical_currency_rate_async**
> ExchangeRateEnvelope get_historical_currency_rate_async(currency_id, var_date=var_date, api_version=api_version, x_api_version=x_api_version)

Get historical rate for a currency

Retrieves the exchange rate for a specific currency as of a specific historical date.

### Example


```python
import openapi_client
from openapi_client.models.exchange_rate_envelope import ExchangeRateEnvelope
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
    api_instance = openapi_client.RatesApi(api_client)
    currency_id = 'currency_id_example' # str | 
    var_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get historical rate for a currency
        api_response = api_instance.get_historical_currency_rate_async(currency_id, var_date=var_date, api_version=api_version, x_api_version=x_api_version)
        print("The response of RatesApi->get_historical_currency_rate_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_historical_currency_rate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**|  | 
 **var_date** | **datetime**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExchangeRateEnvelope**](ExchangeRateEnvelope.md)

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

# **get_historical_currency_rates_async**
> ForexRatesDtoEnvelope get_historical_currency_rates_async(var_date=var_date, api_version=api_version, x_api_version=x_api_version)

Get historical currency rates

Retrieves exchange rates for all supported currencies as of a specific historical date.

### Example


```python
import openapi_client
from openapi_client.models.forex_rates_dto_envelope import ForexRatesDtoEnvelope
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
    api_instance = openapi_client.RatesApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get historical currency rates
        api_response = api_instance.get_historical_currency_rates_async(var_date=var_date, api_version=api_version, x_api_version=x_api_version)
        print("The response of RatesApi->get_historical_currency_rates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_historical_currency_rates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ForexRatesDtoEnvelope**](ForexRatesDtoEnvelope.md)

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

# **get_latest_currency_rate_async**
> ExchangeRateEnvelope get_latest_currency_rate_async(currency_id, api_version=api_version, x_api_version=x_api_version)

Get latest rate for a currency

Retrieves the latest exchange rate for a specific currency by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.exchange_rate_envelope import ExchangeRateEnvelope
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
    api_instance = openapi_client.RatesApi(api_client)
    currency_id = 'currency_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get latest rate for a currency
        api_response = api_instance.get_latest_currency_rate_async(currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RatesApi->get_latest_currency_rate_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_latest_currency_rate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExchangeRateEnvelope**](ExchangeRateEnvelope.md)

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

# **get_latest_currency_rates_model_async**
> ForexRatesDtoEnvelope get_latest_currency_rates_model_async(api_version=api_version, x_api_version=x_api_version)

Get latest currency rates

Retrieves the latest exchange rates for all supported currencies.

### Example


```python
import openapi_client
from openapi_client.models.forex_rates_dto_envelope import ForexRatesDtoEnvelope
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
    api_instance = openapi_client.RatesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get latest currency rates
        api_response = api_instance.get_latest_currency_rates_model_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of RatesApi->get_latest_currency_rates_model_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_latest_currency_rates_model_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ForexRatesDtoEnvelope**](ForexRatesDtoEnvelope.md)

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

