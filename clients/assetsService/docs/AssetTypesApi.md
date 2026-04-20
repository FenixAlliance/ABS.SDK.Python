# openapi_client.AssetTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_type**](AssetTypesApi.md#create_asset_type) | **POST** /api/v2/AssetsService/AssetTypes | Creates a new asset type
[**delete_asset_type**](AssetTypesApi.md#delete_asset_type) | **DELETE** /api/v2/AssetsService/AssetTypes/{typeId} | Deletes an asset type
[**get_asset_type**](AssetTypesApi.md#get_asset_type) | **GET** /api/v2/AssetsService/AssetTypes/{typeId} | Gets a specific asset type
[**get_asset_types**](AssetTypesApi.md#get_asset_types) | **GET** /api/v2/AssetsService/AssetTypes | Gets all asset types for the current tenant
[**get_asset_types_count**](AssetTypesApi.md#get_asset_types_count) | **GET** /api/v2/AssetsService/AssetTypes/count | Gets the count of asset types
[**update_asset_type**](AssetTypesApi.md#update_asset_type) | **PUT** /api/v2/AssetsService/AssetTypes/{typeId} | Updates an existing asset type


# **create_asset_type**
> AssetTypeDtoEnvelope create_asset_type(tenant_id, asset_type_create_dto=asset_type_create_dto)

Creates a new asset type

Creates a new asset type for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_type_create_dto import AssetTypeCreateDto
from openapi_client.models.asset_type_dto_envelope import AssetTypeDtoEnvelope
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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_type_create_dto = openapi_client.AssetTypeCreateDto() # AssetTypeCreateDto |  (optional)

    try:
        # Creates a new asset type
        api_response = api_instance.create_asset_type(tenant_id, asset_type_create_dto=asset_type_create_dto)
        print("The response of AssetTypesApi->create_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->create_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_type_create_dto** | [**AssetTypeCreateDto**](AssetTypeCreateDto.md)|  | [optional] 

### Return type

[**AssetTypeDtoEnvelope**](AssetTypeDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_type**
> delete_asset_type(tenant_id, type_id)

Deletes an asset type

Deletes an asset type for the authenticated tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    type_id = 'type_id_example' # str | 

    try:
        # Deletes an asset type
        api_instance.delete_asset_type(tenant_id, type_id)
    except Exception as e:
        print("Exception when calling AssetTypesApi->delete_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **type_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type**
> AssetTypeDtoEnvelope get_asset_type(tenant_id, type_id)

Gets a specific asset type

Retrieves a specific asset type by ID.

### Example


```python
import openapi_client
from openapi_client.models.asset_type_dto_envelope import AssetTypeDtoEnvelope
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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    type_id = 'type_id_example' # str | 

    try:
        # Gets a specific asset type
        api_response = api_instance.get_asset_type(tenant_id, type_id)
        print("The response of AssetTypesApi->get_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->get_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **type_id** | **str**|  | 

### Return type

[**AssetTypeDtoEnvelope**](AssetTypeDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> AssetTypeDtoListEnvelope get_asset_types(tenant_id)

Gets all asset types for the current tenant

Retrieves all asset types for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_type_dto_list_envelope import AssetTypeDtoListEnvelope
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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets all asset types for the current tenant
        api_response = api_instance.get_asset_types(tenant_id)
        print("The response of AssetTypesApi->get_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->get_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**AssetTypeDtoListEnvelope**](AssetTypeDtoListEnvelope.md)

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

# **get_asset_types_count**
> Int32Envelope get_asset_types_count(tenant_id)

Gets the count of asset types

Returns the total number of asset types for the authenticated tenant.

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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of asset types
        api_response = api_instance.get_asset_types_count(tenant_id)
        print("The response of AssetTypesApi->get_asset_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->get_asset_types_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_type**
> EmptyEnvelope update_asset_type(tenant_id, type_id, asset_type_update_dto=asset_type_update_dto)

Updates an existing asset type

Updates an existing asset type for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_type_update_dto import AssetTypeUpdateDto
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
    api_instance = openapi_client.AssetTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    type_id = 'type_id_example' # str | 
    asset_type_update_dto = openapi_client.AssetTypeUpdateDto() # AssetTypeUpdateDto |  (optional)

    try:
        # Updates an existing asset type
        api_response = api_instance.update_asset_type(tenant_id, type_id, asset_type_update_dto=asset_type_update_dto)
        print("The response of AssetTypesApi->update_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->update_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **type_id** | **str**|  | 
 **asset_type_update_dto** | [**AssetTypeUpdateDto**](AssetTypeUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

