# openapi_client.OAuthApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth_application_async**](OAuthApplicationsApi.md#create_o_auth_application_async) | **POST** /api/v2/SecurityService/OAuthApplications | Create a new OAuth application
[**delete_o_auth_application_async**](OAuthApplicationsApi.md#delete_o_auth_application_async) | **DELETE** /api/v2/SecurityService/OAuthApplications/{applicationId} | Delete an OAuth application
[**get_o_auth_application_by_id_async**](OAuthApplicationsApi.md#get_o_auth_application_by_id_async) | **GET** /api/v2/SecurityService/OAuthApplications/{applicationId} | Get OAuth application by ID
[**get_o_auth_applications_async**](OAuthApplicationsApi.md#get_o_auth_applications_async) | **GET** /api/v2/SecurityService/OAuthApplications | Get all OAuth applications
[**get_o_auth_applications_count_async**](OAuthApplicationsApi.md#get_o_auth_applications_count_async) | **GET** /api/v2/SecurityService/OAuthApplications/Count | Get OAuth applications count
[**get_o_auth_authorization_by_id_async**](OAuthApplicationsApi.md#get_o_auth_authorization_by_id_async) | **GET** /api/v2/SecurityService/OAuthApplications/Authorizations/{authorizationId} | Get OAuth authorization by ID
[**get_o_auth_authorizations_async**](OAuthApplicationsApi.md#get_o_auth_authorizations_async) | **GET** /api/v2/SecurityService/OAuthApplications/Authorizations | Get all OAuth authorizations
[**get_o_auth_authorizations_count_async**](OAuthApplicationsApi.md#get_o_auth_authorizations_count_async) | **GET** /api/v2/SecurityService/OAuthApplications/Authorizations/Count | Get OAuth authorizations count
[**update_o_auth_application_async**](OAuthApplicationsApi.md#update_o_auth_application_async) | **PUT** /api/v2/SecurityService/OAuthApplications/{applicationId} | Update an existing OAuth application


# **create_o_auth_application_async**
> EmptyEnvelope create_o_auth_application_async(tenant_id, o_auth_application_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a new OAuth application

Creates a new OAuth application for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.o_auth_application_create_dto import OAuthApplicationCreateDto
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_auth_application_create_dto = openapi_client.OAuthApplicationCreateDto() # OAuthApplicationCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a new OAuth application
        api_response = api_instance.create_o_auth_application_async(tenant_id, o_auth_application_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->create_o_auth_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->create_o_auth_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_auth_application_create_dto** | [**OAuthApplicationCreateDto**](OAuthApplicationCreateDto.md)|  | 
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

# **delete_o_auth_application_async**
> EmptyEnvelope delete_o_auth_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Delete an OAuth application

Deletes an existing OAuth application.

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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an OAuth application
        api_response = api_instance.delete_o_auth_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->delete_o_auth_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->delete_o_auth_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_application_by_id_async**
> OAuthApplicationDtoEnvelope get_o_auth_application_by_id_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Get OAuth application by ID

Retrieves a specific OAuth application by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.o_auth_application_dto_envelope import OAuthApplicationDtoEnvelope
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get OAuth application by ID
        api_response = api_instance.get_o_auth_application_by_id_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_application_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_application_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OAuthApplicationDtoEnvelope**](OAuthApplicationDtoEnvelope.md)

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

# **get_o_auth_applications_async**
> OAuthApplicationDtoListEnvelope get_o_auth_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all OAuth applications

Retrieves all OAuth applications for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.o_auth_application_dto_list_envelope import OAuthApplicationDtoListEnvelope
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all OAuth applications
        api_response = api_instance.get_o_auth_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_applications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_applications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OAuthApplicationDtoListEnvelope**](OAuthApplicationDtoListEnvelope.md)

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

# **get_o_auth_applications_count_async**
> Int32Envelope get_o_auth_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get OAuth applications count

Retrieves the count of OAuth applications for the specified tenant.

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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get OAuth applications count
        api_response = api_instance.get_o_auth_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_applications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_applications_count_async: %s\n" % e)
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

# **get_o_auth_authorization_by_id_async**
> OAuthAuthorizationDtoEnvelope get_o_auth_authorization_by_id_async(tenant_id, authorization_id, api_version=api_version, x_api_version=x_api_version)

Get OAuth authorization by ID

Retrieves a specific OAuth authorization by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.o_auth_authorization_dto_envelope import OAuthAuthorizationDtoEnvelope
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    authorization_id = 'authorization_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get OAuth authorization by ID
        api_response = api_instance.get_o_auth_authorization_by_id_async(tenant_id, authorization_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_authorization_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_authorization_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **authorization_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OAuthAuthorizationDtoEnvelope**](OAuthAuthorizationDtoEnvelope.md)

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

# **get_o_auth_authorizations_async**
> OAuthAuthorizationDtoListEnvelope get_o_auth_authorizations_async(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)

Get all OAuth authorizations

Retrieves all OAuth authorizations for the specified user.

### Example


```python
import openapi_client
from openapi_client.models.o_auth_authorization_dto_list_envelope import OAuthAuthorizationDtoListEnvelope
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all OAuth authorizations
        api_response = api_instance.get_o_auth_authorizations_async(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_authorizations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_authorizations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OAuthAuthorizationDtoListEnvelope**](OAuthAuthorizationDtoListEnvelope.md)

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

# **get_o_auth_authorizations_count_async**
> Int32Envelope get_o_auth_authorizations_count_async(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)

Get OAuth authorizations count

Retrieves the count of OAuth authorizations for the specified user.

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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get OAuth authorizations count
        api_response = api_instance.get_o_auth_authorizations_count_async(tenant_id, user_id=user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->get_o_auth_authorizations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_authorizations_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
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

# **update_o_auth_application_async**
> EmptyEnvelope update_o_auth_application_async(tenant_id, application_id, o_auth_application_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an existing OAuth application

Updates an existing OAuth application.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.o_auth_application_update_dto import OAuthApplicationUpdateDto
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
    api_instance = openapi_client.OAuthApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    o_auth_application_update_dto = openapi_client.OAuthApplicationUpdateDto() # OAuthApplicationUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an existing OAuth application
        api_response = api_instance.update_o_auth_application_async(tenant_id, application_id, o_auth_application_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of OAuthApplicationsApi->update_o_auth_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->update_o_auth_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **o_auth_application_update_dto** | [**OAuthApplicationUpdateDto**](OAuthApplicationUpdateDto.md)|  | 
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

