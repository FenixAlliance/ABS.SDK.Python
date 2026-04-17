# openapi_client.GrantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_grant_async**](GrantsApi.md#create_grant_async) | **POST** /api/v2/AccountingService/Grants | Create grant
[**delete_grant_async**](GrantsApi.md#delete_grant_async) | **DELETE** /api/v2/AccountingService/Grants/{grantId} | Delete grant
[**get_grant_details_async**](GrantsApi.md#get_grant_details_async) | **GET** /api/v2/AccountingService/Grants/{grantId} | Get grant by ID
[**get_grants_async**](GrantsApi.md#get_grants_async) | **GET** /api/v2/AccountingService/Grants | Get all grants
[**get_grants_count_async**](GrantsApi.md#get_grants_count_async) | **GET** /api/v2/AccountingService/Grants/Count | Count grants
[**update_grant_async**](GrantsApi.md#update_grant_async) | **PUT** /api/v2/AccountingService/Grants/{grantId} | Update grant


# **create_grant_async**
> EmptyEnvelope create_grant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, grant_create_dto=grant_create_dto)

Create grant

Creates a new grant entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.grant_create_dto import GrantCreateDto
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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    grant_create_dto = openapi_client.GrantCreateDto() # GrantCreateDto |  (optional)

    try:
        # Create grant
        api_response = api_instance.create_grant_async(tenant_id, api_version=api_version, x_api_version=x_api_version, grant_create_dto=grant_create_dto)
        print("The response of GrantsApi->create_grant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->create_grant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **grant_create_dto** | [**GrantCreateDto**](GrantCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grant_async**
> EmptyEnvelope delete_grant_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version)

Delete grant

Deletes a grant identified by its ID.

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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete grant
        api_response = api_instance.delete_grant_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of GrantsApi->delete_grant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->delete_grant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **grant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grant_details_async**
> GrantDtoEnvelope get_grant_details_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version)

Get grant by ID

Gets detailed information for a specific grant.

### Example


```python
import openapi_client
from openapi_client.models.grant_dto_envelope import GrantDtoEnvelope
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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get grant by ID
        api_response = api_instance.get_grant_details_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of GrantsApi->get_grant_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->get_grant_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**GrantDtoEnvelope**](GrantDtoEnvelope.md)

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

# **get_grants_async**
> GrantDtoIReadOnlyListEnvelope get_grants_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all grants

Retrieves a list of grants associated with the tenant.

### Example


```python
import openapi_client
from openapi_client.models.grant_dto_i_read_only_list_envelope import GrantDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all grants
        api_response = api_instance.get_grants_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of GrantsApi->get_grants_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->get_grants_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**GrantDtoIReadOnlyListEnvelope**](GrantDtoIReadOnlyListEnvelope.md)

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

# **get_grants_count_async**
> Int32Envelope get_grants_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count grants

Returns the number of grants for the tenant.

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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count grants
        api_response = api_instance.get_grants_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of GrantsApi->get_grants_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->get_grants_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_grant_async**
> EmptyEnvelope update_grant_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version, body=body)

Update grant

Updates an existing grant identified by its ID.

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
    api_instance = openapi_client.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update grant
        api_response = api_instance.update_grant_async(tenant_id, grant_id, api_version=api_version, x_api_version=x_api_version, body=body)
        print("The response of GrantsApi->update_grant_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->update_grant_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

