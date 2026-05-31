# openapi_client.VoyagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_voyage_async**](VoyagesApi.md#cancel_voyage_async) | **POST** /api/v2/LogisticsService/Voyages/{voyageId}/Cancel | Cancel a voyage
[**complete_voyage_async**](VoyagesApi.md#complete_voyage_async) | **POST** /api/v2/LogisticsService/Voyages/{voyageId}/Complete | Complete a voyage
[**create_voyage_async**](VoyagesApi.md#create_voyage_async) | **POST** /api/v2/LogisticsService/Voyages | Create a voyage
[**create_voyage_port_call_async**](VoyagesApi.md#create_voyage_port_call_async) | **POST** /api/v2/LogisticsService/Voyages/{voyageId}/PortCalls | Create a port call
[**delete_voyage_async**](VoyagesApi.md#delete_voyage_async) | **DELETE** /api/v2/LogisticsService/Voyages/{voyageId} | Delete a voyage
[**delete_voyage_port_call_async**](VoyagesApi.md#delete_voyage_port_call_async) | **DELETE** /api/v2/LogisticsService/Voyages/{voyageId}/PortCalls/{portCallId} | Delete a port call
[**get_voyage_by_id_async**](VoyagesApi.md#get_voyage_by_id_async) | **GET** /api/v2/LogisticsService/Voyages/{voyageId} | Get voyage by ID
[**get_voyage_port_calls_async**](VoyagesApi.md#get_voyage_port_calls_async) | **GET** /api/v2/LogisticsService/Voyages/{voyageId}/PortCalls | Get voyage port calls
[**get_voyage_port_calls_count_async**](VoyagesApi.md#get_voyage_port_calls_count_async) | **GET** /api/v2/LogisticsService/Voyages/{voyageId}/PortCalls/Count | Get voyage port calls count
[**get_voyages_async**](VoyagesApi.md#get_voyages_async) | **GET** /api/v2/LogisticsService/Voyages | Get all voyages
[**get_voyages_count_async**](VoyagesApi.md#get_voyages_count_async) | **GET** /api/v2/LogisticsService/Voyages/Count | Get voyages count
[**start_voyage_async**](VoyagesApi.md#start_voyage_async) | **POST** /api/v2/LogisticsService/Voyages/{voyageId}/Start | Start a voyage
[**update_voyage_async**](VoyagesApi.md#update_voyage_async) | **PUT** /api/v2/LogisticsService/Voyages/{voyageId} | Update a voyage
[**update_voyage_port_call_async**](VoyagesApi.md#update_voyage_port_call_async) | **PUT** /api/v2/LogisticsService/Voyages/{voyageId}/PortCalls/{portCallId} | Update a port call


# **cancel_voyage_async**
> EmptyEnvelope cancel_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Cancel a voyage

Cancels a voyage.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel a voyage
        api_response = api_instance.cancel_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->cancel_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->cancel_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_voyage_async**
> EmptyEnvelope complete_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Complete a voyage

Marks a voyage as completed.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Complete a voyage
        api_response = api_instance.complete_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->complete_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->complete_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_voyage_async**
> EmptyEnvelope create_voyage_async(tenant_id, api_version=api_version, x_api_version=x_api_version, voyage_create_dto=voyage_create_dto)

Create a voyage

Creates a new voyage for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.voyage_create_dto import VoyageCreateDto
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    voyage_create_dto = openapi_client.VoyageCreateDto() # VoyageCreateDto |  (optional)

    try:
        # Create a voyage
        api_response = api_instance.create_voyage_async(tenant_id, api_version=api_version, x_api_version=x_api_version, voyage_create_dto=voyage_create_dto)
        print("The response of VoyagesApi->create_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->create_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **voyage_create_dto** | [**VoyageCreateDto**](VoyageCreateDto.md)|  | [optional] 

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

# **create_voyage_port_call_async**
> EmptyEnvelope create_voyage_port_call_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version, voyage_port_call_create_dto=voyage_port_call_create_dto)

Create a port call

Creates a new port call for a voyage.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.voyage_port_call_create_dto import VoyagePortCallCreateDto
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    voyage_port_call_create_dto = openapi_client.VoyagePortCallCreateDto() # VoyagePortCallCreateDto |  (optional)

    try:
        # Create a port call
        api_response = api_instance.create_voyage_port_call_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version, voyage_port_call_create_dto=voyage_port_call_create_dto)
        print("The response of VoyagesApi->create_voyage_port_call_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->create_voyage_port_call_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **voyage_port_call_create_dto** | [**VoyagePortCallCreateDto**](VoyagePortCallCreateDto.md)|  | [optional] 

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

# **delete_voyage_async**
> EmptyEnvelope delete_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Delete a voyage

Deletes a voyage.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a voyage
        api_response = api_instance.delete_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->delete_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->delete_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
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

# **delete_voyage_port_call_async**
> EmptyEnvelope delete_voyage_port_call_async(tenant_id, voyage_id, port_call_id, api_version=api_version, x_api_version=x_api_version)

Delete a port call

Deletes a port call.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    port_call_id = 'port_call_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a port call
        api_response = api_instance.delete_voyage_port_call_async(tenant_id, voyage_id, port_call_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->delete_voyage_port_call_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->delete_voyage_port_call_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **port_call_id** | **str**|  | 
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

# **get_voyage_by_id_async**
> VoyageDtoEnvelope get_voyage_by_id_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Get voyage by ID

Retrieves a specific voyage by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.voyage_dto_envelope import VoyageDtoEnvelope
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get voyage by ID
        api_response = api_instance.get_voyage_by_id_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->get_voyage_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->get_voyage_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**VoyageDtoEnvelope**](VoyageDtoEnvelope.md)

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

# **get_voyage_port_calls_async**
> VoyagePortCallDtoListEnvelope get_voyage_port_calls_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Get voyage port calls

Retrieves all port calls for a specific voyage.

### Example


```python
import openapi_client
from openapi_client.models.voyage_port_call_dto_list_envelope import VoyagePortCallDtoListEnvelope
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get voyage port calls
        api_response = api_instance.get_voyage_port_calls_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->get_voyage_port_calls_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->get_voyage_port_calls_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**VoyagePortCallDtoListEnvelope**](VoyagePortCallDtoListEnvelope.md)

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

# **get_voyage_port_calls_count_async**
> Int32Envelope get_voyage_port_calls_count_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Get voyage port calls count

Returns the count of port calls for a specific voyage.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get voyage port calls count
        api_response = api_instance.get_voyage_port_calls_count_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->get_voyage_port_calls_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->get_voyage_port_calls_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
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

# **get_voyages_async**
> VoyageDtoListEnvelope get_voyages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all voyages

Retrieves all voyages for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.voyage_dto_list_envelope import VoyageDtoListEnvelope
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all voyages
        api_response = api_instance.get_voyages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->get_voyages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->get_voyages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**VoyageDtoListEnvelope**](VoyageDtoListEnvelope.md)

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

# **get_voyages_count_async**
> Int32Envelope get_voyages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get voyages count

Returns the count of voyages for the specified tenant.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get voyages count
        api_response = api_instance.get_voyages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->get_voyages_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->get_voyages_count_async: %s\n" % e)
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

# **start_voyage_async**
> EmptyEnvelope start_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)

Start a voyage

Starts a voyage.

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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Start a voyage
        api_response = api_instance.start_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of VoyagesApi->start_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->start_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_voyage_async**
> EmptyEnvelope update_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version, voyage_update_dto=voyage_update_dto)

Update a voyage

Updates an existing voyage.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.voyage_update_dto import VoyageUpdateDto
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    voyage_update_dto = openapi_client.VoyageUpdateDto() # VoyageUpdateDto |  (optional)

    try:
        # Update a voyage
        api_response = api_instance.update_voyage_async(tenant_id, voyage_id, api_version=api_version, x_api_version=x_api_version, voyage_update_dto=voyage_update_dto)
        print("The response of VoyagesApi->update_voyage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->update_voyage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **voyage_update_dto** | [**VoyageUpdateDto**](VoyageUpdateDto.md)|  | [optional] 

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

# **update_voyage_port_call_async**
> EmptyEnvelope update_voyage_port_call_async(tenant_id, voyage_id, port_call_id, api_version=api_version, x_api_version=x_api_version, voyage_port_call_update_dto=voyage_port_call_update_dto)

Update a port call

Updates an existing port call.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.voyage_port_call_update_dto import VoyagePortCallUpdateDto
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
    api_instance = openapi_client.VoyagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    voyage_id = 'voyage_id_example' # str | 
    port_call_id = 'port_call_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    voyage_port_call_update_dto = openapi_client.VoyagePortCallUpdateDto() # VoyagePortCallUpdateDto |  (optional)

    try:
        # Update a port call
        api_response = api_instance.update_voyage_port_call_async(tenant_id, voyage_id, port_call_id, api_version=api_version, x_api_version=x_api_version, voyage_port_call_update_dto=voyage_port_call_update_dto)
        print("The response of VoyagesApi->update_voyage_port_call_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoyagesApi->update_voyage_port_call_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **voyage_id** | **str**|  | 
 **port_call_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **voyage_port_call_update_dto** | [**VoyagePortCallUpdateDto**](VoyagePortCallUpdateDto.md)|  | [optional] 

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

