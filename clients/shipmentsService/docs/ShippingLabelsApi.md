# openapi_client.ShippingLabelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_label_async**](ShippingLabelsApi.md#create_shipping_label_async) | **POST** /api/v2/ShipmentsService/ShippingLabels | Create a shipping label
[**delete_shipping_label_async**](ShippingLabelsApi.md#delete_shipping_label_async) | **DELETE** /api/v2/ShipmentsService/ShippingLabels/{labelId} | Delete a shipping label
[**get_shipping_label_by_id_async**](ShippingLabelsApi.md#get_shipping_label_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingLabels/{labelId} | Get shipping label by ID
[**get_shipping_labels_async**](ShippingLabelsApi.md#get_shipping_labels_async) | **GET** /api/v2/ShipmentsService/ShippingLabels | Get all shipping labels
[**get_shipping_labels_count_async**](ShippingLabelsApi.md#get_shipping_labels_count_async) | **GET** /api/v2/ShipmentsService/ShippingLabels/Count | Get shipping labels count
[**patch_shipping_label_async**](ShippingLabelsApi.md#patch_shipping_label_async) | **PATCH** /api/v2/ShipmentsService/ShippingLabels/{labelId} | Patch a shipping label
[**update_shipping_label_async**](ShippingLabelsApi.md#update_shipping_label_async) | **PUT** /api/v2/ShipmentsService/ShippingLabels/{labelId} | Update a shipping label


# **create_shipping_label_async**
> create_shipping_label_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_label_create_dto=shipping_label_create_dto)

Create a shipping label

Creates a new shipping label.

### Example


```python
import openapi_client
from openapi_client.models.shipping_label_create_dto import ShippingLabelCreateDto
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_label_create_dto = openapi_client.ShippingLabelCreateDto() # ShippingLabelCreateDto |  (optional)

    try:
        # Create a shipping label
        api_instance.create_shipping_label_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_label_create_dto=shipping_label_create_dto)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->create_shipping_label_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_label_create_dto** | [**ShippingLabelCreateDto**](ShippingLabelCreateDto.md)|  | [optional] 

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

# **delete_shipping_label_async**
> delete_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping label

Deletes a shipping label.

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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    label_id = 'label_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping label
        api_instance.delete_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->delete_shipping_label_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **label_id** | **str**|  | 
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

# **get_shipping_label_by_id_async**
> ShippingLabelDtoEnvelope get_shipping_label_by_id_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version)

Get shipping label by ID

Retrieves a specific shipping label.

### Example


```python
import openapi_client
from openapi_client.models.shipping_label_dto_envelope import ShippingLabelDtoEnvelope
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    label_id = 'label_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping label by ID
        api_response = api_instance.get_shipping_label_by_id_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingLabelsApi->get_shipping_label_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->get_shipping_label_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **label_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingLabelDtoEnvelope**](ShippingLabelDtoEnvelope.md)

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

# **get_shipping_labels_async**
> ShippingLabelDtoListEnvelope get_shipping_labels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping labels

Retrieves all shipping labels for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_label_dto_list_envelope import ShippingLabelDtoListEnvelope
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping labels
        api_response = api_instance.get_shipping_labels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingLabelsApi->get_shipping_labels_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->get_shipping_labels_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingLabelDtoListEnvelope**](ShippingLabelDtoListEnvelope.md)

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

# **get_shipping_labels_count_async**
> Int32Envelope get_shipping_labels_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping labels count

Returns the count of shipping labels.

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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping labels count
        api_response = api_instance.get_shipping_labels_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingLabelsApi->get_shipping_labels_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->get_shipping_labels_count_async: %s\n" % e)
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

# **patch_shipping_label_async**
> EmptyEnvelope patch_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a shipping label

Partially updates an existing shipping label using JSON Patch.

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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    label_id = 'label_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a shipping label
        api_response = api_instance.patch_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ShippingLabelsApi->patch_shipping_label_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->patch_shipping_label_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **label_id** | **str**|  | 
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

# **update_shipping_label_async**
> update_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version, shipping_label_update_dto=shipping_label_update_dto)

Update a shipping label

Updates an existing shipping label.

### Example


```python
import openapi_client
from openapi_client.models.shipping_label_update_dto import ShippingLabelUpdateDto
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    label_id = 'label_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_label_update_dto = openapi_client.ShippingLabelUpdateDto() # ShippingLabelUpdateDto |  (optional)

    try:
        # Update a shipping label
        api_instance.update_shipping_label_async(tenant_id, label_id, api_version=api_version, x_api_version=x_api_version, shipping_label_update_dto=shipping_label_update_dto)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->update_shipping_label_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **label_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_label_update_dto** | [**ShippingLabelUpdateDto**](ShippingLabelUpdateDto.md)|  | [optional] 

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

