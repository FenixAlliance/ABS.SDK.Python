# openapi_client.TeamContactEnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_team_contact_enrollment**](TeamContactEnrollmentsApi.md#create_tenant_team_contact_enrollment) | **POST** /api/v2/TenantsService/TeamContactEnrollments | Create a new tenant team contact enrollment
[**delete_tenant_team_contact_enrollment**](TeamContactEnrollmentsApi.md#delete_tenant_team_contact_enrollment) | **DELETE** /api/v2/TenantsService/TeamContactEnrollments/{tenantTeamContactEnrollmentId} | Delete a tenant team contact enrollment
[**get_tenant_team_contact_enrollment_by_id**](TeamContactEnrollmentsApi.md#get_tenant_team_contact_enrollment_by_id) | **GET** /api/v2/TenantsService/TeamContactEnrollments/{tenantTeamContactEnrollmentId} | Retrieve a single tenant team contact enrollment by its ID
[**get_tenant_team_contact_enrollments**](TeamContactEnrollmentsApi.md#get_tenant_team_contact_enrollments) | **GET** /api/v2/TenantsService/TeamContactEnrollments | Retrieve a list of tenant team contact enrollments
[**get_tenant_team_contact_enrollments_count**](TeamContactEnrollmentsApi.md#get_tenant_team_contact_enrollments_count) | **GET** /api/v2/TenantsService/TeamContactEnrollments/Count | Get the count of tenant team contact enrollments
[**update_tenant_team_contact_enrollment**](TeamContactEnrollmentsApi.md#update_tenant_team_contact_enrollment) | **PUT** /api/v2/TenantsService/TeamContactEnrollments/{tenantTeamContactEnrollmentId} | Update a tenant team contact enrollment


# **create_tenant_team_contact_enrollment**
> EmptyEnvelope create_tenant_team_contact_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_contact_enrollment_create_dto=tenant_team_contact_enrollment_create_dto)

Create a new tenant team contact enrollment

Create a new tenant team contact enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_contact_enrollment_create_dto import TenantTeamContactEnrollmentCreateDto
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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_contact_enrollment_create_dto = openapi_client.TenantTeamContactEnrollmentCreateDto() # TenantTeamContactEnrollmentCreateDto |  (optional)

    try:
        # Create a new tenant team contact enrollment
        api_response = api_instance.create_tenant_team_contact_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_contact_enrollment_create_dto=tenant_team_contact_enrollment_create_dto)
        print("The response of TeamContactEnrollmentsApi->create_tenant_team_contact_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->create_tenant_team_contact_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_contact_enrollment_create_dto** | [**TenantTeamContactEnrollmentCreateDto**](TenantTeamContactEnrollmentCreateDto.md)|  | [optional] 

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

# **delete_tenant_team_contact_enrollment**
> EmptyEnvelope delete_tenant_team_contact_enrollment(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant team contact enrollment

Delete a tenant team contact enrollment

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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_contact_enrollment_id = 'tenant_team_contact_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant team contact enrollment
        api_response = api_instance.delete_tenant_team_contact_enrollment(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamContactEnrollmentsApi->delete_tenant_team_contact_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->delete_tenant_team_contact_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_contact_enrollment_id** | **str**|  | 
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

# **get_tenant_team_contact_enrollment_by_id**
> TenantTeamContactEnrollmentDtoEnvelope get_tenant_team_contact_enrollment_by_id(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant team contact enrollment by its ID

Retrieve a single tenant team contact enrollment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_contact_enrollment_dto_envelope import TenantTeamContactEnrollmentDtoEnvelope
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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_contact_enrollment_id = 'tenant_team_contact_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant team contact enrollment by its ID
        api_response = api_instance.get_tenant_team_contact_enrollment_by_id(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamContactEnrollmentsApi->get_tenant_team_contact_enrollment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->get_tenant_team_contact_enrollment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_contact_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamContactEnrollmentDtoEnvelope**](TenantTeamContactEnrollmentDtoEnvelope.md)

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

# **get_tenant_team_contact_enrollments**
> TenantTeamContactEnrollmentDtoListEnvelope get_tenant_team_contact_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant team contact enrollments

Retrieve a list of tenant team contact enrollments

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_contact_enrollment_dto_list_envelope import TenantTeamContactEnrollmentDtoListEnvelope
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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant team contact enrollments
        api_response = api_instance.get_tenant_team_contact_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamContactEnrollmentsApi->get_tenant_team_contact_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->get_tenant_team_contact_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamContactEnrollmentDtoListEnvelope**](TenantTeamContactEnrollmentDtoListEnvelope.md)

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

# **get_tenant_team_contact_enrollments_count**
> Int32Envelope get_tenant_team_contact_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant team contact enrollments

Get the count of tenant team contact enrollments

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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant team contact enrollments
        api_response = api_instance.get_tenant_team_contact_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamContactEnrollmentsApi->get_tenant_team_contact_enrollments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->get_tenant_team_contact_enrollments_count: %s\n" % e)
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

# **update_tenant_team_contact_enrollment**
> EmptyEnvelope update_tenant_team_contact_enrollment(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_contact_enrollment_update_dto=tenant_team_contact_enrollment_update_dto)

Update a tenant team contact enrollment

Update a tenant team contact enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_contact_enrollment_update_dto import TenantTeamContactEnrollmentUpdateDto
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
    api_instance = openapi_client.TeamContactEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_contact_enrollment_id = 'tenant_team_contact_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_contact_enrollment_update_dto = openapi_client.TenantTeamContactEnrollmentUpdateDto() # TenantTeamContactEnrollmentUpdateDto |  (optional)

    try:
        # Update a tenant team contact enrollment
        api_response = api_instance.update_tenant_team_contact_enrollment(tenant_id, tenant_team_contact_enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_team_contact_enrollment_update_dto=tenant_team_contact_enrollment_update_dto)
        print("The response of TeamContactEnrollmentsApi->update_tenant_team_contact_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamContactEnrollmentsApi->update_tenant_team_contact_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_contact_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_contact_enrollment_update_dto** | [**TenantTeamContactEnrollmentUpdateDto**](TenantTeamContactEnrollmentUpdateDto.md)|  | [optional] 

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

