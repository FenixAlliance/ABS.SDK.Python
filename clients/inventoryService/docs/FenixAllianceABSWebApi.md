# openapi_client.FenixAllianceABSWebApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_logout_post**](FenixAllianceABSWebApi.md#account_logout_post) | **POST** /Account/Logout | 
[**account_manage_download_personal_data_post**](FenixAllianceABSWebApi.md#account_manage_download_personal_data_post) | **POST** /Account/Manage/DownloadPersonalData | 
[**account_manage_link_external_login_post**](FenixAllianceABSWebApi.md#account_manage_link_external_login_post) | **POST** /Account/Manage/LinkExternalLogin | 
[**account_perform_external_login_post**](FenixAllianceABSWebApi.md#account_perform_external_login_post) | **POST** /Account/PerformExternalLogin | 
[**forgot_password_post**](FenixAllianceABSWebApi.md#forgot_password_post) | **POST** /forgotPassword | 
[**health_get**](FenixAllianceABSWebApi.md#health_get) | **GET** /health | 
[**hello_get**](FenixAllianceABSWebApi.md#hello_get) | **GET** /hello | 
[**login_post**](FenixAllianceABSWebApi.md#login_post) | **POST** /login | 
[**manage2fa_post**](FenixAllianceABSWebApi.md#manage2fa_post) | **POST** /manage/2fa | 
[**manage_info_get**](FenixAllianceABSWebApi.md#manage_info_get) | **GET** /manage/info | 
[**manage_info_post**](FenixAllianceABSWebApi.md#manage_info_post) | **POST** /manage/info | 
[**map_identity_api_confirm_email**](FenixAllianceABSWebApi.md#map_identity_api_confirm_email) | **GET** /confirmEmail | 
[**refresh_post**](FenixAllianceABSWebApi.md#refresh_post) | **POST** /refresh | 
[**register_post**](FenixAllianceABSWebApi.md#register_post) | **POST** /register | 
[**resend_confirmation_email_post**](FenixAllianceABSWebApi.md#resend_confirmation_email_post) | **POST** /resendConfirmationEmail | 
[**reset_password_post**](FenixAllianceABSWebApi.md#reset_password_post) | **POST** /resetPassword | 
[**version_get**](FenixAllianceABSWebApi.md#version_get) | **GET** /version | 


# **account_logout_post**
> account_logout_post(return_url=return_url)



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    return_url = 'return_url_example' # str |  (optional)

    try:
        api_instance.account_logout_post(return_url=return_url)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->account_logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_manage_download_personal_data_post**
> account_manage_download_personal_data_post()



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)

    try:
        api_instance.account_manage_download_personal_data_post()
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->account_manage_download_personal_data_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_manage_link_external_login_post**
> account_manage_link_external_login_post(provider=provider)



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    provider = 'provider_example' # str |  (optional)

    try:
        api_instance.account_manage_link_external_login_post(provider=provider)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->account_manage_link_external_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perform_external_login_post**
> account_perform_external_login_post(provider=provider, return_url=return_url)



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    provider = 'provider_example' # str |  (optional)
    return_url = 'return_url_example' # str |  (optional)

    try:
        api_instance.account_perform_external_login_post(provider=provider, return_url=return_url)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->account_perform_external_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] 
 **return_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_post**
> forgot_password_post(forgot_password_request)



### Example


```python
import openapi_client
from openapi_client.models.forgot_password_request import ForgotPasswordRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    forgot_password_request = openapi_client.ForgotPasswordRequest() # ForgotPasswordRequest | 

    try:
        api_instance.forgot_password_post(forgot_password_request)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->forgot_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_request** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_get**
> health_get()



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)

    try:
        api_instance.health_get()
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hello_get**
> hello_get()



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)

    try:
        api_instance.hello_get()
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->hello_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_post**
> AccessTokenResponse login_post(login_request, use_cookies=use_cookies, use_session_cookies=use_session_cookies)



### Example


```python
import openapi_client
from openapi_client.models.access_token_response import AccessTokenResponse
from openapi_client.models.login_request import LoginRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    login_request = openapi_client.LoginRequest() # LoginRequest | 
    use_cookies = True # bool |  (optional)
    use_session_cookies = True # bool |  (optional)

    try:
        api_response = api_instance.login_post(login_request, use_cookies=use_cookies, use_session_cookies=use_session_cookies)
        print("The response of FenixAllianceABSWebApi->login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 
 **use_cookies** | **bool**|  | [optional] 
 **use_session_cookies** | **bool**|  | [optional] 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage2fa_post**
> TwoFactorResponse manage2fa_post(two_factor_request)



### Example


```python
import openapi_client
from openapi_client.models.two_factor_request import TwoFactorRequest
from openapi_client.models.two_factor_response import TwoFactorResponse
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    two_factor_request = openapi_client.TwoFactorRequest() # TwoFactorRequest | 

    try:
        api_response = api_instance.manage2fa_post(two_factor_request)
        print("The response of FenixAllianceABSWebApi->manage2fa_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->manage2fa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_request** | [**TwoFactorRequest**](TwoFactorRequest.md)|  | 

### Return type

[**TwoFactorResponse**](TwoFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_info_get**
> InfoResponse manage_info_get()



### Example


```python
import openapi_client
from openapi_client.models.info_response import InfoResponse
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)

    try:
        api_response = api_instance.manage_info_get()
        print("The response of FenixAllianceABSWebApi->manage_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->manage_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_info_post**
> InfoResponse manage_info_post(info_request)



### Example


```python
import openapi_client
from openapi_client.models.info_request import InfoRequest
from openapi_client.models.info_response import InfoResponse
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    info_request = openapi_client.InfoRequest() # InfoRequest | 

    try:
        api_response = api_instance.manage_info_post(info_request)
        print("The response of FenixAllianceABSWebApi->manage_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->manage_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_request** | [**InfoRequest**](InfoRequest.md)|  | 

### Return type

[**InfoResponse**](InfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_identity_api_confirm_email**
> map_identity_api_confirm_email(user_id, code, changed_email=changed_email)



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    user_id = 'user_id_example' # str | 
    code = 'code_example' # str | 
    changed_email = 'changed_email_example' # str |  (optional)

    try:
        api_instance.map_identity_api_confirm_email(user_id, code, changed_email=changed_email)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->map_identity_api_confirm_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **code** | **str**|  | 
 **changed_email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_post**
> AccessTokenResponse refresh_post(refresh_request)



### Example


```python
import openapi_client
from openapi_client.models.access_token_response import AccessTokenResponse
from openapi_client.models.refresh_request import RefreshRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    refresh_request = openapi_client.RefreshRequest() # RefreshRequest | 

    try:
        api_response = api_instance.refresh_post(refresh_request)
        print("The response of FenixAllianceABSWebApi->refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_request** | [**RefreshRequest**](RefreshRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_post**
> register_post(register_request)



### Example


```python
import openapi_client
from openapi_client.models.register_request import RegisterRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    register_request = openapi_client.RegisterRequest() # RegisterRequest | 

    try:
        api_instance.register_post(register_request)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_confirmation_email_post**
> resend_confirmation_email_post(resend_confirmation_email_request)



### Example


```python
import openapi_client
from openapi_client.models.resend_confirmation_email_request import ResendConfirmationEmailRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    resend_confirmation_email_request = openapi_client.ResendConfirmationEmailRequest() # ResendConfirmationEmailRequest | 

    try:
        api_instance.resend_confirmation_email_post(resend_confirmation_email_request)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->resend_confirmation_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_confirmation_email_request** | [**ResendConfirmationEmailRequest**](ResendConfirmationEmailRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_post**
> reset_password_post(reset_password_request)



### Example


```python
import openapi_client
from openapi_client.models.reset_password_request import ResetPasswordRequest
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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)
    reset_password_request = openapi_client.ResetPasswordRequest() # ResetPasswordRequest | 

    try:
        api_instance.reset_password_post(reset_password_request)
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_get**
> version_get()



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
    api_instance = openapi_client.FenixAllianceABSWebApi(api_client)

    try:
        api_instance.version_get()
    except Exception as e:
        print("Exception when calling FenixAllianceABSWebApi->version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

