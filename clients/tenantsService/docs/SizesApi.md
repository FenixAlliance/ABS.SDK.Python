# openapi_client.SizesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_size**](SizesApi.md#create_tenant_size) | **POST** /api/v2/TenantsService/Sizes | Create a new tenant size
[**delete_tenant_size**](SizesApi.md#delete_tenant_size) | **DELETE** /api/v2/TenantsService/Sizes/{tenantSizeId} | Delete a tenant size
[**get_tenant_size_by_id**](SizesApi.md#get_tenant_size_by_id) | **GET** /api/v2/TenantsService/Sizes/{tenantSizeId} | Retrieve a single tenant size by its ID
[**get_tenant_sizes**](SizesApi.md#get_tenant_sizes) | **GET** /api/v2/TenantsService/Sizes | Retrieve a list of tenant sizes
[**get_tenant_sizes_count**](SizesApi.md#get_tenant_sizes_count) | **GET** /api/v2/TenantsService/Sizes/Count | Get the count of tenant sizes
[**update_tenant_size**](SizesApi.md#update_tenant_size) | **PUT** /api/v2/TenantsService/Sizes/{tenantSizeId} | Update a tenant size


# **create_tenant_size**
> EmptyEnvelope create_tenant_size(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_size_create_dto=tenant_size_create_dto)

Create a new tenant size

Create a new tenant size

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_size_create_dto import TenantSizeCreateDto
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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_size_create_dto = openapi_client.TenantSizeCreateDto() # TenantSizeCreateDto |  (optional)

    try:
        # Create a new tenant size
        api_response = api_instance.create_tenant_size(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_size_create_dto=tenant_size_create_dto)
        print("The response of SizesApi->create_tenant_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->create_tenant_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_size_create_dto** | [**TenantSizeCreateDto**](TenantSizeCreateDto.md)|  | [optional] 

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

# **delete_tenant_size**
> EmptyEnvelope delete_tenant_size(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant size

Delete a tenant size

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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_size_id = 'tenant_size_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant size
        api_response = api_instance.delete_tenant_size(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SizesApi->delete_tenant_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->delete_tenant_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_size_id** | **str**|  | 
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

# **get_tenant_size_by_id**
> TenantSizeDtoEnvelope get_tenant_size_by_id(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant size by its ID

Retrieve a single tenant size by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_size_dto_envelope import TenantSizeDtoEnvelope
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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_size_id = 'tenant_size_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant size by its ID
        api_response = api_instance.get_tenant_size_by_id(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SizesApi->get_tenant_size_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->get_tenant_size_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_size_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantSizeDtoEnvelope**](TenantSizeDtoEnvelope.md)

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

# **get_tenant_sizes**
> TenantSizeDtoListEnvelope get_tenant_sizes(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant sizes

Retrieve a list of tenant sizes

### Example


```python
import openapi_client
from openapi_client.models.tenant_size_dto_list_envelope import TenantSizeDtoListEnvelope
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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant sizes
        api_response = api_instance.get_tenant_sizes(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SizesApi->get_tenant_sizes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->get_tenant_sizes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantSizeDtoListEnvelope**](TenantSizeDtoListEnvelope.md)

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

# **get_tenant_sizes_count**
> Int32Envelope get_tenant_sizes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant sizes

Get the count of tenant sizes

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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant sizes
        api_response = api_instance.get_tenant_sizes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SizesApi->get_tenant_sizes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->get_tenant_sizes_count: %s\n" % e)
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

# **update_tenant_size**
> EmptyEnvelope update_tenant_size(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version, tenant_size_update_dto=tenant_size_update_dto)

Update a tenant size

Update a tenant size

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_size_update_dto import TenantSizeUpdateDto
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
    api_instance = openapi_client.SizesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_size_id = 'tenant_size_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_size_update_dto = openapi_client.TenantSizeUpdateDto() # TenantSizeUpdateDto |  (optional)

    try:
        # Update a tenant size
        api_response = api_instance.update_tenant_size(tenant_id, tenant_size_id, api_version=api_version, x_api_version=x_api_version, tenant_size_update_dto=tenant_size_update_dto)
        print("The response of SizesApi->update_tenant_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SizesApi->update_tenant_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_size_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_size_update_dto** | [**TenantSizeUpdateDto**](TenantSizeUpdateDto.md)|  | [optional] 

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

