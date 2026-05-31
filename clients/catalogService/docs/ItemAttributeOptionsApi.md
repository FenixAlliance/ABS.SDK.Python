# openapi_client.ItemAttributeOptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_attribute_option_async**](ItemAttributeOptionsApi.md#create_item_attribute_option_async) | **POST** /api/v2/CatalogService/ItemAttributeOptions | Create a new item attribute option
[**delete_item_attribute_option_async**](ItemAttributeOptionsApi.md#delete_item_attribute_option_async) | **DELETE** /api/v2/CatalogService/ItemAttributeOptions/{itemAttributeOptionId} | Delete an item attribute option
[**get_item_attribute_option_by_id_async**](ItemAttributeOptionsApi.md#get_item_attribute_option_by_id_async) | **GET** /api/v2/CatalogService/ItemAttributeOptions/{itemAttributeOptionId} | Get item attribute option by ID
[**get_item_attribute_options_async**](ItemAttributeOptionsApi.md#get_item_attribute_options_async) | **GET** /api/v2/CatalogService/ItemAttributeOptions | Get all item attribute options
[**get_item_attribute_options_count_async**](ItemAttributeOptionsApi.md#get_item_attribute_options_count_async) | **GET** /api/v2/CatalogService/ItemAttributeOptions/Count | Get item attribute options count
[**update_item_attribute_option_async**](ItemAttributeOptionsApi.md#update_item_attribute_option_async) | **PUT** /api/v2/CatalogService/ItemAttributeOptions/{itemAttributeOptionId} | Update an item attribute option


# **create_item_attribute_option_async**
> ItemAttributeOptionDtoEnvelope create_item_attribute_option_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attribute_option_create_dto=item_attribute_option_create_dto)

Create a new item attribute option

Creates a new item attribute option for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_create_dto import ItemAttributeOptionCreateDto
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attribute_option_create_dto = openapi_client.ItemAttributeOptionCreateDto() # ItemAttributeOptionCreateDto |  (optional)

    try:
        # Create a new item attribute option
        api_response = api_instance.create_item_attribute_option_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_attribute_option_create_dto=item_attribute_option_create_dto)
        print("The response of ItemAttributeOptionsApi->create_item_attribute_option_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->create_item_attribute_option_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attribute_option_create_dto** | [**ItemAttributeOptionCreateDto**](ItemAttributeOptionCreateDto.md)|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

# **delete_item_attribute_option_async**
> delete_item_attribute_option_async(tenant_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)

Delete an item attribute option

Deletes an item attribute option for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item attribute option
        api_instance.delete_item_attribute_option_async(tenant_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->delete_item_attribute_option_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attribute_option_id** | **str**|  | 
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

# **get_item_attribute_option_by_id_async**
> ItemAttributeOptionDtoEnvelope get_item_attribute_option_by_id_async(item_attribute_option_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item attribute option by ID

Retrieves a specific item attribute option by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item attribute option by ID
        api_response = api_instance.get_item_attribute_option_by_id_async(item_attribute_option_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributeOptionsApi->get_item_attribute_option_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->get_item_attribute_option_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_attribute_option_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

# **get_item_attribute_options_async**
> ItemAttributeOptionDtoListEnvelope get_item_attribute_options_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item attribute options

Retrieves all item attribute options for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_list_envelope import ItemAttributeOptionDtoListEnvelope
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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item attribute options
        api_response = api_instance.get_item_attribute_options_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributeOptionsApi->get_item_attribute_options_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->get_item_attribute_options_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoListEnvelope**](ItemAttributeOptionDtoListEnvelope.md)

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

# **get_item_attribute_options_count_async**
> Int32Envelope get_item_attribute_options_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item attribute options count

Returns the count of item attribute options for the specified tenant.

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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item attribute options count
        api_response = api_instance.get_item_attribute_options_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemAttributeOptionsApi->get_item_attribute_options_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->get_item_attribute_options_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
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

# **update_item_attribute_option_async**
> ItemAttributeOptionDtoEnvelope update_item_attribute_option_async(tenant_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version, item_attribute_option_update_dto=item_attribute_option_update_dto)

Update an item attribute option

Updates an existing item attribute option for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
from openapi_client.models.item_attribute_option_update_dto import ItemAttributeOptionUpdateDto
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
    api_instance = openapi_client.ItemAttributeOptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attribute_option_update_dto = openapi_client.ItemAttributeOptionUpdateDto() # ItemAttributeOptionUpdateDto |  (optional)

    try:
        # Update an item attribute option
        api_response = api_instance.update_item_attribute_option_async(tenant_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version, item_attribute_option_update_dto=item_attribute_option_update_dto)
        print("The response of ItemAttributeOptionsApi->update_item_attribute_option_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemAttributeOptionsApi->update_item_attribute_option_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_attribute_option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attribute_option_update_dto** | [**ItemAttributeOptionUpdateDto**](ItemAttributeOptionUpdateDto.md)|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

