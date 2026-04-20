# openapi_client.MerchantsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchant_by_id**](MerchantsApi.md#get_merchant_by_id) | **GET** /api/v2/CatalogService/Merchants/{merchantId} | Get merchant by ID
[**get_merchants**](MerchantsApi.md#get_merchants) | **GET** /api/v2/CatalogService/Merchants | Get all merchants
[**get_merchants_count**](MerchantsApi.md#get_merchants_count) | **GET** /api/v2/CatalogService/Merchants/Count | Count merchants


# **get_merchant_by_id**
> MerchantDtoEnvelope get_merchant_by_id(merchant_id, api_version=api_version, x_api_version=x_api_version)

Get merchant by ID

Retrieves a merchant by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.merchant_dto_envelope import MerchantDtoEnvelope
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
    api_instance = openapi_client.MerchantsApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get merchant by ID
        api_response = api_instance.get_merchant_by_id(merchant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MerchantsApi->get_merchant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->get_merchant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MerchantDtoEnvelope**](MerchantDtoEnvelope.md)

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

# **get_merchants**
> MerchantDtoListEnvelope get_merchants(api_version=api_version, x_api_version=x_api_version)

Get all merchants

Retrieves all merchants, optionally filtered by OData query options.

### Example


```python
import openapi_client
from openapi_client.models.merchant_dto_list_envelope import MerchantDtoListEnvelope
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
    api_instance = openapi_client.MerchantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all merchants
        api_response = api_instance.get_merchants(api_version=api_version, x_api_version=x_api_version)
        print("The response of MerchantsApi->get_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->get_merchants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MerchantDtoListEnvelope**](MerchantDtoListEnvelope.md)

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

# **get_merchants_count**
> Int32Envelope get_merchants_count(api_version=api_version, x_api_version=x_api_version)

Count merchants

Counts the number of merchants, optionally filtered by OData query options.

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
    api_instance = openapi_client.MerchantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count merchants
        api_response = api_instance.get_merchants_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of MerchantsApi->get_merchants_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->get_merchants_count: %s\n" % e)
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

