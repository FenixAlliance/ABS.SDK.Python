# openapi_client.EmployeeAppraisalSessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_appraisal_session_async**](EmployeeAppraisalSessionsApi.md#create_employee_appraisal_session_async) | **POST** /api/v2/HrmsService/EmployeeAppraisalSessions | Create an employee appraisal session
[**delete_employee_appraisal_session_async**](EmployeeAppraisalSessionsApi.md#delete_employee_appraisal_session_async) | **DELETE** /api/v2/HrmsService/EmployeeAppraisalSessions/{sessionId} | Delete an employee appraisal session
[**get_employee_appraisal_session_by_id_async**](EmployeeAppraisalSessionsApi.md#get_employee_appraisal_session_by_id_async) | **GET** /api/v2/HrmsService/EmployeeAppraisalSessions/{sessionId} | Get employee appraisal session by ID
[**get_employee_appraisal_sessions_async**](EmployeeAppraisalSessionsApi.md#get_employee_appraisal_sessions_async) | **GET** /api/v2/HrmsService/EmployeeAppraisalSessions | Get employee appraisal sessions
[**get_employee_appraisal_sessions_count_async**](EmployeeAppraisalSessionsApi.md#get_employee_appraisal_sessions_count_async) | **GET** /api/v2/HrmsService/EmployeeAppraisalSessions/Count | Count employee appraisal sessions
[**patch_employee_appraisal_session_async**](EmployeeAppraisalSessionsApi.md#patch_employee_appraisal_session_async) | **PATCH** /api/v2/HrmsService/EmployeeAppraisalSessions/{sessionId} | Patch an employee appraisal session
[**update_employee_appraisal_session_async**](EmployeeAppraisalSessionsApi.md#update_employee_appraisal_session_async) | **PUT** /api/v2/HrmsService/EmployeeAppraisalSessions/{sessionId} | Update an employee appraisal session


# **create_employee_appraisal_session_async**
> EmptyEnvelope create_employee_appraisal_session_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_appraisal_session_create_dto=employee_appraisal_session_create_dto)

Create an employee appraisal session

Creates a new employee appraisal session for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_appraisal_session_create_dto import EmployeeAppraisalSessionCreateDto
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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employee_appraisal_session_create_dto = openapi_client.EmployeeAppraisalSessionCreateDto() # EmployeeAppraisalSessionCreateDto |  (optional)

    try:
        # Create an employee appraisal session
        api_response = api_instance.create_employee_appraisal_session_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_appraisal_session_create_dto=employee_appraisal_session_create_dto)
        print("The response of EmployeeAppraisalSessionsApi->create_employee_appraisal_session_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->create_employee_appraisal_session_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employee_appraisal_session_create_dto** | [**EmployeeAppraisalSessionCreateDto**](EmployeeAppraisalSessionCreateDto.md)|  | [optional] 

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

# **delete_employee_appraisal_session_async**
> EmptyEnvelope delete_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version)

Delete an employee appraisal session

Deletes an employee appraisal session for the specified tenant.

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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    session_id = 'session_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an employee appraisal session
        api_response = api_instance.delete_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeAppraisalSessionsApi->delete_employee_appraisal_session_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->delete_employee_appraisal_session_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **session_id** | **str**|  | 
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

# **get_employee_appraisal_session_by_id_async**
> EmployeeAppraisalSessionDtoEnvelope get_employee_appraisal_session_by_id_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version)

Get employee appraisal session by ID

Retrieves a specific employee appraisal session by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.employee_appraisal_session_dto_envelope import EmployeeAppraisalSessionDtoEnvelope
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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    session_id = 'session_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employee appraisal session by ID
        api_response = api_instance.get_employee_appraisal_session_by_id_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeAppraisalSessionsApi->get_employee_appraisal_session_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->get_employee_appraisal_session_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **session_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeAppraisalSessionDtoEnvelope**](EmployeeAppraisalSessionDtoEnvelope.md)

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

# **get_employee_appraisal_sessions_async**
> EmployeeAppraisalSessionDtoListEnvelope get_employee_appraisal_sessions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get employee appraisal sessions

Retrieves employee appraisal sessions for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_appraisal_session_dto_list_envelope import EmployeeAppraisalSessionDtoListEnvelope
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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employee appraisal sessions
        api_response = api_instance.get_employee_appraisal_sessions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeAppraisalSessionsApi->get_employee_appraisal_sessions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->get_employee_appraisal_sessions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeAppraisalSessionDtoListEnvelope**](EmployeeAppraisalSessionDtoListEnvelope.md)

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

# **get_employee_appraisal_sessions_count_async**
> Int32Envelope get_employee_appraisal_sessions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count employee appraisal sessions

Counts employee appraisal sessions for the specified tenant.

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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count employee appraisal sessions
        api_response = api_instance.get_employee_appraisal_sessions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeAppraisalSessionsApi->get_employee_appraisal_sessions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->get_employee_appraisal_sessions_count_async: %s\n" % e)
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

# **patch_employee_appraisal_session_async**
> EmptyEnvelope patch_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an employee appraisal session

Partially updates an existing employee appraisal session for the specified tenant.

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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    session_id = 'session_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an employee appraisal session
        api_response = api_instance.patch_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of EmployeeAppraisalSessionsApi->patch_employee_appraisal_session_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->patch_employee_appraisal_session_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **session_id** | **str**|  | 
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

# **update_employee_appraisal_session_async**
> EmptyEnvelope update_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version, employee_appraisal_session_update_dto=employee_appraisal_session_update_dto)

Update an employee appraisal session

Updates an existing employee appraisal session for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_appraisal_session_update_dto import EmployeeAppraisalSessionUpdateDto
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
    api_instance = openapi_client.EmployeeAppraisalSessionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    session_id = 'session_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employee_appraisal_session_update_dto = openapi_client.EmployeeAppraisalSessionUpdateDto() # EmployeeAppraisalSessionUpdateDto |  (optional)

    try:
        # Update an employee appraisal session
        api_response = api_instance.update_employee_appraisal_session_async(tenant_id, session_id, api_version=api_version, x_api_version=x_api_version, employee_appraisal_session_update_dto=employee_appraisal_session_update_dto)
        print("The response of EmployeeAppraisalSessionsApi->update_employee_appraisal_session_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAppraisalSessionsApi->update_employee_appraisal_session_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **session_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employee_appraisal_session_update_dto** | [**EmployeeAppraisalSessionUpdateDto**](EmployeeAppraisalSessionUpdateDto.md)|  | [optional] 

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

