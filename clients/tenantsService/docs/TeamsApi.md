# openapi_client.TeamsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_team**](TeamsApi.md#create_tenant_team) | **POST** /api/v2/TenantsService/Teams | Create a new tenant team
[**delete_tenant_team**](TeamsApi.md#delete_tenant_team) | **DELETE** /api/v2/TenantsService/Teams/{tenantTeamId} | Delete a tenant team
[**get_tenant_team_by_id**](TeamsApi.md#get_tenant_team_by_id) | **GET** /api/v2/TenantsService/Teams/{tenantTeamId} | Retrieve a single tenant team by its ID
[**get_tenant_teams**](TeamsApi.md#get_tenant_teams) | **GET** /api/v2/TenantsService/Teams | Retrieve a list of tenant teams
[**get_tenant_teams_count**](TeamsApi.md#get_tenant_teams_count) | **GET** /api/v2/TenantsService/Teams/Count | Get the count of tenant teams
[**update_tenant_team**](TeamsApi.md#update_tenant_team) | **PUT** /api/v2/TenantsService/Teams/{tenantTeamId} | Update a tenant team


# **create_tenant_team**
> EmptyEnvelope create_tenant_team(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_create_dto=tenant_team_create_dto)

Create a new tenant team

Create a new tenant team

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_create_dto import TenantTeamCreateDto
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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_create_dto = openapi_client.TenantTeamCreateDto() # TenantTeamCreateDto |  (optional)

    try:
        # Create a new tenant team
        api_response = api_instance.create_tenant_team(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_create_dto=tenant_team_create_dto)
        print("The response of TeamsApi->create_tenant_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->create_tenant_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_create_dto** | [**TenantTeamCreateDto**](TenantTeamCreateDto.md)|  | [optional] 

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

# **delete_tenant_team**
> EmptyEnvelope delete_tenant_team(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant team

Delete a tenant team

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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_id = 'tenant_team_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant team
        api_response = api_instance.delete_tenant_team(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamsApi->delete_tenant_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_tenant_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_id** | **str**|  | 
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

# **get_tenant_team_by_id**
> TenantTeamDtoEnvelope get_tenant_team_by_id(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant team by its ID

Retrieve a single tenant team by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_dto_envelope import TenantTeamDtoEnvelope
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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_id = 'tenant_team_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant team by its ID
        api_response = api_instance.get_tenant_team_by_id(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamsApi->get_tenant_team_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_tenant_team_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamDtoEnvelope**](TenantTeamDtoEnvelope.md)

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

# **get_tenant_teams**
> TenantTeamDtoListEnvelope get_tenant_teams(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant teams

Retrieve a list of tenant teams

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_dto_list_envelope import TenantTeamDtoListEnvelope
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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant teams
        api_response = api_instance.get_tenant_teams(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamsApi->get_tenant_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_tenant_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamDtoListEnvelope**](TenantTeamDtoListEnvelope.md)

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

# **get_tenant_teams_count**
> Int32Envelope get_tenant_teams_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant teams

Get the count of tenant teams

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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant teams
        api_response = api_instance.get_tenant_teams_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamsApi->get_tenant_teams_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_tenant_teams_count: %s\n" % e)
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

# **update_tenant_team**
> EmptyEnvelope update_tenant_team(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version, tenant_team_update_dto=tenant_team_update_dto)

Update a tenant team

Update a tenant team

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_update_dto import TenantTeamUpdateDto
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
    api_instance = openapi_client.TeamsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_id = 'tenant_team_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_update_dto = openapi_client.TenantTeamUpdateDto() # TenantTeamUpdateDto |  (optional)

    try:
        # Update a tenant team
        api_response = api_instance.update_tenant_team(tenant_id, tenant_team_id, api_version=api_version, x_api_version=x_api_version, tenant_team_update_dto=tenant_team_update_dto)
        print("The response of TeamsApi->update_tenant_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->update_tenant_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_update_dto** | [**TenantTeamUpdateDto**](TenantTeamUpdateDto.md)|  | [optional] 

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

