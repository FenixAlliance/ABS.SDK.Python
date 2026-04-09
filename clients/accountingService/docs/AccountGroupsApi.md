# openapi_client.AccountGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_group**](AccountGroupsApi.md#create_account_group) | **POST** /api/v2/AccountingService/AccountGroups | Creates a new account group
[**delete_account_group**](AccountGroupsApi.md#delete_account_group) | **DELETE** /api/v2/AccountingService/AccountGroups/{accountGroupId} | Deletes an existing account group
[**get_account_group**](AccountGroupsApi.md#get_account_group) | **GET** /api/v2/AccountingService/AccountGroups/{accountGroupId} | Gets the current tenant account group
[**get_account_groups**](AccountGroupsApi.md#get_account_groups) | **GET** /api/v2/AccountingService/AccountGroups | Gets the current tenant account groups
[**get_account_groups_count_async**](AccountGroupsApi.md#get_account_groups_count_async) | **GET** /api/v2/AccountingService/AccountGroups/Count | Gets the current tenant accounts count
[**update_account_group**](AccountGroupsApi.md#update_account_group) | **PUT** /api/v2/AccountingService/AccountGroups/{accountGroupId} | Updates an existing account group


# **create_account_group**
> AccountGroupDtoEnvelope create_account_group(tenant_id, api_version=api_version, x_api_version=x_api_version, account_group_create_dto=account_group_create_dto)

Creates a new account group

Creates a new account group.

### Example


```python
import openapi_client
from openapi_client.models.account_group_create_dto import AccountGroupCreateDto
from openapi_client.models.account_group_dto_envelope import AccountGroupDtoEnvelope
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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_group_create_dto = openapi_client.AccountGroupCreateDto() # AccountGroupCreateDto |  (optional)

    try:
        # Creates a new account group
        api_response = api_instance.create_account_group(tenant_id, api_version=api_version, x_api_version=x_api_version, account_group_create_dto=account_group_create_dto)
        print("The response of AccountGroupsApi->create_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->create_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_group_create_dto** | [**AccountGroupCreateDto**](AccountGroupCreateDto.md)|  | [optional] 

### Return type

[**AccountGroupDtoEnvelope**](AccountGroupDtoEnvelope.md)

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

# **delete_account_group**
> delete_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing account group

Deletes an existing account group.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_group_id = 'account_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing account group
        api_instance.delete_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->delete_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_group**
> AccountGroupDtoEnvelope get_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant account group

Get the currently acting tenant account group.

### Example


```python
import openapi_client
from openapi_client.models.account_group_dto_envelope import AccountGroupDtoEnvelope
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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_group_id = 'account_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant account group
        api_response = api_instance.get_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountGroupsApi->get_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->get_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountGroupDtoEnvelope**](AccountGroupDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_groups**
> AccountGroupDtoListEnvelope get_account_groups(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant account groups

Get the currently acting tenant account groups.

### Example


```python
import openapi_client
from openapi_client.models.account_group_dto_list_envelope import AccountGroupDtoListEnvelope
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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant account groups
        api_response = api_instance.get_account_groups(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountGroupsApi->get_account_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->get_account_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountGroupDtoListEnvelope**](AccountGroupDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_groups_count_async**
> Int32Envelope get_account_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant accounts count

Get the currently acting tenant accounts count.

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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant accounts count
        api_response = api_instance.get_account_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountGroupsApi->get_account_groups_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->get_account_groups_count_async: %s\n" % e)
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

# **update_account_group**
> AccountGroupDtoEnvelope update_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version, account_group_update_dto=account_group_update_dto)

Updates an existing account group

Updates an existing account group.

### Example


```python
import openapi_client
from openapi_client.models.account_group_dto_envelope import AccountGroupDtoEnvelope
from openapi_client.models.account_group_update_dto import AccountGroupUpdateDto
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
    api_instance = openapi_client.AccountGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_group_id = 'account_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_group_update_dto = openapi_client.AccountGroupUpdateDto() # AccountGroupUpdateDto |  (optional)

    try:
        # Updates an existing account group
        api_response = api_instance.update_account_group(tenant_id, account_group_id, api_version=api_version, x_api_version=x_api_version, account_group_update_dto=account_group_update_dto)
        print("The response of AccountGroupsApi->update_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->update_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_group_update_dto** | [**AccountGroupUpdateDto**](AccountGroupUpdateDto.md)|  | [optional] 

### Return type

[**AccountGroupDtoEnvelope**](AccountGroupDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

