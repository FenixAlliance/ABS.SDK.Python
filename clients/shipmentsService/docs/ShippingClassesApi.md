# openapi_client.ShippingClassesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_class_async**](ShippingClassesApi.md#create_shipping_class_async) | **POST** /api/v2/ShipmentsService/ShippingClasses | Create a shipping class
[**delete_shipping_class_async**](ShippingClassesApi.md#delete_shipping_class_async) | **DELETE** /api/v2/ShipmentsService/ShippingClasses/{classId} | Delete a shipping class
[**get_shipping_class_by_id_async**](ShippingClassesApi.md#get_shipping_class_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingClasses/{classId} | Get shipping class by ID
[**get_shipping_classes_async**](ShippingClassesApi.md#get_shipping_classes_async) | **GET** /api/v2/ShipmentsService/ShippingClasses | Get all shipping classes
[**get_shipping_classes_count_async**](ShippingClassesApi.md#get_shipping_classes_count_async) | **GET** /api/v2/ShipmentsService/ShippingClasses/Count | Get shipping classes count
[**update_shipping_class_async**](ShippingClassesApi.md#update_shipping_class_async) | **PUT** /api/v2/ShipmentsService/ShippingClasses/{classId} | Update a shipping class


# **create_shipping_class_async**
> create_shipping_class_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_class_create_dto=shipping_class_create_dto)

Create a shipping class

Creates a new shipping class.

### Example


```python
import openapi_client
from openapi_client.models.shipping_class_create_dto import ShippingClassCreateDto
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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_class_create_dto = openapi_client.ShippingClassCreateDto() # ShippingClassCreateDto |  (optional)

    try:
        # Create a shipping class
        api_instance.create_shipping_class_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_class_create_dto=shipping_class_create_dto)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->create_shipping_class_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_class_create_dto** | [**ShippingClassCreateDto**](ShippingClassCreateDto.md)|  | [optional] 

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

# **delete_shipping_class_async**
> delete_shipping_class_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping class

Deletes a shipping class.

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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    class_id = 'class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping class
        api_instance.delete_shipping_class_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->delete_shipping_class_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **class_id** | **str**|  | 
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

# **get_shipping_class_by_id_async**
> ShippingClassDtoEnvelope get_shipping_class_by_id_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version)

Get shipping class by ID

Retrieves a specific shipping class.

### Example


```python
import openapi_client
from openapi_client.models.shipping_class_dto_envelope import ShippingClassDtoEnvelope
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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    class_id = 'class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping class by ID
        api_response = api_instance.get_shipping_class_by_id_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingClassesApi->get_shipping_class_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->get_shipping_class_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **class_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingClassDtoEnvelope**](ShippingClassDtoEnvelope.md)

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

# **get_shipping_classes_async**
> ShippingClassDtoListEnvelope get_shipping_classes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping classes

Retrieves all shipping classes for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_class_dto_list_envelope import ShippingClassDtoListEnvelope
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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping classes
        api_response = api_instance.get_shipping_classes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingClassesApi->get_shipping_classes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->get_shipping_classes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingClassDtoListEnvelope**](ShippingClassDtoListEnvelope.md)

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

# **get_shipping_classes_count_async**
> Int32Envelope get_shipping_classes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping classes count

Returns the count of shipping classes.

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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping classes count
        api_response = api_instance.get_shipping_classes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingClassesApi->get_shipping_classes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->get_shipping_classes_count_async: %s\n" % e)
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

# **update_shipping_class_async**
> update_shipping_class_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version, shipping_class_update_dto=shipping_class_update_dto)

Update a shipping class

Updates an existing shipping class.

### Example


```python
import openapi_client
from openapi_client.models.shipping_class_update_dto import ShippingClassUpdateDto
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
    api_instance = openapi_client.ShippingClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    class_id = 'class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_class_update_dto = openapi_client.ShippingClassUpdateDto() # ShippingClassUpdateDto |  (optional)

    try:
        # Update a shipping class
        api_instance.update_shipping_class_async(tenant_id, class_id, api_version=api_version, x_api_version=x_api_version, shipping_class_update_dto=shipping_class_update_dto)
    except Exception as e:
        print("Exception when calling ShippingClassesApi->update_shipping_class_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **class_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_class_update_dto** | [**ShippingClassUpdateDto**](ShippingClassUpdateDto.md)|  | [optional] 

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

