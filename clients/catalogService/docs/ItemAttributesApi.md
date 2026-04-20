# openapi_client.ItemAttributesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_attributes_async**](ItemAttributesApi.md#count_item_attributes_async) | **GET** /api/v2/CatalogService/ItemAttributes/Count | Count item attributes
[**create_item_attribute_async**](ItemAttributesApi.md#create_item_attribute_async) | **POST** /api/v2/CatalogService/ItemAttributes | Create a new item attribute
[**delete_item_attribute_async**](ItemAttributesApi.md#delete_item_attribute_async) | **DELETE** /api/v2/CatalogService/ItemAttributes/{itemAttributeId} | Delete an item attribute
[**get_item_attribute_by_id_async**](ItemAttributesApi.md#get_item_attribute_by_id_async) | **GET** /api/v2/CatalogService/ItemAttributes/{itemAttributeId} | Get item attribute by ID
[**get_item_attributes_async**](ItemAttributesApi.md#get_item_attributes_async) | **GET** /api/v2/CatalogService/ItemAttributes | Get all item attributes
[**update_item_attribute_async**](ItemAttributesApi.md#update_item_attribute_async) | **PUT** /api/v2/CatalogService/ItemAttributes/{itemAttributeId} | Update an item attribute


# **count_item_attributes_async**
> Int32Envelope count_item_attributes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count item attributes

Counts all item attributes for the specified tenant.

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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item attributes
        api_response = api_instance.count_item_attributes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributesApi->count_item_attributes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->count_item_attributes_async: %s\n" % e)
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

# **create_item_attribute_async**
> ItemAttributeDtoEnvelope create_item_attribute_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attribute_create_dto=item_attribute_create_dto)

Create a new item attribute

Creates a new item attribute for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_create_dto import ItemAttributeCreateDto
from openapi_client.models.item_attribute_dto_envelope import ItemAttributeDtoEnvelope
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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attribute_create_dto = openapi_client.ItemAttributeCreateDto() # ItemAttributeCreateDto |  (optional)

    try:
        # Create a new item attribute
        api_response = api_instance.create_item_attribute_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attribute_create_dto=item_attribute_create_dto)
        print("The response of ItemAttributesApi->create_item_attribute_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->create_item_attribute_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attribute_create_dto** | [**ItemAttributeCreateDto**](ItemAttributeCreateDto.md)|  | [optional] 

### Return type

[**ItemAttributeDtoEnvelope**](ItemAttributeDtoEnvelope.md)

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

# **delete_item_attribute_async**
> delete_item_attribute_async(tenant_id, item_attribute_id, api_version=api_version, x_api_version=x_api_version)

Delete an item attribute

Deletes an item attribute for the specified tenant.

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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attribute_id = 'item_attribute_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item attribute
        api_instance.delete_item_attribute_async(tenant_id, item_attribute_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->delete_item_attribute_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attribute_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_attribute_by_id_async**
> ItemAttributeDtoEnvelope get_item_attribute_by_id_async(item_attribute_id, api_version=api_version, x_api_version=x_api_version)

Get item attribute by ID

Retrieves a specific item attribute by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_dto_envelope import ItemAttributeDtoEnvelope
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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    item_attribute_id = 'item_attribute_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item attribute by ID
        api_response = api_instance.get_item_attribute_by_id_async(item_attribute_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributesApi->get_item_attribute_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->get_item_attribute_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_attribute_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeDtoEnvelope**](ItemAttributeDtoEnvelope.md)

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

# **get_item_attributes_async**
> ItemAttributeDtoListEnvelope get_item_attributes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item attributes

Retrieves all item attributes for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_dto_list_envelope import ItemAttributeDtoListEnvelope
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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item attributes
        api_response = api_instance.get_item_attributes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributesApi->get_item_attributes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->get_item_attributes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeDtoListEnvelope**](ItemAttributeDtoListEnvelope.md)

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

# **update_item_attribute_async**
> update_item_attribute_async(tenant_id, item_attribute_id, api_version=api_version, x_api_version=x_api_version, item_attribute_update_dto=item_attribute_update_dto)

Update an item attribute

Updates an existing item attribute for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_update_dto import ItemAttributeUpdateDto
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
    api_instance = openapi_client.ItemAttributesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attribute_id = 'item_attribute_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attribute_update_dto = openapi_client.ItemAttributeUpdateDto() # ItemAttributeUpdateDto |  (optional)

    try:
        # Update an item attribute
        api_instance.update_item_attribute_async(tenant_id, item_attribute_id, api_version=api_version, x_api_version=x_api_version, item_attribute_update_dto=item_attribute_update_dto)
    except Exception as e:
        print("Exception when calling ItemAttributesApi->update_item_attribute_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attribute_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attribute_update_dto** | [**ItemAttributeUpdateDto**](ItemAttributeUpdateDto.md)|  | [optional] 

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

