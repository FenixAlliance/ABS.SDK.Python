# openapi_client.EmployeesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_async**](EmployeesApi.md#create_employee_async) | **POST** /api/v2/HrmsService/Employees | Create an employee
[**delete_employee_async**](EmployeesApi.md#delete_employee_async) | **DELETE** /api/v2/HrmsService/Employees/{employeeId} | Delete an employee
[**get_employee_by_id_async**](EmployeesApi.md#get_employee_by_id_async) | **GET** /api/v2/HrmsService/Employees/{employeeId} | Get employee by ID
[**get_employees_async**](EmployeesApi.md#get_employees_async) | **GET** /api/v2/HrmsService/Employees | Get employees
[**get_employees_count_async**](EmployeesApi.md#get_employees_count_async) | **GET** /api/v2/HrmsService/Employees/Count | Count employees
[**update_employee_async**](EmployeesApi.md#update_employee_async) | **PUT** /api/v2/HrmsService/Employees/{employeeId} | Update an employee


# **create_employee_async**
> EmptyEnvelope create_employee_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_profile_create_dto=employee_profile_create_dto)

Create an employee

Creates a new employee for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_profile_create_dto import EmployeeProfileCreateDto
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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employee_profile_create_dto = openapi_client.EmployeeProfileCreateDto() # EmployeeProfileCreateDto |  (optional)

    try:
        # Create an employee
        api_response = api_instance.create_employee_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_profile_create_dto=employee_profile_create_dto)
        print("The response of EmployeesApi->create_employee_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_employee_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employee_profile_create_dto** | [**EmployeeProfileCreateDto**](EmployeeProfileCreateDto.md)|  | [optional] 

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

# **delete_employee_async**
> EmptyEnvelope delete_employee_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version)

Delete an employee

Deletes an employee for the specified tenant.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_id = 'employee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an employee
        api_response = api_instance.delete_employee_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeesApi->delete_employee_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->delete_employee_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_id** | **str**|  | 
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

# **get_employee_by_id_async**
> EmployeeProfileDtoEnvelope get_employee_by_id_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version)

Get employee by ID

Retrieves a specific employee by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.employee_profile_dto_envelope import EmployeeProfileDtoEnvelope
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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_id = 'employee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employee by ID
        api_response = api_instance.get_employee_by_id_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeesApi->get_employee_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employee_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeProfileDtoEnvelope**](EmployeeProfileDtoEnvelope.md)

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

# **get_employees_async**
> EmployeeProfileDtoListEnvelope get_employees_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get employees

Retrieves employees for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_profile_dto_list_envelope import EmployeeProfileDtoListEnvelope
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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employees
        api_response = api_instance.get_employees_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeesApi->get_employees_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employees_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeProfileDtoListEnvelope**](EmployeeProfileDtoListEnvelope.md)

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

# **get_employees_count_async**
> Int32Envelope get_employees_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count employees

Counts employees for the specified tenant.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count employees
        api_response = api_instance.get_employees_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeesApi->get_employees_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employees_count_async: %s\n" % e)
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

# **update_employee_async**
> EmptyEnvelope update_employee_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version, body=body)

Update an employee

Updates an existing employee for the specified tenant.

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
    api_instance = openapi_client.EmployeesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_id = 'employee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update an employee
        api_response = api_instance.update_employee_async(tenant_id, employee_id, api_version=api_version, x_api_version=x_api_version, body=body)
        print("The response of EmployeesApi->update_employee_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_employee_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

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

