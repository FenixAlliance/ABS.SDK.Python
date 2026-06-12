# openapi_client.LeaveApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_leave_application_async**](LeaveApplicationsApi.md#create_leave_application_async) | **POST** /api/v2/HrmsService/LeaveApplications | Create a leave application
[**delete_leave_application_async**](LeaveApplicationsApi.md#delete_leave_application_async) | **DELETE** /api/v2/HrmsService/LeaveApplications/{leaveApplicationId} | Delete a leave application
[**get_leave_application_by_id_async**](LeaveApplicationsApi.md#get_leave_application_by_id_async) | **GET** /api/v2/HrmsService/LeaveApplications/{leaveApplicationId} | Get leave application by ID
[**get_leave_applications_async**](LeaveApplicationsApi.md#get_leave_applications_async) | **GET** /api/v2/HrmsService/LeaveApplications | Get leave applications
[**get_leave_applications_count_async**](LeaveApplicationsApi.md#get_leave_applications_count_async) | **GET** /api/v2/HrmsService/LeaveApplications/Count | Count leave applications
[**patch_leave_application_async**](LeaveApplicationsApi.md#patch_leave_application_async) | **PATCH** /api/v2/HrmsService/LeaveApplications/{leaveApplicationId} | Patch a leave application
[**update_leave_application_async**](LeaveApplicationsApi.md#update_leave_application_async) | **PUT** /api/v2/HrmsService/LeaveApplications/{leaveApplicationId} | Update a leave application


# **create_leave_application_async**
> EmptyEnvelope create_leave_application_async(tenant_id, api_version=api_version, x_api_version=x_api_version, leave_application_create_dto=leave_application_create_dto)

Create a leave application

Creates a new leave application for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.leave_application_create_dto import LeaveApplicationCreateDto
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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    leave_application_create_dto = openapi_client.LeaveApplicationCreateDto() # LeaveApplicationCreateDto |  (optional)

    try:
        # Create a leave application
        api_response = api_instance.create_leave_application_async(tenant_id, api_version=api_version, x_api_version=x_api_version, leave_application_create_dto=leave_application_create_dto)
        print("The response of LeaveApplicationsApi->create_leave_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->create_leave_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **leave_application_create_dto** | [**LeaveApplicationCreateDto**](LeaveApplicationCreateDto.md)|  | [optional] 

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

# **delete_leave_application_async**
> EmptyEnvelope delete_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version)

Delete a leave application

Deletes a leave application for the specified tenant.

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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_application_id = 'leave_application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a leave application
        api_response = api_instance.delete_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveApplicationsApi->delete_leave_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->delete_leave_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_application_id** | **str**|  | 
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

# **get_leave_application_by_id_async**
> LeaveApplicationDtoEnvelope get_leave_application_by_id_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version)

Get leave application by ID

Retrieves a specific leave application by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.leave_application_dto_envelope import LeaveApplicationDtoEnvelope
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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_application_id = 'leave_application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get leave application by ID
        api_response = api_instance.get_leave_application_by_id_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveApplicationsApi->get_leave_application_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->get_leave_application_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LeaveApplicationDtoEnvelope**](LeaveApplicationDtoEnvelope.md)

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

# **get_leave_applications_async**
> LeaveApplicationDtoListEnvelope get_leave_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get leave applications

Retrieves leave applications for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.leave_application_dto_list_envelope import LeaveApplicationDtoListEnvelope
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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get leave applications
        api_response = api_instance.get_leave_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveApplicationsApi->get_leave_applications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->get_leave_applications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LeaveApplicationDtoListEnvelope**](LeaveApplicationDtoListEnvelope.md)

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

# **get_leave_applications_count_async**
> Int32Envelope get_leave_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count leave applications

Counts leave applications for the specified tenant.

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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count leave applications
        api_response = api_instance.get_leave_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LeaveApplicationsApi->get_leave_applications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->get_leave_applications_count_async: %s\n" % e)
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

# **patch_leave_application_async**
> EmptyEnvelope patch_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a leave application

Partially updates an existing leave application for the specified tenant.

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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_application_id = 'leave_application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a leave application
        api_response = api_instance.patch_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of LeaveApplicationsApi->patch_leave_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->patch_leave_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_application_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leave_application_async**
> EmptyEnvelope update_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version, leave_application_update_dto=leave_application_update_dto)

Update a leave application

Updates an existing leave application for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.leave_application_update_dto import LeaveApplicationUpdateDto
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
    api_instance = openapi_client.LeaveApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    leave_application_id = 'leave_application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    leave_application_update_dto = openapi_client.LeaveApplicationUpdateDto() # LeaveApplicationUpdateDto |  (optional)

    try:
        # Update a leave application
        api_response = api_instance.update_leave_application_async(tenant_id, leave_application_id, api_version=api_version, x_api_version=x_api_version, leave_application_update_dto=leave_application_update_dto)
        print("The response of LeaveApplicationsApi->update_leave_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaveApplicationsApi->update_leave_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **leave_application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **leave_application_update_dto** | [**LeaveApplicationUpdateDto**](LeaveApplicationUpdateDto.md)|  | [optional] 

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

