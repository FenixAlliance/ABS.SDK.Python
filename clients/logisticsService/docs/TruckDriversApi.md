# openapi_client.TruckDriversApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_truck_driver_async**](TruckDriversApi.md#activate_truck_driver_async) | **POST** /api/v2/LogisticsService/TruckDrivers/{driverId}/Activate | Activate a truck driver
[**create_truck_driver_async**](TruckDriversApi.md#create_truck_driver_async) | **POST** /api/v2/LogisticsService/TruckDrivers | Create a truck driver
[**deactivate_truck_driver_async**](TruckDriversApi.md#deactivate_truck_driver_async) | **POST** /api/v2/LogisticsService/TruckDrivers/{driverId}/Deactivate | Deactivate a truck driver
[**delete_truck_driver_async**](TruckDriversApi.md#delete_truck_driver_async) | **DELETE** /api/v2/LogisticsService/TruckDrivers/{driverId} | Delete a truck driver
[**get_truck_driver_by_id_async**](TruckDriversApi.md#get_truck_driver_by_id_async) | **GET** /api/v2/LogisticsService/TruckDrivers/{driverId} | Get truck driver by ID
[**get_truck_drivers_async**](TruckDriversApi.md#get_truck_drivers_async) | **GET** /api/v2/LogisticsService/TruckDrivers | Get all truck drivers
[**get_truck_drivers_count_async**](TruckDriversApi.md#get_truck_drivers_count_async) | **GET** /api/v2/LogisticsService/TruckDrivers/Count | Get truck drivers count
[**patch_truck_driver_async**](TruckDriversApi.md#patch_truck_driver_async) | **PATCH** /api/v2/LogisticsService/TruckDrivers/{driverId} | Patch a truck driver
[**update_truck_driver_async**](TruckDriversApi.md#update_truck_driver_async) | **PUT** /api/v2/LogisticsService/TruckDrivers/{driverId} | Update a truck driver


# **activate_truck_driver_async**
> EmptyEnvelope activate_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)

Activate a truck driver

Activates a truck driver.

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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Activate a truck driver
        api_response = api_instance.activate_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->activate_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->activate_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_truck_driver_async**
> EmptyEnvelope create_truck_driver_async(tenant_id, api_version=api_version, x_api_version=x_api_version, truck_driver_create_dto=truck_driver_create_dto)

Create a truck driver

Creates a new truck driver for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_driver_create_dto import TruckDriverCreateDto
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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_driver_create_dto = openapi_client.TruckDriverCreateDto() # TruckDriverCreateDto |  (optional)

    try:
        # Create a truck driver
        api_response = api_instance.create_truck_driver_async(tenant_id, api_version=api_version, x_api_version=x_api_version, truck_driver_create_dto=truck_driver_create_dto)
        print("The response of TruckDriversApi->create_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->create_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_driver_create_dto** | [**TruckDriverCreateDto**](TruckDriverCreateDto.md)|  | [optional] 

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

# **deactivate_truck_driver_async**
> EmptyEnvelope deactivate_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)

Deactivate a truck driver

Deactivates a truck driver.

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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deactivate a truck driver
        api_response = api_instance.deactivate_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->deactivate_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->deactivate_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_truck_driver_async**
> EmptyEnvelope delete_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)

Delete a truck driver

Deletes a truck driver.

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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a truck driver
        api_response = api_instance.delete_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->delete_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->delete_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
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

# **get_truck_driver_by_id_async**
> TruckDriverDtoEnvelope get_truck_driver_by_id_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)

Get truck driver by ID

Retrieves a specific truck driver by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.truck_driver_dto_envelope import TruckDriverDtoEnvelope
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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get truck driver by ID
        api_response = api_instance.get_truck_driver_by_id_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->get_truck_driver_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->get_truck_driver_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TruckDriverDtoEnvelope**](TruckDriverDtoEnvelope.md)

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

# **get_truck_drivers_async**
> TruckDriverDtoListEnvelope get_truck_drivers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all truck drivers

Retrieves all truck drivers for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.truck_driver_dto_list_envelope import TruckDriverDtoListEnvelope
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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all truck drivers
        api_response = api_instance.get_truck_drivers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->get_truck_drivers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->get_truck_drivers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TruckDriverDtoListEnvelope**](TruckDriverDtoListEnvelope.md)

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

# **get_truck_drivers_count_async**
> Int32Envelope get_truck_drivers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get truck drivers count

Returns the count of truck drivers for the specified tenant.

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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get truck drivers count
        api_response = api_instance.get_truck_drivers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TruckDriversApi->get_truck_drivers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->get_truck_drivers_count_async: %s\n" % e)
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

# **patch_truck_driver_async**
> EmptyEnvelope patch_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a truck driver

Partially updates an existing truck driver using JSON Patch.

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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a truck driver
        api_response = api_instance.patch_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TruckDriversApi->patch_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->patch_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
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

# **update_truck_driver_async**
> EmptyEnvelope update_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version, truck_driver_update_dto=truck_driver_update_dto)

Update a truck driver

Updates an existing truck driver.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_driver_update_dto import TruckDriverUpdateDto
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
    api_instance = openapi_client.TruckDriversApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    driver_id = 'driver_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_driver_update_dto = openapi_client.TruckDriverUpdateDto() # TruckDriverUpdateDto |  (optional)

    try:
        # Update a truck driver
        api_response = api_instance.update_truck_driver_async(tenant_id, driver_id, api_version=api_version, x_api_version=x_api_version, truck_driver_update_dto=truck_driver_update_dto)
        print("The response of TruckDriversApi->update_truck_driver_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TruckDriversApi->update_truck_driver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **driver_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_driver_update_dto** | [**TruckDriverUpdateDto**](TruckDriverUpdateDto.md)|  | [optional] 

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

