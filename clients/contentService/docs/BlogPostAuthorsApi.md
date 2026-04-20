# openapi_client.BlogPostAuthorsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_blog_posts_by_author_async**](BlogPostAuthorsApi.md#count_blog_posts_by_author_async) | **GET** /api/v2/ContentService/BlogPostAuthors/{authorId}/BlogPosts/Count | Count blog posts by author
[**get_blog_author_by_id_async**](BlogPostAuthorsApi.md#get_blog_author_by_id_async) | **GET** /api/v2/ContentService/BlogPostAuthors/{authorId} | Get blog author by ID
[**get_blog_authors_async**](BlogPostAuthorsApi.md#get_blog_authors_async) | **GET** /api/v2/ContentService/BlogPostAuthors | Get blog authors
[**get_blog_posts_by_author_async**](BlogPostAuthorsApi.md#get_blog_posts_by_author_async) | **GET** /api/v2/ContentService/BlogPostAuthors/{authorId}/BlogPosts | Get blog posts by author


# **count_blog_posts_by_author_async**
> Int32Envelope count_blog_posts_by_author_async(author_id, api_version=api_version, x_api_version=x_api_version)

Count blog posts by author

Returns the count of blog posts written by a specific author.

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
    api_instance = openapi_client.BlogPostAuthorsApi(api_client)
    author_id = 'author_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count blog posts by author
        api_response = api_instance.count_blog_posts_by_author_async(author_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostAuthorsApi->count_blog_posts_by_author_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostAuthorsApi->count_blog_posts_by_author_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**|  | 
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

# **get_blog_author_by_id_async**
> BlogAuthorDtoEnvelope get_blog_author_by_id_async(author_id, api_version=api_version, x_api_version=x_api_version)

Get blog author by ID

Retrieves a specific blog author by their identifier.

### Example


```python
import openapi_client
from openapi_client.models.blog_author_dto_envelope import BlogAuthorDtoEnvelope
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
    api_instance = openapi_client.BlogPostAuthorsApi(api_client)
    author_id = 'author_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog author by ID
        api_response = api_instance.get_blog_author_by_id_async(author_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostAuthorsApi->get_blog_author_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostAuthorsApi->get_blog_author_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogAuthorDtoEnvelope**](BlogAuthorDtoEnvelope.md)

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

# **get_blog_authors_async**
> BlogAuthorDtoListEnvelope get_blog_authors_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get blog authors

Retrieves all blog authors, optionally filtered by tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_author_dto_list_envelope import BlogAuthorDtoListEnvelope
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
    api_instance = openapi_client.BlogPostAuthorsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog authors
        api_response = api_instance.get_blog_authors_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostAuthorsApi->get_blog_authors_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostAuthorsApi->get_blog_authors_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogAuthorDtoListEnvelope**](BlogAuthorDtoListEnvelope.md)

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

# **get_blog_posts_by_author_async**
> BlogPostDtoListEnvelope get_blog_posts_by_author_async(author_id, api_version=api_version, x_api_version=x_api_version)

Get blog posts by author

Retrieves all blog posts written by a specific author.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_dto_list_envelope import BlogPostDtoListEnvelope
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
    api_instance = openapi_client.BlogPostAuthorsApi(api_client)
    author_id = 'author_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog posts by author
        api_response = api_instance.get_blog_posts_by_author_async(author_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostAuthorsApi->get_blog_posts_by_author_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostAuthorsApi->get_blog_posts_by_author_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogPostDtoListEnvelope**](BlogPostDtoListEnvelope.md)

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

