# openapi_client.ShippingCouriersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_courier_async**](ShippingCouriersApi.md#create_shipping_courier_async) | **POST** /api/v2/ShipmentsService/ShippingCouriers | Create a shipping courier
[**delete_shipping_courier_async**](ShippingCouriersApi.md#delete_shipping_courier_async) | **DELETE** /api/v2/ShipmentsService/ShippingCouriers/{courierId} | Delete a shipping courier
[**get_shipping_courier_by_id_async**](ShippingCouriersApi.md#get_shipping_courier_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingCouriers/{courierId} | Get shipping courier by ID
[**get_shipping_couriers_async**](ShippingCouriersApi.md#get_shipping_couriers_async) | **GET** /api/v2/ShipmentsService/ShippingCouriers | Get all shipping couriers
[**get_shipping_couriers_count_async**](ShippingCouriersApi.md#get_shipping_couriers_count_async) | **GET** /api/v2/ShipmentsService/ShippingCouriers/Count | Get shipping couriers count
[**update_shipping_courier_async**](ShippingCouriersApi.md#update_shipping_courier_async) | **PUT** /api/v2/ShipmentsService/ShippingCouriers/{courierId} | Update a shipping courier


# **create_shipping_courier_async**
> create_shipping_courier_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_courier_create_dto=shipping_courier_create_dto)

Create a shipping courier

Creates a new shipping courier.

### Example


```python
import openapi_client
from openapi_client.models.shipping_courier_create_dto import ShippingCourierCreateDto
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
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_courier_create_dto = openapi_client.ShippingCourierCreateDto() # ShippingCourierCreateDto |  (optional)

    try:
        # Create a shipping courier
        api_instance.create_shipping_courier_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_courier_create_dto=shipping_courier_create_dto)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->create_shipping_courier_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_courier_create_dto** | [**ShippingCourierCreateDto**](ShippingCourierCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipping_courier_async**
> delete_shipping_courier_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping courier

Deletes a shipping courier.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    courier_id = 'courier_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping courier
        api_instance.delete_shipping_courier_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->delete_shipping_courier_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **courier_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **get_shipping_courier_by_id_async**
> ShippingCourierDtoEnvelope get_shipping_courier_by_id_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version)

Get shipping courier by ID

Retrieves a specific shipping courier by its ID.

### Example


```python
import openapi_client
from openapi_client.models.shipping_courier_dto_envelope import ShippingCourierDtoEnvelope
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
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    courier_id = 'courier_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping courier by ID
        api_response = api_instance.get_shipping_courier_by_id_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingCouriersApi->get_shipping_courier_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->get_shipping_courier_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **courier_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingCourierDtoEnvelope**](ShippingCourierDtoEnvelope.md)

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

# **get_shipping_couriers_async**
> ShippingCourierDtoListEnvelope get_shipping_couriers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping couriers

Retrieves all shipping couriers for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_courier_dto_list_envelope import ShippingCourierDtoListEnvelope
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
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping couriers
        api_response = api_instance.get_shipping_couriers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingCouriersApi->get_shipping_couriers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->get_shipping_couriers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingCourierDtoListEnvelope**](ShippingCourierDtoListEnvelope.md)

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

# **get_shipping_couriers_count_async**
> Int32Envelope get_shipping_couriers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping couriers count

Returns the count of shipping couriers for the specified tenant.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping couriers count
        api_response = api_instance.get_shipping_couriers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingCouriersApi->get_shipping_couriers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->get_shipping_couriers_count_async: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_courier_async**
> update_shipping_courier_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version, shipping_courier_update_dto=shipping_courier_update_dto)

Update a shipping courier

Updates an existing shipping courier.

### Example


```python
import openapi_client
from openapi_client.models.shipping_courier_update_dto import ShippingCourierUpdateDto
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
    api_instance = openapi_client.ShippingCouriersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    courier_id = 'courier_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_courier_update_dto = openapi_client.ShippingCourierUpdateDto() # ShippingCourierUpdateDto |  (optional)

    try:
        # Update a shipping courier
        api_instance.update_shipping_courier_async(tenant_id, courier_id, api_version=api_version, x_api_version=x_api_version, shipping_courier_update_dto=shipping_courier_update_dto)
    except Exception as e:
        print("Exception when calling ShippingCouriersApi->update_shipping_courier_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **courier_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_courier_update_dto** | [**ShippingCourierUpdateDto**](ShippingCourierUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

