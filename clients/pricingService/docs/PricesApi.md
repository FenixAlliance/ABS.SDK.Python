# openapi_client.PricesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_pricing_service_prices_item_id_final_price_get**](PricesApi.md#api_v2_pricing_service_prices_item_id_final_price_get) | **GET** /api/v2/PricingService/Prices/{itemId}/FinalPrice | 
[**api_v2_pricing_service_prices_item_id_price_get**](PricesApi.md#api_v2_pricing_service_prices_item_id_price_get) | **GET** /api/v2/PricingService/Prices/{itemId}/Price | 
[**api_v2_pricing_service_prices_item_id_total_savings_get**](PricesApi.md#api_v2_pricing_service_prices_item_id_total_savings_get) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalSavings | 
[**api_v2_pricing_service_prices_item_id_total_taxes_get**](PricesApi.md#api_v2_pricing_service_prices_item_id_total_taxes_get) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalTaxes | 


# **api_v2_pricing_service_prices_item_id_final_price_get**
> MoneyEnvelope api_v2_pricing_service_prices_item_id_final_price_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_prices_item_id_final_price_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->api_v2_pricing_service_prices_item_id_final_price_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->api_v2_pricing_service_prices_item_id_final_price_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **currency_id** | **str**|  | [optional] [default to &#39;USD.USA&#39;]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_prices_item_id_price_get**
> PriceCalculationDtoEnvelope api_v2_pricing_service_prices_item_id_price_get(item_id, price_list_id=price_list_id, discounts_list_id=discounts_list_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.price_calculation_dto_envelope import PriceCalculationDtoEnvelope
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
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    price_list_id = 'price_list_id_example' # str |  (optional)
    discounts_list_id = 'discounts_list_id_example' # str |  (optional)
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_prices_item_id_price_get(item_id, price_list_id=price_list_id, discounts_list_id=discounts_list_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->api_v2_pricing_service_prices_item_id_price_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->api_v2_pricing_service_prices_item_id_price_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **price_list_id** | **str**|  | [optional] 
 **discounts_list_id** | **str**|  | [optional] 
 **currency_id** | **str**|  | [optional] [default to &#39;USD.USA&#39;]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PriceCalculationDtoEnvelope**](PriceCalculationDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_prices_item_id_total_savings_get**
> MoneyEnvelope api_v2_pricing_service_prices_item_id_total_savings_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_prices_item_id_total_savings_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->api_v2_pricing_service_prices_item_id_total_savings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->api_v2_pricing_service_prices_item_id_total_savings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **currency_id** | **str**|  | [optional] [default to &#39;USD.USA&#39;]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_prices_item_id_total_taxes_get**
> MoneyEnvelope api_v2_pricing_service_prices_item_id_total_taxes_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_prices_item_id_total_taxes_get(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->api_v2_pricing_service_prices_item_id_total_taxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->api_v2_pricing_service_prices_item_id_total_taxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **currency_id** | **str**|  | [optional] [default to &#39;USD.USA&#39;]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

