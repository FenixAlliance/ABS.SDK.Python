# openapi_client.SocialProfilesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_conversations_async**](SocialProfilesApi.md#count_conversations_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Conversations/Count | Count Conversations
[**count_followed_profiles_async**](SocialProfilesApi.md#count_followed_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/Profiles/Count | Count Followed Profiles
[**count_follower_profiles_async**](SocialProfilesApi.md#count_follower_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Followers/Profiles/Count | Count Follower Profiles
[**count_followers_async**](SocialProfilesApi.md#count_followers_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Followers/Count | Count Followers
[**count_follows_async**](SocialProfilesApi.md#count_follows_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/Count | Count Follows
[**count_messages_async**](SocialProfilesApi.md#count_messages_async) | **GET** /api/v2/SocialService/SocialProfiles/{conversationId}/Messages/Count | Count Messages
[**count_notifications_async**](SocialProfilesApi.md#count_notifications_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Notifications/Count | Count Notifications
[**count_social_profiles_async**](SocialProfilesApi.md#count_social_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles/Count | Count Social Profiles
[**create_conversation_async**](SocialProfilesApi.md#create_conversation_async) | **POST** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Conversations | Create Conversation
[**create_message_async**](SocialProfilesApi.md#create_message_async) | **POST** /api/v2/SocialService/SocialProfiles/{conversationId}/Messages | Create Message
[**delete_message_async**](SocialProfilesApi.md#delete_message_async) | **DELETE** /api/v2/SocialService/SocialProfiles/{conversationId}/Messages/{messageId} | Delete Message
[**follow_async**](SocialProfilesApi.md#follow_async) | **POST** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/{followedSocialProfileId} | Follow
[**follow_exists_async**](SocialProfilesApi.md#follow_exists_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/{followedSocialProfileId} | Check if Follow Exists
[**get_conversations_async**](SocialProfilesApi.md#get_conversations_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Conversations | Get Conversations
[**get_followed_profiles_async**](SocialProfilesApi.md#get_followed_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/Profiles | Get Followed Profiles
[**get_follower_profiles_async**](SocialProfilesApi.md#get_follower_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Followers/Profiles | Get Follower Profiles
[**get_followers_async**](SocialProfilesApi.md#get_followers_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Followers | Get Followers
[**get_follows_async**](SocialProfilesApi.md#get_follows_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows | Get Follows
[**get_messages_async**](SocialProfilesApi.md#get_messages_async) | **GET** /api/v2/SocialService/SocialProfiles/{conversationId}/Messages | Get Messages
[**get_notifications_async**](SocialProfilesApi.md#get_notifications_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Notifications | Get Notifications
[**get_social_profile_async**](SocialProfilesApi.md#get_social_profile_async) | **GET** /api/v2/SocialService/SocialProfiles/{socialProfileId} | Get Social Profile
[**get_social_profiles_async**](SocialProfilesApi.md#get_social_profiles_async) | **GET** /api/v2/SocialService/SocialProfiles | Get Social Profiles
[**unfollow_async**](SocialProfilesApi.md#unfollow_async) | **DELETE** /api/v2/SocialService/SocialProfiles/{socialProfileId}/Follows/{followedSocialProfileId} | Unfollow
[**update_message_async**](SocialProfilesApi.md#update_message_async) | **PUT** /api/v2/SocialService/SocialProfiles/{conversationId}/Messages/{messageId} | Update Message


# **count_conversations_async**
> Int32Envelope count_conversations_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Conversations

Count conversations for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Conversations
        api_response = api_instance.count_conversations_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_conversations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_conversations_async: %s\n" % e)
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

# **count_followed_profiles_async**
> Int32Envelope count_followed_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Followed Profiles

Count followed profiles for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Followed Profiles
        api_response = api_instance.count_followed_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_followed_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_followed_profiles_async: %s\n" % e)
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

# **count_follower_profiles_async**
> Int32Envelope count_follower_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Follower Profiles

Count follower profiles for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Follower Profiles
        api_response = api_instance.count_follower_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_follower_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_follower_profiles_async: %s\n" % e)
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

# **count_followers_async**
> Int32Envelope count_followers_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Followers

Count followers for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Followers
        api_response = api_instance.count_followers_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_followers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_followers_async: %s\n" % e)
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

# **count_follows_async**
> Int32Envelope count_follows_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Follows

Count follows for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Follows
        api_response = api_instance.count_follows_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_follows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_follows_async: %s\n" % e)
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

# **count_messages_async**
> Int32Envelope count_messages_async(conversation_id, api_version=api_version, x_api_version=x_api_version)

Count Messages

Count messages for a conversation.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Messages
        api_response = api_instance.count_messages_async(conversation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_messages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_messages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
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

# **count_notifications_async**
> Int32Envelope count_notifications_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Count Notifications

Count notifications for a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Notifications
        api_response = api_instance.count_notifications_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_notifications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_notifications_async: %s\n" % e)
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

# **count_social_profiles_async**
> Int32Envelope count_social_profiles_async(api_version=api_version, x_api_version=x_api_version)

Count Social Profiles

Count social profiles.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Social Profiles
        api_response = api_instance.count_social_profiles_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->count_social_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->count_social_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **create_conversation_async**
> EmptyEnvelope create_conversation_async(social_profile_id, api_version=api_version, x_api_version=x_api_version, conversation_create_dto=conversation_create_dto)

Create Conversation

Create a new conversation.

### Example


```python
import openapi_client
from openapi_client.models.conversation_create_dto import ConversationCreateDto
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    conversation_create_dto = openapi_client.ConversationCreateDto() # ConversationCreateDto |  (optional)

    try:
        # Create Conversation
        api_response = api_instance.create_conversation_async(social_profile_id, api_version=api_version, x_api_version=x_api_version, conversation_create_dto=conversation_create_dto)
        print("The response of SocialProfilesApi->create_conversation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->create_conversation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **conversation_create_dto** | [**ConversationCreateDto**](ConversationCreateDto.md)|  | [optional] 

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

# **create_message_async**
> EmptyEnvelope create_message_async(social_profile_id, conversation_id, api_version=api_version, x_api_version=x_api_version, private_message_create_dto=private_message_create_dto)

Create Message

Create a new message.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.private_message_create_dto import PrivateMessageCreateDto
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    conversation_id = 'conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    private_message_create_dto = openapi_client.PrivateMessageCreateDto() # PrivateMessageCreateDto |  (optional)

    try:
        # Create Message
        api_response = api_instance.create_message_async(social_profile_id, conversation_id, api_version=api_version, x_api_version=x_api_version, private_message_create_dto=private_message_create_dto)
        print("The response of SocialProfilesApi->create_message_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->create_message_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **conversation_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **private_message_create_dto** | [**PrivateMessageCreateDto**](PrivateMessageCreateDto.md)|  | [optional] 

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

# **delete_message_async**
> EmptyEnvelope delete_message_async(social_profile_id, conversation_id, message_id, api_version=api_version, x_api_version=x_api_version)

Delete Message

Delete a message.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    conversation_id = 'conversation_id_example' # str | 
    message_id = 'message_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete Message
        api_response = api_instance.delete_message_async(social_profile_id, conversation_id, message_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->delete_message_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->delete_message_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **conversation_id** | **str**|  | 
 **message_id** | **str**|  | 
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

# **follow_async**
> EmptyEnvelope follow_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)

Follow

Follow a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    followed_social_profile_id = 'followed_social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Follow
        api_response = api_instance.follow_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->follow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->follow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **followed_social_profile_id** | **str**|  | 
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

# **follow_exists_async**
> BooleanEnvelope follow_exists_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)

Check if Follow Exists

Check if a follow record exists between two social profiles.

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    followed_social_profile_id = 'followed_social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if Follow Exists
        api_response = api_instance.follow_exists_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->follow_exists_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->follow_exists_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **followed_social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

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

# **get_conversations_async**
> ConversationDtoListEnvelope get_conversations_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Conversations

Get a list of conversations for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.conversation_dto_list_envelope import ConversationDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Conversations
        api_response = api_instance.get_conversations_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_conversations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_conversations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ConversationDtoListEnvelope**](ConversationDtoListEnvelope.md)

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

# **get_followed_profiles_async**
> SocialProfileDtoListEnvelope get_followed_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Followed Profiles

Get a list of followed profiles for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.social_profile_dto_list_envelope import SocialProfileDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Followed Profiles
        api_response = api_instance.get_followed_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_followed_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_followed_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoListEnvelope**](SocialProfileDtoListEnvelope.md)

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

# **get_follower_profiles_async**
> SocialProfileDtoListEnvelope get_follower_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Follower Profiles

Get a list of follower profiles for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.social_profile_dto_list_envelope import SocialProfileDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Follower Profiles
        api_response = api_instance.get_follower_profiles_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_follower_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_follower_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoListEnvelope**](SocialProfileDtoListEnvelope.md)

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

# **get_followers_async**
> FollowRecordDtoListEnvelope get_followers_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Followers

Get a list of followers for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.follow_record_dto_list_envelope import FollowRecordDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Followers
        api_response = api_instance.get_followers_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_followers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_followers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FollowRecordDtoListEnvelope**](FollowRecordDtoListEnvelope.md)

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

# **get_follows_async**
> FollowRecordDtoListEnvelope get_follows_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Follows

Get a list of follows for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.follow_record_dto_list_envelope import FollowRecordDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Follows
        api_response = api_instance.get_follows_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_follows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_follows_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FollowRecordDtoListEnvelope**](FollowRecordDtoListEnvelope.md)

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

# **get_messages_async**
> PrivateMessageDtoListEnvelope get_messages_async(conversation_id, api_version=api_version, x_api_version=x_api_version)

Get Messages

Get a list of messages for a conversation.

### Example


```python
import openapi_client
from openapi_client.models.private_message_dto_list_envelope import PrivateMessageDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Messages
        api_response = api_instance.get_messages_async(conversation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_messages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_messages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PrivateMessageDtoListEnvelope**](PrivateMessageDtoListEnvelope.md)

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

# **get_notifications_async**
> NotificationDtoListEnvelope get_notifications_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Notifications

Get a list of notifications for a social profile.

### Example


```python
import openapi_client
from openapi_client.models.notification_dto_list_envelope import NotificationDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Notifications
        api_response = api_instance.get_notifications_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_notifications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_notifications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NotificationDtoListEnvelope**](NotificationDtoListEnvelope.md)

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

# **get_social_profile_async**
> SocialProfileDtoEnvelope get_social_profile_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)

Get Social Profile

Get a social profile by ID.

### Example


```python
import openapi_client
from openapi_client.models.social_profile_dto_envelope import SocialProfileDtoEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Social Profile
        api_response = api_instance.get_social_profile_async(social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_social_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_social_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoEnvelope**](SocialProfileDtoEnvelope.md)

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

# **get_social_profiles_async**
> SocialProfileDtoListEnvelope get_social_profiles_async(api_version=api_version, x_api_version=x_api_version)

Get Social Profiles

Get a list of social profiles.

### Example


```python
import openapi_client
from openapi_client.models.social_profile_dto_list_envelope import SocialProfileDtoListEnvelope
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Social Profiles
        api_response = api_instance.get_social_profiles_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->get_social_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->get_social_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoListEnvelope**](SocialProfileDtoListEnvelope.md)

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

# **unfollow_async**
> EmptyEnvelope unfollow_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)

Unfollow

Unfollow a social profile.

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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    followed_social_profile_id = 'followed_social_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Unfollow
        api_response = api_instance.unfollow_async(social_profile_id, followed_social_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialProfilesApi->unfollow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->unfollow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **followed_social_profile_id** | **str**|  | 
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

# **update_message_async**
> EmptyEnvelope update_message_async(social_profile_id, conversation_id, message_id, api_version=api_version, x_api_version=x_api_version, private_message_update_dto=private_message_update_dto)

Update Message

Update a message.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.private_message_update_dto import PrivateMessageUpdateDto
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
    api_instance = openapi_client.SocialProfilesApi(api_client)
    social_profile_id = 'social_profile_id_example' # str | 
    conversation_id = 'conversation_id_example' # str | 
    message_id = 'message_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    private_message_update_dto = openapi_client.PrivateMessageUpdateDto() # PrivateMessageUpdateDto |  (optional)

    try:
        # Update Message
        api_response = api_instance.update_message_async(social_profile_id, conversation_id, message_id, api_version=api_version, x_api_version=x_api_version, private_message_update_dto=private_message_update_dto)
        print("The response of SocialProfilesApi->update_message_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialProfilesApi->update_message_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_profile_id** | **str**|  | 
 **conversation_id** | **str**|  | 
 **message_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **private_message_update_dto** | [**PrivateMessageUpdateDto**](PrivateMessageUpdateDto.md)|  | [optional] 

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

