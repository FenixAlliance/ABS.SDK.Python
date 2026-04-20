# openapi_client.EnrollmentsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_enrollment**](EnrollmentsApi.md#create_tenant_enrollment) | **POST** /api/v2/TenantsService/Enrollments | Create a new tenant enrollment
[**delete_tenant_enrollment**](EnrollmentsApi.md#delete_tenant_enrollment) | **DELETE** /api/v2/TenantsService/Enrollments/{enrollmentId} | Delete a tenant enrollment
[**get_extended_tenant_enrollments**](EnrollmentsApi.md#get_extended_tenant_enrollments) | **GET** /api/v2/TenantsService/Enrollments/Extended | Retrieve a list of tenant enrollments
[**get_extended_tenant_enrollments_count**](EnrollmentsApi.md#get_extended_tenant_enrollments_count) | **GET** /api/v2/TenantsService/Enrollments/Extended/Count | Get the count of tenant enrollments
[**get_tenant_enrollment_by_id**](EnrollmentsApi.md#get_tenant_enrollment_by_id) | **GET** /api/v2/TenantsService/Enrollments/{enrollmentId} | Retrieve a single tenant enrollment by its ID
[**get_tenant_enrollments**](EnrollmentsApi.md#get_tenant_enrollments) | **GET** /api/v2/TenantsService/Enrollments | Retrieve a list of tenant enrollments
[**get_tenant_enrollments_count**](EnrollmentsApi.md#get_tenant_enrollments_count) | **GET** /api/v2/TenantsService/Enrollments/Count | Get the count of tenant enrollments
[**update_tenant_enrollment**](EnrollmentsApi.md#update_tenant_enrollment) | **PUT** /api/v2/TenantsService/Enrollments/{enrollmentId} | Update a tenant enrollment


# **create_tenant_enrollment**
> EmptyEnvelope create_tenant_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_enrollment_create_dto=tenant_enrollment_create_dto)

Create a new tenant enrollment

Create a new tenant enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_enrollment_create_dto import TenantEnrollmentCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_enrollment_create_dto = openapi_client.TenantEnrollmentCreateDto() # TenantEnrollmentCreateDto |  (optional)

    try:
        # Create a new tenant enrollment
        api_response = api_instance.create_tenant_enrollment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_enrollment_create_dto=tenant_enrollment_create_dto)
        print("The response of EnrollmentsApi->create_tenant_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->create_tenant_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_enrollment_create_dto** | [**TenantEnrollmentCreateDto**](TenantEnrollmentCreateDto.md)|  | [optional] 

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

# **delete_tenant_enrollment**
> EmptyEnvelope delete_tenant_enrollment(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant enrollment

Delete a tenant enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant enrollment
        api_response = api_instance.delete_tenant_enrollment(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->delete_tenant_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->delete_tenant_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
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

# **get_extended_tenant_enrollments**
> TenantEnrollmentDtoListEnvelope get_extended_tenant_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant enrollments

Retrieve a list of tenant enrollments

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_list_envelope import TenantEnrollmentDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant enrollments
        api_response = api_instance.get_extended_tenant_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->get_extended_tenant_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->get_extended_tenant_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoListEnvelope**](TenantEnrollmentDtoListEnvelope.md)

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

# **get_extended_tenant_enrollments_count**
> Int32Envelope get_extended_tenant_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant enrollments

Get the count of tenant enrollments

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant enrollments
        api_response = api_instance.get_extended_tenant_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->get_extended_tenant_enrollments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->get_extended_tenant_enrollments_count: %s\n" % e)
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

# **get_tenant_enrollment_by_id**
> TenantEnrollmentDtoEnvelope get_tenant_enrollment_by_id(tenant_id, enrollment_id, user_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant enrollment by its ID

Retrieve a single tenant enrollment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_envelope import TenantEnrollmentDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    user_id = 'user_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant enrollment by its ID
        api_response = api_instance.get_tenant_enrollment_by_id(tenant_id, enrollment_id, user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->get_tenant_enrollment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->get_tenant_enrollment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **user_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoEnvelope**](TenantEnrollmentDtoEnvelope.md)

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

# **get_tenant_enrollments**
> TenantEnrollmentDtoListEnvelope get_tenant_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant enrollments

Retrieve a list of tenant enrollments

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_list_envelope import TenantEnrollmentDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant enrollments
        api_response = api_instance.get_tenant_enrollments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->get_tenant_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->get_tenant_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoListEnvelope**](TenantEnrollmentDtoListEnvelope.md)

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

# **get_tenant_enrollments_count**
> Int32Envelope get_tenant_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant enrollments

Get the count of tenant enrollments

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant enrollments
        api_response = api_instance.get_tenant_enrollments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EnrollmentsApi->get_tenant_enrollments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->get_tenant_enrollments_count: %s\n" % e)
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

# **update_tenant_enrollment**
> EmptyEnvelope update_tenant_enrollment(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_enrollment_update_dto=tenant_enrollment_update_dto)

Update a tenant enrollment

Update a tenant enrollment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_enrollment_update_dto import TenantEnrollmentUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_enrollment_update_dto = openapi_client.TenantEnrollmentUpdateDto() # TenantEnrollmentUpdateDto |  (optional)

    try:
        # Update a tenant enrollment
        api_response = api_instance.update_tenant_enrollment(tenant_id, enrollment_id, api_version=api_version, x_api_version=x_api_version, tenant_enrollment_update_dto=tenant_enrollment_update_dto)
        print("The response of EnrollmentsApi->update_tenant_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentsApi->update_tenant_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_enrollment_update_dto** | [**TenantEnrollmentUpdateDto**](TenantEnrollmentUpdateDto.md)|  | [optional] 

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

