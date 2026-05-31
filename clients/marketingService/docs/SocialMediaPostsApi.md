# openapi_client.SocialMediaPostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_social_media_post_async**](SocialMediaPostsApi.md#create_social_media_post_async) | **POST** /api/v2/MarketingService/SocialMediaPosts | Create a social media post
[**delete_social_media_post_async**](SocialMediaPostsApi.md#delete_social_media_post_async) | **DELETE** /api/v2/MarketingService/SocialMediaPosts/{socialmediapostId} | Delete a social media post
[**get_social_media_post_details_async**](SocialMediaPostsApi.md#get_social_media_post_details_async) | **GET** /api/v2/MarketingService/SocialMediaPosts/{socialmediapostId} | Get social media post by ID
[**get_social_media_posts_count_async**](SocialMediaPostsApi.md#get_social_media_posts_count_async) | **GET** /api/v2/MarketingService/SocialMediaPosts/Count | Get social media posts count
[**get_social_media_posts_o_data_async**](SocialMediaPostsApi.md#get_social_media_posts_o_data_async) | **GET** /api/v2/MarketingService/SocialMediaPosts | Get social media posts
[**update_social_media_post_async**](SocialMediaPostsApi.md#update_social_media_post_async) | **PUT** /api/v2/MarketingService/SocialMediaPosts/{socialmediapostId} | Update a social media post


# **create_social_media_post_async**
> EmptyEnvelope create_social_media_post_async(tenant_id, social_media_post_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a social media post

Creates a new social media post for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_media_post_create_dto import SocialMediaPostCreateDto
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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_media_post_create_dto = openapi_client.SocialMediaPostCreateDto() # SocialMediaPostCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a social media post
        api_response = api_instance.create_social_media_post_async(tenant_id, social_media_post_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->create_social_media_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->create_social_media_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **social_media_post_create_dto** | [**SocialMediaPostCreateDto**](SocialMediaPostCreateDto.md)|  | 
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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_social_media_post_async**
> EmptyEnvelope delete_social_media_post_async(tenant_id, socialmediapost_id, api_version=api_version, x_api_version=x_api_version)

Delete a social media post

Deletes a social media post by its ID.

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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialmediapost_id = 'socialmediapost_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social media post
        api_response = api_instance.delete_social_media_post_async(tenant_id, socialmediapost_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->delete_social_media_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->delete_social_media_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialmediapost_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_media_post_details_async**
> SocialMediaPostDtoEnvelope get_social_media_post_details_async(tenant_id, socialmediapost_id, api_version=api_version, x_api_version=x_api_version)

Get social media post by ID

Retrieves the details of a specific social media post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_media_post_dto_envelope import SocialMediaPostDtoEnvelope
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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialmediapost_id = 'socialmediapost_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social media post by ID
        api_response = api_instance.get_social_media_post_details_async(tenant_id, socialmediapost_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->get_social_media_post_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->get_social_media_post_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialmediapost_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialMediaPostDtoEnvelope**](SocialMediaPostDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_media_posts_count_async**
> Int32Envelope get_social_media_posts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get social media posts count

Returns the count of social media posts for the specified tenant using OData query options.

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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social media posts count
        api_response = api_instance.get_social_media_posts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->get_social_media_posts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->get_social_media_posts_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_media_posts_o_data_async**
> SocialMediaPostDtoListEnvelope get_social_media_posts_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get social media posts

Retrieves a collection of social media posts for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.social_media_post_dto_list_envelope import SocialMediaPostDtoListEnvelope
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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social media posts
        api_response = api_instance.get_social_media_posts_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->get_social_media_posts_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->get_social_media_posts_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialMediaPostDtoListEnvelope**](SocialMediaPostDtoListEnvelope.md)

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

# **update_social_media_post_async**
> EmptyEnvelope update_social_media_post_async(tenant_id, socialmediapost_id, social_media_post_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a social media post

Updates an existing social media post by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_media_post_update_dto import SocialMediaPostUpdateDto
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
    api_instance = openapi_client.SocialMediaPostsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialmediapost_id = 'socialmediapost_id_example' # str | 
    social_media_post_update_dto = openapi_client.SocialMediaPostUpdateDto() # SocialMediaPostUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a social media post
        api_response = api_instance.update_social_media_post_async(tenant_id, socialmediapost_id, social_media_post_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialMediaPostsApi->update_social_media_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaPostsApi->update_social_media_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialmediapost_id** | **str**|  | 
 **social_media_post_update_dto** | [**SocialMediaPostUpdateDto**](SocialMediaPostUpdateDto.md)|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

