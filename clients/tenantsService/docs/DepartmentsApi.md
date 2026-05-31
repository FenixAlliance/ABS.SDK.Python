# openapi_client.DepartmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_department**](DepartmentsApi.md#create_tenant_department) | **POST** /api/v2/TenantsService/Departments | Create a new tenant department
[**delete_tenant_department**](DepartmentsApi.md#delete_tenant_department) | **DELETE** /api/v2/TenantsService/Departments/{tenantDepartmentId} | Delete a tenant department
[**get_tenant_department_by_id**](DepartmentsApi.md#get_tenant_department_by_id) | **GET** /api/v2/TenantsService/Departments/{tenantDepartmentId} | Retrieve a single tenant department by its ID
[**get_tenant_departments**](DepartmentsApi.md#get_tenant_departments) | **GET** /api/v2/TenantsService/Departments | Retrieve a list of tenant departments
[**get_tenant_departments_count**](DepartmentsApi.md#get_tenant_departments_count) | **GET** /api/v2/TenantsService/Departments/Count | Get the count of tenant departments
[**update_tenant_department**](DepartmentsApi.md#update_tenant_department) | **PUT** /api/v2/TenantsService/Departments/{tenantDepartmentId} | Update a tenant department


# **create_tenant_department**
> EmptyEnvelope create_tenant_department(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_department_create_dto=tenant_department_create_dto)

Create a new tenant department

Create a new tenant department

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_department_create_dto import TenantDepartmentCreateDto
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_department_create_dto = openapi_client.TenantDepartmentCreateDto() # TenantDepartmentCreateDto |  (optional)

    try:
        # Create a new tenant department
        api_response = api_instance.create_tenant_department(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_department_create_dto=tenant_department_create_dto)
        print("The response of DepartmentsApi->create_tenant_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->create_tenant_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_department_create_dto** | [**TenantDepartmentCreateDto**](TenantDepartmentCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_department**
> EmptyEnvelope delete_tenant_department(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant department

Delete a tenant department

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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_department_id = 'tenant_department_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant department
        api_response = api_instance.delete_tenant_department(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DepartmentsApi->delete_tenant_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->delete_tenant_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_department_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_department_by_id**
> TenantDepartmentDtoEnvelope get_tenant_department_by_id(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant department by its ID

Retrieve a single tenant department by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_department_dto_envelope import TenantDepartmentDtoEnvelope
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_department_id = 'tenant_department_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant department by its ID
        api_response = api_instance.get_tenant_department_by_id(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DepartmentsApi->get_tenant_department_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_tenant_department_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_department_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDepartmentDtoEnvelope**](TenantDepartmentDtoEnvelope.md)

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

# **get_tenant_departments**
> TenantDepartmentDtoListEnvelope get_tenant_departments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant departments

Retrieve a list of tenant departments

### Example


```python
import openapi_client
from openapi_client.models.tenant_department_dto_list_envelope import TenantDepartmentDtoListEnvelope
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant departments
        api_response = api_instance.get_tenant_departments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DepartmentsApi->get_tenant_departments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_tenant_departments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDepartmentDtoListEnvelope**](TenantDepartmentDtoListEnvelope.md)

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

# **get_tenant_departments_count**
> Int32Envelope get_tenant_departments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant departments

Get the count of tenant departments

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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant departments
        api_response = api_instance.get_tenant_departments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DepartmentsApi->get_tenant_departments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_tenant_departments_count: %s\n" % e)
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

# **update_tenant_department**
> EmptyEnvelope update_tenant_department(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version, tenant_department_update_dto=tenant_department_update_dto)

Update a tenant department

Update a tenant department

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_department_update_dto import TenantDepartmentUpdateDto
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_department_id = 'tenant_department_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_department_update_dto = openapi_client.TenantDepartmentUpdateDto() # TenantDepartmentUpdateDto |  (optional)

    try:
        # Update a tenant department
        api_response = api_instance.update_tenant_department(tenant_id, tenant_department_id, api_version=api_version, x_api_version=x_api_version, tenant_department_update_dto=tenant_department_update_dto)
        print("The response of DepartmentsApi->update_tenant_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->update_tenant_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_department_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_department_update_dto** | [**TenantDepartmentUpdateDto**](TenantDepartmentUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

