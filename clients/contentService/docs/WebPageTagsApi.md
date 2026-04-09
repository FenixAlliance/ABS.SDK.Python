# openapi_client.WebPageTagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_page_tag_async**](WebPageTagsApi.md#create_web_page_tag_async) | **POST** /api/v2/ContentService/WebPageTags | Create a web page tag
[**delete_web_page_tag_async**](WebPageTagsApi.md#delete_web_page_tag_async) | **DELETE** /api/v2/ContentService/WebPageTags/{webPageTagId} | Delete a web page tag
[**get_web_page_tag_by_id_async**](WebPageTagsApi.md#get_web_page_tag_by_id_async) | **GET** /api/v2/ContentService/WebPageTags/{webPageTagId} | Get web page tag by ID
[**get_web_page_tags_async**](WebPageTagsApi.md#get_web_page_tags_async) | **GET** /api/v2/ContentService/WebPageTags | Get web page tags
[**update_web_page_tag_async**](WebPageTagsApi.md#update_web_page_tag_async) | **PUT** /api/v2/ContentService/WebPageTags/{webPageTagId} | Update a web page tag


# **create_web_page_tag_async**
> EmptyEnvelope create_web_page_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_create_dto=web_page_tag_create_dto)

Create a web page tag

Creates a new web page tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_page_tag_create_dto import WebPageTagCreateDto
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
    api_instance = openapi_client.WebPageTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_tag_create_dto = openapi_client.WebPageTagCreateDto() # WebPageTagCreateDto |  (optional)

    try:
        # Create a web page tag
        api_response = api_instance.create_web_page_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_create_dto=web_page_tag_create_dto)
        print("The response of WebPageTagsApi->create_web_page_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageTagsApi->create_web_page_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_tag_create_dto** | [**WebPageTagCreateDto**](WebPageTagCreateDto.md)|  | [optional] 

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

# **delete_web_page_tag_async**
> EmptyEnvelope delete_web_page_tag_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version)

Delete a web page tag

Deletes a web page tag for the specified tenant.

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
    api_instance = openapi_client.WebPageTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_tag_id = 'web_page_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web page tag
        api_response = api_instance.delete_web_page_tag_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageTagsApi->delete_web_page_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageTagsApi->delete_web_page_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_tag_id** | **str**|  | 
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

# **get_web_page_tag_by_id_async**
> WebPageTagDtoEnvelope get_web_page_tag_by_id_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version)

Get web page tag by ID

Retrieves a specific web page tag by its ID.

### Example


```python
import openapi_client
from openapi_client.models.web_page_tag_dto_envelope import WebPageTagDtoEnvelope
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
    api_instance = openapi_client.WebPageTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_tag_id = 'web_page_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web page tag by ID
        api_response = api_instance.get_web_page_tag_by_id_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageTagsApi->get_web_page_tag_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageTagsApi->get_web_page_tag_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageTagDtoEnvelope**](WebPageTagDtoEnvelope.md)

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

# **get_web_page_tags_async**
> WebPageTagDtoListEnvelope get_web_page_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web page tags

Retrieves all web page tags for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_page_tag_dto_list_envelope import WebPageTagDtoListEnvelope
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
    api_instance = openapi_client.WebPageTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web page tags
        api_response = api_instance.get_web_page_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageTagsApi->get_web_page_tags_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageTagsApi->get_web_page_tags_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageTagDtoListEnvelope**](WebPageTagDtoListEnvelope.md)

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

# **update_web_page_tag_async**
> EmptyEnvelope update_web_page_tag_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_update_dto=web_page_tag_update_dto)

Update a web page tag

Updates an existing web page tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_page_tag_update_dto import WebPageTagUpdateDto
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
    api_instance = openapi_client.WebPageTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_tag_id = 'web_page_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_tag_update_dto = openapi_client.WebPageTagUpdateDto() # WebPageTagUpdateDto |  (optional)

    try:
        # Update a web page tag
        api_response = api_instance.update_web_page_tag_async(tenant_id, web_page_tag_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_update_dto=web_page_tag_update_dto)
        print("The response of WebPageTagsApi->update_web_page_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageTagsApi->update_web_page_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_tag_update_dto** | [**WebPageTagUpdateDto**](WebPageTagUpdateDto.md)|  | [optional] 

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

