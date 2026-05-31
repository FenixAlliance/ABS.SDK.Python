# openapi_client.LeaveTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_leave_type_async**](LeaveTypesApi.md#create_leave_type_async) | **POST** /api/v2/HrmsService/LeaveTypes | Create a leave type
[**delete_leave_type_async**](LeaveTypesApi.md#delete_leave_type_async) | **DELETE** /api/v2/HrmsService/LeaveTypes/{leaveTypeId} | Delete a leave type
[**get_leave_type_by_id_async**](LeaveTypesApi.md#get_leave_type_by_id_async) | **GET** /api/v2/HrmsService/LeaveTypes/{leaveTypeId} | Get leave type by ID
[**get_leave_types_async**](LeaveTypesApi.md#get_leave_types_async) | **GET** /api/v2/HrmsService/LeaveTypes | Get leave types
[**get_leave_types_count_async**](LeaveTypesApi.md#get_leave_types_count_async) | **GET** /api/v2/HrmsService/LeaveTypes/Count | Count leave types
[**update_leave_type_async**](LeaveTypesApi.md#update_leave_type_async) | **PUT** /api/v2/HrmsService/LeaveTypes/{leaveTypeId} | Update a leave type


# **create_leave_type_async**
> EmptyEnvelope create_leave_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, leave_type_create_dto=leave_type_create_dto)

Create a leave type

Creates a new leave type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.leave_type_create_dto import LeaveTypeCreateDto
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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    leave_type_create_dto = openapi_client.LeaveTypeCreateDto() # LeaveTypeCreateDto |  (optional)

    try:
        # Create a leave type
        api_response = api_instance.create_leave_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, leave_type_create_dto=leave_type_create_dto)
        print("The response of LeaveTypesApi->create_leave_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->create_leave_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **leave_type_create_dto** | [**LeaveTypeCreateDto**](LeaveTypeCreateDto.md)|  | [optional] 

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

# **delete_leave_type_async**
> EmptyEnvelope delete_leave_type_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a leave type

Deletes a leave type for the specified tenant.

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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_type_id = 'leave_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a leave type
        api_response = api_instance.delete_leave_type_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveTypesApi->delete_leave_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->delete_leave_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_type_id** | **str**|  | 
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

# **get_leave_type_by_id_async**
> LeaveTypeDtoEnvelope get_leave_type_by_id_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version)

Get leave type by ID

Retrieves a specific leave type by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.leave_type_dto_envelope import LeaveTypeDtoEnvelope
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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_type_id = 'leave_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get leave type by ID
        api_response = api_instance.get_leave_type_by_id_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveTypesApi->get_leave_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->get_leave_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LeaveTypeDtoEnvelope**](LeaveTypeDtoEnvelope.md)

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

# **get_leave_types_async**
> LeaveTypeDtoListEnvelope get_leave_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get leave types

Retrieves leave types for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.leave_type_dto_list_envelope import LeaveTypeDtoListEnvelope
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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get leave types
        api_response = api_instance.get_leave_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveTypesApi->get_leave_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->get_leave_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LeaveTypeDtoListEnvelope**](LeaveTypeDtoListEnvelope.md)

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

# **get_leave_types_count_async**
> Int32Envelope get_leave_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count leave types

Counts leave types for the specified tenant.

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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count leave types
        api_response = api_instance.get_leave_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveTypesApi->get_leave_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->get_leave_types_count_async: %s\n" % e)
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

# **update_leave_type_async**
> EmptyEnvelope update_leave_type_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version, leave_type_update_dto=leave_type_update_dto)

Update a leave type

Updates an existing leave type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.leave_type_update_dto import LeaveTypeUpdateDto
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
    api_instance = openapi_client.LeaveTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_type_id = 'leave_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    leave_type_update_dto = openapi_client.LeaveTypeUpdateDto() # LeaveTypeUpdateDto |  (optional)

    try:
        # Update a leave type
        api_response = api_instance.update_leave_type_async(tenant_id, leave_type_id, api_version=api_version, x_api_version=x_api_version, leave_type_update_dto=leave_type_update_dto)
        print("The response of LeaveTypesApi->update_leave_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveTypesApi->update_leave_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **leave_type_update_dto** | [**LeaveTypeUpdateDto**](LeaveTypeUpdateDto.md)|  | [optional] 

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

