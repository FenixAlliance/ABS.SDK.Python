# openapi_client.ItemTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_types_async**](ItemTypesApi.md#count_item_types_async) | **GET** /api/v2/CatalogService/ItemTypes/Count | Count item types
[**create_item_type_async**](ItemTypesApi.md#create_item_type_async) | **POST** /api/v2/CatalogService/ItemTypes | Create a new item type
[**delete_item_type_async**](ItemTypesApi.md#delete_item_type_async) | **DELETE** /api/v2/CatalogService/ItemTypes/{itemTypeID} | Delete an item type
[**get_item_type_by_id_async**](ItemTypesApi.md#get_item_type_by_id_async) | **GET** /api/v2/CatalogService/ItemTypes/{itemTypeID} | Get item type by ID
[**get_item_types_async**](ItemTypesApi.md#get_item_types_async) | **GET** /api/v2/CatalogService/ItemTypes | Get all item types
[**update_item_type_async**](ItemTypesApi.md#update_item_type_async) | **PUT** /api/v2/CatalogService/ItemTypes/{itemTypeID} | Update an item type


# **count_item_types_async**
> Int32Envelope count_item_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count item types

Counts all item types for the specified tenant.

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
    api_instance = openapi_client.ItemTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item types
        api_response = api_instance.count_item_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTypesApi->count_item_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTypesApi->count_item_types_async: %s\n" % e)
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

# **create_item_type_async**
> ItemTypeDtoEnvelope create_item_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_type_create_dto=item_type_create_dto)

Create a new item type

Creates a new item type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_type_create_dto import ItemTypeCreateDto
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_type_create_dto = openapi_client.ItemTypeCreateDto() # ItemTypeCreateDto |  (optional)

    try:
        # Create a new item type
        api_response = api_instance.create_item_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_type_create_dto=item_type_create_dto)
        print("The response of ItemTypesApi->create_item_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTypesApi->create_item_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_type_create_dto** | [**ItemTypeCreateDto**](ItemTypeCreateDto.md)|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **delete_item_type_async**
> ItemTypeDtoEnvelope delete_item_type_async(tenant_id, item_type_id, api_version=api_version, x_api_version=x_api_version)

Delete an item type

Deletes an item type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item type
        api_response = api_instance.delete_item_type_async(tenant_id, item_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTypesApi->delete_item_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTypesApi->delete_item_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **get_item_type_by_id_async**
> ItemTypeDtoEnvelope get_item_type_by_id_async(item_type_id, api_version=api_version, x_api_version=x_api_version)

Get item type by ID

Retrieves a specific item type by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemTypesApi(api_client)
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item type by ID
        api_response = api_instance.get_item_type_by_id_async(item_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTypesApi->get_item_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTypesApi->get_item_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **get_item_types_async**
> ItemTypeDtoListEnvelope get_item_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item types

Retrieves all item types for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_list_envelope import ItemTypeDtoListEnvelope
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
    api_instance = openapi_client.ItemTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item types
        api_response = api_instance.get_item_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTypesApi->get_item_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTypesApi->get_item_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoListEnvelope**](ItemTypeDtoListEnvelope.md)

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

# **update_item_type_async**
> update_item_type_async(tenant_id, item_type_id, api_version=api_version, x_api_version=x_api_version, item_type_update_dto=item_type_update_dto)

Update an item type

Updates an existing item type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_type_update_dto import ItemTypeUpdateDto
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
    api_instance = openapi_client.ItemTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_type_update_dto = openapi_client.ItemTypeUpdateDto() # ItemTypeUpdateDto |  (optional)

    try:
        # Update an item type
        api_instance.update_item_type_async(tenant_id, item_type_id, api_version=api_version, x_api_version=x_api_version, item_type_update_dto=item_type_update_dto)
    except Exception as e:
        print("Exception when calling ItemTypesApi->update_item_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_type_update_dto** | [**ItemTypeUpdateDto**](ItemTypeUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

