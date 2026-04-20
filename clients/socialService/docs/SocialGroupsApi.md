# openapi_client.SocialGroupsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_social_groups_async**](SocialGroupsApi.md#count_social_groups_async) | **GET** /api/v2/SocialService/SocialGroups/Count | Count social groups
[**create_social_group_async**](SocialGroupsApi.md#create_social_group_async) | **POST** /api/v2/SocialService/SocialGroups | Create a social group
[**delete_social_group_async**](SocialGroupsApi.md#delete_social_group_async) | **DELETE** /api/v2/SocialService/SocialGroups/{socialGroupId} | Delete a social group
[**get_social_group_by_id_async**](SocialGroupsApi.md#get_social_group_by_id_async) | **GET** /api/v2/SocialService/SocialGroups/{socialGroupId} | Get social group by ID
[**get_social_groups_async**](SocialGroupsApi.md#get_social_groups_async) | **GET** /api/v2/SocialService/SocialGroups | Get social groups
[**update_social_group_async**](SocialGroupsApi.md#update_social_group_async) | **PUT** /api/v2/SocialService/SocialGroups/{socialGroupId} | Update a social group


# **count_social_groups_async**
> Int32Envelope count_social_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count social groups

Counts all social groups for the specified tenant.

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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count social groups
        api_response = api_instance.count_social_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialGroupsApi->count_social_groups_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->count_social_groups_async: %s\n" % e)
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

# **create_social_group_async**
> EmptyEnvelope create_social_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, social_group_create_dto=social_group_create_dto)

Create a social group

Creates a new social group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_group_create_dto import SocialGroupCreateDto
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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_group_create_dto = openapi_client.SocialGroupCreateDto() # SocialGroupCreateDto |  (optional)

    try:
        # Create a social group
        api_response = api_instance.create_social_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, social_group_create_dto=social_group_create_dto)
        print("The response of SocialGroupsApi->create_social_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->create_social_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_group_create_dto** | [**SocialGroupCreateDto**](SocialGroupCreateDto.md)|  | [optional] 

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

# **delete_social_group_async**
> EmptyEnvelope delete_social_group_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version)

Delete a social group

Deletes a social group for the specified tenant.

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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_group_id = 'social_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social group
        api_response = api_instance.delete_social_group_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialGroupsApi->delete_social_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->delete_social_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **social_group_id** | **str**|  | 
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

# **get_social_group_by_id_async**
> SocialGroupDtoEnvelope get_social_group_by_id_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version)

Get social group by ID

Retrieves a specific social group by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_group_dto_envelope import SocialGroupDtoEnvelope
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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_group_id = 'social_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social group by ID
        api_response = api_instance.get_social_group_by_id_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialGroupsApi->get_social_group_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->get_social_group_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **social_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialGroupDtoEnvelope**](SocialGroupDtoEnvelope.md)

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

# **get_social_groups_async**
> SocialGroupDtoListEnvelope get_social_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get social groups

Retrieves all social groups for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.social_group_dto_list_envelope import SocialGroupDtoListEnvelope
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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social groups
        api_response = api_instance.get_social_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialGroupsApi->get_social_groups_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->get_social_groups_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialGroupDtoListEnvelope**](SocialGroupDtoListEnvelope.md)

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

# **update_social_group_async**
> EmptyEnvelope update_social_group_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version, social_group_update_dto=social_group_update_dto)

Update a social group

Updates an existing social group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_group_update_dto import SocialGroupUpdateDto
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
    api_instance = openapi_client.SocialGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_group_id = 'social_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    social_group_update_dto = openapi_client.SocialGroupUpdateDto() # SocialGroupUpdateDto |  (optional)

    try:
        # Update a social group
        api_response = api_instance.update_social_group_async(tenant_id, social_group_id, api_version=api_version, x_api_version=x_api_version, social_group_update_dto=social_group_update_dto)
        print("The response of SocialGroupsApi->update_social_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialGroupsApi->update_social_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **social_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **social_group_update_dto** | [**SocialGroupUpdateDto**](SocialGroupUpdateDto.md)|  | [optional] 

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

