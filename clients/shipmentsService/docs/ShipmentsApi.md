# openapi_client.ShipmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipment_async**](ShipmentsApi.md#create_shipment_async) | **POST** /api/v2/ShipmentsService/Shipments | Create a shipment
[**delete_shipment_async**](ShipmentsApi.md#delete_shipment_async) | **DELETE** /api/v2/ShipmentsService/Shipments/{shipmentId} | Delete a shipment
[**get_shipment_by_id_async**](ShipmentsApi.md#get_shipment_by_id_async) | **GET** /api/v2/ShipmentsService/Shipments/{shipmentId} | Get shipment by ID
[**get_shipments_async**](ShipmentsApi.md#get_shipments_async) | **GET** /api/v2/ShipmentsService/Shipments | Get all shipments
[**get_shipments_count_async**](ShipmentsApi.md#get_shipments_count_async) | **GET** /api/v2/ShipmentsService/Shipments/Count | Get shipments count
[**patch_shipment_async**](ShipmentsApi.md#patch_shipment_async) | **PATCH** /api/v2/ShipmentsService/Shipments/{shipmentId} | Patch a shipment
[**update_shipment_async**](ShipmentsApi.md#update_shipment_async) | **PUT** /api/v2/ShipmentsService/Shipments/{shipmentId} | Update a shipment


# **create_shipment_async**
> create_shipment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipment_create_dto=shipment_create_dto)

Create a shipment

Creates a new shipment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipment_create_dto import ShipmentCreateDto
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipment_create_dto = openapi_client.ShipmentCreateDto() # ShipmentCreateDto |  (optional)

    try:
        # Create a shipment
        api_instance.create_shipment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipment_create_dto=shipment_create_dto)
    except Exception as e:
        print("Exception when calling ShipmentsApi->create_shipment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipment_create_dto** | [**ShipmentCreateDto**](ShipmentCreateDto.md)|  | [optional] 

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

# **delete_shipment_async**
> delete_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipment

Deletes a shipment.

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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shipment_id = 'shipment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipment
        api_instance.delete_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShipmentsApi->delete_shipment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shipment_id** | **str**|  | 
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

# **get_shipment_by_id_async**
> ShipmentDtoEnvelope get_shipment_by_id_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version)

Get shipment by ID

Retrieves a specific shipment by its ID.

### Example


```python
import openapi_client
from openapi_client.models.shipment_dto_envelope import ShipmentDtoEnvelope
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shipment_id = 'shipment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipment by ID
        api_response = api_instance.get_shipment_by_id_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShipmentsApi->get_shipment_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipment_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shipment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShipmentDtoEnvelope**](ShipmentDtoEnvelope.md)

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

# **get_shipments_async**
> ShipmentDtoListEnvelope get_shipments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipments

Retrieves all shipments for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipment_dto_list_envelope import ShipmentDtoListEnvelope
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipments
        api_response = api_instance.get_shipments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShipmentsApi->get_shipments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShipmentDtoListEnvelope**](ShipmentDtoListEnvelope.md)

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

# **get_shipments_count_async**
> Int32Envelope get_shipments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipments count

Returns the count of shipments for the specified tenant.

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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipments count
        api_response = api_instance.get_shipments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShipmentsApi->get_shipments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipments_count_async: %s\n" % e)
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

# **patch_shipment_async**
> EmptyEnvelope patch_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a shipment

Partially updates an existing shipment using JSON Patch.

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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shipment_id = 'shipment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a shipment
        api_response = api_instance.patch_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ShipmentsApi->patch_shipment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->patch_shipment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shipment_id** | **str**|  | 
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

# **update_shipment_async**
> update_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version, shipment_update_dto=shipment_update_dto)

Update a shipment

Updates an existing shipment.

### Example


```python
import openapi_client
from openapi_client.models.shipment_update_dto import ShipmentUpdateDto
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shipment_id = 'shipment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipment_update_dto = openapi_client.ShipmentUpdateDto() # ShipmentUpdateDto |  (optional)

    try:
        # Update a shipment
        api_instance.update_shipment_async(tenant_id, shipment_id, api_version=api_version, x_api_version=x_api_version, shipment_update_dto=shipment_update_dto)
    except Exception as e:
        print("Exception when calling ShipmentsApi->update_shipment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shipment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipment_update_dto** | [**ShipmentUpdateDto**](ShipmentUpdateDto.md)|  | [optional] 

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

