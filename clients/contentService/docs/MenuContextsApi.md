# openapi_client.MenuContextsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_menu_contexts_async**](MenuContextsApi.md#count_menu_contexts_async) | **GET** /api/v2/ContentService/MenuContexts/Count | Count menu contexts
[**create_menu_context_async**](MenuContextsApi.md#create_menu_context_async) | **POST** /api/v2/ContentService/MenuContexts | Create a menu context
[**delete_menu_context_async**](MenuContextsApi.md#delete_menu_context_async) | **DELETE** /api/v2/ContentService/MenuContexts/{menuContextId} | Delete a menu context
[**get_menu_context_by_id_async**](MenuContextsApi.md#get_menu_context_by_id_async) | **GET** /api/v2/ContentService/MenuContexts/{menuContextId} | Get menu context by ID
[**get_menu_contexts_async**](MenuContextsApi.md#get_menu_contexts_async) | **GET** /api/v2/ContentService/MenuContexts | Get menu contexts
[**update_menu_context_async**](MenuContextsApi.md#update_menu_context_async) | **PUT** /api/v2/ContentService/MenuContexts/{menuContextId} | Update a menu context


# **count_menu_contexts_async**
> Int32Envelope count_menu_contexts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count menu contexts

Counts all menu contexts for the specified tenant.

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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count menu contexts
        api_response = api_instance.count_menu_contexts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->count_menu_contexts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->count_menu_contexts_async: %s\n" % e)
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

# **create_menu_context_async**
> EmptyEnvelope create_menu_context_async(tenant_id, menu_context_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a menu context

Creates a new menu context for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.menu_context_create_dto import MenuContextCreateDto
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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    menu_context_create_dto = openapi_client.MenuContextCreateDto() # MenuContextCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a menu context
        api_response = api_instance.create_menu_context_async(tenant_id, menu_context_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->create_menu_context_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->create_menu_context_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **menu_context_create_dto** | [**MenuContextCreateDto**](MenuContextCreateDto.md)|  | 
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

# **delete_menu_context_async**
> EmptyEnvelope delete_menu_context_async(tenant_id, menu_context_id, api_version=api_version, x_api_version=x_api_version)

Delete a menu context

Deletes a menu context for the specified tenant.

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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    menu_context_id = 'menu_context_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a menu context
        api_response = api_instance.delete_menu_context_async(tenant_id, menu_context_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->delete_menu_context_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->delete_menu_context_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **menu_context_id** | **str**|  | 
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

# **get_menu_context_by_id_async**
> MenuContextDtoEnvelope get_menu_context_by_id_async(tenant_id, menu_context_id, api_version=api_version, x_api_version=x_api_version)

Get menu context by ID

Retrieves a specific menu context by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.menu_context_dto_envelope import MenuContextDtoEnvelope
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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    menu_context_id = 'menu_context_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get menu context by ID
        api_response = api_instance.get_menu_context_by_id_async(tenant_id, menu_context_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->get_menu_context_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->get_menu_context_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **menu_context_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MenuContextDtoEnvelope**](MenuContextDtoEnvelope.md)

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

# **get_menu_contexts_async**
> MenuContextDtoListEnvelope get_menu_contexts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get menu contexts

Retrieves all menu contexts for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.menu_context_dto_list_envelope import MenuContextDtoListEnvelope
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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get menu contexts
        api_response = api_instance.get_menu_contexts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->get_menu_contexts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->get_menu_contexts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MenuContextDtoListEnvelope**](MenuContextDtoListEnvelope.md)

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

# **update_menu_context_async**
> EmptyEnvelope update_menu_context_async(tenant_id, menu_context_id, menu_context_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a menu context

Updates an existing menu context for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.menu_context_update_dto import MenuContextUpdateDto
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
    api_instance = openapi_client.MenuContextsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    menu_context_id = 'menu_context_id_example' # str | 
    menu_context_update_dto = openapi_client.MenuContextUpdateDto() # MenuContextUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a menu context
        api_response = api_instance.update_menu_context_async(tenant_id, menu_context_id, menu_context_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MenuContextsApi->update_menu_context_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuContextsApi->update_menu_context_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **menu_context_id** | **str**|  | 
 **menu_context_update_dto** | [**MenuContextUpdateDto**](MenuContextUpdateDto.md)|  | 
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

