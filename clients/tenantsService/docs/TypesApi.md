# openapi_client.TypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_type**](TypesApi.md#create_tenant_type) | **POST** /api/v2/TenantsService/Types | Create a new tenant type
[**delete_tenant_type**](TypesApi.md#delete_tenant_type) | **DELETE** /api/v2/TenantsService/Types/{tenantTypeId} | Delete a tenant type
[**get_tenant_type_by_id**](TypesApi.md#get_tenant_type_by_id) | **GET** /api/v2/TenantsService/Types/{tenantTypeId} | Retrieve a single tenant type by its ID
[**get_tenant_types**](TypesApi.md#get_tenant_types) | **GET** /api/v2/TenantsService/Types | Retrieve a list of tenant types
[**get_tenant_types_count**](TypesApi.md#get_tenant_types_count) | **GET** /api/v2/TenantsService/Types/Count | Get the count of tenant types
[**update_tenant_type**](TypesApi.md#update_tenant_type) | **PUT** /api/v2/TenantsService/Types/{tenantTypeId} | Update a tenant type


# **create_tenant_type**
> EmptyEnvelope create_tenant_type(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_type_create_dto=tenant_type_create_dto)

Create a new tenant type

Create a new tenant type

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_type_create_dto import TenantTypeCreateDto
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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_type_create_dto = openapi_client.TenantTypeCreateDto() # TenantTypeCreateDto |  (optional)

    try:
        # Create a new tenant type
        api_response = api_instance.create_tenant_type(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_type_create_dto=tenant_type_create_dto)
        print("The response of TypesApi->create_tenant_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->create_tenant_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_type_create_dto** | [**TenantTypeCreateDto**](TenantTypeCreateDto.md)|  | [optional] 

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

# **delete_tenant_type**
> EmptyEnvelope delete_tenant_type(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant type

Delete a tenant type

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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_type_id = 'tenant_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant type
        api_response = api_instance.delete_tenant_type(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TypesApi->delete_tenant_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->delete_tenant_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_type_id** | **str**|  | 
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

# **get_tenant_type_by_id**
> TenantTypeDtoEnvelope get_tenant_type_by_id(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant type by its ID

Retrieve a single tenant type by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_type_dto_envelope import TenantTypeDtoEnvelope
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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_type_id = 'tenant_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant type by its ID
        api_response = api_instance.get_tenant_type_by_id(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TypesApi->get_tenant_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->get_tenant_type_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTypeDtoEnvelope**](TenantTypeDtoEnvelope.md)

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

# **get_tenant_types**
> TenantTypeDtoListEnvelope get_tenant_types(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant types

Retrieve a list of tenant types

### Example


```python
import openapi_client
from openapi_client.models.tenant_type_dto_list_envelope import TenantTypeDtoListEnvelope
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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant types
        api_response = api_instance.get_tenant_types(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TypesApi->get_tenant_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->get_tenant_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTypeDtoListEnvelope**](TenantTypeDtoListEnvelope.md)

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

# **get_tenant_types_count**
> Int32Envelope get_tenant_types_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant types

Get the count of tenant types

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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant types
        api_response = api_instance.get_tenant_types_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TypesApi->get_tenant_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->get_tenant_types_count: %s\n" % e)
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

# **update_tenant_type**
> EmptyEnvelope update_tenant_type(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version, tenant_type_update_dto=tenant_type_update_dto)

Update a tenant type

Update a tenant type

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_type_update_dto import TenantTypeUpdateDto
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
    api_instance = openapi_client.TypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_type_id = 'tenant_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_type_update_dto = openapi_client.TenantTypeUpdateDto() # TenantTypeUpdateDto |  (optional)

    try:
        # Update a tenant type
        api_response = api_instance.update_tenant_type(tenant_id, tenant_type_id, api_version=api_version, x_api_version=x_api_version, tenant_type_update_dto=tenant_type_update_dto)
        print("The response of TypesApi->update_tenant_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->update_tenant_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_type_update_dto** | [**TenantTypeUpdateDto**](TenantTypeUpdateDto.md)|  | [optional] 

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

