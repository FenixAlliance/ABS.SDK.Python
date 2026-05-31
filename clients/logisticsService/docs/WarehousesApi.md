# openapi_client.WarehousesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_warehouse_async**](WarehousesApi.md#create_warehouse_async) | **POST** /api/v2/LogisticsService/Warehouses | Create a warehouse
[**delete_warehouse_async**](WarehousesApi.md#delete_warehouse_async) | **DELETE** /api/v2/LogisticsService/Warehouses/{warehouseId} | Delete a warehouse
[**get_warehouse_by_id_async**](WarehousesApi.md#get_warehouse_by_id_async) | **GET** /api/v2/LogisticsService/Warehouses/{warehouseId} | Get warehouse by ID
[**get_warehouses_async**](WarehousesApi.md#get_warehouses_async) | **GET** /api/v2/LogisticsService/Warehouses | Get all warehouses
[**get_warehouses_count_async**](WarehousesApi.md#get_warehouses_count_async) | **GET** /api/v2/LogisticsService/Warehouses/Count | Get warehouses count
[**update_warehouse_async**](WarehousesApi.md#update_warehouse_async) | **PUT** /api/v2/LogisticsService/Warehouses/{warehouseId} | Update a warehouse


# **create_warehouse_async**
> EmptyEnvelope create_warehouse_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warehouse_create_dto=warehouse_create_dto)

Create a warehouse

Creates a new warehouse.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warehouse_create_dto import WarehouseCreateDto
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
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warehouse_create_dto = openapi_client.WarehouseCreateDto() # WarehouseCreateDto |  (optional)

    try:
        # Create a warehouse
        api_response = api_instance.create_warehouse_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warehouse_create_dto=warehouse_create_dto)
        print("The response of WarehousesApi->create_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->create_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warehouse_create_dto** | [**WarehouseCreateDto**](WarehouseCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_async**
> EmptyEnvelope delete_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)

Delete a warehouse

Deletes a warehouse.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a warehouse
        api_response = api_instance.delete_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousesApi->delete_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->delete_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_by_id_async**
> WarehouseDtoEnvelope get_warehouse_by_id_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)

Get warehouse by ID

Retrieves a specific warehouse.

### Example


```python
import openapi_client
from openapi_client.models.warehouse_dto_envelope import WarehouseDtoEnvelope
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
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warehouse by ID
        api_response = api_instance.get_warehouse_by_id_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousesApi->get_warehouse_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_warehouse_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarehouseDtoEnvelope**](WarehouseDtoEnvelope.md)

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

# **get_warehouses_async**
> WarehouseDtoListEnvelope get_warehouses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all warehouses

Retrieves all warehouses for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.warehouse_dto_list_envelope import WarehouseDtoListEnvelope
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
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all warehouses
        api_response = api_instance.get_warehouses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousesApi->get_warehouses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_warehouses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarehouseDtoListEnvelope**](WarehouseDtoListEnvelope.md)

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

# **get_warehouses_count_async**
> Int32Envelope get_warehouses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get warehouses count

Returns the count of warehouses.

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
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warehouses count
        api_response = api_instance.get_warehouses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousesApi->get_warehouses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_warehouses_count_async: %s\n" % e)
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

# **update_warehouse_async**
> EmptyEnvelope update_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version, warehouse_update_dto=warehouse_update_dto)

Update a warehouse

Updates an existing warehouse.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warehouse_update_dto import WarehouseUpdateDto
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
    api_instance = openapi_client.WarehousesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warehouse_update_dto = openapi_client.WarehouseUpdateDto() # WarehouseUpdateDto |  (optional)

    try:
        # Update a warehouse
        api_response = api_instance.update_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version, warehouse_update_dto=warehouse_update_dto)
        print("The response of WarehousesApi->update_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->update_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warehouse_update_dto** | [**WarehouseUpdateDto**](WarehouseUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

