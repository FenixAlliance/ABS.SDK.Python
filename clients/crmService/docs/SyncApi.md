# openapi_client.SyncApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_current_holder_to_current_tenant_crm**](SyncApi.md#sync_current_holder_to_current_tenant_crm) | **POST** /api/v2/CrmService/Sync | Sync the current user into the current tenant&#39;s contact list
[**sync_current_holder_to_tenant_crm**](SyncApi.md#sync_current_holder_to_tenant_crm) | **POST** /api/v2/CrmService/Sync/Me | Sync the current user into a tenant&#39;s contact list
[**sync_holder_to_tenant_crm_async**](SyncApi.md#sync_holder_to_tenant_crm_async) | **POST** /api/v2/CrmService/Sync/User | Sync a user into a tenant&#39;s contact list
[**sync_tenant_to_tenant_crm**](SyncApi.md#sync_tenant_to_tenant_crm) | **POST** /api/v2/CrmService/Sync/Tenant | Sync a tenant into another tenant&#39;s contact list


# **sync_current_holder_to_current_tenant_crm**
> Envelope sync_current_holder_to_current_tenant_crm(tenant_id, api_version=api_version, x_api_version=x_api_version)

Sync the current user into the current tenant's contact list

Synchronizes the currently authenticated user into the current tenant's CRM contact list.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.SyncApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Sync the current user into the current tenant's contact list
        api_response = api_instance.sync_current_holder_to_current_tenant_crm(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SyncApi->sync_current_holder_to_current_tenant_crm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->sync_current_holder_to_current_tenant_crm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **sync_current_holder_to_tenant_crm**
> Envelope sync_current_holder_to_tenant_crm(tenant_id, api_version=api_version, x_api_version=x_api_version)

Sync the current user into a tenant's contact list

Synchronizes the currently authenticated user into the specified tenant's CRM contact list.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.SyncApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Sync the current user into a tenant's contact list
        api_response = api_instance.sync_current_holder_to_tenant_crm(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SyncApi->sync_current_holder_to_tenant_crm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->sync_current_holder_to_tenant_crm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **sync_holder_to_tenant_crm_async**
> Envelope sync_holder_to_tenant_crm_async(tenant_id, related_user_id, api_version=api_version, x_api_version=x_api_version)

Sync a user into a tenant's contact list

Synchronizes a specified user into the tenant's CRM contact list.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.SyncApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    related_user_id = 'related_user_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Sync a user into a tenant's contact list
        api_response = api_instance.sync_holder_to_tenant_crm_async(tenant_id, related_user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SyncApi->sync_holder_to_tenant_crm_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->sync_holder_to_tenant_crm_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **related_user_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **sync_tenant_to_tenant_crm**
> EmptyEnvelope sync_tenant_to_tenant_crm(tenant_id, related_tenant_id, api_version=api_version, x_api_version=x_api_version)

Sync a tenant into another tenant's contact list

Synchronizes a tenant into another tenant's CRM contact list.

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
    api_instance = openapi_client.SyncApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    related_tenant_id = 'related_tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Sync a tenant into another tenant's contact list
        api_response = api_instance.sync_tenant_to_tenant_crm(tenant_id, related_tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SyncApi->sync_tenant_to_tenant_crm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->sync_tenant_to_tenant_crm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **related_tenant_id** | **str**|  | 
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

