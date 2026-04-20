# openapi_client.BlogPostsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blog_post_async**](BlogPostsApi.md#create_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts | Create a new blog post
[**create_category_for_blog_post_async**](BlogPostsApi.md#create_category_for_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Categories | Create a category for a blog post
[**create_comment_for_blog_post_async**](BlogPostsApi.md#create_comment_for_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Comments | Create a comment for a blog post
[**create_tag_for_blog_post_async**](BlogPostsApi.md#create_tag_for_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Tags | Create a tag for a blog post
[**delete_blog_post_async**](BlogPostsApi.md#delete_blog_post_async) | **DELETE** /api/v2/ContentService/BlogPosts/{blogPostId} | Delete a blog post
[**delete_comment_from_blog_post_async**](BlogPostsApi.md#delete_comment_from_blog_post_async) | **DELETE** /api/v2/ContentService/BlogPosts/{blogPostId}/Comments/{commentId} | Delete a blog post comment
[**get_blog_post_by_id_async**](BlogPostsApi.md#get_blog_post_by_id_async) | **GET** /api/v2/ContentService/BlogPosts/{blogPostId} | Get a blog post by ID
[**get_blog_posts_async**](BlogPostsApi.md#get_blog_posts_async) | **GET** /api/v2/ContentService/BlogPosts | Retrieve a list of blog posts
[**get_blog_posts_count_async**](BlogPostsApi.md#get_blog_posts_count_async) | **GET** /api/v2/ContentService/BlogPosts/Count | Get the count of blog posts
[**get_categories_for_blog_post_async**](BlogPostsApi.md#get_categories_for_blog_post_async) | **GET** /api/v2/ContentService/BlogPosts/{blogPostId}/Categories | Get categories for a blog post
[**get_comments_for_blog_post_async**](BlogPostsApi.md#get_comments_for_blog_post_async) | **GET** /api/v2/ContentService/BlogPosts/{blogPostId}/Comments | Get comments for a blog post
[**get_replies_for_comment_async**](BlogPostsApi.md#get_replies_for_comment_async) | **GET** /api/v2/ContentService/BlogPosts/{blogPostId}/Comments/{commentId}/Replies | Get replies for a comment
[**get_tags_for_blog_post_async**](BlogPostsApi.md#get_tags_for_blog_post_async) | **GET** /api/v2/ContentService/BlogPosts/{blogPostId}/Tags | Get tags for a blog post
[**relate_category_to_blog_post_async**](BlogPostsApi.md#relate_category_to_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Categories/{categoryId} | Relate an existing category to a blog post
[**relate_tag_to_blog_post_async**](BlogPostsApi.md#relate_tag_to_blog_post_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Tags/{tagId} | Relate an existing tag to a blog post
[**reply_to_comment_async**](BlogPostsApi.md#reply_to_comment_async) | **POST** /api/v2/ContentService/BlogPosts/{blogPostId}/Comments/{commentId}/Reply | Reply to a blog post comment
[**unrelate_category_from_blog_post_async**](BlogPostsApi.md#unrelate_category_from_blog_post_async) | **DELETE** /api/v2/ContentService/BlogPosts/{blogPostId}/Categories/{categoryId} | Remove a category from a blog post
[**unrelate_tag_from_blog_post_async**](BlogPostsApi.md#unrelate_tag_from_blog_post_async) | **DELETE** /api/v2/ContentService/BlogPosts/{blogPostId}/Tags/{tagId} | Remove a tag from a blog post
[**update_blog_post_async**](BlogPostsApi.md#update_blog_post_async) | **PUT** /api/v2/ContentService/BlogPosts/{blogPostId} | Update a blog post


# **create_blog_post_async**
> EmptyEnvelope create_blog_post_async(tenant_id, blog_post_create_dto=blog_post_create_dto)

Create a new blog post

Creates a new blog post for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_create_dto import BlogPostCreateDto
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_create_dto = openapi_client.BlogPostCreateDto() # BlogPostCreateDto |  (optional)

    try:
        # Create a new blog post
        api_response = api_instance.create_blog_post_async(tenant_id, blog_post_create_dto=blog_post_create_dto)
        print("The response of BlogPostsApi->create_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->create_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_create_dto** | [**BlogPostCreateDto**](BlogPostCreateDto.md)|  | [optional] 

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

# **create_category_for_blog_post_async**
> EmptyEnvelope create_category_for_blog_post_async(tenant_id, blog_post_id, blog_post_category_create_dto=blog_post_category_create_dto)

Create a category for a blog post

Creates a new category and relates it to a specific blog post.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_create_dto import BlogPostCategoryCreateDto
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    blog_post_category_create_dto = openapi_client.BlogPostCategoryCreateDto() # BlogPostCategoryCreateDto |  (optional)

    try:
        # Create a category for a blog post
        api_response = api_instance.create_category_for_blog_post_async(tenant_id, blog_post_id, blog_post_category_create_dto=blog_post_category_create_dto)
        print("The response of BlogPostsApi->create_category_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->create_category_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **blog_post_category_create_dto** | [**BlogPostCategoryCreateDto**](BlogPostCategoryCreateDto.md)|  | [optional] 

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

# **create_comment_for_blog_post_async**
> EmptyEnvelope create_comment_for_blog_post_async(tenant_id, blog_post_id, blog_post_comment_create_dto=blog_post_comment_create_dto)

Create a comment for a blog post

Creates a new comment on a specific blog post.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_comment_create_dto import BlogPostCommentCreateDto
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    blog_post_comment_create_dto = openapi_client.BlogPostCommentCreateDto() # BlogPostCommentCreateDto |  (optional)

    try:
        # Create a comment for a blog post
        api_response = api_instance.create_comment_for_blog_post_async(tenant_id, blog_post_id, blog_post_comment_create_dto=blog_post_comment_create_dto)
        print("The response of BlogPostsApi->create_comment_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->create_comment_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **blog_post_comment_create_dto** | [**BlogPostCommentCreateDto**](BlogPostCommentCreateDto.md)|  | [optional] 

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

# **create_tag_for_blog_post_async**
> EmptyEnvelope create_tag_for_blog_post_async(tenant_id, blog_post_id, blog_post_tag_create_dto=blog_post_tag_create_dto)

Create a tag for a blog post

Creates a new tag and relates it to a specific blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    blog_post_tag_create_dto = openapi_client.BlogPostTagCreateDto() # BlogPostTagCreateDto |  (optional)

    try:
        # Create a tag for a blog post
        api_response = api_instance.create_tag_for_blog_post_async(tenant_id, blog_post_id, blog_post_tag_create_dto=blog_post_tag_create_dto)
        print("The response of BlogPostsApi->create_tag_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->create_tag_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
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

# **delete_blog_post_async**
> EmptyEnvelope delete_blog_post_async(tenant_id, blog_post_id)

Delete a blog post

Deletes a blog post for the specified tenant.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Delete a blog post
        api_response = api_instance.delete_blog_post_async(tenant_id, blog_post_id)
        print("The response of BlogPostsApi->delete_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->delete_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 

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

# **delete_comment_from_blog_post_async**
> EmptyEnvelope delete_comment_from_blog_post_async(tenant_id, blog_post_id, comment_id)

Delete a blog post comment

Deletes a comment from a specific blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        # Delete a blog post comment
        api_response = api_instance.delete_comment_from_blog_post_async(tenant_id, blog_post_id, comment_id)
        print("The response of BlogPostsApi->delete_comment_from_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->delete_comment_from_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **comment_id** | **str**|  | 

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

# **get_blog_post_by_id_async**
> BlogPostDtoEnvelope get_blog_post_by_id_async(blog_post_id)

Get a blog post by ID

Retrieves a single blog post by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_dto_envelope import BlogPostDtoEnvelope
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Get a blog post by ID
        api_response = api_instance.get_blog_post_by_id_async(blog_post_id)
        print("The response of BlogPostsApi->get_blog_post_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_blog_post_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_post_id** | **str**|  | 

### Return type

[**BlogPostDtoEnvelope**](BlogPostDtoEnvelope.md)

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

# **get_blog_posts_async**
> BlogPostDtoListEnvelope get_blog_posts_async(tenant_id=tenant_id)

Retrieve a list of blog posts

Retrieves all blog posts, optionally filtered by tenant using OData query options.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        # Retrieve a list of blog posts
        api_response = api_instance.get_blog_posts_async(tenant_id=tenant_id)
        print("The response of BlogPostsApi->get_blog_posts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_blog_posts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 

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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blog_posts_count_async**
> Int32Envelope get_blog_posts_count_async(tenant_id=tenant_id)

Get the count of blog posts

Returns the total count of blog posts, optionally filtered by tenant using OData query options.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        # Get the count of blog posts
        api_response = api_instance.get_blog_posts_count_async(tenant_id=tenant_id)
        print("The response of BlogPostsApi->get_blog_posts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_blog_posts_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 

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

# **get_categories_for_blog_post_async**
> BlogPostCategoryDtoListEnvelope get_categories_for_blog_post_async(blog_post_id)

Get categories for a blog post

Retrieves all categories related to a specific blog post.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_dto_list_envelope import BlogPostCategoryDtoListEnvelope
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Get categories for a blog post
        api_response = api_instance.get_categories_for_blog_post_async(blog_post_id)
        print("The response of BlogPostsApi->get_categories_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_categories_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_post_id** | **str**|  | 

### Return type

[**BlogPostCategoryDtoListEnvelope**](BlogPostCategoryDtoListEnvelope.md)

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

# **get_comments_for_blog_post_async**
> BlogPostCommentDtoListEnvelope get_comments_for_blog_post_async(blog_post_id)

Get comments for a blog post

Retrieves all comments for a specific blog post.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_comment_dto_list_envelope import BlogPostCommentDtoListEnvelope
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Get comments for a blog post
        api_response = api_instance.get_comments_for_blog_post_async(blog_post_id)
        print("The response of BlogPostsApi->get_comments_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_comments_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_post_id** | **str**|  | 

### Return type

[**BlogPostCommentDtoListEnvelope**](BlogPostCommentDtoListEnvelope.md)

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

# **get_replies_for_comment_async**
> BlogPostCommentDtoListEnvelope get_replies_for_comment_async(comment_id, blog_post_id)

Get replies for a comment

Retrieves all replies for a specific blog post comment.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_comment_dto_list_envelope import BlogPostCommentDtoListEnvelope
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    comment_id = 'comment_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Get replies for a comment
        api_response = api_instance.get_replies_for_comment_async(comment_id, blog_post_id)
        print("The response of BlogPostsApi->get_replies_for_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_replies_for_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **blog_post_id** | **str**|  | 

### Return type

[**BlogPostCommentDtoListEnvelope**](BlogPostCommentDtoListEnvelope.md)

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

# **get_tags_for_blog_post_async**
> BlogPostTagDtoListEnvelope get_tags_for_blog_post_async(blog_post_id)

Get tags for a blog post

Retrieves all tags related to a specific blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    blog_post_id = 'blog_post_id_example' # str | 

    try:
        # Get tags for a blog post
        api_response = api_instance.get_tags_for_blog_post_async(blog_post_id)
        print("The response of BlogPostsApi->get_tags_for_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->get_tags_for_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_post_id** | **str**|  | 

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

# **relate_category_to_blog_post_async**
> EmptyEnvelope relate_category_to_blog_post_async(tenant_id, blog_post_id, category_id)

Relate an existing category to a blog post

Creates a relationship between an existing category and a blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Relate an existing category to a blog post
        api_response = api_instance.relate_category_to_blog_post_async(tenant_id, blog_post_id, category_id)
        print("The response of BlogPostsApi->relate_category_to_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->relate_category_to_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **category_id** | **str**|  | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relate_tag_to_blog_post_async**
> EmptyEnvelope relate_tag_to_blog_post_async(tenant_id, blog_post_id, tag_id)

Relate an existing tag to a blog post

Creates a relationship between an existing tag and a blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    tag_id = 'tag_id_example' # str | 

    try:
        # Relate an existing tag to a blog post
        api_response = api_instance.relate_tag_to_blog_post_async(tenant_id, blog_post_id, tag_id)
        print("The response of BlogPostsApi->relate_tag_to_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->relate_tag_to_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **tag_id** | **str**|  | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_to_comment_async**
> EmptyEnvelope reply_to_comment_async(tenant_id, blog_post_id, comment_id, blog_post_comment_create_dto=blog_post_comment_create_dto)

Reply to a blog post comment

Creates a reply to an existing comment on a blog post.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_comment_create_dto import BlogPostCommentCreateDto
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    blog_post_comment_create_dto = openapi_client.BlogPostCommentCreateDto() # BlogPostCommentCreateDto |  (optional)

    try:
        # Reply to a blog post comment
        api_response = api_instance.reply_to_comment_async(tenant_id, blog_post_id, comment_id, blog_post_comment_create_dto=blog_post_comment_create_dto)
        print("The response of BlogPostsApi->reply_to_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->reply_to_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **blog_post_comment_create_dto** | [**BlogPostCommentCreateDto**](BlogPostCommentCreateDto.md)|  | [optional] 

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

# **unrelate_category_from_blog_post_async**
> EmptyEnvelope unrelate_category_from_blog_post_async(tenant_id, blog_post_id, category_id)

Remove a category from a blog post

Removes the relationship between a category and a blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Remove a category from a blog post
        api_response = api_instance.unrelate_category_from_blog_post_async(tenant_id, blog_post_id, category_id)
        print("The response of BlogPostsApi->unrelate_category_from_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->unrelate_category_from_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **category_id** | **str**|  | 

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

# **unrelate_tag_from_blog_post_async**
> EmptyEnvelope unrelate_tag_from_blog_post_async(tenant_id, blog_post_id, tag_id)

Remove a tag from a blog post

Removes the relationship between a tag and a blog post.

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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    tag_id = 'tag_id_example' # str | 

    try:
        # Remove a tag from a blog post
        api_response = api_instance.unrelate_tag_from_blog_post_async(tenant_id, blog_post_id, tag_id)
        print("The response of BlogPostsApi->unrelate_tag_from_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->unrelate_tag_from_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **tag_id** | **str**|  | 

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

# **update_blog_post_async**
> EmptyEnvelope update_blog_post_async(tenant_id, blog_post_id, blog_post_update_dto=blog_post_update_dto)

Update a blog post

Updates an existing blog post for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_update_dto import BlogPostUpdateDto
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
    api_instance = openapi_client.BlogPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_id = 'blog_post_id_example' # str | 
    blog_post_update_dto = openapi_client.BlogPostUpdateDto() # BlogPostUpdateDto |  (optional)

    try:
        # Update a blog post
        api_response = api_instance.update_blog_post_async(tenant_id, blog_post_id, blog_post_update_dto=blog_post_update_dto)
        print("The response of BlogPostsApi->update_blog_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostsApi->update_blog_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_id** | **str**|  | 
 **blog_post_update_dto** | [**BlogPostUpdateDto**](BlogPostUpdateDto.md)|  | [optional] 

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

