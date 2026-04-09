# openapi_client.EmployeeEnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_employee_enrollment**](EmployeeEnrollmentsApi.md#create_tenant_employee_enrollment) | **POST** /api/v2/TenantsService/EmployeeEnrollments | Create a new tenant employee enrollment
[**delete_tenant_employee_enrollment**](EmployeeEnrollmentsApi.md#delete_tenant_employee_enrollment) | **DELETE** /api/v2/TenantsService/EmployeeEnrollments/{tenantEmployeeEnrollmentId} | Delete a tenant employee enrollment
[**get_tenant_employee_enrollment_by_id**](EmployeeEnrollmentsApi.md#get_tenant_employee_enrollment_by_id) | **GET** /api/v2/TenantsService/EmployeeEnrollments/{tenantEmployeeEnrollmentId} | Retrieve a single tenant employee enrollment by its ID
[**get_tenant_employee_enrollments**](EmployeeEnrollmentsApi.md#get_tenant_employee_enrollments) | **GET** /api/v2/TenantsService/EmployeeEnrollments | Retrieve a list of tenant employee enrollments
[**get_tenant_employee_enrollments_count**](EmployeeEnrollmentsApi.md#get_tenant_employee_enrollments_count) | **GET** /api/v2/TenantsService/EmployeeEnrollments/Count | Get the count of tenant employee enrollments
[**update_tenant_employee_enrollment**](EmployeeEnrollmentsApi.md#update_tenant_employee_enrollment) | **PUT** /api/v2/TenantsService/EmployeeEnrollments/{tenantEmployeeEnrollmentId} | Update a tenant employee enrollment


# **create_tenant_employee_enrollment**
> EmptyEnvelope create_tenant_employee_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_employee_enrollment_create_dto=tenant_team_employee_enrollment_create_dto)

Create a new tenant employee enrollment

Create a new tenant employee enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_employee_enrollment_create_dto import TenantTeamEmployeeEnrollmentCreateDto
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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_employee_enrollment_create_dto = openapi_client.TenantTeamEmployeeEnrollmentCreateDto() # TenantTeamEmployeeEnrollmentCreateDto |  (optional)

    try:
        # Create a new tenant employee enrollment
        api_response = api_instance.create_tenant_employee_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_employee_enrollment_create_dto=tenant_team_employee_enrollment_create_dto)
        print("The response of EmployeeEnrollmentsApi->create_tenant_employee_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->create_tenant_employee_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_employee_enrollment_create_dto** | [**TenantTeamEmployeeEnrollmentCreateDto**](TenantTeamEmployeeEnrollmentCreateDto.md)|  | [optional] 

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

# **delete_tenant_employee_enrollment**
> EmptyEnvelope delete_tenant_employee_enrollment(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant employee enrollment

Delete a tenant employee enrollment

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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_employee_enrollment_id = 'tenant_employee_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant employee enrollment
        api_response = api_instance.delete_tenant_employee_enrollment(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeEnrollmentsApi->delete_tenant_employee_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->delete_tenant_employee_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_employee_enrollment_id** | **str**|  | 
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

# **get_tenant_employee_enrollment_by_id**
> TenantTeamEmployeeEnrollmentDtoEnvelope get_tenant_employee_enrollment_by_id(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant employee enrollment by its ID

Retrieve a single tenant employee enrollment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_employee_enrollment_dto_envelope import TenantTeamEmployeeEnrollmentDtoEnvelope
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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_employee_enrollment_id = 'tenant_employee_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant employee enrollment by its ID
        api_response = api_instance.get_tenant_employee_enrollment_by_id(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeEnrollmentsApi->get_tenant_employee_enrollment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->get_tenant_employee_enrollment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_employee_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamEmployeeEnrollmentDtoEnvelope**](TenantTeamEmployeeEnrollmentDtoEnvelope.md)

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

# **get_tenant_employee_enrollments**
> TenantTeamEmployeeEnrollmentDtoListEnvelope get_tenant_employee_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant employee enrollments

Retrieve a list of tenant employee enrollments

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_employee_enrollment_dto_list_envelope import TenantTeamEmployeeEnrollmentDtoListEnvelope
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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant employee enrollments
        api_response = api_instance.get_tenant_employee_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeEnrollmentsApi->get_tenant_employee_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->get_tenant_employee_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamEmployeeEnrollmentDtoListEnvelope**](TenantTeamEmployeeEnrollmentDtoListEnvelope.md)

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

# **get_tenant_employee_enrollments_count**
> Int32Envelope get_tenant_employee_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant employee enrollments

Get the count of tenant employee enrollments

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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant employee enrollments
        api_response = api_instance.get_tenant_employee_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployeeEnrollmentsApi->get_tenant_employee_enrollments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->get_tenant_employee_enrollments_count: %s\n" % e)
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

# **update_tenant_employee_enrollment**
> EmptyEnvelope update_tenant_employee_enrollment(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_employee_enrollment_update_dto=tenant_team_employee_enrollment_update_dto)

Update a tenant employee enrollment

Update a tenant employee enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_employee_enrollment_update_dto import TenantTeamEmployeeEnrollmentUpdateDto
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
    api_instance = openapi_client.EmployeeEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_employee_enrollment_id = 'tenant_employee_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_employee_enrollment_update_dto = openapi_client.TenantTeamEmployeeEnrollmentUpdateDto() # TenantTeamEmployeeEnrollmentUpdateDto |  (optional)

    try:
        # Update a tenant employee enrollment
        api_response = api_instance.update_tenant_employee_enrollment(tenant_id, tenant_employee_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_employee_enrollment_update_dto=tenant_team_employee_enrollment_update_dto)
        print("The response of EmployeeEnrollmentsApi->update_tenant_employee_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeEnrollmentsApi->update_tenant_employee_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_employee_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_employee_enrollment_update_dto** | [**TenantTeamEmployeeEnrollmentUpdateDto**](TenantTeamEmployeeEnrollmentUpdateDto.md)|  | [optional] 

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

