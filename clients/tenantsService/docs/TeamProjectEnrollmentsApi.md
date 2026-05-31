# openapi_client.TeamProjectEnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_team_project_enrollment**](TeamProjectEnrollmentsApi.md#create_tenant_team_project_enrollment) | **POST** /api/v2/TenantsService/TeamProjectEnrollments | Create a new tenant team project enrollment
[**delete_tenant_team_project_enrollment**](TeamProjectEnrollmentsApi.md#delete_tenant_team_project_enrollment) | **DELETE** /api/v2/TenantsService/TeamProjectEnrollments/{tenantTeamProjectEnrollmentId} | Delete a tenant team project enrollment
[**get_tenant_team_project_enrollment_by_id**](TeamProjectEnrollmentsApi.md#get_tenant_team_project_enrollment_by_id) | **GET** /api/v2/TenantsService/TeamProjectEnrollments/{tenantTeamProjectEnrollmentId} | Retrieve a single tenant team project enrollment by its ID
[**get_tenant_team_project_enrollments**](TeamProjectEnrollmentsApi.md#get_tenant_team_project_enrollments) | **GET** /api/v2/TenantsService/TeamProjectEnrollments | Retrieve a list of tenant team project enrollments
[**get_tenant_team_project_enrollments_count**](TeamProjectEnrollmentsApi.md#get_tenant_team_project_enrollments_count) | **GET** /api/v2/TenantsService/TeamProjectEnrollments/Count | Get the count of tenant team project enrollments
[**update_tenant_team_project_enrollment**](TeamProjectEnrollmentsApi.md#update_tenant_team_project_enrollment) | **PUT** /api/v2/TenantsService/TeamProjectEnrollments/{tenantTeamProjectEnrollmentId} | Update a tenant team project enrollment


# **create_tenant_team_project_enrollment**
> EmptyEnvelope create_tenant_team_project_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_project_enrollment_create_dto=tenant_team_project_enrollment_create_dto)

Create a new tenant team project enrollment

Create a new tenant team project enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_project_enrollment_create_dto import TenantTeamProjectEnrollmentCreateDto
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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_project_enrollment_create_dto = openapi_client.TenantTeamProjectEnrollmentCreateDto() # TenantTeamProjectEnrollmentCreateDto |  (optional)

    try:
        # Create a new tenant team project enrollment
        api_response = api_instance.create_tenant_team_project_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_project_enrollment_create_dto=tenant_team_project_enrollment_create_dto)
        print("The response of TeamProjectEnrollmentsApi->create_tenant_team_project_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->create_tenant_team_project_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_project_enrollment_create_dto** | [**TenantTeamProjectEnrollmentCreateDto**](TenantTeamProjectEnrollmentCreateDto.md)|  | [optional] 

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

# **delete_tenant_team_project_enrollment**
> EmptyEnvelope delete_tenant_team_project_enrollment(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant team project enrollment

Delete a tenant team project enrollment

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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_project_enrollment_id = 'tenant_team_project_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant team project enrollment
        api_response = api_instance.delete_tenant_team_project_enrollment(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamProjectEnrollmentsApi->delete_tenant_team_project_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->delete_tenant_team_project_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_project_enrollment_id** | **str**|  | 
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

# **get_tenant_team_project_enrollment_by_id**
> TenantTeamProjectEnrollmentDtoEnvelope get_tenant_team_project_enrollment_by_id(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant team project enrollment by its ID

Retrieve a single tenant team project enrollment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_project_enrollment_dto_envelope import TenantTeamProjectEnrollmentDtoEnvelope
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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_project_enrollment_id = 'tenant_team_project_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant team project enrollment by its ID
        api_response = api_instance.get_tenant_team_project_enrollment_by_id(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamProjectEnrollmentsApi->get_tenant_team_project_enrollment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->get_tenant_team_project_enrollment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_project_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamProjectEnrollmentDtoEnvelope**](TenantTeamProjectEnrollmentDtoEnvelope.md)

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

# **get_tenant_team_project_enrollments**
> TenantTeamProjectEnrollmentDtoListEnvelope get_tenant_team_project_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant team project enrollments

Retrieve a list of tenant team project enrollments

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_project_enrollment_dto_list_envelope import TenantTeamProjectEnrollmentDtoListEnvelope
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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant team project enrollments
        api_response = api_instance.get_tenant_team_project_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamProjectEnrollmentsApi->get_tenant_team_project_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->get_tenant_team_project_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamProjectEnrollmentDtoListEnvelope**](TenantTeamProjectEnrollmentDtoListEnvelope.md)

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

# **get_tenant_team_project_enrollments_count**
> Int32Envelope get_tenant_team_project_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant team project enrollments

Get the count of tenant team project enrollments

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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant team project enrollments
        api_response = api_instance.get_tenant_team_project_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamProjectEnrollmentsApi->get_tenant_team_project_enrollments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->get_tenant_team_project_enrollments_count: %s\n" % e)
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

# **update_tenant_team_project_enrollment**
> EmptyEnvelope update_tenant_team_project_enrollment(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_project_enrollment_update_dto=tenant_team_project_enrollment_update_dto)

Update a tenant team project enrollment

Update a tenant team project enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_project_enrollment_update_dto import TenantTeamProjectEnrollmentUpdateDto
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
    api_instance = openapi_client.TeamProjectEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_project_enrollment_id = 'tenant_team_project_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_project_enrollment_update_dto = openapi_client.TenantTeamProjectEnrollmentUpdateDto() # TenantTeamProjectEnrollmentUpdateDto |  (optional)

    try:
        # Update a tenant team project enrollment
        api_response = api_instance.update_tenant_team_project_enrollment(tenant_id, tenant_team_project_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_project_enrollment_update_dto=tenant_team_project_enrollment_update_dto)
        print("The response of TeamProjectEnrollmentsApi->update_tenant_team_project_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamProjectEnrollmentsApi->update_tenant_team_project_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_project_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_project_enrollment_update_dto** | [**TenantTeamProjectEnrollmentUpdateDto**](TenantTeamProjectEnrollmentUpdateDto.md)|  | [optional] 

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

