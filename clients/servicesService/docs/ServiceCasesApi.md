# openapi_client.ServiceCasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_case_async**](ServiceCasesApi.md#create_service_case_async) | **POST** /api/v2/ServicesService/ServiceCases | Create a service case
[**delete_service_case_async**](ServiceCasesApi.md#delete_service_case_async) | **DELETE** /api/v2/ServicesService/ServiceCases/{serviceCaseId} | Delete a service case
[**get_service_case_by_id_async**](ServiceCasesApi.md#get_service_case_by_id_async) | **GET** /api/v2/ServicesService/ServiceCases/{serviceCaseId} | Get a service case by ID
[**get_service_cases_async**](ServiceCasesApi.md#get_service_cases_async) | **GET** /api/v2/ServicesService/ServiceCases | Get all service cases
[**get_service_cases_count_async**](ServiceCasesApi.md#get_service_cases_count_async) | **GET** /api/v2/ServicesService/ServiceCases/Count | Get service cases count
[**update_service_case_async**](ServiceCasesApi.md#update_service_case_async) | **PUT** /api/v2/ServicesService/ServiceCases/{serviceCaseId} | Update a service case


# **create_service_case_async**
> Envelope create_service_case_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_case_create_dto=service_case_create_dto)

Create a service case

Creates a new service case for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_case_create_dto import ServiceCaseCreateDto
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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_case_create_dto = openapi_client.ServiceCaseCreateDto() # ServiceCaseCreateDto |  (optional)

    try:
        # Create a service case
        api_response = api_instance.create_service_case_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_case_create_dto=service_case_create_dto)
        print("The response of ServiceCasesApi->create_service_case_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->create_service_case_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_case_create_dto** | [**ServiceCaseCreateDto**](ServiceCaseCreateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **delete_service_case_async**
> Envelope delete_service_case_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version)

Delete a service case

Deletes a service case by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_id = 'service_case_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service case
        api_response = api_instance.delete_service_case_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCasesApi->delete_service_case_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->delete_service_case_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **get_service_case_by_id_async**
> ServiceCaseDtoEnvelope get_service_case_by_id_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version)

Get a service case by ID

Retrieves a service case by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_case_dto_envelope import ServiceCaseDtoEnvelope
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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_id = 'service_case_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service case by ID
        api_response = api_instance.get_service_case_by_id_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCasesApi->get_service_case_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->get_service_case_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceCaseDtoEnvelope**](ServiceCaseDtoEnvelope.md)

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

# **get_service_cases_async**
> ServiceCaseDtoIReadOnlyListEnvelope get_service_cases_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service cases

Retrieves all service cases for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_case_dto_i_read_only_list_envelope import ServiceCaseDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service cases
        api_response = api_instance.get_service_cases_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCasesApi->get_service_cases_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->get_service_cases_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceCaseDtoIReadOnlyListEnvelope**](ServiceCaseDtoIReadOnlyListEnvelope.md)

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

# **get_service_cases_count_async**
> Int32Envelope get_service_cases_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get service cases count

Returns the count of service cases for the specified tenant.

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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get service cases count
        api_response = api_instance.get_service_cases_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCasesApi->get_service_cases_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->get_service_cases_count_async: %s\n" % e)
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

# **update_service_case_async**
> Envelope update_service_case_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version, service_case_update_dto=service_case_update_dto)

Update a service case

Updates an existing service case.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_case_update_dto import ServiceCaseUpdateDto
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
    api_instance = openapi_client.ServiceCasesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_id = 'service_case_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_case_update_dto = openapi_client.ServiceCaseUpdateDto() # ServiceCaseUpdateDto |  (optional)

    try:
        # Update a service case
        api_response = api_instance.update_service_case_async(tenant_id, service_case_id, api_version=api_version, x_api_version=x_api_version, service_case_update_dto=service_case_update_dto)
        print("The response of ServiceCasesApi->update_service_case_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCasesApi->update_service_case_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_case_update_dto** | [**ServiceCaseUpdateDto**](ServiceCaseUpdateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

