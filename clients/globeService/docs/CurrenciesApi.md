# openapi_client.CurrenciesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_currencies_async**](CurrenciesApi.md#count_currencies_async) | **GET** /api/v2/GlobeService/Currencies/Count | Count currencies
[**get_currency_by_id_async**](CurrenciesApi.md#get_currency_by_id_async) | **GET** /api/v2/GlobeService/Currencies/{currencyId} | Get currency by ID
[**get_enabled_currencies_async**](CurrenciesApi.md#get_enabled_currencies_async) | **GET** /api/v2/GlobeService/Currencies | Get all currencies


# **count_currencies_async**
> Int32Envelope count_currencies_async(api_version=api_version, x_api_version=x_api_version)

Count currencies

Returns the total number of enabled currencies, with optional OData filtering.

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
    api_instance = openapi_client.CurrenciesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count currencies
        api_response = api_instance.count_currencies_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of CurrenciesApi->count_currencies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->count_currencies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_currency_by_id_async**
> CurrencyDtoEnvelope get_currency_by_id_async(currency_id, api_version=api_version, x_api_version=x_api_version)

Get currency by ID

Retrieves a single currency by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.currency_dto_envelope import CurrencyDtoEnvelope
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
    api_instance = openapi_client.CurrenciesApi(api_client)
    currency_id = 'currency_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get currency by ID
        api_response = api_instance.get_currency_by_id_async(currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CurrenciesApi->get_currency_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->get_currency_by_id_async: %s\n" % e)
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

# **get_enabled_currencies_async**
> CurrencyDtoListEnvelope get_enabled_currencies_async(api_version=api_version, x_api_version=x_api_version)

Get all currencies

Retrieves the list of all enabled currencies with optional OData pagination and filtering.

### Example


```python
import openapi_client
from openapi_client.models.currency_dto_list_envelope import CurrencyDtoListEnvelope
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
    api_instance = openapi_client.CurrenciesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all currencies
        api_response = api_instance.get_enabled_currencies_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of CurrenciesApi->get_enabled_currencies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->get_enabled_currencies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CurrencyDtoListEnvelope**](CurrencyDtoListEnvelope.md)

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

