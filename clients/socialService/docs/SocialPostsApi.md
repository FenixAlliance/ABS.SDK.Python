# openapi_client.SocialPostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_social_post_async**](SocialPostsApi.md#create_social_post_async) | **POST** /api/v2/SocialService/SocialPosts | Create a social post
[**create_social_post_attachment_async**](SocialPostsApi.md#create_social_post_attachment_async) | **POST** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments | Create a social post attachment
[**create_social_post_comment_async**](SocialPostsApi.md#create_social_post_comment_async) | **POST** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments | Create a social post comment
[**create_social_post_reaction_async**](SocialPostsApi.md#create_social_post_reaction_async) | **POST** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions | Create a social post reaction
[**delete_social_post_async**](SocialPostsApi.md#delete_social_post_async) | **DELETE** /api/v2/SocialService/SocialPosts/{socialPostId} | Delete a social post
[**delete_social_post_attachment_async**](SocialPostsApi.md#delete_social_post_attachment_async) | **DELETE** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments/{attachmentId} | Delete a social post attachment
[**delete_social_post_comment_async**](SocialPostsApi.md#delete_social_post_comment_async) | **DELETE** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments/{commentId} | Delete a social post comment
[**delete_social_post_reaction_async**](SocialPostsApi.md#delete_social_post_reaction_async) | **DELETE** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions/{reactionId} | Delete a social post reaction
[**get_social_post_async**](SocialPostsApi.md#get_social_post_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId} | Get social post by ID
[**get_social_post_attachment_async**](SocialPostsApi.md#get_social_post_attachment_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments/{attachmentId} | Get social post attachment by ID
[**get_social_post_attachments_async**](SocialPostsApi.md#get_social_post_attachments_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments | Get social post attachments
[**get_social_post_attachments_count_async**](SocialPostsApi.md#get_social_post_attachments_count_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments/Count | Count social post attachments
[**get_social_post_comment_async**](SocialPostsApi.md#get_social_post_comment_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments/{commentId} | Get social post comment by ID
[**get_social_post_comments_async**](SocialPostsApi.md#get_social_post_comments_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments | Get social post comments
[**get_social_post_comments_count_async**](SocialPostsApi.md#get_social_post_comments_count_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments/Count | Count social post comments
[**get_social_post_reaction_async**](SocialPostsApi.md#get_social_post_reaction_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions/{reactionId} | Get social post reaction by ID
[**get_social_post_reactions_async**](SocialPostsApi.md#get_social_post_reactions_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions | Get social post reactions
[**get_social_post_reactions_count_async**](SocialPostsApi.md#get_social_post_reactions_count_async) | **GET** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions/Count | Count social post reactions
[**get_social_posts_async**](SocialPostsApi.md#get_social_posts_async) | **GET** /api/v2/SocialService/SocialPosts | Get social posts
[**get_social_posts_count_async**](SocialPostsApi.md#get_social_posts_count_async) | **GET** /api/v2/SocialService/SocialPosts/Count | Count social posts
[**update_social_post_async**](SocialPostsApi.md#update_social_post_async) | **PUT** /api/v2/SocialService/SocialPosts/{socialPostId} | Update a social post
[**update_social_post_attachment_async**](SocialPostsApi.md#update_social_post_attachment_async) | **PUT** /api/v2/SocialService/SocialPosts/{socialPostId}/Attachments/{attachmentId} | Update a social post attachment
[**update_social_post_comment_async**](SocialPostsApi.md#update_social_post_comment_async) | **PUT** /api/v2/SocialService/SocialPosts/{socialPostId}/Comments/{commentId} | Update a social post comment
[**update_social_post_reaction_async**](SocialPostsApi.md#update_social_post_reaction_async) | **PUT** /api/v2/SocialService/SocialPosts/{socialPostId}/Reactions/{reactionId} | Update a social post reaction


# **create_social_post_async**
> SocialPostDtoEnvelope create_social_post_async(social_profile_id, api_version=api_version, x_api_version=x_api_version, social_post_create_dto=social_post_create_dto)

Create a social post

Creates a new social post for the specified social profile.

### Example


```python
import openapi_client
from openapi_client.models.social_post_create_dto import SocialPostCreateDto
from openapi_client.models.social_post_dto_envelope import SocialPostDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_create_dto = openapi_client.SocialPostCreateDto() # SocialPostCreateDto |  (optional)

    try:
        # Create a social post
        api_response = api_instance.create_social_post_async(social_profile_id, api_version=api_version, x_api_version=x_api_version, social_post_create_dto=social_post_create_dto)
        print("The response of SocialPostsApi->create_social_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->create_social_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_create_dto** | [**SocialPostCreateDto**](SocialPostCreateDto.md)|  | [optional] 

### Return type

[**SocialPostDtoEnvelope**](SocialPostDtoEnvelope.md)

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

# **create_social_post_attachment_async**
> SocialPostAttachmentDtoEnvelope create_social_post_attachment_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version, social_post_attachment_create_dto=social_post_attachment_create_dto)

Create a social post attachment

Creates a new attachment for a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.social_post_attachment_create_dto import SocialPostAttachmentCreateDto
from openapi_client.models.social_post_attachment_dto_envelope import SocialPostAttachmentDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_attachment_create_dto = openapi_client.SocialPostAttachmentCreateDto() # SocialPostAttachmentCreateDto |  (optional)

    try:
        # Create a social post attachment
        api_response = api_instance.create_social_post_attachment_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version, social_post_attachment_create_dto=social_post_attachment_create_dto)
        print("The response of SocialPostsApi->create_social_post_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->create_social_post_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_attachment_create_dto** | [**SocialPostAttachmentCreateDto**](SocialPostAttachmentCreateDto.md)|  | [optional] 

### Return type

[**SocialPostAttachmentDtoEnvelope**](SocialPostAttachmentDtoEnvelope.md)

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

# **create_social_post_comment_async**
> EmptyEnvelope create_social_post_comment_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version, social_post_comment_create_dto=social_post_comment_create_dto)

Create a social post comment

Creates a new comment on a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_comment_create_dto import SocialPostCommentCreateDto
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_comment_create_dto = openapi_client.SocialPostCommentCreateDto() # SocialPostCommentCreateDto |  (optional)

    try:
        # Create a social post comment
        api_response = api_instance.create_social_post_comment_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version, social_post_comment_create_dto=social_post_comment_create_dto)
        print("The response of SocialPostsApi->create_social_post_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->create_social_post_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_comment_create_dto** | [**SocialPostCommentCreateDto**](SocialPostCommentCreateDto.md)|  | [optional] 

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

# **create_social_post_reaction_async**
> SocialReactionDtoEnvelope create_social_post_reaction_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version, social_reaction_create_dto=social_reaction_create_dto)

Create a social post reaction

Creates a new reaction on a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.social_reaction_create_dto import SocialReactionCreateDto
from openapi_client.models.social_reaction_dto_envelope import SocialReactionDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_reaction_create_dto = openapi_client.SocialReactionCreateDto() # SocialReactionCreateDto |  (optional)

    try:
        # Create a social post reaction
        api_response = api_instance.create_social_post_reaction_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version, social_reaction_create_dto=social_reaction_create_dto)
        print("The response of SocialPostsApi->create_social_post_reaction_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->create_social_post_reaction_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_reaction_create_dto** | [**SocialReactionCreateDto**](SocialReactionCreateDto.md)|  | [optional] 

### Return type

[**SocialReactionDtoEnvelope**](SocialReactionDtoEnvelope.md)

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

# **delete_social_post_async**
> EmptyEnvelope delete_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)

Delete a social post

Deletes a social post by its ID.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social post
        api_response = api_instance.delete_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->delete_social_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->delete_social_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
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

# **delete_social_post_attachment_async**
> EmptyEnvelope delete_social_post_attachment_async(social_profile_id, social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version)

Delete a social post attachment

Deletes an attachment from a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social post attachment
        api_response = api_instance.delete_social_post_attachment_async(social_profile_id, social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->delete_social_post_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->delete_social_post_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **attachment_id** | **str**|  | 
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

# **delete_social_post_comment_async**
> EmptyEnvelope delete_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version)

Delete a social post comment

Deletes a comment from a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social post comment
        api_response = api_instance.delete_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->delete_social_post_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->delete_social_post_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **comment_id** | **str**|  | 
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

# **delete_social_post_reaction_async**
> EmptyEnvelope delete_social_post_reaction_async(social_profile_id, social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version)

Delete a social post reaction

Deletes a reaction from a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    reaction_id = 'reaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social post reaction
        api_response = api_instance.delete_social_post_reaction_async(social_profile_id, social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->delete_social_post_reaction_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->delete_social_post_reaction_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **reaction_id** | **str**|  | 
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

# **get_social_post_async**
> SocialPostDtoEnvelope get_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)

Get social post by ID

Retrieves a specific social post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_post_dto_envelope import SocialPostDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post by ID
        api_response = api_instance.get_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostDtoEnvelope**](SocialPostDtoEnvelope.md)

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

# **get_social_post_attachment_async**
> EmptyEnvelope get_social_post_attachment_async(social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version)

Get social post attachment by ID

Retrieves a specific attachment from a social post by its ID.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post attachment by ID
        api_response = api_instance.get_social_post_attachment_async(social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **attachment_id** | **str**|  | 
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

# **get_social_post_attachments_async**
> SocialPostAttachmentDtoListEnvelope get_social_post_attachments_async(social_post_id, api_version=api_version, x_api_version=x_api_version)

Get social post attachments

Retrieves a list of attachments for a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.social_post_attachment_dto_list_envelope import SocialPostAttachmentDtoListEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post attachments
        api_response = api_instance.get_social_post_attachments_async(social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_attachments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_attachments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostAttachmentDtoListEnvelope**](SocialPostAttachmentDtoListEnvelope.md)

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

# **get_social_post_attachments_count_async**
> Int32Envelope get_social_post_attachments_count_async(social_post_id, api_version=api_version, x_api_version=x_api_version)

Count social post attachments

Returns the count of attachments for a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social post attachments
        api_response = api_instance.get_social_post_attachments_count_async(social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_attachments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_attachments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
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

# **get_social_post_comment_async**
> SocialPostCommentDtoEnvelope get_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version)

Get social post comment by ID

Retrieves a specific comment from a social post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_post_comment_dto_envelope import SocialPostCommentDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post comment by ID
        api_response = api_instance.get_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostCommentDtoEnvelope**](SocialPostCommentDtoEnvelope.md)

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

# **get_social_post_comments_async**
> SocialPostCommentDtoListEnvelope get_social_post_comments_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)

Get social post comments

Retrieves a list of comments for a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.social_post_comment_dto_list_envelope import SocialPostCommentDtoListEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post comments
        api_response = api_instance.get_social_post_comments_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_comments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_comments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostCommentDtoListEnvelope**](SocialPostCommentDtoListEnvelope.md)

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

# **get_social_post_comments_count_async**
> Int32Envelope get_social_post_comments_count_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)

Count social post comments

Returns the count of comments for a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social post comments
        api_response = api_instance.get_social_post_comments_count_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_comments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_comments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
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

# **get_social_post_reaction_async**
> SocialReactionDtoEnvelope get_social_post_reaction_async(social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version)

Get social post reaction by ID

Retrieves a specific reaction from a social post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_reaction_dto_envelope import SocialReactionDtoEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    reaction_id = 'reaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post reaction by ID
        api_response = api_instance.get_social_post_reaction_async(social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_reaction_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_reaction_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **reaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialReactionDtoEnvelope**](SocialReactionDtoEnvelope.md)

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

# **get_social_post_reactions_async**
> SocialReactionDtoListEnvelope get_social_post_reactions_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get social post reactions

Retrieves a list of reactions for a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.social_reaction_dto_list_envelope import SocialReactionDtoListEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post reactions
        api_response = api_instance.get_social_post_reactions_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_reactions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_reactions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialReactionDtoListEnvelope**](SocialReactionDtoListEnvelope.md)

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

# **get_social_post_reactions_count_async**
> Int32Envelope get_social_post_reactions_count_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count social post reactions

Returns the count of reactions for a specific social post.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_post_id = 'social_post_id_example' # str | 
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social post reactions
        api_response = api_instance.get_social_post_reactions_count_async(social_post_id, social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_post_reactions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_post_reactions_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_post_id** | **str**|  | 
 **social_profile_id** | **str**|  | 
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

# **get_social_posts_async**
> SocialPostDtoListEnvelope get_social_posts_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get social posts

Retrieves a list of social posts for the specified social profile.

### Example


```python
import openapi_client
from openapi_client.models.social_post_dto_list_envelope import SocialPostDtoListEnvelope
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social posts
        api_response = api_instance.get_social_posts_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_posts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_posts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostDtoListEnvelope**](SocialPostDtoListEnvelope.md)

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

# **get_social_posts_count_async**
> Int32Envelope get_social_posts_count_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count social posts

Returns the count of social posts for the specified social profile.

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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social posts
        api_response = api_instance.get_social_posts_count_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostsApi->get_social_posts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->get_social_posts_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
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

# **update_social_post_async**
> EmptyEnvelope update_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version, social_post_update_dto=social_post_update_dto)

Update a social post

Updates an existing social post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_update_dto import SocialPostUpdateDto
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_update_dto = openapi_client.SocialPostUpdateDto() # SocialPostUpdateDto |  (optional)

    try:
        # Update a social post
        api_response = api_instance.update_social_post_async(social_profile_id, social_post_id, api_version=api_version, x_api_version=x_api_version, social_post_update_dto=social_post_update_dto)
        print("The response of SocialPostsApi->update_social_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->update_social_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_update_dto** | [**SocialPostUpdateDto**](SocialPostUpdateDto.md)|  | [optional] 

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

# **update_social_post_attachment_async**
> EmptyEnvelope update_social_post_attachment_async(social_profile_id, social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version, social_post_attachment_update_dto=social_post_attachment_update_dto)

Update a social post attachment

Updates an existing attachment on a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_attachment_update_dto import SocialPostAttachmentUpdateDto
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_attachment_update_dto = openapi_client.SocialPostAttachmentUpdateDto() # SocialPostAttachmentUpdateDto |  (optional)

    try:
        # Update a social post attachment
        api_response = api_instance.update_social_post_attachment_async(social_profile_id, social_post_id, attachment_id, api_version=api_version, x_api_version=x_api_version, social_post_attachment_update_dto=social_post_attachment_update_dto)
        print("The response of SocialPostsApi->update_social_post_attachment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->update_social_post_attachment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_attachment_update_dto** | [**SocialPostAttachmentUpdateDto**](SocialPostAttachmentUpdateDto.md)|  | [optional] 

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

# **update_social_post_comment_async**
> EmptyEnvelope update_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version, social_post_comment_update_dto=social_post_comment_update_dto)

Update a social post comment

Updates an existing comment on a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_comment_update_dto import SocialPostCommentUpdateDto
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_post_comment_update_dto = openapi_client.SocialPostCommentUpdateDto() # SocialPostCommentUpdateDto |  (optional)

    try:
        # Update a social post comment
        api_response = api_instance.update_social_post_comment_async(social_profile_id, social_post_id, comment_id, api_version=api_version, x_api_version=x_api_version, social_post_comment_update_dto=social_post_comment_update_dto)
        print("The response of SocialPostsApi->update_social_post_comment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->update_social_post_comment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_post_comment_update_dto** | [**SocialPostCommentUpdateDto**](SocialPostCommentUpdateDto.md)|  | [optional] 

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

# **update_social_post_reaction_async**
> EmptyEnvelope update_social_post_reaction_async(social_profile_id, social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version, social_reaction_update_dto=social_reaction_update_dto)

Update a social post reaction

Updates an existing reaction on a specific social post.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_reaction_update_dto import SocialReactionUpdateDto
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
    api_instance = openapi_client.SocialPostsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_post_id = 'social_post_id_example' # str | 
    reaction_id = 'reaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_reaction_update_dto = openapi_client.SocialReactionUpdateDto() # SocialReactionUpdateDto |  (optional)

    try:
        # Update a social post reaction
        api_response = api_instance.update_social_post_reaction_async(social_profile_id, social_post_id, reaction_id, api_version=api_version, x_api_version=x_api_version, social_reaction_update_dto=social_reaction_update_dto)
        print("The response of SocialPostsApi->update_social_post_reaction_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostsApi->update_social_post_reaction_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_post_id** | **str**|  | 
 **reaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_reaction_update_dto** | [**SocialReactionUpdateDto**](SocialReactionUpdateDto.md)|  | [optional] 

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

