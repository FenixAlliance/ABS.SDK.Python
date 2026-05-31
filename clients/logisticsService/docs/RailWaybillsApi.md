# openapi_client.RailWaybillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rail_waybill_line_async**](RailWaybillsApi.md#add_rail_waybill_line_async) | **POST** /api/v2/LogisticsService/RailWaybills/{waybillId}/Lines | Add a line to rail waybill
[**cancel_rail_waybill_async**](RailWaybillsApi.md#cancel_rail_waybill_async) | **POST** /api/v2/LogisticsService/RailWaybills/{waybillId}/Cancel | Cancel a rail waybill
[**create_rail_waybill_async**](RailWaybillsApi.md#create_rail_waybill_async) | **POST** /api/v2/LogisticsService/RailWaybills | Create a rail waybill
[**delete_rail_waybill_async**](RailWaybillsApi.md#delete_rail_waybill_async) | **DELETE** /api/v2/LogisticsService/RailWaybills/{waybillId} | Delete a rail waybill
[**get_rail_waybill_by_id_async**](RailWaybillsApi.md#get_rail_waybill_by_id_async) | **GET** /api/v2/LogisticsService/RailWaybills/{waybillId} | Get rail waybill by ID
[**get_rail_waybill_lines_async**](RailWaybillsApi.md#get_rail_waybill_lines_async) | **GET** /api/v2/LogisticsService/RailWaybills/{waybillId}/Lines | Get rail waybill lines
[**get_rail_waybill_lines_count_async**](RailWaybillsApi.md#get_rail_waybill_lines_count_async) | **GET** /api/v2/LogisticsService/RailWaybills/{waybillId}/Lines/Count | Get rail waybill lines count
[**get_rail_waybills_async**](RailWaybillsApi.md#get_rail_waybills_async) | **GET** /api/v2/LogisticsService/RailWaybills | Get all rail waybills
[**get_rail_waybills_count_async**](RailWaybillsApi.md#get_rail_waybills_count_async) | **GET** /api/v2/LogisticsService/RailWaybills/Count | Get rail waybills count
[**issue_rail_waybill_async**](RailWaybillsApi.md#issue_rail_waybill_async) | **POST** /api/v2/LogisticsService/RailWaybills/{waybillId}/Issue | Issue a rail waybill
[**mark_rail_waybill_delivered_async**](RailWaybillsApi.md#mark_rail_waybill_delivered_async) | **POST** /api/v2/LogisticsService/RailWaybills/{waybillId}/MarkDelivered | Mark rail waybill delivered
[**mark_rail_waybill_in_transit_async**](RailWaybillsApi.md#mark_rail_waybill_in_transit_async) | **POST** /api/v2/LogisticsService/RailWaybills/{waybillId}/MarkInTransit | Mark rail waybill in transit
[**remove_rail_waybill_line_async**](RailWaybillsApi.md#remove_rail_waybill_line_async) | **DELETE** /api/v2/LogisticsService/RailWaybills/{waybillId}/Lines/{lineId} | Remove a rail waybill line
[**update_rail_waybill_async**](RailWaybillsApi.md#update_rail_waybill_async) | **PUT** /api/v2/LogisticsService/RailWaybills/{waybillId} | Update a rail waybill
[**update_rail_waybill_line_async**](RailWaybillsApi.md#update_rail_waybill_line_async) | **PUT** /api/v2/LogisticsService/RailWaybills/{waybillId}/Lines/{lineId} | Update a rail waybill line


# **add_rail_waybill_line_async**
> EmptyEnvelope add_rail_waybill_line_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)

Add a line to rail waybill

Adds a new line to a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_create_dto = openapi_client.WaybillLineCreateDto() # WaybillLineCreateDto |  (optional)

    try:
        # Add a line to rail waybill
        api_response = api_instance.add_rail_waybill_line_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)
        print("The response of RailWaybillsApi->add_rail_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->add_rail_waybill_line_async: %s\n" % e)
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

# **cancel_rail_waybill_async**
> EmptyEnvelope cancel_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Cancel a rail waybill

Cancels a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel a rail waybill
        api_response = api_instance.cancel_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->cancel_rail_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->cancel_rail_waybill_async: %s\n" % e)
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

# **create_rail_waybill_async**
> EmptyEnvelope create_rail_waybill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, rail_waybill_create_dto=rail_waybill_create_dto)

Create a rail waybill

Creates a new rail waybill for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.rail_waybill_create_dto import RailWaybillCreateDto
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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    rail_waybill_create_dto = openapi_client.RailWaybillCreateDto() # RailWaybillCreateDto |  (optional)

    try:
        # Create a rail waybill
        api_response = api_instance.create_rail_waybill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, rail_waybill_create_dto=rail_waybill_create_dto)
        print("The response of RailWaybillsApi->create_rail_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->create_rail_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **rail_waybill_create_dto** | [**RailWaybillCreateDto**](RailWaybillCreateDto.md)|  | [optional] 

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

# **delete_rail_waybill_async**
> EmptyEnvelope delete_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Delete a rail waybill

Deletes a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a rail waybill
        api_response = api_instance.delete_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->delete_rail_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->delete_rail_waybill_async: %s\n" % e)
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

# **get_rail_waybill_by_id_async**
> RailWaybillDtoEnvelope get_rail_waybill_by_id_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get rail waybill by ID

Retrieves a specific rail waybill by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.rail_waybill_dto_envelope import RailWaybillDtoEnvelope
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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get rail waybill by ID
        api_response = api_instance.get_rail_waybill_by_id_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->get_rail_waybill_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->get_rail_waybill_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RailWaybillDtoEnvelope**](RailWaybillDtoEnvelope.md)

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

# **get_rail_waybill_lines_async**
> WaybillLineDtoListEnvelope get_rail_waybill_lines_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get rail waybill lines

Retrieves all lines for a specific rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get rail waybill lines
        api_response = api_instance.get_rail_waybill_lines_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->get_rail_waybill_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->get_rail_waybill_lines_async: %s\n" % e)
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

# **get_rail_waybill_lines_count_async**
> Int32Envelope get_rail_waybill_lines_count_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Get rail waybill lines count

Returns the count of lines for a specific rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get rail waybill lines count
        api_response = api_instance.get_rail_waybill_lines_count_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->get_rail_waybill_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->get_rail_waybill_lines_count_async: %s\n" % e)
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

# **get_rail_waybills_async**
> RailWaybillDtoListEnvelope get_rail_waybills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all rail waybills

Retrieves all rail waybills for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.rail_waybill_dto_list_envelope import RailWaybillDtoListEnvelope
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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all rail waybills
        api_response = api_instance.get_rail_waybills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->get_rail_waybills_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->get_rail_waybills_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RailWaybillDtoListEnvelope**](RailWaybillDtoListEnvelope.md)

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

# **get_rail_waybills_count_async**
> Int32Envelope get_rail_waybills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get rail waybills count

Returns the count of rail waybills for the specified tenant.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get rail waybills count
        api_response = api_instance.get_rail_waybills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->get_rail_waybills_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->get_rail_waybills_count_async: %s\n" % e)
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

# **issue_rail_waybill_async**
> EmptyEnvelope issue_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Issue a rail waybill

Issues a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Issue a rail waybill
        api_response = api_instance.issue_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->issue_rail_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->issue_rail_waybill_async: %s\n" % e)
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

# **mark_rail_waybill_delivered_async**
> EmptyEnvelope mark_rail_waybill_delivered_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Mark rail waybill delivered

Marks a rail waybill as delivered.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark rail waybill delivered
        api_response = api_instance.mark_rail_waybill_delivered_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->mark_rail_waybill_delivered_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->mark_rail_waybill_delivered_async: %s\n" % e)
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

# **mark_rail_waybill_in_transit_async**
> EmptyEnvelope mark_rail_waybill_in_transit_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)

Mark rail waybill in transit

Marks a rail waybill as in transit.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark rail waybill in transit
        api_response = api_instance.mark_rail_waybill_in_transit_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->mark_rail_waybill_in_transit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->mark_rail_waybill_in_transit_async: %s\n" % e)
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

# **remove_rail_waybill_line_async**
> EmptyEnvelope remove_rail_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove a rail waybill line

Removes a line from a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a rail waybill line
        api_response = api_instance.remove_rail_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RailWaybillsApi->remove_rail_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->remove_rail_waybill_line_async: %s\n" % e)
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

# **update_rail_waybill_async**
> EmptyEnvelope update_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, rail_waybill_update_dto=rail_waybill_update_dto)

Update a rail waybill

Updates an existing rail waybill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.rail_waybill_update_dto import RailWaybillUpdateDto
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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    rail_waybill_update_dto = openapi_client.RailWaybillUpdateDto() # RailWaybillUpdateDto |  (optional)

    try:
        # Update a rail waybill
        api_response = api_instance.update_rail_waybill_async(tenant_id, waybill_id, api_version=api_version, x_api_version=x_api_version, rail_waybill_update_dto=rail_waybill_update_dto)
        print("The response of RailWaybillsApi->update_rail_waybill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->update_rail_waybill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **waybill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **rail_waybill_update_dto** | [**RailWaybillUpdateDto**](RailWaybillUpdateDto.md)|  | [optional] 

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

# **update_rail_waybill_line_async**
> EmptyEnvelope update_rail_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)

Update a rail waybill line

Updates an existing line on a rail waybill.

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
    api_instance = openapi_client.RailWaybillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    waybill_id = 'waybill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_update_dto = openapi_client.WaybillLineUpdateDto() # WaybillLineUpdateDto |  (optional)

    try:
        # Update a rail waybill line
        api_response = api_instance.update_rail_waybill_line_async(tenant_id, waybill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)
        print("The response of RailWaybillsApi->update_rail_waybill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RailWaybillsApi->update_rail_waybill_line_async: %s\n" % e)
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

