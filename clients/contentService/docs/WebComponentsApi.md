# openapi_client.WebComponentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_web_components_async**](WebComponentsApi.md#count_web_components_async) | **GET** /api/v2/ContentService/WebComponents/Count | Count web components
[**create_web_component_async**](WebComponentsApi.md#create_web_component_async) | **POST** /api/v2/ContentService/WebComponents | Create a web component
[**delete_web_component_async**](WebComponentsApi.md#delete_web_component_async) | **DELETE** /api/v2/ContentService/WebComponents/{webComponentId} | Delete a web component
[**get_web_component_by_id_async**](WebComponentsApi.md#get_web_component_by_id_async) | **GET** /api/v2/ContentService/WebComponents/{webComponentId} | Get web component by ID
[**get_web_components_async**](WebComponentsApi.md#get_web_components_async) | **GET** /api/v2/ContentService/WebComponents | Get web components
[**update_web_component_async**](WebComponentsApi.md#update_web_component_async) | **PUT** /api/v2/ContentService/WebComponents/{webComponentId} | Update a web component


# **count_web_components_async**
> Int32Envelope count_web_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count web components

Counts all web components for the specified tenant.

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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count web components
        api_response = api_instance.count_web_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->count_web_components_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->count_web_components_async: %s\n" % e)
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

# **create_web_component_async**
> EmptyEnvelope create_web_component_async(tenant_id, web_component_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a web component

Creates a new web component for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_component_create_dto import WebComponentCreateDto
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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_component_create_dto = openapi_client.WebComponentCreateDto() # WebComponentCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a web component
        api_response = api_instance.create_web_component_async(tenant_id, web_component_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->create_web_component_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->create_web_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_component_create_dto** | [**WebComponentCreateDto**](WebComponentCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **delete_web_component_async**
> EmptyEnvelope delete_web_component_async(tenant_id, web_component_id, api_version=api_version, x_api_version=x_api_version)

Delete a web component

Deletes a web component for the specified tenant.

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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_component_id = 'web_component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web component
        api_response = api_instance.delete_web_component_async(tenant_id, web_component_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->delete_web_component_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->delete_web_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_component_id** | **str**|  | 
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

# **get_web_component_by_id_async**
> WebComponentDtoEnvelope get_web_component_by_id_async(tenant_id, web_component_id, api_version=api_version, x_api_version=x_api_version)

Get web component by ID

Retrieves a specific web component by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.web_component_dto_envelope import WebComponentDtoEnvelope
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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_component_id = 'web_component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web component by ID
        api_response = api_instance.get_web_component_by_id_async(tenant_id, web_component_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->get_web_component_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->get_web_component_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_component_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebComponentDtoEnvelope**](WebComponentDtoEnvelope.md)

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

# **get_web_components_async**
> WebComponentDtoListEnvelope get_web_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web components

Retrieves all web components for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_component_dto_list_envelope import WebComponentDtoListEnvelope
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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web components
        api_response = api_instance.get_web_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->get_web_components_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->get_web_components_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebComponentDtoListEnvelope**](WebComponentDtoListEnvelope.md)

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

# **update_web_component_async**
> EmptyEnvelope update_web_component_async(tenant_id, web_component_id, web_component_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a web component

Updates an existing web component for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_component_update_dto import WebComponentUpdateDto
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
    api_instance = openapi_client.WebComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_component_id = 'web_component_id_example' # str | 
    web_component_update_dto = openapi_client.WebComponentUpdateDto() # WebComponentUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a web component
        api_response = api_instance.update_web_component_async(tenant_id, web_component_id, web_component_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebComponentsApi->update_web_component_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebComponentsApi->update_web_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_component_id** | **str**|  | 
 **web_component_update_dto** | [**WebComponentUpdateDto**](WebComponentUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

