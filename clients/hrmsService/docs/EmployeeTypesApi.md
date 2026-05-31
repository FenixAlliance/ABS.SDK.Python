# openapi_client.EmployeeTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_type_async**](EmployeeTypesApi.md#create_employee_type_async) | **POST** /api/v2/HrmsService/EmployeeTypes | Create an employee type
[**delete_employee_type_async**](EmployeeTypesApi.md#delete_employee_type_async) | **DELETE** /api/v2/HrmsService/EmployeeTypes/{employeeTypeId} | Delete an employee type
[**get_employee_type_by_id_async**](EmployeeTypesApi.md#get_employee_type_by_id_async) | **GET** /api/v2/HrmsService/EmployeeTypes/{employeeTypeId} | Get employee type by ID
[**get_employee_types_async**](EmployeeTypesApi.md#get_employee_types_async) | **GET** /api/v2/HrmsService/EmployeeTypes | Get employee types
[**get_employee_types_count_async**](EmployeeTypesApi.md#get_employee_types_count_async) | **GET** /api/v2/HrmsService/EmployeeTypes/Count | Count employee types
[**update_employee_type_async**](EmployeeTypesApi.md#update_employee_type_async) | **PUT** /api/v2/HrmsService/EmployeeTypes/{employeeTypeId} | Update an employee type


# **create_employee_type_async**
> EmptyEnvelope create_employee_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_type_create_dto=employee_type_create_dto)

Create an employee type

Creates a new employee type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_type_create_dto import EmployeeTypeCreateDto
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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employee_type_create_dto = openapi_client.EmployeeTypeCreateDto() # EmployeeTypeCreateDto |  (optional)

    try:
        # Create an employee type
        api_response = api_instance.create_employee_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employee_type_create_dto=employee_type_create_dto)
        print("The response of EmployeeTypesApi->create_employee_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->create_employee_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employee_type_create_dto** | [**EmployeeTypeCreateDto**](EmployeeTypeCreateDto.md)|  | [optional] 

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

# **delete_employee_type_async**
> EmptyEnvelope delete_employee_type_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version)

Delete an employee type

Deletes an employee type for the specified tenant.

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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_type_id = 'employee_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an employee type
        api_response = api_instance.delete_employee_type_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeTypesApi->delete_employee_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->delete_employee_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_type_id** | **str**|  | 
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

# **get_employee_type_by_id_async**
> EmployeeTypeDtoEnvelope get_employee_type_by_id_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version)

Get employee type by ID

Retrieves a specific employee type by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.employee_type_dto_envelope import EmployeeTypeDtoEnvelope
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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_type_id = 'employee_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employee type by ID
        api_response = api_instance.get_employee_type_by_id_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeTypesApi->get_employee_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->get_employee_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeTypeDtoEnvelope**](EmployeeTypeDtoEnvelope.md)

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

# **get_employee_types_async**
> EmployeeTypeDtoListEnvelope get_employee_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get employee types

Retrieves employee types for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_type_dto_list_envelope import EmployeeTypeDtoListEnvelope
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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employee types
        api_response = api_instance.get_employee_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeTypesApi->get_employee_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->get_employee_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployeeTypeDtoListEnvelope**](EmployeeTypeDtoListEnvelope.md)

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

# **get_employee_types_count_async**
> Int32Envelope get_employee_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count employee types

Counts employee types for the specified tenant.

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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count employee types
        api_response = api_instance.get_employee_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeTypesApi->get_employee_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->get_employee_types_count_async: %s\n" % e)
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

# **update_employee_type_async**
> EmptyEnvelope update_employee_type_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version, employee_type_update_dto=employee_type_update_dto)

Update an employee type

Updates an existing employee type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employee_type_update_dto import EmployeeTypeUpdateDto
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
    api_instance = openapi_client.EmployeeTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employee_type_id = 'employee_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employee_type_update_dto = openapi_client.EmployeeTypeUpdateDto() # EmployeeTypeUpdateDto |  (optional)

    try:
        # Update an employee type
        api_response = api_instance.update_employee_type_async(tenant_id, employee_type_id, api_version=api_version, x_api_version=x_api_version, employee_type_update_dto=employee_type_update_dto)
        print("The response of EmployeeTypesApi->update_employee_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeTypesApi->update_employee_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employee_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employee_type_update_dto** | [**EmployeeTypeUpdateDto**](EmployeeTypeUpdateDto.md)|  | [optional] 

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

