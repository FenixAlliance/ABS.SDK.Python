# openapi_client.BlogPostTagsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_blog_post_tags_async**](BlogPostTagsApi.md#count_blog_post_tags_async) | **GET** /api/v2/ContentService/BlogPostTags/Count | Count blog post tags
[**create_blog_post_tag_async**](BlogPostTagsApi.md#create_blog_post_tag_async) | **POST** /api/v2/ContentService/BlogPostTags | Create a blog post tag
[**delete_blog_post_tag_async**](BlogPostTagsApi.md#delete_blog_post_tag_async) | **DELETE** /api/v2/ContentService/BlogPostTags/{blogPostTagId} | Delete a blog post tag
[**get_blog_post_tag_by_id_async**](BlogPostTagsApi.md#get_blog_post_tag_by_id_async) | **GET** /api/v2/ContentService/BlogPostTags/{blogPostTagId} | Get blog post tag by ID
[**get_blog_post_tags_async**](BlogPostTagsApi.md#get_blog_post_tags_async) | **GET** /api/v2/ContentService/BlogPostTags | Get blog post tags
[**update_blog_post_tag_async**](BlogPostTagsApi.md#update_blog_post_tag_async) | **PUT** /api/v2/ContentService/BlogPostTags/{blogPostTagId} | Update a blog post tag


# **count_blog_post_tags_async**
> Int32Envelope count_blog_post_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count blog post tags

Counts all blog post tags for the specified tenant.

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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count blog post tags
        api_response = api_instance.count_blog_post_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostTagsApi->count_blog_post_tags_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->count_blog_post_tags_async: %s\n" % e)
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

# **create_blog_post_tag_async**
> EmptyEnvelope create_blog_post_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blog_post_tag_create_dto=blog_post_tag_create_dto)

Create a blog post tag

Creates a new blog post tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_tag_create_dto import BlogPostTagCreateDto
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blog_post_tag_create_dto = openapi_client.BlogPostTagCreateDto() # BlogPostTagCreateDto |  (optional)

    try:
        # Create a blog post tag
        api_response = api_instance.create_blog_post_tag_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blog_post_tag_create_dto=blog_post_tag_create_dto)
        print("The response of BlogPostTagsApi->create_blog_post_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->create_blog_post_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blog_post_tag_create_dto** | [**BlogPostTagCreateDto**](BlogPostTagCreateDto.md)|  | [optional] 

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

# **delete_blog_post_tag_async**
> EmptyEnvelope delete_blog_post_tag_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version)

Delete a blog post tag

Deletes a blog post tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_tag_id = 'blog_post_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a blog post tag
        api_response = api_instance.delete_blog_post_tag_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostTagsApi->delete_blog_post_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->delete_blog_post_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_tag_id** | **str**|  | 
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

# **get_blog_post_tag_by_id_async**
> BlogPostTagDtoEnvelope get_blog_post_tag_by_id_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version)

Get blog post tag by ID

Retrieves a specific blog post tag by its ID.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_tag_dto_envelope import BlogPostTagDtoEnvelope
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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_tag_id = 'blog_post_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog post tag by ID
        api_response = api_instance.get_blog_post_tag_by_id_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostTagsApi->get_blog_post_tag_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->get_blog_post_tag_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogPostTagDtoEnvelope**](BlogPostTagDtoEnvelope.md)

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

# **get_blog_post_tags_async**
> BlogPostTagDtoListEnvelope get_blog_post_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get blog post tags

Retrieves all blog post tags for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_tag_dto_list_envelope import BlogPostTagDtoListEnvelope
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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog post tags
        api_response = api_instance.get_blog_post_tags_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostTagsApi->get_blog_post_tags_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->get_blog_post_tags_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogPostTagDtoListEnvelope**](BlogPostTagDtoListEnvelope.md)

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

# **update_blog_post_tag_async**
> EmptyEnvelope update_blog_post_tag_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version, blog_post_tag_update_dto=blog_post_tag_update_dto)

Update a blog post tag

Updates an existing blog post tag for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_tag_update_dto import BlogPostTagUpdateDto
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.BlogPostTagsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_tag_id = 'blog_post_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blog_post_tag_update_dto = openapi_client.BlogPostTagUpdateDto() # BlogPostTagUpdateDto |  (optional)

    try:
        # Update a blog post tag
        api_response = api_instance.update_blog_post_tag_async(tenant_id, blog_post_tag_id, api_version=api_version, x_api_version=x_api_version, blog_post_tag_update_dto=blog_post_tag_update_dto)
        print("The response of BlogPostTagsApi->update_blog_post_tag_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostTagsApi->update_blog_post_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blog_post_tag_update_dto** | [**BlogPostTagUpdateDto**](BlogPostTagUpdateDto.md)|  | [optional] 

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

