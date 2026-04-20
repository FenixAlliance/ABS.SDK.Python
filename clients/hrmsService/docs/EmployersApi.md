# openapi_client.EmployersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employer_async**](EmployersApi.md#create_employer_async) | **POST** /api/v2/HrmsService/Employers | Create an employer
[**delete_employer_async**](EmployersApi.md#delete_employer_async) | **DELETE** /api/v2/HrmsService/Employers/{employerId} | Delete an employer
[**get_employer_by_id_async**](EmployersApi.md#get_employer_by_id_async) | **GET** /api/v2/HrmsService/Employers/{employerId} | Get employer by ID
[**get_employers_async**](EmployersApi.md#get_employers_async) | **GET** /api/v2/HrmsService/Employers | Get employers
[**get_employers_count_async**](EmployersApi.md#get_employers_count_async) | **GET** /api/v2/HrmsService/Employers/Count | Count employers
[**update_employer_async**](EmployersApi.md#update_employer_async) | **PUT** /api/v2/HrmsService/Employers/{employerId} | Update an employer


# **create_employer_async**
> EmptyEnvelope create_employer_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employer_profile_create_dto=employer_profile_create_dto)

Create an employer

Creates a new employer for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employer_profile_create_dto import EmployerProfileCreateDto
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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    employer_profile_create_dto = openapi_client.EmployerProfileCreateDto() # EmployerProfileCreateDto |  (optional)

    try:
        # Create an employer
        api_response = api_instance.create_employer_async(tenant_id, api_version=api_version, x_api_version=x_api_version, employer_profile_create_dto=employer_profile_create_dto)
        print("The response of EmployersApi->create_employer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->create_employer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **employer_profile_create_dto** | [**EmployerProfileCreateDto**](EmployerProfileCreateDto.md)|  | [optional] 

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

# **delete_employer_async**
> EmptyEnvelope delete_employer_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version)

Delete an employer

Deletes an employer for the specified tenant.

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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employer_id = 'employer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an employer
        api_response = api_instance.delete_employer_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployersApi->delete_employer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->delete_employer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employer_id** | **str**|  | 
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

# **get_employer_by_id_async**
> EmployerProfileDtoEnvelope get_employer_by_id_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version)

Get employer by ID

Retrieves a specific employer by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.employer_profile_dto_envelope import EmployerProfileDtoEnvelope
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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employer_id = 'employer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employer by ID
        api_response = api_instance.get_employer_by_id_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployersApi->get_employer_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->get_employer_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employer_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployerProfileDtoEnvelope**](EmployerProfileDtoEnvelope.md)

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

# **get_employers_async**
> EmployerProfileDtoListEnvelope get_employers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get employers

Retrieves employers for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.employer_profile_dto_list_envelope import EmployerProfileDtoListEnvelope
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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get employers
        api_response = api_instance.get_employers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployersApi->get_employers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->get_employers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmployerProfileDtoListEnvelope**](EmployerProfileDtoListEnvelope.md)

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

# **get_employers_count_async**
> Int32Envelope get_employers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count employers

Counts employers for the specified tenant.

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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count employers
        api_response = api_instance.get_employers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmployersApi->get_employers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->get_employers_count_async: %s\n" % e)
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

# **update_employer_async**
> EmptyEnvelope update_employer_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version, body=body)

Update an employer

Updates an existing employer for the specified tenant.

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
    api_instance = openapi_client.EmployersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    employer_id = 'employer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update an employer
        api_response = api_instance.update_employer_async(tenant_id, employer_id, api_version=api_version, x_api_version=x_api_version, body=body)
        print("The response of EmployersApi->update_employer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployersApi->update_employer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **employer_id** | **str**|  | 
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

