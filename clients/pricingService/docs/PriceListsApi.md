# openapi_client.PriceListsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_pricing_service_price_lists_count_get**](PriceListsApi.md#api_v2_pricing_service_price_lists_count_get) | **GET** /api/v2/PricingService/PriceLists/Count | 
[**api_v2_pricing_service_price_lists_get**](PriceListsApi.md#api_v2_pricing_service_price_lists_get) | **GET** /api/v2/PricingService/PriceLists | 
[**api_v2_pricing_service_price_lists_post**](PriceListsApi.md#api_v2_pricing_service_price_lists_post) | **POST** /api/v2/PricingService/PriceLists | 
[**api_v2_pricing_service_price_lists_price_list_id_delete**](PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_delete) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId} | 
[**api_v2_pricing_service_price_lists_price_list_id_prices_post**](PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_post) | **POST** /api/v2/PricingService/PriceLists/{priceListId}/Prices | 
[**api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete**](PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
[**api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put**](PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put) | **PUT** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
[**api_v2_pricing_service_price_lists_price_list_id_put**](PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_put) | **PUT** /api/v2/PricingService/PriceLists/{priceListId} | 
[**get_price_list_async**](PriceListsApi.md#get_price_list_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId} | 
[**get_price_list_price_async**](PriceListsApi.md#get_price_list_price_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
[**get_price_list_prices_async**](PriceListsApi.md#get_price_list_prices_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices | 


# **api_v2_pricing_service_price_lists_count_get**
> Int32Envelope api_v2_pricing_service_price_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_count_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_get**
> PriceListDtoListEnvelope api_v2_pricing_service_price_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.price_list_dto_list_envelope import PriceListDtoListEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PriceListDtoListEnvelope**](PriceListDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_post**
> EmptyEnvelope api_v2_pricing_service_price_lists_post(tenant_id, api_version=api_version, x_api_version=x_api_version, price_list_create_dto=price_list_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.price_list_create_dto import PriceListCreateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    price_list_create_dto = openapi_client.PriceListCreateDto() # PriceListCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_post(tenant_id, api_version=api_version, x_api_version=x_api_version, price_list_create_dto=price_list_create_dto)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **price_list_create_dto** | [**PriceListCreateDto**](PriceListCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_price_list_id_delete**
> EmptyEnvelope api_v2_pricing_service_price_lists_price_list_id_delete(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_price_list_id_delete(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_price_list_id_prices_post**
> EmptyEnvelope api_v2_pricing_service_price_lists_price_list_id_prices_post(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version, item_price_create_dto=item_price_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_price_create_dto import ItemPriceCreateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_price_create_dto = openapi_client.ItemPriceCreateDto() # ItemPriceCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_price_list_id_prices_post(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version, item_price_create_dto=item_price_create_dto)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_price_create_dto** | [**ItemPriceCreateDto**](ItemPriceCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete**
> EmptyEnvelope api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put**
> EmptyEnvelope api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version, item_price_update_dto=item_price_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_price_update_dto import ItemPriceUpdateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_price_update_dto = openapi_client.ItemPriceUpdateDto() # ItemPriceUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version, item_price_update_dto=item_price_update_dto)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_price_update_dto** | [**ItemPriceUpdateDto**](ItemPriceUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_price_lists_price_list_id_put**
> EmptyEnvelope api_v2_pricing_service_price_lists_price_list_id_put(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version, price_list_update_dto=price_list_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.price_list_update_dto import PriceListUpdateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    price_list_update_dto = openapi_client.PriceListUpdateDto() # PriceListUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_price_lists_price_list_id_put(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version, price_list_update_dto=price_list_update_dto)
        print("The response of PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->api_v2_pricing_service_price_lists_price_list_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **price_list_update_dto** | [**PriceListUpdateDto**](PriceListUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_async**
> PriceListDtoEnvelope get_price_list_async(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.price_list_dto_envelope import PriceListDtoEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_price_list_async(tenant_id, price_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->get_price_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PriceListDtoEnvelope**](PriceListDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_price_async**
> ItemPriceDtoEnvelope get_price_list_price_async(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.item_price_dto_envelope import ItemPriceDtoEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_price_list_price_async(tenant_id, price_list_id, price_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->get_price_list_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPriceDtoEnvelope**](ItemPriceDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_prices_async**
> ItemPriceDtoListEnvelope get_price_list_prices_async(tenant_id, price_list_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.item_price_dto_list_envelope import ItemPriceDtoListEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_price_list_prices_async(tenant_id, price_list_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PriceListsApi->get_price_list_prices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_prices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPriceDtoListEnvelope**](ItemPriceDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

