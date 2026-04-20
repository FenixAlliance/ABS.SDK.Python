# openapi_client.OrdersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_order**](OrdersApi.md#calculate_order) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Calculate | Calculates totals for an order.
[**calculate_order_line**](OrdersApi.md#calculate_order_line) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId}/Calculate | Calculates totals for an order line.
[**create_order**](OrdersApi.md#create_order) | **POST** /api/v2/OrdersService/Orders | Creates a new order.
[**create_order_line**](OrdersApi.md#create_order_line) | **POST** /api/v2/OrdersService/Orders/{orderId}/Lines | Creates a new order line.
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /api/v2/OrdersService/Orders/{orderId} | Deletes an order.
[**delete_order_line**](OrdersApi.md#delete_order_line) | **DELETE** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | Deletes an order line.
[**get_extended_orders**](OrdersApi.md#get_extended_orders) | **GET** /api/v2/OrdersService/Orders/Extended | Gets a list of extended orders for a tenant.
[**get_order**](OrdersApi.md#get_order) | **GET** /api/v2/OrdersService/Orders/{orderId} | Gets a specific order by ID.
[**get_order_line**](OrdersApi.md#get_order_line) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | Gets a specific order line.
[**get_order_lines**](OrdersApi.md#get_order_lines) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines | Gets order lines for an order.
[**get_order_lines_count**](OrdersApi.md#get_order_lines_count) | **GET** /api/v2/OrdersService/Orders/{orderId}/Lines/Count | Gets the count of order lines for an order.
[**get_orders**](OrdersApi.md#get_orders) | **GET** /api/v2/OrdersService/Orders | Gets a list of orders for a tenant.
[**get_orders_count**](OrdersApi.md#get_orders_count) | **GET** /api/v2/OrdersService/Orders/Count | Gets the count of orders for a tenant.
[**preview_order_email_template**](OrdersApi.md#preview_order_email_template) | **POST** /api/v2/OrdersService/Orders/{orderId}/Emails/Preview | Preview the rendered email for an Order.
[**send_order_email**](OrdersApi.md#send_order_email) | **POST** /api/v2/OrdersService/Orders/{orderId}/Emails/Send | Send a transactional email for an order.
[**submit_cart**](OrdersApi.md#submit_cart) | **POST** /api/v2/OrdersService/Orders/SubmitCart | Submits a cart and creates an order.
[**update_order**](OrdersApi.md#update_order) | **PUT** /api/v2/OrdersService/Orders/{orderId} | Updates an existing order.
[**update_order_line**](OrdersApi.md#update_order_line) | **PUT** /api/v2/OrdersService/Orders/{orderId}/Lines/{orderLineId} | Updates an order line.


# **calculate_order**
> EmptyEnvelope calculate_order(tenant_id, order_id)

Calculates totals for an order.

Performs calculation of totals and taxes for the specified order.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        # Calculates totals for an order.
        api_response = api_instance.calculate_order(tenant_id, order_id)
        print("The response of OrdersApi->calculate_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->calculate_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_order_line**
> EmptyEnvelope calculate_order_line(tenant_id, order_id, order_line_id)

Calculates totals for an order line.

Performs calculation of totals and taxes for the specified order line.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        # Calculates totals for an order line.
        api_response = api_instance.calculate_order_line(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->calculate_order_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->calculate_order_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> EmptyEnvelope create_order(tenant_id, order_create_dto=order_create_dto)

Creates a new order.

Creates a new order for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_create_dto import OrderCreateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_create_dto = openapi_client.OrderCreateDto() # OrderCreateDto |  (optional)

    try:
        # Creates a new order.
        api_response = api_instance.create_order(tenant_id, order_create_dto=order_create_dto)
        print("The response of OrdersApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_create_dto** | [**OrderCreateDto**](OrderCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order_line**
> EmptyEnvelope create_order_line(tenant_id, order_id, order_line_create_dto=order_line_create_dto)

Creates a new order line.

Creates a new line (item) for the specified order.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_line_create_dto import OrderLineCreateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_create_dto = openapi_client.OrderLineCreateDto() # OrderLineCreateDto |  (optional)

    try:
        # Creates a new order line.
        api_response = api_instance.create_order_line(tenant_id, order_id, order_line_create_dto=order_line_create_dto)
        print("The response of OrdersApi->create_order_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> EmptyEnvelope delete_order(tenant_id, order_id)

Deletes an order.

Deletes the specified order.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        # Deletes an order.
        api_response = api_instance.delete_order(tenant_id, order_id)
        print("The response of OrdersApi->delete_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_line**
> EmptyEnvelope delete_order_line(tenant_id, order_id, order_line_id)

Deletes an order line.

Deletes the specified order line.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        # Deletes an order line.
        api_response = api_instance.delete_order_line(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->delete_order_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_order_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_orders**
> ExtendedOrderDtoListEnvelope get_extended_orders(tenant_id)

Gets a list of extended orders for a tenant.

Retrieves a list of extended order details for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.extended_order_dto_list_envelope import ExtendedOrderDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a list of extended orders for a tenant.
        api_response = api_instance.get_extended_orders(tenant_id)
        print("The response of OrdersApi->get_extended_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_extended_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedOrderDtoListEnvelope**](ExtendedOrderDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderDtoEnvelope get_order(tenant_id, order_id)

Gets a specific order by ID.

Retrieves the details of a specific order by its ID.

### Example


```python
import openapi_client
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        # Gets a specific order by ID.
        api_response = api_instance.get_order(tenant_id, order_id)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

### Return type

[**OrderDtoEnvelope**](OrderDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line**
> OrderLineDtoEnvelope get_order_line(tenant_id, order_id, order_line_id)

Gets a specific order line.

Retrieves the details of a specific order line by its ID.

### Example


```python
import openapi_client
from openapi_client.models.order_line_dto_envelope import OrderLineDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 

    try:
        # Gets a specific order line.
        api_response = api_instance.get_order_line(tenant_id, order_id, order_line_id)
        print("The response of OrdersApi->get_order_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_lines**
> OrderLineDtoListEnvelope get_order_lines(tenant_id, order_id, item_id=item_id)

Gets order lines for an order.

Retrieves the lines (items) for the specified order.

### Example


```python
import openapi_client
from openapi_client.models.order_line_dto_list_envelope import OrderLineDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Gets order lines for an order.
        api_response = api_instance.get_order_lines(tenant_id, order_id, item_id=item_id)
        print("The response of OrdersApi->get_order_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_lines: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_lines_count**
> Int32Envelope get_order_lines_count(tenant_id, order_id)

Gets the count of order lines for an order.

Retrieves the total number of lines for the specified order.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 

    try:
        # Gets the count of order lines for an order.
        api_response = api_instance.get_order_lines_count(tenant_id, order_id)
        print("The response of OrdersApi->get_order_lines_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_lines_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> OrderDtoListEnvelope get_orders(tenant_id)

Gets a list of orders for a tenant.

Retrieves a list of orders for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.order_dto_list_envelope import OrderDtoListEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a list of orders for a tenant.
        api_response = api_instance.get_orders(tenant_id)
        print("The response of OrdersApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**OrderDtoListEnvelope**](OrderDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_count**
> Int32Envelope get_orders_count(tenant_id)

Gets the count of orders for a tenant.

Retrieves the total number of orders for the specified tenant.

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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of orders for a tenant.
        api_response = api_instance.get_orders_count(tenant_id)
        print("The response of OrdersApi->get_orders_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_order_email_template**
> preview_order_email_template(order_id, tenant_id, email_dispatch_request=email_dispatch_request)

Preview the rendered email for an Order.

Previews the rendered email template for the specified order. Only users with the 'send_email' permission are permitted.

### Example


```python
import openapi_client
from openapi_client.models.email_dispatch_request import EmailDispatchRequest
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
    api_instance = openapi_client.OrdersApi(api_client)
    order_id = 'order_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Preview the rendered email for an Order.
        api_instance.preview_order_email_template(order_id, tenant_id, email_dispatch_request=email_dispatch_request)
    except Exception as e:
        print("Exception when calling OrdersApi->preview_order_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **email_dispatch_request** | [**EmailDispatchRequest**](EmailDispatchRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_order_email**
> EmptyEnvelope send_order_email(tenant_id, order_id, email_dispatch_request=email_dispatch_request)

Send a transactional email for an order.

Sends a transactional email for the specified order. Only users with the 'send_email' permission are permitted.

### Example


```python
import openapi_client
from openapi_client.models.email_dispatch_request import EmailDispatchRequest
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Send a transactional email for an order.
        api_response = api_instance.send_order_email(tenant_id, order_id, email_dispatch_request=email_dispatch_request)
        print("The response of OrdersApi->send_order_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->send_order_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **order_id** | **str**|  | 
 **email_dispatch_request** | [**EmailDispatchRequest**](EmailDispatchRequest.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cart**
> OrderDtoEnvelope submit_cart(cart_id)

Submits a cart and creates an order.

Submits the specified cart and creates an order for the authenticated user.

### Example


```python
import openapi_client
from openapi_client.models.order_dto_envelope import OrderDtoEnvelope
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
    api_instance = openapi_client.OrdersApi(api_client)
    cart_id = 'cart_id_example' # str | 

    try:
        # Submits a cart and creates an order.
        api_response = api_instance.submit_cart(cart_id)
        print("The response of OrdersApi->submit_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->submit_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 

### Return type

[**OrderDtoEnvelope**](OrderDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> EmptyEnvelope update_order(tenant_id, order_id, order_update_dto=order_update_dto)

Updates an existing order.

Updates the details of an existing order.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_update_dto import OrderUpdateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_update_dto = openapi_client.OrderUpdateDto() # OrderUpdateDto |  (optional)

    try:
        # Updates an existing order.
        api_response = api_instance.update_order(tenant_id, order_id, order_update_dto=order_update_dto)
        print("The response of OrdersApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_order: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_line**
> EmptyEnvelope update_order_line(tenant_id, order_id, order_line_id, order_line_update_dto=order_line_update_dto)

Updates an order line.

Updates the details of a specific order line.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.order_line_update_dto import OrderLineUpdateDto
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
    api_instance = openapi_client.OrdersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    order_id = 'order_id_example' # str | 
    order_line_id = 'order_line_id_example' # str | 
    order_line_update_dto = openapi_client.OrderLineUpdateDto() # OrderLineUpdateDto |  (optional)

    try:
        # Updates an order line.
        api_response = api_instance.update_order_line(tenant_id, order_id, order_line_id, order_line_update_dto=order_line_update_dto)
        print("The response of OrdersApi->update_order_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_order_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

