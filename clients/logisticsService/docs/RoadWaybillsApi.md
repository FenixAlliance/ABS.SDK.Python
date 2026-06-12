# openapi_client.RoadWaybillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_road_waybill_line_async**](RoadWaybillsApi.md#add_road_waybill_line_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines | Add a line to road waybill
[**cancel_road_waybill_async**](RoadWaybillsApi.md#cancel_road_waybill_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Cancel | Cancel a road waybill
[**create_road_waybill_async**](RoadWaybillsApi.md#create_road_waybill_async) | **POST** /api/v2/LogisticsService/RoadWaybills | Create a road waybill
[**delete_road_waybill_async**](RoadWaybillsApi.md#delete_road_waybill_async) | **DELETE** /api/v2/LogisticsService/RoadWaybills/{waybillId} | Delete a road waybill
[**dispute_road_waybill_async**](RoadWaybillsApi.md#dispute_road_waybill_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Dispute | Dispute a road waybill
[**get_road_waybill_by_id_async**](RoadWaybillsApi.md#get_road_waybill_by_id_async) | **GET** /api/v2/LogisticsService/RoadWaybills/{waybillId} | Get road waybill by ID
[**get_road_waybill_lines_async**](RoadWaybillsApi.md#get_road_waybill_lines_async) | **GET** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines | Get road waybill lines
[**get_road_waybill_lines_count_async**](RoadWaybillsApi.md#get_road_waybill_lines_count_async) | **GET** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines/Count | Get road waybill lines count
[**get_road_waybills_async**](RoadWaybillsApi.md#get_road_waybills_async) | **GET** /api/v2/LogisticsService/RoadWaybills | Get all road waybills
[**get_road_waybills_count_async**](RoadWaybillsApi.md#get_road_waybills_count_async) | **GET** /api/v2/LogisticsService/RoadWaybills/Count | Get road waybills count
[**issue_road_waybill_async**](RoadWaybillsApi.md#issue_road_waybill_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Issue | Issue a road waybill
[**mark_road_waybill_delivered_async**](RoadWaybillsApi.md#mark_road_waybill_delivered_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/MarkDelivered | Mark road waybill delivered
[**mark_road_waybill_in_transit_async**](RoadWaybillsApi.md#mark_road_waybill_in_transit_async) | **POST** /api/v2/LogisticsService/RoadWaybills/{waybillId}/MarkInTransit | Mark road waybill in transit
[**patch_road_waybill_async**](RoadWaybillsApi.md#patch_road_waybill_async) | **PATCH** /api/v2/LogisticsService/RoadWaybills/{waybillId} | Patch a road waybill
[**patch_road_waybill_line_async**](RoadWaybillsApi.md#patch_road_waybill_line_async) | **PATCH** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines/{lineId} | Patch a road waybill line
[**remove_road_waybill_line_async**](RoadWaybillsApi.md#remove_road_waybill_line_async) | **DELETE** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines/{lineId} | Remove a road waybill line
[**update_road_waybill_async**](RoadWaybillsApi.md#update_road_waybill_async) | **PUT** /api/v2/LogisticsService/RoadWaybills/{waybillId} | Update a road waybill
[**update_road_waybill_line_async**](RoadWaybillsApi.md#update_road_waybill_line_async) | **PUT** /api/v2/LogisticsService/RoadWaybills/{waybillId}/Lines/{lineId} | Update a road waybill line


# **add_road_waybill_line_async**
> EmptyEnvelope add_road_waybill_line_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)

Add a line to road waybill

Adds a new line to a road waybill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_create_dto import WaybillLineCreateDto
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_create_dto = openapi_client.WaybillLineCreateDto() # WaybillLineCreateDto |  (optional)

    try:
        # Add a line to road waybill
        api_response = api_instance.add_road_waybill_line_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)
        print("The response of RoadWaybillsApi->add_road_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->add_road_waybill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_create_dto** | [**WaybillLineCreateDto**](WaybillLineCreateDto.md)|  | [optional] 

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

# **cancel_road_waybill_async**
> EmptyEnvelope cancel_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Cancel a road waybill

Cancels a road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel a road waybill
        api_response = api_instance.cancel_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->cancel_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->cancel_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **create_road_waybill_async**
> EmptyEnvelope create_road_waybill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, road_waybill_create_dto=road_waybill_create_dto)

Create a road waybill

Creates a new road waybill for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.road_waybill_create_dto import RoadWaybillCreateDto
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    road_waybill_create_dto = openapi_client.RoadWaybillCreateDto() # RoadWaybillCreateDto |  (optional)

    try:
        # Create a road waybill
        api_response = api_instance.create_road_waybill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, road_waybill_create_dto=road_waybill_create_dto)
        print("The response of RoadWaybillsApi->create_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->create_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **road_waybill_create_dto** | [**RoadWaybillCreateDto**](RoadWaybillCreateDto.md)|  | [optional] 

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

# **delete_road_waybill_async**
> EmptyEnvelope delete_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Delete a road waybill

Deletes a road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a road waybill
        api_response = api_instance.delete_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->delete_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->delete_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **dispute_road_waybill_async**
> EmptyEnvelope dispute_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Dispute a road waybill

Disputes a road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Dispute a road waybill
        api_response = api_instance.dispute_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->dispute_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->dispute_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **get_road_waybill_by_id_async**
> RoadWaybillDtoEnvelope get_road_waybill_by_id_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get road waybill by ID

Retrieves a specific road waybill by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.road_waybill_dto_envelope import RoadWaybillDtoEnvelope
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get road waybill by ID
        api_response = api_instance.get_road_waybill_by_id_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->get_road_waybill_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->get_road_waybill_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RoadWaybillDtoEnvelope**](RoadWaybillDtoEnvelope.md)

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

# **get_road_waybill_lines_async**
> WaybillLineDtoListEnvelope get_road_waybill_lines_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get road waybill lines

Retrieves all lines for a specific road waybill.

### Example


```python
import openapi_client
from openapi_client.models.waybill_line_dto_list_envelope import WaybillLineDtoListEnvelope
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get road waybill lines
        api_response = api_instance.get_road_waybill_lines_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->get_road_waybill_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->get_road_waybill_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WaybillLineDtoListEnvelope**](WaybillLineDtoListEnvelope.md)

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

# **get_road_waybill_lines_count_async**
> Int32Envelope get_road_waybill_lines_count_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get road waybill lines count

Returns the count of lines for a specific road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get road waybill lines count
        api_response = api_instance.get_road_waybill_lines_count_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->get_road_waybill_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->get_road_waybill_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **get_road_waybills_async**
> RoadWaybillDtoListEnvelope get_road_waybills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all road waybills

Retrieves all road waybills for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.road_waybill_dto_list_envelope import RoadWaybillDtoListEnvelope
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all road waybills
        api_response = api_instance.get_road_waybills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->get_road_waybills_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->get_road_waybills_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RoadWaybillDtoListEnvelope**](RoadWaybillDtoListEnvelope.md)

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

# **get_road_waybills_count_async**
> Int32Envelope get_road_waybills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get road waybills count

Returns the count of road waybills for the specified tenant.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get road waybills count
        api_response = api_instance.get_road_waybills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->get_road_waybills_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->get_road_waybills_count_async: %s\n" % e)
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

# **issue_road_waybill_async**
> EmptyEnvelope issue_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Issue a road waybill

Issues a road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Issue a road waybill
        api_response = api_instance.issue_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->issue_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->issue_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **mark_road_waybill_delivered_async**
> EmptyEnvelope mark_road_waybill_delivered_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Mark road waybill delivered

Marks a road waybill as delivered.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark road waybill delivered
        api_response = api_instance.mark_road_waybill_delivered_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->mark_road_waybill_delivered_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->mark_road_waybill_delivered_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **mark_road_waybill_in_transit_async**
> EmptyEnvelope mark_road_waybill_in_transit_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Mark road waybill in transit

Marks a road waybill as in transit.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark road waybill in transit
        api_response = api_instance.mark_road_waybill_in_transit_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->mark_road_waybill_in_transit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->mark_road_waybill_in_transit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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

# **patch_road_waybill_async**
> EmptyEnvelope patch_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a road waybill

Partially updates an existing road waybill using a JSON Patch document.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a road waybill
        api_response = api_instance.patch_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of RoadWaybillsApi->patch_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->patch_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_road_waybill_line_async**
> EmptyEnvelope patch_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a road waybill line

Partially updates a line on a road waybill using a JSON Patch document.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a road waybill line
        api_response = api_instance.patch_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of RoadWaybillsApi->patch_road_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->patch_road_waybill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **line_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_road_waybill_line_async**
> EmptyEnvelope remove_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove a road waybill line

Removes a line from a road waybill.

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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a road waybill line
        api_response = api_instance.remove_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoadWaybillsApi->remove_road_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->remove_road_waybill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **update_road_waybill_async**
> EmptyEnvelope update_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, road_waybill_update_dto=road_waybill_update_dto)

Update a road waybill

Updates an existing road waybill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.road_waybill_update_dto import RoadWaybillUpdateDto
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    road_waybill_update_dto = openapi_client.RoadWaybillUpdateDto() # RoadWaybillUpdateDto |  (optional)

    try:
        # Update a road waybill
        api_response = api_instance.update_road_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, road_waybill_update_dto=road_waybill_update_dto)
        print("The response of RoadWaybillsApi->update_road_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->update_road_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **road_waybill_update_dto** | [**RoadWaybillUpdateDto**](RoadWaybillUpdateDto.md)|  | [optional] 

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

# **update_road_waybill_line_async**
> EmptyEnvelope update_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)

Update a road waybill line

Updates an existing line on a road waybill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_update_dto import WaybillLineUpdateDto
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
    api_instance = openapi_client.RoadWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_update_dto = openapi_client.WaybillLineUpdateDto() # WaybillLineUpdateDto |  (optional)

    try:
        # Update a road waybill line
        api_response = api_instance.update_road_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)
        print("The response of RoadWaybillsApi->update_road_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadWaybillsApi->update_road_waybill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_update_dto** | [**WaybillLineUpdateDto**](WaybillLineUpdateDto.md)|  | [optional] 

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

