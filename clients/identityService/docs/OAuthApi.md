# openapi_client.OAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_password_sign_in_async**](OAuthApi.md#check_password_sign_in_async) | **GET** /api/v2/OAuth/SignIn | Check password sign-in
[**get**](OAuthApi.md#get) | **GET** /api/v2/OAuth/WhoAmI | Get current user identity
[**get_jw_ks**](OAuthApi.md#get_jw_ks) | **GET** /api/v2/OAuth/{applicationId}/Keys | Get JSON Web Key Set
[**get_open_id_configuration**](OAuthApi.md#get_open_id_configuration) | **GET** /api/v2/OAuth/{tenantId}/{applicationId}/.Well-Known/OpenId-Configuration | Get OpenID configuration
[**get_permissions**](OAuthApi.md#get_permissions) | **GET** /api/v2/OAuth/Permissions | Get user permissions
[**password_sign_in_async**](OAuthApi.md#password_sign_in_async) | **POST** /api/v2/OAuth/SignIn | Sign in with password
[**token**](OAuthApi.md#token) | **POST** /api/v2/OAuth/Token | Get OAuth token


# **check_password_sign_in_async**
> UserCreateDtoEnvelope check_password_sign_in_async(api_version=api_version, x_api_version=x_api_version)

Check password sign-in

Verifies sign-in credentials and returns user details without creating a session.

### Example


```python
import openapi_client
from openapi_client.models.user_create_dto_envelope import UserCreateDtoEnvelope
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
    api_instance = openapi_client.OAuthApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check password sign-in
        api_response = api_instance.check_password_sign_in_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApi->check_password_sign_in_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->check_password_sign_in_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UserCreateDtoEnvelope**](UserCreateDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> AuthorizationResultEnvelope get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get current user identity

Returns the authorization result for the authenticated user, including identity and tenant context.

### Example


```python
import openapi_client
from openapi_client.models.authorization_result_envelope import AuthorizationResultEnvelope
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
    api_instance = openapi_client.OAuthApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user identity
        api_response = api_instance.get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AuthorizationResultEnvelope**](AuthorizationResultEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jw_ks**
> JsonWebKeySetEnvelope get_jw_ks(application_id, api_version=api_version, x_api_version=x_api_version)

Get JSON Web Key Set

Retrieves the signing keys (JWKS) for a specific application.

### Example


```python
import openapi_client
from openapi_client.models.json_web_key_set_envelope import JsonWebKeySetEnvelope
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
    api_instance = openapi_client.OAuthApi(api_client)
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get JSON Web Key Set
        api_response = api_instance.get_jw_ks(application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApi->get_jw_ks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_jw_ks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JsonWebKeySetEnvelope**](JsonWebKeySetEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_id_configuration**
> OpenIdConfigurationEnvelope get_open_id_configuration(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Get OpenID configuration

Retrieves the OpenID Connect discovery document for a specific application within a tenant.

### Example


```python
import openapi_client
from openapi_client.models.open_id_configuration_envelope import OpenIdConfigurationEnvelope
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
    api_instance = openapi_client.OAuthApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get OpenID configuration
        api_response = api_instance.get_open_id_configuration(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApi->get_open_id_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_open_id_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OpenIdConfigurationEnvelope**](OpenIdConfigurationEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> StringListEnvelope get_permissions(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)

Get user permissions

Retrieves the list of permission identifiers for a specific user within a tenant context.

### Example


```python
import openapi_client
from openapi_client.models.string_list_envelope import StringListEnvelope
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
    api_instance = openapi_client.OAuthApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get user permissions
        api_response = api_instance.get_permissions(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApi->get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StringListEnvelope**](StringListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_sign_in_async**
> JsonWebTokenEnvelope password_sign_in_async(api_version=api_version, x_api_version=x_api_version, signin_model=signin_model)

Sign in with password

Authenticates a user using email and password credentials.

### Example


```python
import openapi_client
from openapi_client.models.json_web_token_envelope import JsonWebTokenEnvelope
from openapi_client.models.signin_model import SigninModel
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
    api_instance = openapi_client.OAuthApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    signin_model = openapi_client.SigninModel() # SigninModel |  (optional)

    try:
        # Sign in with password
        api_response = api_instance.password_sign_in_async(api_version=api_version, x_api_version=x_api_version, signin_model=signin_model)
        print("The response of OAuthApi->password_sign_in_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->password_sign_in_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **signin_model** | [**SigninModel**](SigninModel.md)|  | [optional] 

### Return type

[**JsonWebTokenEnvelope**](JsonWebTokenEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> JsonWebTokenEnvelope token(api_version=api_version, x_api_version=x_api_version, o_auth_token_request=o_auth_token_request)

Get OAuth token

Generates an OAuth token based on the provided credentials or grant type.

### Example


```python
import openapi_client
from openapi_client.models.json_web_token_envelope import JsonWebTokenEnvelope
from openapi_client.models.o_auth_token_request import OAuthTokenRequest
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
    api_instance = openapi_client.OAuthApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    o_auth_token_request = openapi_client.OAuthTokenRequest() # OAuthTokenRequest |  (optional)

    try:
        # Get OAuth token
        api_response = api_instance.token(api_version=api_version, x_api_version=x_api_version, o_auth_token_request=o_auth_token_request)
        print("The response of OAuthApi->token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **o_auth_token_request** | [**OAuthTokenRequest**](OAuthTokenRequest.md)|  | [optional] 

### Return type

[**JsonWebTokenEnvelope**](JsonWebTokenEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

