# openapi_client.ServiceCaseTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_case_type_async**](ServiceCaseTypesApi.md#create_service_case_type_async) | **POST** /api/v2/ServicesService/ServiceCaseTypes | Create a service case type
[**delete_service_case_type_async**](ServiceCaseTypesApi.md#delete_service_case_type_async) | **DELETE** /api/v2/ServicesService/ServiceCaseTypes/{serviceCaseTypeId} | Delete a service case type
[**get_service_case_type_by_id_async**](ServiceCaseTypesApi.md#get_service_case_type_by_id_async) | **GET** /api/v2/ServicesService/ServiceCaseTypes/{serviceCaseTypeId} | Get a service case type by ID
[**get_service_case_types_async**](ServiceCaseTypesApi.md#get_service_case_types_async) | **GET** /api/v2/ServicesService/ServiceCaseTypes | Get all service case types
[**get_service_case_types_count_async**](ServiceCaseTypesApi.md#get_service_case_types_count_async) | **GET** /api/v2/ServicesService/ServiceCaseTypes/Count | Get service case types count
[**update_service_case_type_async**](ServiceCaseTypesApi.md#update_service_case_type_async) | **PUT** /api/v2/ServicesService/ServiceCaseTypes/{serviceCaseTypeId} | Update a service case type


# **create_service_case_type_async**
> Envelope create_service_case_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_case_type_create_dto=service_case_type_create_dto)

Create a service case type

Creates a new service case type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_case_type_create_dto import ServiceCaseTypeCreateDto
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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_case_type_create_dto = openapi_client.ServiceCaseTypeCreateDto() # ServiceCaseTypeCreateDto |  (optional)

    try:
        # Create a service case type
        api_response = api_instance.create_service_case_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_case_type_create_dto=service_case_type_create_dto)
        print("The response of ServiceCaseTypesApi->create_service_case_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->create_service_case_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_case_type_create_dto** | [**ServiceCaseTypeCreateDto**](ServiceCaseTypeCreateDto.md)|  | [optional] 

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

# **delete_service_case_type_async**
> Envelope delete_service_case_type_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a service case type

Deletes a service case type by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_type_id = 'service_case_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service case type
        api_response = api_instance.delete_service_case_type_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCaseTypesApi->delete_service_case_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->delete_service_case_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_type_id** | **str**|  | 
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

# **get_service_case_type_by_id_async**
> ServiceCaseTypeDtoEnvelope get_service_case_type_by_id_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version)

Get a service case type by ID

Retrieves a service case type by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_case_type_dto_envelope import ServiceCaseTypeDtoEnvelope
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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_type_id = 'service_case_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service case type by ID
        api_response = api_instance.get_service_case_type_by_id_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCaseTypesApi->get_service_case_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->get_service_case_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceCaseTypeDtoEnvelope**](ServiceCaseTypeDtoEnvelope.md)

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

# **get_service_case_types_async**
> ServiceCaseTypeDtoIReadOnlyListEnvelope get_service_case_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service case types

Retrieves all service case types for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_case_type_dto_i_read_only_list_envelope import ServiceCaseTypeDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service case types
        api_response = api_instance.get_service_case_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCaseTypesApi->get_service_case_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->get_service_case_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceCaseTypeDtoIReadOnlyListEnvelope**](ServiceCaseTypeDtoIReadOnlyListEnvelope.md)

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

# **get_service_case_types_count_async**
> Int32Envelope get_service_case_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get service case types count

Returns the count of service case types for the specified tenant.

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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get service case types count
        api_response = api_instance.get_service_case_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceCaseTypesApi->get_service_case_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->get_service_case_types_count_async: %s\n" % e)
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

# **update_service_case_type_async**
> Envelope update_service_case_type_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version, service_case_type_update_dto=service_case_type_update_dto)

Update a service case type

Updates an existing service case type.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_case_type_update_dto import ServiceCaseTypeUpdateDto
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
    api_instance = openapi_client.ServiceCaseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_case_type_id = 'service_case_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_case_type_update_dto = openapi_client.ServiceCaseTypeUpdateDto() # ServiceCaseTypeUpdateDto |  (optional)

    try:
        # Update a service case type
        api_response = api_instance.update_service_case_type_async(tenant_id, service_case_type_id, api_version=api_version, x_api_version=x_api_version, service_case_type_update_dto=service_case_type_update_dto)
        print("The response of ServiceCaseTypesApi->update_service_case_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCaseTypesApi->update_service_case_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_case_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_case_type_update_dto** | [**ServiceCaseTypeUpdateDto**](ServiceCaseTypeUpdateDto.md)|  | [optional] 

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

