# openapi_client.EmailGroupsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_group_async**](EmailGroupsApi.md#create_email_group_async) | **POST** /api/v2/MarketingService/EmailGroups | Create an email group
[**delete_email_group_async**](EmailGroupsApi.md#delete_email_group_async) | **DELETE** /api/v2/MarketingService/EmailGroups/{emailgroupId} | Delete an email group
[**get_email_group_details_async**](EmailGroupsApi.md#get_email_group_details_async) | **GET** /api/v2/MarketingService/EmailGroups/{emailgroupId} | Get email group by ID
[**get_email_groups_count_async**](EmailGroupsApi.md#get_email_groups_count_async) | **GET** /api/v2/MarketingService/EmailGroups/Count | Get email groups count
[**get_email_groups_o_data_async**](EmailGroupsApi.md#get_email_groups_o_data_async) | **GET** /api/v2/MarketingService/EmailGroups | Get email groups
[**update_email_group_async**](EmailGroupsApi.md#update_email_group_async) | **PUT** /api/v2/MarketingService/EmailGroups/{emailgroupId} | Update an email group


# **create_email_group_async**
> EmptyEnvelope create_email_group_async(tenant_id, email_group_create_dto, api_version=api_version, x_api_version=x_api_version)

Create an email group

Creates a new email group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.email_group_create_dto import EmailGroupCreateDto
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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_group_create_dto = openapi_client.EmailGroupCreateDto() # EmailGroupCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create an email group
        api_response = api_instance.create_email_group_async(tenant_id, email_group_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->create_email_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->create_email_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_group_create_dto** | [**EmailGroupCreateDto**](EmailGroupCreateDto.md)|  | 
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

# **delete_email_group_async**
> EmptyEnvelope delete_email_group_async(tenant_id, emailgroup_id, api_version=api_version, x_api_version=x_api_version)

Delete an email group

Deletes an email group by its ID.

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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailgroup_id = 'emailgroup_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an email group
        api_response = api_instance.delete_email_group_async(tenant_id, emailgroup_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->delete_email_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->delete_email_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailgroup_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_group_details_async**
> EmailGroupDtoEnvelope get_email_group_details_async(tenant_id, emailgroup_id, api_version=api_version, x_api_version=x_api_version)

Get email group by ID

Retrieves the details of a specific email group by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_group_dto_envelope import EmailGroupDtoEnvelope
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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailgroup_id = 'emailgroup_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email group by ID
        api_response = api_instance.get_email_group_details_async(tenant_id, emailgroup_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->get_email_group_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->get_email_group_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailgroup_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailGroupDtoEnvelope**](EmailGroupDtoEnvelope.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_groups_count_async**
> Int32Envelope get_email_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email groups count

Returns the count of email groups for the specified tenant using OData query options.

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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email groups count
        api_response = api_instance.get_email_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->get_email_groups_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->get_email_groups_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_groups_o_data_async**
> EmailGroupDtoListEnvelope get_email_groups_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email groups

Retrieves a collection of email groups for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.email_group_dto_list_envelope import EmailGroupDtoListEnvelope
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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email groups
        api_response = api_instance.get_email_groups_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->get_email_groups_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->get_email_groups_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailGroupDtoListEnvelope**](EmailGroupDtoListEnvelope.md)

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

# **update_email_group_async**
> EmptyEnvelope update_email_group_async(tenant_id, emailgroup_id, email_group_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an email group

Updates an existing email group by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_group_update_dto import EmailGroupUpdateDto
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
    api_instance = openapi_client.EmailGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailgroup_id = 'emailgroup_id_example' # str | 
    email_group_update_dto = openapi_client.EmailGroupUpdateDto() # EmailGroupUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an email group
        api_response = api_instance.update_email_group_async(tenant_id, emailgroup_id, email_group_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailGroupsApi->update_email_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailGroupsApi->update_email_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailgroup_id** | **str**|  | 
 **email_group_update_dto** | [**EmailGroupUpdateDto**](EmailGroupUpdateDto.md)|  | 
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

