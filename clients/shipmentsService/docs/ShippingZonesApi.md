# openapi_client.ShippingZonesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_zone_async**](ShippingZonesApi.md#create_shipping_zone_async) | **POST** /api/v2/ShipmentsService/ShippingZones | Create a shipping zone
[**delete_shipping_zone_async**](ShippingZonesApi.md#delete_shipping_zone_async) | **DELETE** /api/v2/ShipmentsService/ShippingZones/{zoneId} | Delete a shipping zone
[**get_shipping_zone_by_id_async**](ShippingZonesApi.md#get_shipping_zone_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingZones/{zoneId} | Get shipping zone by ID
[**get_shipping_zones_async**](ShippingZonesApi.md#get_shipping_zones_async) | **GET** /api/v2/ShipmentsService/ShippingZones | Get all shipping zones
[**get_shipping_zones_count_async**](ShippingZonesApi.md#get_shipping_zones_count_async) | **GET** /api/v2/ShipmentsService/ShippingZones/Count | Get shipping zones count
[**patch_shipping_zone_async**](ShippingZonesApi.md#patch_shipping_zone_async) | **PATCH** /api/v2/ShipmentsService/ShippingZones/{zoneId} | Patch a shipping zone
[**update_shipping_zone_async**](ShippingZonesApi.md#update_shipping_zone_async) | **PUT** /api/v2/ShipmentsService/ShippingZones/{zoneId} | Update a shipping zone


# **create_shipping_zone_async**
> create_shipping_zone_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_zone_create_dto=shipping_zone_create_dto)

Create a shipping zone

Creates a new shipping zone.

### Example


```python
import openapi_client
from openapi_client.models.shipping_zone_create_dto import ShippingZoneCreateDto
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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_zone_create_dto = openapi_client.ShippingZoneCreateDto() # ShippingZoneCreateDto |  (optional)

    try:
        # Create a shipping zone
        api_instance.create_shipping_zone_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_zone_create_dto=shipping_zone_create_dto)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->create_shipping_zone_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_zone_create_dto** | [**ShippingZoneCreateDto**](ShippingZoneCreateDto.md)|  | [optional] 

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

# **delete_shipping_zone_async**
> delete_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping zone

Deletes a shipping zone.

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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    zone_id = 'zone_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping zone
        api_instance.delete_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->delete_shipping_zone_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **zone_id** | **str**|  | 
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

# **get_shipping_zone_by_id_async**
> ShippingZoneDtoEnvelope get_shipping_zone_by_id_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version)

Get shipping zone by ID

Retrieves a specific shipping zone.

### Example


```python
import openapi_client
from openapi_client.models.shipping_zone_dto_envelope import ShippingZoneDtoEnvelope
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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    zone_id = 'zone_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping zone by ID
        api_response = api_instance.get_shipping_zone_by_id_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingZonesApi->get_shipping_zone_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->get_shipping_zone_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **zone_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingZoneDtoEnvelope**](ShippingZoneDtoEnvelope.md)

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

# **get_shipping_zones_async**
> ShippingZoneDtoListEnvelope get_shipping_zones_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping zones

Retrieves all shipping zones for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_zone_dto_list_envelope import ShippingZoneDtoListEnvelope
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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping zones
        api_response = api_instance.get_shipping_zones_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingZonesApi->get_shipping_zones_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->get_shipping_zones_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingZoneDtoListEnvelope**](ShippingZoneDtoListEnvelope.md)

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

# **get_shipping_zones_count_async**
> Int32Envelope get_shipping_zones_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping zones count

Returns the count of shipping zones.

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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping zones count
        api_response = api_instance.get_shipping_zones_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingZonesApi->get_shipping_zones_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->get_shipping_zones_count_async: %s\n" % e)
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

# **patch_shipping_zone_async**
> EmptyEnvelope patch_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a shipping zone

Partially updates an existing shipping zone using JSON Patch.

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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    zone_id = 'zone_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a shipping zone
        api_response = api_instance.patch_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ShippingZonesApi->patch_shipping_zone_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->patch_shipping_zone_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **zone_id** | **str**|  | 
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

# **update_shipping_zone_async**
> update_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version, shipping_zone_update_dto=shipping_zone_update_dto)

Update a shipping zone

Updates an existing shipping zone.

### Example


```python
import openapi_client
from openapi_client.models.shipping_zone_update_dto import ShippingZoneUpdateDto
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
    api_instance = openapi_client.ShippingZonesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    zone_id = 'zone_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_zone_update_dto = openapi_client.ShippingZoneUpdateDto() # ShippingZoneUpdateDto |  (optional)

    try:
        # Update a shipping zone
        api_instance.update_shipping_zone_async(tenant_id, zone_id, api_version=api_version, x_api_version=x_api_version, shipping_zone_update_dto=shipping_zone_update_dto)
    except Exception as e:
        print("Exception when calling ShippingZonesApi->update_shipping_zone_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **zone_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_zone_update_dto** | [**ShippingZoneUpdateDto**](ShippingZoneUpdateDto.md)|  | [optional] 

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

