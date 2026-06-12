# openapi_client.PortsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_port_async**](PortsApi.md#create_port_async) | **POST** /api/v2/LogisticsService/Ports | Create a port
[**delete_port_async**](PortsApi.md#delete_port_async) | **DELETE** /api/v2/LogisticsService/Ports/{portId} | Delete a port
[**get_port_by_id_async**](PortsApi.md#get_port_by_id_async) | **GET** /api/v2/LogisticsService/Ports/{portId} | Get port by ID
[**get_ports_async**](PortsApi.md#get_ports_async) | **GET** /api/v2/LogisticsService/Ports | Get all ports
[**get_ports_count_async**](PortsApi.md#get_ports_count_async) | **GET** /api/v2/LogisticsService/Ports/Count | Get ports count
[**patch_port_async**](PortsApi.md#patch_port_async) | **PATCH** /api/v2/LogisticsService/Ports/{portId} | Patch a port
[**update_port_async**](PortsApi.md#update_port_async) | **PUT** /api/v2/LogisticsService/Ports/{portId} | Update a port


# **create_port_async**
> EmptyEnvelope create_port_async(tenant_id, api_version=api_version, x_api_version=x_api_version, port_create_dto=port_create_dto)

Create a port

Creates a new port for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.port_create_dto import PortCreateDto
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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    port_create_dto = openapi_client.PortCreateDto() # PortCreateDto |  (optional)

    try:
        # Create a port
        api_response = api_instance.create_port_async(tenant_id, api_version=api_version, x_api_version=x_api_version, port_create_dto=port_create_dto)
        print("The response of PortsApi->create_port_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->create_port_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **port_create_dto** | [**PortCreateDto**](PortCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_async**
> EmptyEnvelope delete_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version)

Delete a port

Deletes a port.

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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    port_id = 'port_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a port
        api_response = api_instance.delete_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortsApi->delete_port_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->delete_port_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **port_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_by_id_async**
> PortDtoEnvelope get_port_by_id_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version)

Get port by ID

Retrieves a specific port by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.port_dto_envelope import PortDtoEnvelope
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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    port_id = 'port_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get port by ID
        api_response = api_instance.get_port_by_id_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortsApi->get_port_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_port_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **port_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PortDtoEnvelope**](PortDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ports_async**
> PortDtoListEnvelope get_ports_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all ports

Retrieves all ports for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.port_dto_list_envelope import PortDtoListEnvelope
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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all ports
        api_response = api_instance.get_ports_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortsApi->get_ports_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_ports_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PortDtoListEnvelope**](PortDtoListEnvelope.md)

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

# **get_ports_count_async**
> Int32Envelope get_ports_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get ports count

Returns the count of ports for the specified tenant.

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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get ports count
        api_response = api_instance.get_ports_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortsApi->get_ports_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_ports_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_port_async**
> EmptyEnvelope patch_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a port

Partially updates an existing port using JSON Patch.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    port_id = 'port_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a port
        api_response = api_instance.patch_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of PortsApi->patch_port_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->patch_port_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **port_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_port_async**
> EmptyEnvelope update_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version, port_update_dto=port_update_dto)

Update a port

Updates an existing port.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.port_update_dto import PortUpdateDto
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
    api_instance = openapi_client.PortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    port_id = 'port_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    port_update_dto = openapi_client.PortUpdateDto() # PortUpdateDto |  (optional)

    try:
        # Update a port
        api_response = api_instance.update_port_async(tenant_id, port_id, api_version=api_version, x_api_version=x_api_version, port_update_dto=port_update_dto)
        print("The response of PortsApi->update_port_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->update_port_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **port_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **port_update_dto** | [**PortUpdateDto**](PortUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

