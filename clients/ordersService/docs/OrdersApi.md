# openapi_client.OrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_orders_service_orders_count_get**](OrdersApi.md#api_v2_orders_service_orders_count_get) | **GET** /api/v2/OrdersService/Orders/Count | 
[**api_v2_orders_service_orders_extended_get**](OrdersApi.md#api_v2_orders_service_orders_extended_get) | **GET** /api/v2/OrdersService/Orders/Extended | 
[**api_v2_orders_service_orders_order_id_calculate_put**](OrdersApi.md#api_v2_orders_service_orders_order_id_calculate_put) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Calculate | 
[**api_v2_orders_service_orders_order_id_delete**](OrdersApi.md#api_v2_orders_service_orders_order_id_delete) | **DELETE** /api/v2/OrdersService/Orders/{orderId} | 
[**api_v2_orders_service_orders_order_id_lines_count_get**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_count_get) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines/Count | 
[**api_v2_orders_service_orders_order_id_lines_get**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_get) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines | 
[**api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId}/Calculate | 
[**api_v2_orders_service_orders_order_id_lines_order_line_id_delete**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_order_line_id_delete) | **DELETE** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | 
[**api_v2_orders_service_orders_order_id_lines_order_line_id_get**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_order_line_id_get) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | 
[**api_v2_orders_service_orders_order_id_lines_order_line_id_put**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_order_line_id_put) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | 
[**api_v2_orders_service_orders_order_id_lines_post**](OrdersApi.md#api_v2_orders_service_orders_order_id_lines_post) | **POST** /api/v2/OrdersService/Orders/{orderId}/Lines | 
[**api_v2_orders_service_orders_order_id_put**](OrdersApi.md#api_v2_orders_service_orders_order_id_put) | **PUT** /api/v2/OrdersService/Orders/{orderId} | 
[**api_v2_orders_service_orders_post**](OrdersApi.md#api_v2_orders_service_orders_post) | **POST** /api/v2/OrdersService/Orders | 
[**api_v2_orders_service_orders_submit_cart_post**](OrdersApi.md#api_v2_orders_service_orders_submit_cart_post) | **POST** /api/v2/OrdersService/Orders/SubmitCart | 
[**get_order_async**](OrdersApi.md#get_order_async) | **GET** /api/v2/OrdersService/Orders/{orderId} | 
[**get_orders_async**](OrdersApi.md#get_orders_async) | **GET** /api/v2/OrdersService/Orders | 


# **api_v2_orders_service_orders_count_get**
> Int32Envelope api_v2_orders_service_orders_count_get(tenant_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_count_get(tenant_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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

# **api_v2_orders_service_orders_extended_get**
> ExtendedOrderDtoListEnvelope api_v2_orders_service_orders_extended_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_order_dto_list_envelope import ExtendedOrderDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_extended_get(tenant_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedOrderDtoListEnvelope**](ExtendedOrderDtoListEnvelope.md)

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

# **api_v2_orders_service_orders_order_id_calculate_put**
> EmptyEnvelope api_v2_orders_service_orders_order_id_calculate_put(tenant_id, order_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_calculate_put(tenant_id, order_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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

# **api_v2_orders_service_orders_order_id_delete**
> EmptyEnvelope api_v2_orders_service_orders_order_id_delete(tenant_id, order_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_delete(tenant_id, order_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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

# **api_v2_orders_service_orders_order_id_lines_count_get**
> Int32Envelope api_v2_orders_service_orders_order_id_lines_count_get(tenant_id, order_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_count_get(tenant_id, order_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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

# **api_v2_orders_service_orders_order_id_lines_get**
> OrderLineDtoListEnvelope api_v2_orders_service_orders_order_id_lines_get(tenant_id, order_id, item_id=item_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.order_line_dto_list_envelope import OrderLineDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_get(tenant_id, order_id, item_id=item_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**OrderLineDtoListEnvelope**](OrderLineDtoListEnvelope.md)

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

# **api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put**
> EmptyEnvelope api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put(tenant_id, order_id, order_line_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_line_id** | **str**|  | 

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

# **api_v2_orders_service_orders_order_id_lines_order_line_id_delete**
> EmptyEnvelope api_v2_orders_service_orders_order_id_lines_order_line_id_delete(tenant_id, order_id, order_line_id)



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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_order_line_id_delete(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_line_id** | **str**|  | 

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

# **api_v2_orders_service_orders_order_id_lines_order_line_id_get**
> OrderLineDtoEnvelope api_v2_orders_service_orders_order_id_lines_order_line_id_get(tenant_id, order_id, order_line_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.order_line_dto_envelope import OrderLineDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_order_line_id_get(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_line_id** | **str**|  | 

### Return type

[**OrderLineDtoEnvelope**](OrderLineDtoEnvelope.md)

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

# **api_v2_orders_service_orders_order_id_lines_order_line_id_put**
> EmptyEnvelope api_v2_orders_service_orders_order_id_lines_order_line_id_put(tenant_id, order_id, order_line_id, order_line_update_dto=order_line_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_line_update_dto import OrderLineUpdateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 
    order_line_update_dto = openapi_client.OrderLineUpdateDto() # OrderLineUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_order_line_id_put(tenant_id, order_id, order_line_id, order_line_update_dto=order_line_update_dto)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_order_line_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_line_id** | **str**|  | 
 **order_line_update_dto** | [**OrderLineUpdateDto**](OrderLineUpdateDto.md)|  | [optional] 

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

# **api_v2_orders_service_orders_order_id_lines_post**
> EmptyEnvelope api_v2_orders_service_orders_order_id_lines_post(tenant_id, order_id, order_line_create_dto=order_line_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_line_create_dto import OrderLineCreateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_create_dto = openapi_client.OrderLineCreateDto() # OrderLineCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_lines_post(tenant_id, order_id, order_line_create_dto=order_line_create_dto)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_lines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_lines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_line_create_dto** | [**OrderLineCreateDto**](OrderLineCreateDto.md)|  | [optional] 

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

# **api_v2_orders_service_orders_order_id_put**
> EmptyEnvelope api_v2_orders_service_orders_order_id_put(tenant_id, order_id, order_update_dto=order_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_update_dto import OrderUpdateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_update_dto = openapi_client.OrderUpdateDto() # OrderUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_orders_service_orders_order_id_put(tenant_id, order_id, order_update_dto=order_update_dto)
        print("The response of OrdersApi->api_v2_orders_service_orders_order_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_order_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **order_update_dto** | [**OrderUpdateDto**](OrderUpdateDto.md)|  | [optional] 

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

# **api_v2_orders_service_orders_post**
> EmptyEnvelope api_v2_orders_service_orders_post(tenant_id, order_create_dto=order_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_create_dto import OrderCreateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_create_dto = openapi_client.OrderCreateDto() # OrderCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_orders_service_orders_post(tenant_id, order_create_dto=order_create_dto)
        print("The response of OrdersApi->api_v2_orders_service_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_create_dto** | [**OrderCreateDto**](OrderCreateDto.md)|  | [optional] 

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

# **api_v2_orders_service_orders_submit_cart_post**
> OrderDtoEnvelope api_v2_orders_service_orders_submit_cart_post(cart_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    cart_id = 'cart_id_example' # str | 

    try:
        api_response = api_instance.api_v2_orders_service_orders_submit_cart_post(cart_id)
        print("The response of OrdersApi->api_v2_orders_service_orders_submit_cart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api_v2_orders_service_orders_submit_cart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 

### Return type

[**OrderDtoEnvelope**](OrderDtoEnvelope.md)

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

# **get_order_async**
> OrderDtoEnvelope get_order_async(tenant_id, order_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        api_response = api_instance.get_order_async(tenant_id, order_id)
        print("The response of OrdersApi->get_order_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

### Return type

[**OrderDtoEnvelope**](OrderDtoEnvelope.md)

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

# **get_orders_async**
> OrderDtoListEnvelope get_orders_async(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.order_dto_list_envelope import OrderDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.get_orders_async(tenant_id)
        print("The response of OrdersApi->get_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**OrderDtoListEnvelope**](OrderDtoListEnvelope.md)

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

