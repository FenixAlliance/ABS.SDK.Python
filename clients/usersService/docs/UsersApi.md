# openapi_client.UsersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_current_user_followers_async**](UsersApi.md#count_current_user_followers_async) | **GET** /api/v2/Me/Followers/Count | Count the social profiles that follow the current user
[**count_current_user_follows_async**](UsersApi.md#count_current_user_follows_async) | **GET** /api/v2/Me/Follows/Count | Count the social profiles that the current user follows
[**count_current_user_notifications_async**](UsersApi.md#count_current_user_notifications_async) | **GET** /api/v2/Me/Notifications/Count | Count the notifications for the current user
[**count_current_user_tenants_async**](UsersApi.md#count_current_user_tenants_async) | **GET** /api/v2/Me/Tenants/Count | Count the tenants that the current user is enrolled in
[**get_current_user_addresses_async**](UsersApi.md#get_current_user_addresses_async) | **GET** /api/v2/Me/Addresses | Get the list of addresses for the current user
[**get_current_user_async**](UsersApi.md#get_current_user_async) | **GET** /api/v2/Me | Gets the current user
[**get_current_user_avatar_async**](UsersApi.md#get_current_user_avatar_async) | **GET** /api/v2/Me/Avatar | Get the current user&#39;s avatar
[**get_current_user_cart_async**](UsersApi.md#get_current_user_cart_async) | **GET** /api/v2/Me/Cart | Get the current user&#39;s cart
[**get_current_user_enrollments_async**](UsersApi.md#get_current_user_enrollments_async) | **GET** /api/v2/Me/Enrollments | Get the list of enrollments for the current user
[**get_current_user_enrollments_extended_async**](UsersApi.md#get_current_user_enrollments_extended_async) | **GET** /api/v2/Me/Enrollments/Extended | Get the list of enrollments for the current user
[**get_current_user_followers_async**](UsersApi.md#get_current_user_followers_async) | **GET** /api/v2/Me/Followers | Get the social profiles that follow the current user
[**get_current_user_follows_async**](UsersApi.md#get_current_user_follows_async) | **GET** /api/v2/Me/Follows | Get the social profiles that the current user follows
[**get_current_user_invitation_async**](UsersApi.md#get_current_user_invitation_async) | **GET** /api/v2/Me/Invitations | Get the list of tenant enrollment invitations for the current user
[**get_current_user_notifications_async**](UsersApi.md#get_current_user_notifications_async) | **GET** /api/v2/Me/Notifications | Get the list of notifications for the current user
[**get_current_user_settings_async**](UsersApi.md#get_current_user_settings_async) | **GET** /api/v2/Me/Settings | Get the settings for the current user
[**get_current_user_social_profile_async**](UsersApi.md#get_current_user_social_profile_async) | **GET** /api/v2/Me/SocialProfile | Get the current user&#39;s social profile
[**get_current_user_tenants_async**](UsersApi.md#get_current_user_tenants_async) | **GET** /api/v2/Me/Tenants | Get the tenants that the current user is enrolled in
[**get_current_user_tenants_extended_async**](UsersApi.md#get_current_user_tenants_extended_async) | **GET** /api/v2/Me/Tenants/Extended | Get the tenants that the current user is enrolled in
[**get_current_user_wallet_async**](UsersApi.md#get_current_user_wallet_async) | **GET** /api/v2/Me/Wallet | Get the current user&#39;s billing profile
[**get_enrollment_async**](UsersApi.md#get_enrollment_async) | **GET** /api/v2/Me/Enrollments/{enrollmentId} | Get a single TenantEnrollment by its ID
[**get_extended_current_user_async**](UsersApi.md#get_extended_current_user_async) | **GET** /api/v2/Me/Extended | Get the current user&#39;s extended profile
[**patch_current_user_async**](UsersApi.md#patch_current_user_async) | **PATCH** /api/v2/Me | Partially update the current user&#39;s profile
[**update_avatar_async**](UsersApi.md#update_avatar_async) | **POST** /api/v2/Me/Avatar | Update the current user&#39;s avatar
[**update_current_user_async**](UsersApi.md#update_current_user_async) | **PUT** /api/v2/Me | Update the current user&#39;s profile
[**update_current_user_settings_async**](UsersApi.md#update_current_user_settings_async) | **PUT** /api/v2/Me/Settings | Update the settings for the current user


# **count_current_user_followers_async**
> Int32Envelope count_current_user_followers_async(api_version=api_version, x_api_version=x_api_version)

Count the social profiles that follow the current user

Count the social profiles that follow the current user

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count the social profiles that follow the current user
        api_response = api_instance.count_current_user_followers_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->count_current_user_followers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->count_current_user_followers_async: %s\n" % e)
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
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_current_user_follows_async**
> Int32Envelope count_current_user_follows_async(api_version=api_version, x_api_version=x_api_version)

Count the social profiles that the current user follows

Count the social profiles that the current user follows

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count the social profiles that the current user follows
        api_response = api_instance.count_current_user_follows_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->count_current_user_follows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->count_current_user_follows_async: %s\n" % e)
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
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_current_user_notifications_async**
> Int32Envelope count_current_user_notifications_async(api_version=api_version, x_api_version=x_api_version)

Count the notifications for the current user

Count the notifications for the current user

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count the notifications for the current user
        api_response = api_instance.count_current_user_notifications_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->count_current_user_notifications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->count_current_user_notifications_async: %s\n" % e)
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
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_current_user_tenants_async**
> Int32Envelope count_current_user_tenants_async(api_version=api_version, x_api_version=x_api_version)

Count the tenants that the current user is enrolled in

Count the tenants that the current user is enrolled in

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count the tenants that the current user is enrolled in
        api_response = api_instance.count_current_user_tenants_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->count_current_user_tenants_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->count_current_user_tenants_async: %s\n" % e)
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
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_addresses_async**
> AddressDtoListEnvelope get_current_user_addresses_async(api_version=api_version, x_api_version=x_api_version)

Get the list of addresses for the current user

Get the list of addresses for the current user

### Example


```python
import openapi_client
from openapi_client.models.address_dto_list_envelope import AddressDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of addresses for the current user
        api_response = api_instance.get_current_user_addresses_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_addresses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_addresses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AddressDtoListEnvelope**](AddressDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_async**
> UserDtoEnvelope get_current_user_async(api_version=api_version, x_api_version=x_api_version)

Gets the current user

Get the currently acting user.

### Example


```python
import openapi_client
from openapi_client.models.user_dto_envelope import UserDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current user
        api_response = api_instance.get_current_user_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UserDtoEnvelope**](UserDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_avatar_async**
> bytearray get_current_user_avatar_async(api_version=api_version, x_api_version=x_api_version)

Get the current user's avatar

Get the current user's avatar

### Example


```python
import openapi_client
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's avatar
        api_response = api_instance.get_current_user_avatar_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_cart_async**
> CartDtoEnvelope get_current_user_cart_async(api_version=api_version, x_api_version=x_api_version)

Get the current user's cart

Get the current user's cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's cart
        api_response = api_instance.get_current_user_cart_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_enrollments_async**
> TenantEnrollmentDtoListEnvelope get_current_user_enrollments_async(api_version=api_version, x_api_version=x_api_version)

Get the list of enrollments for the current user

Get the list of enrollments for the current user

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_list_envelope import TenantEnrollmentDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of enrollments for the current user
        api_response = api_instance.get_current_user_enrollments_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_enrollments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_enrollments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoListEnvelope**](TenantEnrollmentDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_enrollments_extended_async**
> ExtendedTenantEnrollmentDtoListEnvelope get_current_user_enrollments_extended_async(api_version=api_version, x_api_version=x_api_version)

Get the list of enrollments for the current user

Get the list of enrollments for the current user

### Example


```python
import openapi_client
from openapi_client.models.extended_tenant_enrollment_dto_list_envelope import ExtendedTenantEnrollmentDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of enrollments for the current user
        api_response = api_instance.get_current_user_enrollments_extended_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_enrollments_extended_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_enrollments_extended_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedTenantEnrollmentDtoListEnvelope**](ExtendedTenantEnrollmentDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_followers_async**
> FollowRecordDtoListEnvelope get_current_user_followers_async(api_version=api_version, x_api_version=x_api_version)

Get the social profiles that follow the current user

Get the social profiles that follow the current user

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the social profiles that follow the current user
        api_response = api_instance.get_current_user_followers_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_followers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_followers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FollowRecordDtoListEnvelope**](FollowRecordDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_follows_async**
> FollowRecordDtoListEnvelope get_current_user_follows_async(api_version=api_version, x_api_version=x_api_version)

Get the social profiles that the current user follows

Get the social profiles that the current user follows

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the social profiles that the current user follows
        api_response = api_instance.get_current_user_follows_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_follows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_follows_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FollowRecordDtoListEnvelope**](FollowRecordDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_invitation_async**
> TenantInvitationDtoListEnvelope get_current_user_invitation_async(api_version=api_version, x_api_version=x_api_version)

Get the list of tenant enrollment invitations for the current user

Get the list of tenant enrollment invitations for the current user

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_list_envelope import TenantInvitationDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of tenant enrollment invitations for the current user
        api_response = api_instance.get_current_user_invitation_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_invitation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_invitation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_notifications_async**
> NotificationDtoListEnvelope get_current_user_notifications_async(api_version=api_version, x_api_version=x_api_version)

Get the list of notifications for the current user

Get the list of notifications for the current user

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the list of notifications for the current user
        api_response = api_instance.get_current_user_notifications_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_notifications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_notifications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NotificationDtoListEnvelope**](NotificationDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_settings_async**
> UserSettingsDtoEnvelope get_current_user_settings_async(api_version=api_version, x_api_version=x_api_version)

Get the settings for the current user

Get the settings for the current user

### Example


```python
import openapi_client
from openapi_client.models.user_settings_dto_envelope import UserSettingsDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the settings for the current user
        api_response = api_instance.get_current_user_settings_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_settings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_settings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UserSettingsDtoEnvelope**](UserSettingsDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_social_profile_async**
> SocialProfileDtoEnvelope get_current_user_social_profile_async(api_version=api_version, x_api_version=x_api_version)

Get the current user's social profile

Get the current user's social profile

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's social profile
        api_response = api_instance.get_current_user_social_profile_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_social_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_social_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoEnvelope**](SocialProfileDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_tenants_async**
> TenantDtoListEnvelope get_current_user_tenants_async(api_version=api_version, x_api_version=x_api_version)

Get the tenants that the current user is enrolled in

Get the tenants that the current user is enrolled in

### Example


```python
import openapi_client
from openapi_client.models.tenant_dto_list_envelope import TenantDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the tenants that the current user is enrolled in
        api_response = api_instance.get_current_user_tenants_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_tenants_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_tenants_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoListEnvelope**](TenantDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_tenants_extended_async**
> ExtendedTenantDtoListEnvelope get_current_user_tenants_extended_async(api_version=api_version, x_api_version=x_api_version)

Get the tenants that the current user is enrolled in

Get the tenants that the current user is enrolled in

### Example


```python
import openapi_client
from openapi_client.models.extended_tenant_dto_list_envelope import ExtendedTenantDtoListEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the tenants that the current user is enrolled in
        api_response = api_instance.get_current_user_tenants_extended_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_tenants_extended_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_tenants_extended_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedTenantDtoListEnvelope**](ExtendedTenantDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_wallet_async**
> WalletDtoEnvelope get_current_user_wallet_async(api_version=api_version, x_api_version=x_api_version)

Get the current user's billing profile

Get the current user's billing profile

### Example


```python
import openapi_client
from openapi_client.models.wallet_dto_envelope import WalletDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's billing profile
        api_response = api_instance.get_current_user_wallet_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_current_user_wallet_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_wallet_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletDtoEnvelope**](WalletDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_async**
> TenantEnrollmentDtoEnvelope get_enrollment_async(enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get a single TenantEnrollment by its ID

Get a single TenantEnrollment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_enrollment_dto_envelope import TenantEnrollmentDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    enrollment_id = 'enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a single TenantEnrollment by its ID
        api_response = api_instance.get_enrollment_async(enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantEnrollmentDtoEnvelope**](TenantEnrollmentDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_current_user_async**
> ExtendedUserDtoEnvelope get_extended_current_user_async(api_version=api_version, x_api_version=x_api_version)

Get the current user's extended profile

Get the current user's extended profile

### Example


```python
import openapi_client
from openapi_client.models.extended_user_dto_envelope import ExtendedUserDtoEnvelope
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's extended profile
        api_response = api_instance.get_extended_current_user_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of UsersApi->get_extended_current_user_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_extended_current_user_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedUserDtoEnvelope**](ExtendedUserDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_current_user_async**
> EmptyEnvelope patch_current_user_async(api_version=api_version, x_api_version=x_api_version, operation=operation)

Partially update the current user's profile

Partially update the current user's profile

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Partially update the current user's profile
        api_response = api_instance.patch_current_user_async(api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of UsersApi->patch_current_user_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->patch_current_user_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar_async**
> EmptyEnvelope update_avatar_async(api_version=api_version, x_api_version=x_api_version, avatar=avatar)

Update the current user's avatar

Update the current user's avatar

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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    avatar = None # bytearray |  (optional)

    try:
        # Update the current user's avatar
        api_response = api_instance.update_avatar_async(api_version=api_version, x_api_version=x_api_version, avatar=avatar)
        print("The response of UsersApi->update_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **avatar** | **bytearray**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json, application/xml
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_async**
> EmptyEnvelope update_current_user_async(api_version=api_version, x_api_version=x_api_version, user_update_dto=user_update_dto)

Update the current user's profile

Update the current user's profile

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.user_update_dto import UserUpdateDto
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    user_update_dto = openapi_client.UserUpdateDto() # UserUpdateDto |  (optional)

    try:
        # Update the current user's profile
        api_response = api_instance.update_current_user_async(api_version=api_version, x_api_version=x_api_version, user_update_dto=user_update_dto)
        print("The response of UsersApi->update_current_user_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **user_update_dto** | [**UserUpdateDto**](UserUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_settings_async**
> UserSettingsDtoEnvelope update_current_user_settings_async(api_version=api_version, x_api_version=x_api_version, user_settings_update_dto=user_settings_update_dto)

Update the settings for the current user

Update the settings for the current user

### Example


```python
import openapi_client
from openapi_client.models.user_settings_dto_envelope import UserSettingsDtoEnvelope
from openapi_client.models.user_settings_update_dto import UserSettingsUpdateDto
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
    api_instance = openapi_client.UsersApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    user_settings_update_dto = openapi_client.UserSettingsUpdateDto() # UserSettingsUpdateDto |  (optional)

    try:
        # Update the settings for the current user
        api_response = api_instance.update_current_user_settings_async(api_version=api_version, x_api_version=x_api_version, user_settings_update_dto=user_settings_update_dto)
        print("The response of UsersApi->update_current_user_settings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user_settings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **user_settings_update_dto** | [**UserSettingsUpdateDto**](UserSettingsUpdateDto.md)|  | [optional] 

### Return type

[**UserSettingsDtoEnvelope**](UserSettingsDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

