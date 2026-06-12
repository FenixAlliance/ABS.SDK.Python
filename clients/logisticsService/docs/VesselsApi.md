# openapi_client.VesselsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vessel_async**](VesselsApi.md#create_vessel_async) | **POST** /api/v2/LogisticsService/Vessels | Create a vessel
[**delete_vessel_async**](VesselsApi.md#delete_vessel_async) | **DELETE** /api/v2/LogisticsService/Vessels/{vesselId} | Delete a vessel
[**get_vessel_by_id_async**](VesselsApi.md#get_vessel_by_id_async) | **GET** /api/v2/LogisticsService/Vessels/{vesselId} | Get vessel by ID
[**get_vessels_async**](VesselsApi.md#get_vessels_async) | **GET** /api/v2/LogisticsService/Vessels | Get all vessels
[**get_vessels_count_async**](VesselsApi.md#get_vessels_count_async) | **GET** /api/v2/LogisticsService/Vessels/Count | Get vessels count
[**patch_vessel_async**](VesselsApi.md#patch_vessel_async) | **PATCH** /api/v2/LogisticsService/Vessels/{vesselId} | Patch a vessel
[**update_vessel_async**](VesselsApi.md#update_vessel_async) | **PUT** /api/v2/LogisticsService/Vessels/{vesselId} | Update a vessel


# **create_vessel_async**
> EmptyEnvelope create_vessel_async(tenant_id, api_version=api_version, x_api_version=x_api_version, vessel_create_dto=vessel_create_dto)

Create a vessel

Creates a new vessel for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.vessel_create_dto import VesselCreateDto
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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    vessel_create_dto = openapi_client.VesselCreateDto() # VesselCreateDto |  (optional)

    try:
        # Create a vessel
        api_response = api_instance.create_vessel_async(tenant_id, api_version=api_version, x_api_version=x_api_version, vessel_create_dto=vessel_create_dto)
        print("The response of VesselsApi->create_vessel_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->create_vessel_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **vessel_create_dto** | [**VesselCreateDto**](VesselCreateDto.md)|  | [optional] 

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

# **delete_vessel_async**
> EmptyEnvelope delete_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version)

Delete a vessel

Deletes a vessel.

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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vessel_id = 'vessel_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a vessel
        api_response = api_instance.delete_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VesselsApi->delete_vessel_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->delete_vessel_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **vessel_id** | **str**|  | 
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

# **get_vessel_by_id_async**
> VesselDtoEnvelope get_vessel_by_id_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version)

Get vessel by ID

Retrieves a specific vessel by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.vessel_dto_envelope import VesselDtoEnvelope
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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vessel_id = 'vessel_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get vessel by ID
        api_response = api_instance.get_vessel_by_id_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VesselsApi->get_vessel_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->get_vessel_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **vessel_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**VesselDtoEnvelope**](VesselDtoEnvelope.md)

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

# **get_vessels_async**
> VesselDtoListEnvelope get_vessels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all vessels

Retrieves all vessels for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.vessel_dto_list_envelope import VesselDtoListEnvelope
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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all vessels
        api_response = api_instance.get_vessels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VesselsApi->get_vessels_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->get_vessels_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**VesselDtoListEnvelope**](VesselDtoListEnvelope.md)

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

# **get_vessels_count_async**
> Int32Envelope get_vessels_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get vessels count

Returns the count of vessels for the specified tenant.

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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get vessels count
        api_response = api_instance.get_vessels_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VesselsApi->get_vessels_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->get_vessels_count_async: %s\n" % e)
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

# **patch_vessel_async**
> EmptyEnvelope patch_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a vessel

Partially updates an existing vessel using JSON Patch.

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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vessel_id = 'vessel_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a vessel
        api_response = api_instance.patch_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of VesselsApi->patch_vessel_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->patch_vessel_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **vessel_id** | **str**|  | 
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

# **update_vessel_async**
> EmptyEnvelope update_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version, vessel_update_dto=vessel_update_dto)

Update a vessel

Updates an existing vessel.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.vessel_update_dto import VesselUpdateDto
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
    api_instance = openapi_client.VesselsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vessel_id = 'vessel_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    vessel_update_dto = openapi_client.VesselUpdateDto() # VesselUpdateDto |  (optional)

    try:
        # Update a vessel
        api_response = api_instance.update_vessel_async(tenant_id, vessel_id, api_version=api_version, x_api_version=x_api_version, vessel_update_dto=vessel_update_dto)
        print("The response of VesselsApi->update_vessel_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VesselsApi->update_vessel_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **vessel_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **vessel_update_dto** | [**VesselUpdateDto**](VesselUpdateDto.md)|  | [optional] 

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

