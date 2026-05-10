# openapi_client.ShippingRegionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_region_async**](ShippingRegionsApi.md#create_shipping_region_async) | **POST** /api/v2/ShipmentsService/ShippingRegions | Create a shipping region
[**delete_shipping_region_async**](ShippingRegionsApi.md#delete_shipping_region_async) | **DELETE** /api/v2/ShipmentsService/ShippingRegions/{regionId} | Delete a shipping region
[**get_shipping_region_by_id_async**](ShippingRegionsApi.md#get_shipping_region_by_id_async) | **GET** /api/v2/ShipmentsService/ShippingRegions/{regionId} | Get shipping region by ID
[**get_shipping_regions_async**](ShippingRegionsApi.md#get_shipping_regions_async) | **GET** /api/v2/ShipmentsService/ShippingRegions | Get all shipping regions
[**get_shipping_regions_count_async**](ShippingRegionsApi.md#get_shipping_regions_count_async) | **GET** /api/v2/ShipmentsService/ShippingRegions/Count | Get shipping regions count
[**update_shipping_region_async**](ShippingRegionsApi.md#update_shipping_region_async) | **PUT** /api/v2/ShipmentsService/ShippingRegions/{regionId} | Update a shipping region


# **create_shipping_region_async**
> create_shipping_region_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_region_create_dto=shipping_region_create_dto)

Create a shipping region

Creates a new shipping region.

### Example


```python
import openapi_client
from openapi_client.models.shipping_region_create_dto import ShippingRegionCreateDto
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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_region_create_dto = openapi_client.ShippingRegionCreateDto() # ShippingRegionCreateDto |  (optional)

    try:
        # Create a shipping region
        api_instance.create_shipping_region_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shipping_region_create_dto=shipping_region_create_dto)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->create_shipping_region_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_region_create_dto** | [**ShippingRegionCreateDto**](ShippingRegionCreateDto.md)|  | [optional] 

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

# **delete_shipping_region_async**
> delete_shipping_region_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version)

Delete a shipping region

Deletes a shipping region.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    region_id = 'region_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shipping region
        api_instance.delete_shipping_region_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->delete_shipping_region_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **region_id** | **str**|  | 
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

# **get_shipping_region_by_id_async**
> ShippingRegionDtoEnvelope get_shipping_region_by_id_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version)

Get shipping region by ID

Retrieves a specific shipping region.

### Example


```python
import openapi_client
from openapi_client.models.shipping_region_dto_envelope import ShippingRegionDtoEnvelope
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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    region_id = 'region_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping region by ID
        api_response = api_instance.get_shipping_region_by_id_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingRegionsApi->get_shipping_region_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->get_shipping_region_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **region_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingRegionDtoEnvelope**](ShippingRegionDtoEnvelope.md)

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

# **get_shipping_regions_async**
> ShippingRegionDtoListEnvelope get_shipping_regions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all shipping regions

Retrieves all shipping regions for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipping_region_dto_list_envelope import ShippingRegionDtoListEnvelope
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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all shipping regions
        api_response = api_instance.get_shipping_regions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingRegionsApi->get_shipping_regions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->get_shipping_regions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShippingRegionDtoListEnvelope**](ShippingRegionDtoListEnvelope.md)

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

# **get_shipping_regions_count_async**
> Int32Envelope get_shipping_regions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shipping regions count

Returns the count of shipping regions.

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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping regions count
        api_response = api_instance.get_shipping_regions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShippingRegionsApi->get_shipping_regions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->get_shipping_regions_count_async: %s\n" % e)
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

# **update_shipping_region_async**
> update_shipping_region_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version, shipping_region_update_dto=shipping_region_update_dto)

Update a shipping region

Updates an existing shipping region.

### Example


```python
import openapi_client
from openapi_client.models.shipping_region_update_dto import ShippingRegionUpdateDto
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
    api_instance = openapi_client.ShippingRegionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    region_id = 'region_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shipping_region_update_dto = openapi_client.ShippingRegionUpdateDto() # ShippingRegionUpdateDto |  (optional)

    try:
        # Update a shipping region
        api_instance.update_shipping_region_async(tenant_id, region_id, api_version=api_version, x_api_version=x_api_version, shipping_region_update_dto=shipping_region_update_dto)
    except Exception as e:
        print("Exception when calling ShippingRegionsApi->update_shipping_region_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **region_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shipping_region_update_dto** | [**ShippingRegionUpdateDto**](ShippingRegionUpdateDto.md)|  | [optional] 

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

