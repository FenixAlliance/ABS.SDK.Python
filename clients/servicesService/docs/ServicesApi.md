# openapi_client.ServicesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_async**](ServicesApi.md#create_service_async) | **POST** /api/v2/ServicesService/Services | Create a service
[**delete_service_async**](ServicesApi.md#delete_service_async) | **DELETE** /api/v2/ServicesService/Services/{serviceId} | Delete a service
[**get_service_by_id_async**](ServicesApi.md#get_service_by_id_async) | **GET** /api/v2/ServicesService/Services/{serviceId} | Get a service by ID
[**get_services_async**](ServicesApi.md#get_services_async) | **GET** /api/v2/ServicesService/Services | Get all services
[**get_services_count_async**](ServicesApi.md#get_services_count_async) | **GET** /api/v2/ServicesService/Services/Count | Get services count
[**update_service_async**](ServicesApi.md#update_service_async) | **PUT** /api/v2/ServicesService/Services/{serviceId} | Update a service


# **create_service_async**
> Envelope create_service_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_create_dto=service_create_dto)

Create a service

Creates a new service for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_create_dto import ServiceCreateDto
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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_create_dto = openapi_client.ServiceCreateDto() # ServiceCreateDto |  (optional)

    try:
        # Create a service
        api_response = api_instance.create_service_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_create_dto=service_create_dto)
        print("The response of ServicesApi->create_service_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_create_dto** | [**ServiceCreateDto**](ServiceCreateDto.md)|  | [optional] 

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

# **delete_service_async**
> Envelope delete_service_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)

Delete a service

Deletes a service by its identifier.

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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service
        api_response = api_instance.delete_service_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServicesApi->delete_service_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
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

# **get_service_by_id_async**
> ServiceDtoEnvelope get_service_by_id_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)

Get a service by ID

Retrieves a service by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_dto_envelope import ServiceDtoEnvelope
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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service by ID
        api_response = api_instance.get_service_by_id_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServicesApi->get_service_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceDtoEnvelope**](ServiceDtoEnvelope.md)

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

# **get_services_async**
> ServiceDtoIReadOnlyListEnvelope get_services_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all services

Retrieves all services for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_dto_i_read_only_list_envelope import ServiceDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all services
        api_response = api_instance.get_services_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServicesApi->get_services_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceDtoIReadOnlyListEnvelope**](ServiceDtoIReadOnlyListEnvelope.md)

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

# **get_services_count_async**
> Int32Envelope get_services_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get services count

Returns the count of services for the specified tenant.

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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get services count
        api_response = api_instance.get_services_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServicesApi->get_services_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_count_async: %s\n" % e)
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

# **update_service_async**
> Envelope update_service_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version, service_update_dto=service_update_dto)

Update a service

Updates an existing service.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_update_dto import ServiceUpdateDto
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
    api_instance = openapi_client.ServicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_update_dto = openapi_client.ServiceUpdateDto() # ServiceUpdateDto |  (optional)

    try:
        # Update a service
        api_response = api_instance.update_service_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version, service_update_dto=service_update_dto)
        print("The response of ServicesApi->update_service_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_update_dto** | [**ServiceUpdateDto**](ServiceUpdateDto.md)|  | [optional] 

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

