# openapi_client.ServiceLevelsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_all_service_levels_async**](ServiceLevelsApi.md#count_all_service_levels_async) | **GET** /api/v2/ServicesService/ServiceLevels/Count | Get all service levels count
[**create_service_level_async**](ServiceLevelsApi.md#create_service_level_async) | **POST** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels | Create a service level
[**delete_service_level_async**](ServiceLevelsApi.md#delete_service_level_async) | **DELETE** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels/{serviceLevelId} | Delete a service level
[**get_all_service_levels_async**](ServiceLevelsApi.md#get_all_service_levels_async) | **GET** /api/v2/ServicesService/ServiceLevels | Get all service levels
[**get_service_level_by_id_async**](ServiceLevelsApi.md#get_service_level_by_id_async) | **GET** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels/{serviceLevelId} | Get a service level by ID
[**get_service_levels_async**](ServiceLevelsApi.md#get_service_levels_async) | **GET** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels | Get all service levels
[**get_service_levels_count_async**](ServiceLevelsApi.md#get_service_levels_count_async) | **GET** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels/Count | Get service levels count
[**update_service_level_async**](ServiceLevelsApi.md#update_service_level_async) | **PUT** /api/v2/ServicesService/Services/{serviceId}/ServiceLevels/{serviceLevelId} | Update a service level


# **count_all_service_levels_async**
> Int32Envelope count_all_service_levels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service levels count

Returns the count of all service levels for the specified tenant.

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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service levels count
        api_response = api_instance.count_all_service_levels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->count_all_service_levels_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->count_all_service_levels_async: %s\n" % e)
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

# **create_service_level_async**
> Envelope create_service_level_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version, service_level_create_dto=service_level_create_dto)

Create a service level

Creates a new service level for the specified service.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_level_create_dto import ServiceLevelCreateDto
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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_level_create_dto = openapi_client.ServiceLevelCreateDto() # ServiceLevelCreateDto |  (optional)

    try:
        # Create a service level
        api_response = api_instance.create_service_level_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version, service_level_create_dto=service_level_create_dto)
        print("The response of ServiceLevelsApi->create_service_level_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->create_service_level_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_level_create_dto** | [**ServiceLevelCreateDto**](ServiceLevelCreateDto.md)|  | [optional] 

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

# **delete_service_level_async**
> Envelope delete_service_level_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version)

Delete a service level

Deletes a service level by its identifier.

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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    service_level_id = 'service_level_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service level
        api_response = api_instance.delete_service_level_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->delete_service_level_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->delete_service_level_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **service_level_id** | **str**|  | 
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

# **get_all_service_levels_async**
> ServiceLevelDtoIReadOnlyListEnvelope get_all_service_levels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service levels

Retrieves all service levels for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_level_dto_i_read_only_list_envelope import ServiceLevelDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service levels
        api_response = api_instance.get_all_service_levels_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->get_all_service_levels_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->get_all_service_levels_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceLevelDtoIReadOnlyListEnvelope**](ServiceLevelDtoIReadOnlyListEnvelope.md)

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

# **get_service_level_by_id_async**
> ServiceLevelDtoEnvelope get_service_level_by_id_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version)

Get a service level by ID

Retrieves a service level by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_level_dto_envelope import ServiceLevelDtoEnvelope
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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    service_level_id = 'service_level_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service level by ID
        api_response = api_instance.get_service_level_by_id_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->get_service_level_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->get_service_level_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **service_level_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceLevelDtoEnvelope**](ServiceLevelDtoEnvelope.md)

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

# **get_service_levels_async**
> ServiceLevelDtoIReadOnlyListEnvelope get_service_levels_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)

Get all service levels

Retrieves all service levels for the specified service.

### Example


```python
import openapi_client
from openapi_client.models.service_level_dto_i_read_only_list_envelope import ServiceLevelDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service levels
        api_response = api_instance.get_service_levels_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->get_service_levels_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->get_service_levels_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceLevelDtoIReadOnlyListEnvelope**](ServiceLevelDtoIReadOnlyListEnvelope.md)

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

# **get_service_levels_count_async**
> Int32Envelope get_service_levels_count_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)

Get service levels count

Returns the count of service levels for the specified service.

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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get service levels count
        api_response = api_instance.get_service_levels_count_async(tenant_id, service_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelsApi->get_service_levels_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->get_service_levels_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
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

# **update_service_level_async**
> Envelope update_service_level_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version, service_level_update_dto=service_level_update_dto)

Update a service level

Updates an existing service level.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_level_update_dto import ServiceLevelUpdateDto
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
    api_instance = openapi_client.ServiceLevelsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_id = 'service_id_example' # str | 
    service_level_id = 'service_level_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_level_update_dto = openapi_client.ServiceLevelUpdateDto() # ServiceLevelUpdateDto |  (optional)

    try:
        # Update a service level
        api_response = api_instance.update_service_level_async(tenant_id, service_id, service_level_id, api_version=api_version, x_api_version=x_api_version, service_level_update_dto=service_level_update_dto)
        print("The response of ServiceLevelsApi->update_service_level_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelsApi->update_service_level_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_id** | **str**|  | 
 **service_level_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_level_update_dto** | [**ServiceLevelUpdateDto**](ServiceLevelUpdateDto.md)|  | [optional] 

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

