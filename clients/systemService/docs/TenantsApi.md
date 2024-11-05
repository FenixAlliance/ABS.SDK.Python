# openapi_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantsApi.md#create_tenant) | **POST** /api/v2/SystemService/Tenants | Create a new tenant.
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /api/v2/SystemService/Tenants/{tenantId} | Delete a specific tenant by ID.
[**get_all_extended_tenants**](TenantsApi.md#get_all_extended_tenants) | **GET** /api/v2/SystemService/Tenants/Extended | Get all extended tenants available on this suite server instance.
[**get_all_tenants**](TenantsApi.md#get_all_tenants) | **GET** /api/v2/SystemService/Tenants | Get all tenants available on this suite server instance.
[**get_extended_tenants_count**](TenantsApi.md#get_extended_tenants_count) | **GET** /api/v2/SystemService/Tenants/Extended/Count | Get the total count of extended tenants available on this suite server instance.
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /api/v2/SystemService/Tenants/{tenantId} | Get a specific tenant by ID.
[**get_tenants_count**](TenantsApi.md#get_tenants_count) | **GET** /api/v2/SystemService/Tenants/Count | Get the total count of tenants available on this suite server instance.
[**update_tenant**](TenantsApi.md#update_tenant) | **PUT** /api/v2/SystemService/Tenants/{tenantId} | Update a specific tenant by ID.


# **create_tenant**
> TenantDtoEnvelope create_tenant(api_version=api_version, x_api_version=x_api_version, tenant_create_dto=tenant_create_dto)

Create a new tenant.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.tenant_create_dto import TenantCreateDto
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_create_dto = openapi_client.TenantCreateDto() # TenantCreateDto |  (optional)

    try:
        # Create a new tenant.
        api_response = api_instance.create_tenant(api_version=api_version, x_api_version=x_api_version, tenant_create_dto=tenant_create_dto)
        print("The response of TenantsApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_create_dto** | [**TenantCreateDto**](TenantCreateDto.md)|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **delete_tenant**
> EmptyEnvelope delete_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version)

Delete a specific tenant by ID.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a specific tenant by ID.
        api_response = api_instance.delete_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->delete_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_extended_tenants**
> ExtendedTenantDtoListEnvelope get_all_extended_tenants(api_version=api_version, x_api_version=x_api_version)

Get all extended tenants available on this suite server instance.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_tenant_dto_list_envelope import ExtendedTenantDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all extended tenants available on this suite server instance.
        api_response = api_instance.get_all_extended_tenants(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_all_extended_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_all_extended_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedTenantDtoListEnvelope**](ExtendedTenantDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_all_tenants**
> TenantDtoListEnvelope get_all_tenants(api_version=api_version, x_api_version=x_api_version)

Get all tenants available on this suite server instance.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.tenant_dto_list_envelope import TenantDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all tenants available on this suite server instance.
        api_response = api_instance.get_all_tenants(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_all_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_all_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoListEnvelope**](TenantDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_extended_tenants_count**
> Int32Envelope get_extended_tenants_count(api_version=api_version, x_api_version=x_api_version)

Get the total count of extended tenants available on this suite server instance.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the total count of extended tenants available on this suite server instance.
        api_response = api_instance.get_extended_tenants_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_extended_tenants_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_extended_tenants_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_tenant**
> TenantDtoEnvelope get_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get a specific tenant by ID.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific tenant by ID.
        api_response = api_instance.get_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_tenants_count**
> Int32Envelope get_tenants_count(api_version=api_version, x_api_version=x_api_version)

Get the total count of tenants available on this suite server instance.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the total count of tenants available on this suite server instance.
        api_response = api_instance.get_tenants_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of TenantsApi->get_tenants_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenants_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **update_tenant**
> TenantDtoEnvelope update_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_update_dto=tenant_update_dto)

Update a specific tenant by ID.

This action is only available for global administrators.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.tenant_dto_envelope import TenantDtoEnvelope
from openapi_client.models.tenant_update_dto import TenantUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_update_dto = openapi_client.TenantUpdateDto() # TenantUpdateDto |  (optional)

    try:
        # Update a specific tenant by ID.
        api_response = api_instance.update_tenant(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_update_dto=tenant_update_dto)
        print("The response of TenantsApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_update_dto** | [**TenantUpdateDto**](TenantUpdateDto.md)|  | [optional] 

### Return type

[**TenantDtoEnvelope**](TenantDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

