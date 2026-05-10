# openapi_client.CartsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_cart**](CartsApi.md#delete_system_cart) | **DELETE** /api/v2/SystemService/Carts/{cartId} | Delete a system cart
[**get_system_cart_by_id**](CartsApi.md#get_system_cart_by_id) | **GET** /api/v2/SystemService/Carts/{cartId} | Retrieve a single system cart by its ID
[**get_system_carts**](CartsApi.md#get_system_carts) | **GET** /api/v2/SystemService/Carts | Retrieve a list of system carts
[**get_system_carts_count**](CartsApi.md#get_system_carts_count) | **GET** /api/v2/SystemService/Carts/Count | Get the count of system carts


# **delete_system_cart**
> EmptyEnvelope delete_system_cart(cart_id, api_version=api_version, x_api_version=x_api_version)

Delete a system cart

Delete a system cart by its ID

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a system cart
        api_response = api_instance.delete_system_cart(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->delete_system_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->delete_system_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

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

# **get_system_cart_by_id**
> CartDtoEnvelope get_system_cart_by_id(cart_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single system cart by its ID

Retrieve a single system cart by its ID

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single system cart by its ID
        api_response = api_instance.get_system_cart_by_id(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_system_cart_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_system_cart_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

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

# **get_system_carts**
> CartDtoListEnvelope get_system_carts(api_version=api_version, x_api_version=x_api_version)

Retrieve a list of system carts

Retrieve a list of all carts in the system

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_list_envelope import CartDtoListEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of system carts
        api_response = api_instance.get_system_carts(api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_system_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_system_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoListEnvelope**](CartDtoListEnvelope.md)

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

# **get_system_carts_count**
> Int32Envelope get_system_carts_count(api_version=api_version, x_api_version=x_api_version)

Get the count of system carts

Get the count of all carts in the system

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
    api_instance = openapi_client.CartsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of system carts
        api_response = api_instance.get_system_carts_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_system_carts_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_system_carts_count: %s\n" % e)
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

