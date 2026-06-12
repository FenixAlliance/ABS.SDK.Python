# openapi_client.ShippingMethodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_method_async**](ShippingMethodsApi.md#create_shipping_method_async) | **POST** /api/v2/ShipmentsService/ShippingMethods | Create a shipping method
[**delete_shipping_method_async**](ShippingMethodsApi.md#delete_shipping_method_async) | **DELETE** /api/v2/ShipmentsService/ShippingMethods/{methodId} | Delete a shipping method
[**get_shipping_method_by_id_async**](ShippingMethodsApi.md#get_shipping_method_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingMethods/{methodId} | Get shipping method by ID
[**get_shipping_methods_async**](ShippingMethodsApi.md#get_shipping_methods_async) | **GET** /api/v2/ShipmentsService/ShippingMethods | Get all shipping methods
[**get_shipping_methods_count_async**](ShippingMethodsApi.md#get_shipping_methods_count_async) | **GET** /api/v2/ShipmentsService/ShippingMethods/Count | Get shipping methods count
[**patch_shipping_method_async**](ShippingMethodsApi.md#patch_shipping_method_async) | **PATCH** /api/v2/ShipmentsService/ShippingMethods/{methodId} | Patch a shipping method
[**update_shipping_method_async**](ShippingMethodsApi.md#update_shipping_method_async) | **PUT** /api/v2/ShipmentsService/ShippingMethods/{methodId} | Update a shipping method


# **create_shipping_method_async**
> create_shipping_method_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_method_create_dto=shipping_method_create_dto)

Create a shipping method

Creates a new shipping method.

### Example


```python
import openapi_client
from openapi_client.models.shipping_method_create_dto import ShippingMethodCreateDto
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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_method_create_dto = openapi_client.ShippingMethodCreateDto() # ShippingMethodCreateDto |  (optional)

    try:
        # Create a shipping method
        api_instance.create_shipping_method_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_method_create_dto=shipping_method_create_dto)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->create_shipping_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_method_create_dto** | [**ShippingMethodCreateDto**](ShippingMethodCreateDto.md)|  | [optional] 

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

# **delete_shipping_method_async**
> delete_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping method

Deletes a shipping method.

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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    method_id = 'method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping method
        api_instance.delete_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->delete_shipping_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **method_id** | **str**|  | 
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

# **get_shipping_method_by_id_async**
> ShippingMethodDtoEnvelope get_shipping_method_by_id_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version)

Get shipping method by ID

Retrieves a specific shipping method.

### Example


```python
import openapi_client
from openapi_client.models.shipping_method_dto_envelope import ShippingMethodDtoEnvelope
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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    method_id = 'method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping method by ID
        api_response = api_instance.get_shipping_method_by_id_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingMethodsApi->get_shipping_method_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->get_shipping_method_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **method_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingMethodDtoEnvelope**](ShippingMethodDtoEnvelope.md)

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

# **get_shipping_methods_async**
> ShippingMethodDtoListEnvelope get_shipping_methods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping methods

Retrieves all shipping methods for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_method_dto_list_envelope import ShippingMethodDtoListEnvelope
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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping methods
        api_response = api_instance.get_shipping_methods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingMethodsApi->get_shipping_methods_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->get_shipping_methods_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingMethodDtoListEnvelope**](ShippingMethodDtoListEnvelope.md)

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

# **get_shipping_methods_count_async**
> Int32Envelope get_shipping_methods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping methods count

Returns the count of shipping methods.

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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping methods count
        api_response = api_instance.get_shipping_methods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingMethodsApi->get_shipping_methods_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->get_shipping_methods_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_shipping_method_async**
> EmptyEnvelope patch_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a shipping method

Partially updates an existing shipping method using JSON Patch.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    method_id = 'method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a shipping method
        api_response = api_instance.patch_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ShippingMethodsApi->patch_shipping_method_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->patch_shipping_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **method_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_method_async**
> update_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version, shipping_method_update_dto=shipping_method_update_dto)

Update a shipping method

Updates an existing shipping method.

### Example


```python
import openapi_client
from openapi_client.models.shipping_method_update_dto import ShippingMethodUpdateDto
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
    api_instance = openapi_client.ShippingMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    method_id = 'method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_method_update_dto = openapi_client.ShippingMethodUpdateDto() # ShippingMethodUpdateDto |  (optional)

    try:
        # Update a shipping method
        api_instance.update_shipping_method_async(tenant_id, method_id, api_version=api_version, x_api_version=x_api_version, shipping_method_update_dto=shipping_method_update_dto)
    except Exception as e:
        print("Exception when calling ShippingMethodsApi->update_shipping_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **method_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_method_update_dto** | [**ShippingMethodUpdateDto**](ShippingMethodUpdateDto.md)|  | [optional] 

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

