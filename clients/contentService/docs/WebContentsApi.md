# openapi_client.WebContentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_web_contents_async**](WebContentsApi.md#count_web_contents_async) | **GET** /api/v2/ContentService/WebContents/Count | Count web contents
[**create_web_content_async**](WebContentsApi.md#create_web_content_async) | **POST** /api/v2/ContentService/WebContents | Create a web content
[**delete_web_content_async**](WebContentsApi.md#delete_web_content_async) | **DELETE** /api/v2/ContentService/WebContents/{webContentId} | Delete a web content
[**get_web_content_by_id_async**](WebContentsApi.md#get_web_content_by_id_async) | **GET** /api/v2/ContentService/WebContents/{webContentId} | Get web content by ID
[**get_web_contents_async**](WebContentsApi.md#get_web_contents_async) | **GET** /api/v2/ContentService/WebContents | Get web contents
[**update_web_content_async**](WebContentsApi.md#update_web_content_async) | **PUT** /api/v2/ContentService/WebContents/{webContentId} | Update a web content


# **count_web_contents_async**
> Int32Envelope count_web_contents_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count web contents

Counts all web contents for the specified tenant.

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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count web contents
        api_response = api_instance.count_web_contents_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebContentsApi->count_web_contents_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->count_web_contents_async: %s\n" % e)
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

# **create_web_content_async**
> EmptyEnvelope create_web_content_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_content_create_dto=web_content_create_dto)

Create a web content

Creates a new web content for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_content_create_dto import WebContentCreateDto
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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_content_create_dto = openapi_client.WebContentCreateDto() # WebContentCreateDto |  (optional)

    try:
        # Create a web content
        api_response = api_instance.create_web_content_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_content_create_dto=web_content_create_dto)
        print("The response of WebContentsApi->create_web_content_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->create_web_content_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_content_create_dto** | [**WebContentCreateDto**](WebContentCreateDto.md)|  | [optional] 

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

# **delete_web_content_async**
> EmptyEnvelope delete_web_content_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version)

Delete a web content

Deletes a web content for the specified tenant.

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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_content_id = 'web_content_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web content
        api_response = api_instance.delete_web_content_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebContentsApi->delete_web_content_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->delete_web_content_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_content_id** | **str**|  | 
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

# **get_web_content_by_id_async**
> WebContentDtoEnvelope get_web_content_by_id_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version)

Get web content by ID

Retrieves a specific web content by its ID.

### Example


```python
import openapi_client
from openapi_client.models.web_content_dto_envelope import WebContentDtoEnvelope
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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_content_id = 'web_content_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web content by ID
        api_response = api_instance.get_web_content_by_id_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebContentsApi->get_web_content_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->get_web_content_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_content_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebContentDtoEnvelope**](WebContentDtoEnvelope.md)

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

# **get_web_contents_async**
> WebContentDtoListEnvelope get_web_contents_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web contents

Retrieves all web contents for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_content_dto_list_envelope import WebContentDtoListEnvelope
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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web contents
        api_response = api_instance.get_web_contents_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebContentsApi->get_web_contents_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->get_web_contents_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebContentDtoListEnvelope**](WebContentDtoListEnvelope.md)

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

# **update_web_content_async**
> EmptyEnvelope update_web_content_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version, web_content_update_dto=web_content_update_dto)

Update a web content

Updates an existing web content for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_content_update_dto import WebContentUpdateDto
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
    api_instance = openapi_client.WebContentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_content_id = 'web_content_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_content_update_dto = openapi_client.WebContentUpdateDto() # WebContentUpdateDto |  (optional)

    try:
        # Update a web content
        api_response = api_instance.update_web_content_async(tenant_id, web_content_id, api_version=api_version, x_api_version=x_api_version, web_content_update_dto=web_content_update_dto)
        print("The response of WebContentsApi->update_web_content_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebContentsApi->update_web_content_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_content_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_content_update_dto** | [**WebContentUpdateDto**](WebContentUpdateDto.md)|  | [optional] 

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

