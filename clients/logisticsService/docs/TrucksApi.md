# openapi_client.TrucksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**arrive_trip_async**](TrucksApi.md#arrive_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId}/Arrive | Arrive a trip
[**cancel_trip_async**](TrucksApi.md#cancel_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId}/Cancel | Cancel a trip
[**create_truck_async**](TrucksApi.md#create_truck_async) | **POST** /api/v2/LogisticsService/Trucks | Create a truck
[**create_truck_trip_async**](TrucksApi.md#create_truck_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips | Create a truck trip
[**delete_truck_async**](TrucksApi.md#delete_truck_async) | **DELETE** /api/v2/LogisticsService/Trucks/{truckId} | Delete a truck
[**delete_truck_trip_async**](TrucksApi.md#delete_truck_trip_async) | **DELETE** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId} | Delete a truck trip
[**deliver_trip_async**](TrucksApi.md#deliver_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId}/Deliver | Deliver a trip
[**depart_trip_async**](TrucksApi.md#depart_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId}/Depart | Depart a trip
[**dispatch_trip_async**](TrucksApi.md#dispatch_trip_async) | **POST** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId}/Dispatch | Dispatch a trip
[**get_truck_by_id_async**](TrucksApi.md#get_truck_by_id_async) | **GET** /api/v2/LogisticsService/Trucks/{truckId} | Get truck by ID
[**get_truck_trips_async**](TrucksApi.md#get_truck_trips_async) | **GET** /api/v2/LogisticsService/Trucks/{truckId}/Trips | Get truck trips
[**get_truck_trips_count_async**](TrucksApi.md#get_truck_trips_count_async) | **GET** /api/v2/LogisticsService/Trucks/{truckId}/Trips/Count | Get truck trips count
[**get_trucks_async**](TrucksApi.md#get_trucks_async) | **GET** /api/v2/LogisticsService/Trucks | Get all trucks
[**get_trucks_count_async**](TrucksApi.md#get_trucks_count_async) | **GET** /api/v2/LogisticsService/Trucks/Count | Get trucks count
[**patch_truck_async**](TrucksApi.md#patch_truck_async) | **PATCH** /api/v2/LogisticsService/Trucks/{truckId} | Patch a truck
[**patch_truck_trip_async**](TrucksApi.md#patch_truck_trip_async) | **PATCH** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId} | Patch a truck trip
[**update_truck_async**](TrucksApi.md#update_truck_async) | **PUT** /api/v2/LogisticsService/Trucks/{truckId} | Update a truck
[**update_truck_trip_async**](TrucksApi.md#update_truck_trip_async) | **PUT** /api/v2/LogisticsService/Trucks/{truckId}/Trips/{tripId} | Update a truck trip


# **arrive_trip_async**
> EmptyEnvelope arrive_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Arrive a trip

Marks a truck trip as arrived.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Arrive a trip
        api_response = api_instance.arrive_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->arrive_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->arrive_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **cancel_trip_async**
> EmptyEnvelope cancel_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Cancel a trip

Cancels a truck trip.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel a trip
        api_response = api_instance.cancel_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->cancel_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->cancel_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **create_truck_async**
> EmptyEnvelope create_truck_async(tenant_id, api_version=api_version, x_api_version=x_api_version, truck_create_dto=truck_create_dto)

Create a truck

Creates a new truck for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_create_dto import TruckCreateDto
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_create_dto = openapi_client.TruckCreateDto() # TruckCreateDto |  (optional)

    try:
        # Create a truck
        api_response = api_instance.create_truck_async(tenant_id, api_version=api_version, x_api_version=x_api_version, truck_create_dto=truck_create_dto)
        print("The response of TrucksApi->create_truck_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->create_truck_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_create_dto** | [**TruckCreateDto**](TruckCreateDto.md)|  | [optional] 

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

# **create_truck_trip_async**
> EmptyEnvelope create_truck_trip_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, truck_trip_create_dto=truck_trip_create_dto)

Create a truck trip

Creates a new trip for a truck.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_trip_create_dto import TruckTripCreateDto
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_trip_create_dto = openapi_client.TruckTripCreateDto() # TruckTripCreateDto |  (optional)

    try:
        # Create a truck trip
        api_response = api_instance.create_truck_trip_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, truck_trip_create_dto=truck_trip_create_dto)
        print("The response of TrucksApi->create_truck_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->create_truck_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_trip_create_dto** | [**TruckTripCreateDto**](TruckTripCreateDto.md)|  | [optional] 

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

# **delete_truck_async**
> EmptyEnvelope delete_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)

Delete a truck

Deletes a truck.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a truck
        api_response = api_instance.delete_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->delete_truck_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->delete_truck_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
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

# **delete_truck_trip_async**
> EmptyEnvelope delete_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Delete a truck trip

Deletes a truck trip.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a truck trip
        api_response = api_instance.delete_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->delete_truck_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->delete_truck_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **deliver_trip_async**
> EmptyEnvelope deliver_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Deliver a trip

Marks a truck trip as delivered.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deliver a trip
        api_response = api_instance.deliver_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->deliver_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->deliver_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **depart_trip_async**
> EmptyEnvelope depart_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Depart a trip

Marks a truck trip as departed.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Depart a trip
        api_response = api_instance.depart_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->depart_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->depart_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **dispatch_trip_async**
> EmptyEnvelope dispatch_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)

Dispatch a trip

Dispatches a truck trip.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Dispatch a trip
        api_response = api_instance.dispatch_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->dispatch_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->dispatch_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **get_truck_by_id_async**
> TruckDtoEnvelope get_truck_by_id_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)

Get truck by ID

Retrieves a specific truck by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.truck_dto_envelope import TruckDtoEnvelope
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get truck by ID
        api_response = api_instance.get_truck_by_id_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->get_truck_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->get_truck_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TruckDtoEnvelope**](TruckDtoEnvelope.md)

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

# **get_truck_trips_async**
> TruckTripDtoListEnvelope get_truck_trips_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)

Get truck trips

Retrieves all trips for a specific truck.

### Example


```python
import openapi_client
from openapi_client.models.truck_trip_dto_list_envelope import TruckTripDtoListEnvelope
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get truck trips
        api_response = api_instance.get_truck_trips_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->get_truck_trips_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->get_truck_trips_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TruckTripDtoListEnvelope**](TruckTripDtoListEnvelope.md)

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

# **get_truck_trips_count_async**
> Int32Envelope get_truck_trips_count_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)

Get truck trips count

Returns the count of trips for a specific truck.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get truck trips count
        api_response = api_instance.get_truck_trips_count_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->get_truck_trips_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->get_truck_trips_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
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

# **get_trucks_async**
> TruckDtoListEnvelope get_trucks_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all trucks

Retrieves all trucks for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.truck_dto_list_envelope import TruckDtoListEnvelope
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all trucks
        api_response = api_instance.get_trucks_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->get_trucks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->get_trucks_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TruckDtoListEnvelope**](TruckDtoListEnvelope.md)

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

# **get_trucks_count_async**
> Int32Envelope get_trucks_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get trucks count

Returns the count of trucks for the specified tenant.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get trucks count
        api_response = api_instance.get_trucks_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrucksApi->get_trucks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->get_trucks_count_async: %s\n" % e)
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

# **patch_truck_async**
> EmptyEnvelope patch_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a truck

Partially updates an existing truck using JSON Patch.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a truck
        api_response = api_instance.patch_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TrucksApi->patch_truck_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->patch_truck_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
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

# **patch_truck_trip_async**
> EmptyEnvelope patch_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a truck trip

Partially updates an existing truck trip using JSON Patch.

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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a truck trip
        api_response = api_instance.patch_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TrucksApi->patch_truck_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->patch_truck_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
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

# **update_truck_async**
> EmptyEnvelope update_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, truck_update_dto=truck_update_dto)

Update a truck

Updates an existing truck.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_update_dto import TruckUpdateDto
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_update_dto = openapi_client.TruckUpdateDto() # TruckUpdateDto |  (optional)

    try:
        # Update a truck
        api_response = api_instance.update_truck_async(tenant_id, truck_id, api_version=api_version, x_api_version=x_api_version, truck_update_dto=truck_update_dto)
        print("The response of TrucksApi->update_truck_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->update_truck_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_update_dto** | [**TruckUpdateDto**](TruckUpdateDto.md)|  | [optional] 

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

# **update_truck_trip_async**
> EmptyEnvelope update_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version, truck_trip_update_dto=truck_trip_update_dto)

Update a truck trip

Updates an existing truck trip.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.truck_trip_update_dto import TruckTripUpdateDto
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
    api_instance = openapi_client.TrucksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    truck_id = 'truck_id_example' # str | 
    trip_id = 'trip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    truck_trip_update_dto = openapi_client.TruckTripUpdateDto() # TruckTripUpdateDto |  (optional)

    try:
        # Update a truck trip
        api_response = api_instance.update_truck_trip_async(tenant_id, truck_id, trip_id, api_version=api_version, x_api_version=x_api_version, truck_trip_update_dto=truck_trip_update_dto)
        print("The response of TrucksApi->update_truck_trip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrucksApi->update_truck_trip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **truck_id** | **str**|  | 
 **trip_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **truck_trip_update_dto** | [**TruckTripUpdateDto**](TruckTripUpdateDto.md)|  | [optional] 

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

