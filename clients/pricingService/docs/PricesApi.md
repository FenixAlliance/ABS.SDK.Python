# openapi_client.PricesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_final_price**](PricesApi.md#get_final_price) | **GET** /api/v2/PricingService/Prices/{itemId}/FinalPrice | Gets the final price for an item
[**get_price**](PricesApi.md#get_price) | **GET** /api/v2/PricingService/Prices/{itemId}/Price | Gets the calculated price for an item
[**get_total_savings_in_usd**](PricesApi.md#get_total_savings_in_usd) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalSavings | Gets total savings for an item
[**get_total_taxes_in_usd**](PricesApi.md#get_total_taxes_in_usd) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalTaxes | Gets total taxes for an item


# **get_final_price**
> MoneyEnvelope get_final_price(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)

Gets the final price for an item

Gets the final price for an item after all discounts and taxes in the specified currency.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the final price for an item
        api_response = api_instance.get_final_price(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->get_final_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_final_price: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price**
> ItemPriceCalculationEnvelope get_price(item_id, price_list_id=price_list_id, discounts_list_id=discounts_list_id, quantity=quantity, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)

Gets the calculated price for an item

Calculates the price for an item considering price list, discount list, quantity, and currency.

### Example


```python
import openapi_client
from openapi_client.models.item_price_calculation_envelope import ItemPriceCalculationEnvelope
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
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    price_list_id = 'price_list_id_example' # str |  (optional)
    discounts_list_id = 'discounts_list_id_example' # str |  (optional)
    quantity = 1 # float |  (optional) (default to 1)
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the calculated price for an item
        api_response = api_instance.get_price(item_id, price_list_id=price_list_id, discounts_list_id=discounts_list_id, quantity=quantity, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->get_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **price_list_id** | **str**|  | [optional] 
 **discounts_list_id** | **str**|  | [optional] 
 **quantity** | **float**|  | [optional] [default to 1]
 **currency_id** | **str**|  | [optional] [default to &#39;USD.USA&#39;]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPriceCalculationEnvelope**](ItemPriceCalculationEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_savings_in_usd**
> MoneyEnvelope get_total_savings_in_usd(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)

Gets total savings for an item

Gets the total savings amount for an item in the specified currency.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets total savings for an item
        api_response = api_instance.get_total_savings_in_usd(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->get_total_savings_in_usd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_total_savings_in_usd: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_taxes_in_usd**
> MoneyEnvelope get_total_taxes_in_usd(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)

Gets total taxes for an item

Gets the total tax amount for an item in the specified currency.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PricesApi(api_client)
    item_id = 'item_id_example' # str | 
    currency_id = 'USD.USA' # str |  (optional) (default to 'USD.USA')
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets total taxes for an item
        api_response = api_instance.get_total_taxes_in_usd(item_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricesApi->get_total_taxes_in_usd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_total_taxes_in_usd: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

