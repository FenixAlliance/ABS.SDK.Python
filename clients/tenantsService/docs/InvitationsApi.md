# openapi_client.InvitationsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_tenant_invitation**](InvitationsApi.md#accept_tenant_invitation) | **POST** /api/v2/TenantsService/Invitations/{invitationId}/Accept | Accept an invitation to join a tenant
[**decline_tenant_invitation**](InvitationsApi.md#decline_tenant_invitation) | **POST** /api/v2/TenantsService/Invitations/{invitationId}/Decline | Decline an invitation to join a tenant
[**delete_tenant_invitation**](InvitationsApi.md#delete_tenant_invitation) | **DELETE** /api/v2/TenantsService/Invitations/{invitationId} | Delete a tenant invitation
[**get_tenant_invitation_by_id**](InvitationsApi.md#get_tenant_invitation_by_id) | **GET** /api/v2/TenantsService/Invitations/{invitationId} | Get a tenant invitation by its ID
[**get_tenant_invitations**](InvitationsApi.md#get_tenant_invitations) | **GET** /api/v2/TenantsService/Invitations | Retrieve a list of tenant invitations
[**get_tenant_invitations_count**](InvitationsApi.md#get_tenant_invitations_count) | **GET** /api/v2/TenantsService/Invitations/Count | Get the count of tenant invitations
[**send_tenant_invitation**](InvitationsApi.md#send_tenant_invitation) | **POST** /api/v2/TenantsService/Invitations | Send an invitation to a user to join a tenant


# **accept_tenant_invitation**
> EmptyEnvelope accept_tenant_invitation(invitation_id, api_version=api_version, x_api_version=x_api_version)

Accept an invitation to join a tenant

Accept an invitation to join a tenant

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
    api_instance = openapi_client.InvitationsApi(api_client)
    invitation_id = 'invitation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Accept an invitation to join a tenant
        api_response = api_instance.accept_tenant_invitation(invitation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->accept_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->accept_tenant_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  | 
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

# **decline_tenant_invitation**
> EmptyEnvelope decline_tenant_invitation(invitation_id, api_version=api_version, x_api_version=x_api_version)

Decline an invitation to join a tenant

Decline an invitation to join a tenant

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
    api_instance = openapi_client.InvitationsApi(api_client)
    invitation_id = 'invitation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Decline an invitation to join a tenant
        api_response = api_instance.decline_tenant_invitation(invitation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->decline_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->decline_tenant_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  | 
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

# **delete_tenant_invitation**
> EmptyEnvelope delete_tenant_invitation(tenant_id, invitation_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant invitation

Delete a tenant invitation

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
    api_instance = openapi_client.InvitationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invitation_id = 'invitation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant invitation
        api_response = api_instance.delete_tenant_invitation(tenant_id, invitation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->delete_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->delete_tenant_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invitation_id** | **str**|  | 
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

# **get_tenant_invitation_by_id**
> TenantInvitationDtoEnvelope get_tenant_invitation_by_id(tenant_id, invitation_id, api_version=api_version, x_api_version=x_api_version)

Get a tenant invitation by its ID

Get a tenant invitation by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_invitation_dto_envelope import TenantInvitationDtoEnvelope
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
    api_instance = openapi_client.InvitationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invitation_id = 'invitation_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a tenant invitation by its ID
        api_response = api_instance.get_tenant_invitation_by_id(tenant_id, invitation_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->get_tenant_invitation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_tenant_invitation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invitation_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoEnvelope**](TenantInvitationDtoEnvelope.md)

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

# **get_tenant_invitations**
> TenantInvitationDtoListEnvelope get_tenant_invitations(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant invitations

Retrieve a list of tenant invitations

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
    api_instance = openapi_client.InvitationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant invitations
        api_response = api_instance.get_tenant_invitations(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->get_tenant_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_tenant_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantInvitationDtoListEnvelope**](TenantInvitationDtoListEnvelope.md)

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

# **get_tenant_invitations_count**
> Int32Envelope get_tenant_invitations_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant invitations

Get the count of tenant invitations

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
    api_instance = openapi_client.InvitationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant invitations
        api_response = api_instance.get_tenant_invitations_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvitationsApi->get_tenant_invitations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_tenant_invitations_count: %s\n" % e)
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

# **send_tenant_invitation**
> EmptyEnvelope send_tenant_invitation(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_invitation_create_dto=tenant_invitation_create_dto)

Send an invitation to a user to join a tenant

Send an invitation to a user to join a tenant

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_invitation_create_dto import TenantInvitationCreateDto
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
    api_instance = openapi_client.InvitationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_invitation_create_dto = openapi_client.TenantInvitationCreateDto() # TenantInvitationCreateDto |  (optional)

    try:
        # Send an invitation to a user to join a tenant
        api_response = api_instance.send_tenant_invitation(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_invitation_create_dto=tenant_invitation_create_dto)
        print("The response of InvitationsApi->send_tenant_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->send_tenant_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_invitation_create_dto** | [**TenantInvitationCreateDto**](TenantInvitationCreateDto.md)|  | [optional] 

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

