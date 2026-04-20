# openapi_client.ServiceQueuesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_queue_async**](ServiceQueuesApi.md#create_service_queue_async) | **POST** /api/v2/ServicesService/ServiceQueues | Create a service queue
[**delete_service_queue_async**](ServiceQueuesApi.md#delete_service_queue_async) | **DELETE** /api/v2/ServicesService/ServiceQueues/{serviceQueueId} | Delete a service queue
[**get_service_queue_by_id_async**](ServiceQueuesApi.md#get_service_queue_by_id_async) | **GET** /api/v2/ServicesService/ServiceQueues/{serviceQueueId} | Get a service queue by ID
[**get_service_queues_async**](ServiceQueuesApi.md#get_service_queues_async) | **GET** /api/v2/ServicesService/ServiceQueues | Get all service queues
[**get_service_queues_count_async**](ServiceQueuesApi.md#get_service_queues_count_async) | **GET** /api/v2/ServicesService/ServiceQueues/Count | Get service queues count
[**update_service_queue_async**](ServiceQueuesApi.md#update_service_queue_async) | **PUT** /api/v2/ServicesService/ServiceQueues/{serviceQueueId} | Update a service queue


# **create_service_queue_async**
> Envelope create_service_queue_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_queue_create_dto=service_queue_create_dto)

Create a service queue

Creates a new service queue for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_queue_create_dto import ServiceQueueCreateDto
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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_queue_create_dto = openapi_client.ServiceQueueCreateDto() # ServiceQueueCreateDto |  (optional)

    try:
        # Create a service queue
        api_response = api_instance.create_service_queue_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_queue_create_dto=service_queue_create_dto)
        print("The response of ServiceQueuesApi->create_service_queue_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->create_service_queue_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_queue_create_dto** | [**ServiceQueueCreateDto**](ServiceQueueCreateDto.md)|  | [optional] 

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

# **delete_service_queue_async**
> Envelope delete_service_queue_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version)

Delete a service queue

Deletes a service queue by its identifier.

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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_queue_id = 'service_queue_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service queue
        api_response = api_instance.delete_service_queue_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceQueuesApi->delete_service_queue_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->delete_service_queue_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_queue_id** | **str**|  | 
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

# **get_service_queue_by_id_async**
> ServiceQueueDtoEnvelope get_service_queue_by_id_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version)

Get a service queue by ID

Retrieves a service queue by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_queue_dto_envelope import ServiceQueueDtoEnvelope
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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_queue_id = 'service_queue_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service queue by ID
        api_response = api_instance.get_service_queue_by_id_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceQueuesApi->get_service_queue_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->get_service_queue_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_queue_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceQueueDtoEnvelope**](ServiceQueueDtoEnvelope.md)

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

# **get_service_queues_async**
> ServiceQueueDtoIReadOnlyListEnvelope get_service_queues_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service queues

Retrieves all service queues for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_queue_dto_i_read_only_list_envelope import ServiceQueueDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service queues
        api_response = api_instance.get_service_queues_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceQueuesApi->get_service_queues_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->get_service_queues_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceQueueDtoIReadOnlyListEnvelope**](ServiceQueueDtoIReadOnlyListEnvelope.md)

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

# **get_service_queues_count_async**
> Int32Envelope get_service_queues_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get service queues count

Returns the count of service queues for the specified tenant.

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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get service queues count
        api_response = api_instance.get_service_queues_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceQueuesApi->get_service_queues_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->get_service_queues_count_async: %s\n" % e)
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

# **update_service_queue_async**
> Envelope update_service_queue_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version, service_queue_update_dto=service_queue_update_dto)

Update a service queue

Updates an existing service queue.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_queue_update_dto import ServiceQueueUpdateDto
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
    api_instance = openapi_client.ServiceQueuesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_queue_id = 'service_queue_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_queue_update_dto = openapi_client.ServiceQueueUpdateDto() # ServiceQueueUpdateDto |  (optional)

    try:
        # Update a service queue
        api_response = api_instance.update_service_queue_async(tenant_id, service_queue_id, api_version=api_version, x_api_version=x_api_version, service_queue_update_dto=service_queue_update_dto)
        print("The response of ServiceQueuesApi->update_service_queue_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQueuesApi->update_service_queue_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_queue_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_queue_update_dto** | [**ServiceQueueUpdateDto**](ServiceQueueUpdateDto.md)|  | [optional] 

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

