# openapi_client.ShiftsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shift_async**](ShiftsApi.md#create_shift_async) | **POST** /api/v2/HrmsService/Shifts | Create a shift
[**delete_shift_async**](ShiftsApi.md#delete_shift_async) | **DELETE** /api/v2/HrmsService/Shifts/{shiftId} | Delete a shift
[**get_shift_by_id_async**](ShiftsApi.md#get_shift_by_id_async) | **GET** /api/v2/HrmsService/Shifts/{shiftId} | Get shift by ID
[**get_shifts_async**](ShiftsApi.md#get_shifts_async) | **GET** /api/v2/HrmsService/Shifts | Get shifts
[**get_shifts_count_async**](ShiftsApi.md#get_shifts_count_async) | **GET** /api/v2/HrmsService/Shifts/Count | Count shifts
[**update_shift_async**](ShiftsApi.md#update_shift_async) | **PUT** /api/v2/HrmsService/Shifts/{shiftId} | Update a shift


# **create_shift_async**
> EmptyEnvelope create_shift_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shift_create_dto=shift_create_dto)

Create a shift

Creates a new shift for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.shift_create_dto import ShiftCreateDto
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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shift_create_dto = openapi_client.ShiftCreateDto() # ShiftCreateDto |  (optional)

    try:
        # Create a shift
        api_response = api_instance.create_shift_async(tenant_id, api_version=api_version, x_api_version=x_api_version, shift_create_dto=shift_create_dto)
        print("The response of ShiftsApi->create_shift_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->create_shift_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shift_create_dto** | [**ShiftCreateDto**](ShiftCreateDto.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shift_async**
> EmptyEnvelope delete_shift_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version)

Delete a shift

Deletes a shift for the specified tenant.

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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shift_id = 'shift_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a shift
        api_response = api_instance.delete_shift_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShiftsApi->delete_shift_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->delete_shift_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shift_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shift_by_id_async**
> ShiftDtoEnvelope get_shift_by_id_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version)

Get shift by ID

Retrieves a specific shift by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.shift_dto_envelope import ShiftDtoEnvelope
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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shift_id = 'shift_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shift by ID
        api_response = api_instance.get_shift_by_id_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShiftsApi->get_shift_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->get_shift_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shift_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShiftDtoEnvelope**](ShiftDtoEnvelope.md)

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

# **get_shifts_async**
> ShiftDtoListEnvelope get_shifts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get shifts

Retrieves shifts for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shift_dto_list_envelope import ShiftDtoListEnvelope
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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shifts
        api_response = api_instance.get_shifts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShiftsApi->get_shifts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->get_shifts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShiftDtoListEnvelope**](ShiftDtoListEnvelope.md)

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

# **get_shifts_count_async**
> Int32Envelope get_shifts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count shifts

Counts shifts for the specified tenant.

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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count shifts
        api_response = api_instance.get_shifts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShiftsApi->get_shifts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->get_shifts_count_async: %s\n" % e)
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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shift_async**
> EmptyEnvelope update_shift_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version, shift_update_dto=shift_update_dto)

Update a shift

Updates an existing shift for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.shift_update_dto import ShiftUpdateDto
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
    api_instance = openapi_client.ShiftsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    shift_id = 'shift_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    shift_update_dto = openapi_client.ShiftUpdateDto() # ShiftUpdateDto |  (optional)

    try:
        # Update a shift
        api_response = api_instance.update_shift_async(tenant_id, shift_id, api_version=api_version, x_api_version=x_api_version, shift_update_dto=shift_update_dto)
        print("The response of ShiftsApi->update_shift_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftsApi->update_shift_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **shift_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **shift_update_dto** | [**ShiftUpdateDto**](ShiftUpdateDto.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

