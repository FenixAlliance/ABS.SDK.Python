# openapi_client.SocialFeedsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feed_post_async**](SocialFeedsApi.md#create_feed_post_async) | **POST** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts | Create a social feed post
[**delete_feed_post_async**](SocialFeedsApi.md#delete_feed_post_async) | **DELETE** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts/{feedPostId} | Delete a social feed post
[**get_feed_notifications**](SocialFeedsApi.md#get_feed_notifications) | **GET** /api/v2/SocialService/SocialFeeds | Get social feeds
[**get_feed_post_async**](SocialFeedsApi.md#get_feed_post_async) | **GET** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts/{feedPostId} | Get social feed post by ID
[**get_feed_posts_async**](SocialFeedsApi.md#get_feed_posts_async) | **GET** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts | Get social feed posts
[**get_feed_posts_count_async**](SocialFeedsApi.md#get_feed_posts_count_async) | **GET** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts/Count | Count social feed posts
[**get_notification_async**](SocialFeedsApi.md#get_notification_async) | **GET** /api/v2/SocialService/SocialFeeds/{socialFeedId} | Get social feed by ID
[**get_notifications_count_async**](SocialFeedsApi.md#get_notifications_count_async) | **GET** /api/v2/SocialService/SocialFeeds/Count | Count social feeds
[**update_feed_post_async**](SocialFeedsApi.md#update_feed_post_async) | **PUT** /api/v2/SocialService/SocialFeeds/{socialFeedId}/Posts/{feedPostId} | Update a social feed post


# **create_feed_post_async**
> SocialFeedPostDtoEnvelope create_feed_post_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version, social_feed_post_create_dto=social_feed_post_create_dto)

Create a social feed post

Creates a new post in a specific social feed.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_post_create_dto import SocialFeedPostCreateDto
from openapi_client.models.social_feed_post_dto_envelope import SocialFeedPostDtoEnvelope
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_feed_post_create_dto = openapi_client.SocialFeedPostCreateDto() # SocialFeedPostCreateDto |  (optional)

    try:
        # Create a social feed post
        api_response = api_instance.create_feed_post_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version, social_feed_post_create_dto=social_feed_post_create_dto)
        print("The response of SocialFeedsApi->create_feed_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->create_feed_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_feed_post_create_dto** | [**SocialFeedPostCreateDto**](SocialFeedPostCreateDto.md)|  | [optional] 

### Return type

[**SocialFeedPostDtoEnvelope**](SocialFeedPostDtoEnvelope.md)

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

# **delete_feed_post_async**
> EmptyEnvelope delete_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version)

Delete a social feed post

Deletes a post from a specific social feed.

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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    feed_post_id = 'feed_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social feed post
        api_response = api_instance.delete_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->delete_feed_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->delete_feed_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **feed_post_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_notifications**
> SocialFeedDtoListEnvelope get_feed_notifications(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get social feeds

Retrieves a list of social feeds for the specified social profile.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_dto_list_envelope import SocialFeedDtoListEnvelope
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social feeds
        api_response = api_instance.get_feed_notifications(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_feed_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_feed_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialFeedDtoListEnvelope**](SocialFeedDtoListEnvelope.md)

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

# **get_feed_post_async**
> SocialFeedPostDtoEnvelope get_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version)

Get social feed post by ID

Retrieves a specific post from a social feed by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_post_dto_envelope import SocialFeedPostDtoEnvelope
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    feed_post_id = 'feed_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social feed post by ID
        api_response = api_instance.get_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_feed_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_feed_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **feed_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialFeedPostDtoEnvelope**](SocialFeedPostDtoEnvelope.md)

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

# **get_feed_posts_async**
> SocialFeedPostDtoListEnvelope get_feed_posts_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)

Get social feed posts

Retrieves a list of posts for a specific social feed.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_post_dto_list_envelope import SocialFeedPostDtoListEnvelope
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social feed posts
        api_response = api_instance.get_feed_posts_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_feed_posts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_feed_posts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialFeedPostDtoListEnvelope**](SocialFeedPostDtoListEnvelope.md)

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

# **get_feed_posts_count_async**
> Int32Envelope get_feed_posts_count_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)

Count social feed posts

Returns the count of posts for a specific social feed.

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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social feed posts
        api_response = api_instance.get_feed_posts_count_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_feed_posts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_feed_posts_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
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

# **get_notification_async**
> SocialFeedDtoEnvelope get_notification_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)

Get social feed by ID

Retrieves a specific social feed by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_dto_envelope import SocialFeedDtoEnvelope
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social feed by ID
        api_response = api_instance.get_notification_async(social_profile_id, social_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_notification_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_notification_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialFeedDtoEnvelope**](SocialFeedDtoEnvelope.md)

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

# **get_notifications_count_async**
> Int32Envelope get_notifications_count_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count social feeds

Returns the count of social feeds for the specified social profile.

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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social feeds
        api_response = api_instance.get_notifications_count_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialFeedsApi->get_notifications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->get_notifications_count_async: %s\n" % e)
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

# **update_feed_post_async**
> SocialFeedPostDtoEnvelope update_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version, social_feed_post_update_dto=social_feed_post_update_dto)

Update a social feed post

Updates an existing post in a specific social feed.

### Example


```python
import openapi_client
from openapi_client.models.social_feed_post_dto_envelope import SocialFeedPostDtoEnvelope
from openapi_client.models.social_feed_post_update_dto import SocialFeedPostUpdateDto
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
    api_instance = openapi_client.SocialFeedsApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    social_feed_id = 'social_feed_id_example' # str | 
    feed_post_id = 'feed_post_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_feed_post_update_dto = openapi_client.SocialFeedPostUpdateDto() # SocialFeedPostUpdateDto |  (optional)

    try:
        # Update a social feed post
        api_response = api_instance.update_feed_post_async(social_profile_id, social_feed_id, feed_post_id, api_version=api_version, x_api_version=x_api_version, social_feed_post_update_dto=social_feed_post_update_dto)
        print("The response of SocialFeedsApi->update_feed_post_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialFeedsApi->update_feed_post_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **social_feed_id** | **str**|  | 
 **feed_post_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_feed_post_update_dto** | [**SocialFeedPostUpdateDto**](SocialFeedPostUpdateDto.md)|  | [optional] 

### Return type

[**SocialFeedPostDtoEnvelope**](SocialFeedPostDtoEnvelope.md)

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

