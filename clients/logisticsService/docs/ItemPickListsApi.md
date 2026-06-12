# openapi_client.ItemPickListsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_pick_list_async**](ItemPickListsApi.md#create_item_pick_list_async) | **POST** /api/v2/LogisticsService/ItemPickLists | Create an item pick list
[**create_item_pick_list_entry_async**](ItemPickListsApi.md#create_item_pick_list_entry_async) | **POST** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries | Create a pick list entry
[**delete_item_pick_list_async**](ItemPickListsApi.md#delete_item_pick_list_async) | **DELETE** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Delete an item pick list
[**delete_item_pick_list_entry_async**](ItemPickListsApi.md#delete_item_pick_list_entry_async) | **DELETE** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Delete a pick list entry
[**get_item_pick_list_by_id_async**](ItemPickListsApi.md#get_item_pick_list_by_id_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Get item pick list by ID
[**get_item_pick_list_entries_async**](ItemPickListsApi.md#get_item_pick_list_entries_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries | Get pick list entries
[**get_item_pick_list_entries_count_async**](ItemPickListsApi.md#get_item_pick_list_entries_count_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/Count | Get pick list entries count
[**get_item_pick_list_entry_by_id_async**](ItemPickListsApi.md#get_item_pick_list_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Get pick list entry by ID
[**get_item_pick_lists_async**](ItemPickListsApi.md#get_item_pick_lists_async) | **GET** /api/v2/LogisticsService/ItemPickLists | Get all item pick lists
[**get_item_pick_lists_count_async**](ItemPickListsApi.md#get_item_pick_lists_count_async) | **GET** /api/v2/LogisticsService/ItemPickLists/Count | Get item pick lists count
[**patch_item_pick_list_async**](ItemPickListsApi.md#patch_item_pick_list_async) | **PATCH** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Patch an item pick list
[**patch_item_pick_list_entry_async**](ItemPickListsApi.md#patch_item_pick_list_entry_async) | **PATCH** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Patch a pick list entry
[**update_item_pick_list_async**](ItemPickListsApi.md#update_item_pick_list_async) | **PUT** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Update an item pick list
[**update_item_pick_list_entry_async**](ItemPickListsApi.md#update_item_pick_list_entry_async) | **PUT** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Update a pick list entry


# **create_item_pick_list_async**
> EmptyEnvelope create_item_pick_list_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_create_dto=item_pick_list_create_dto)

Create an item pick list

Creates a new item pick list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_pick_list_create_dto import ItemPickListCreateDto
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_create_dto = openapi_client.ItemPickListCreateDto() # ItemPickListCreateDto |  (optional)

    try:
        # Create an item pick list
        api_response = api_instance.create_item_pick_list_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_create_dto=item_pick_list_create_dto)
        print("The response of ItemPickListsApi->create_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->create_item_pick_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_pick_list_create_dto** | [**ItemPickListCreateDto**](ItemPickListCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_pick_list_entry_async**
> EmptyEnvelope create_item_pick_list_entry_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_create_dto=item_pick_list_entry_create_dto)

Create a pick list entry

Creates a new pick list entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_pick_list_entry_create_dto import ItemPickListEntryCreateDto
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_entry_create_dto = openapi_client.ItemPickListEntryCreateDto() # ItemPickListEntryCreateDto |  (optional)

    try:
        # Create a pick list entry
        api_response = api_instance.create_item_pick_list_entry_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_create_dto=item_pick_list_entry_create_dto)
        print("The response of ItemPickListsApi->create_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->create_item_pick_list_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_pick_list_entry_create_dto** | [**ItemPickListEntryCreateDto**](ItemPickListEntryCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_pick_list_async**
> EmptyEnvelope delete_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)

Delete an item pick list

Deletes an item pick list.

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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item pick list
        api_response = api_instance.delete_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->delete_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->delete_item_pick_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_pick_list_entry_async**
> EmptyEnvelope delete_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Delete a pick list entry

Deletes a pick list entry.

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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a pick list entry
        api_response = api_instance.delete_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->delete_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->delete_item_pick_list_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **entry_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_pick_list_by_id_async**
> ItemPickListDtoEnvelope get_item_pick_list_by_id_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)

Get item pick list by ID

Retrieves a specific item pick list.

### Example


```python
import openapi_client
from openapi_client.models.item_pick_list_dto_envelope import ItemPickListDtoEnvelope
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item pick list by ID
        api_response = api_instance.get_item_pick_list_by_id_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_list_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_list_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPickListDtoEnvelope**](ItemPickListDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_pick_list_entries_async**
> ItemPickListEntryDtoListEnvelope get_item_pick_list_entries_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)

Get pick list entries

Retrieves all entries for the specified pick list.

### Example


```python
import openapi_client
from openapi_client.models.item_pick_list_entry_dto_list_envelope import ItemPickListEntryDtoListEnvelope
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entries
        api_response = api_instance.get_item_pick_list_entries_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_list_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_list_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPickListEntryDtoListEnvelope**](ItemPickListEntryDtoListEnvelope.md)

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

# **get_item_pick_list_entries_count_async**
> Int32Envelope get_item_pick_list_entries_count_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)

Get pick list entries count

Returns the count of pick list entries.

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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entries count
        api_response = api_instance.get_item_pick_list_entries_count_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_list_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_list_entries_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
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

# **get_item_pick_list_entry_by_id_async**
> ItemPickListEntryDtoEnvelope get_item_pick_list_entry_by_id_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Get pick list entry by ID

Retrieves a specific pick list entry.

### Example


```python
import openapi_client
from openapi_client.models.item_pick_list_entry_dto_envelope import ItemPickListEntryDtoEnvelope
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entry by ID
        api_response = api_instance.get_item_pick_list_entry_by_id_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_list_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_list_entry_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPickListEntryDtoEnvelope**](ItemPickListEntryDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_pick_lists_async**
> ItemPickListDtoListEnvelope get_item_pick_lists_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item pick lists

Retrieves all item pick lists for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_pick_list_dto_list_envelope import ItemPickListDtoListEnvelope
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item pick lists
        api_response = api_instance.get_item_pick_lists_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_lists_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_lists_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPickListDtoListEnvelope**](ItemPickListDtoListEnvelope.md)

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

# **get_item_pick_lists_count_async**
> Int32Envelope get_item_pick_lists_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item pick lists count

Returns the count of item pick lists.

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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item pick lists count
        api_response = api_instance.get_item_pick_lists_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPickListsApi->get_item_pick_lists_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->get_item_pick_lists_count_async: %s\n" % e)
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

# **patch_item_pick_list_async**
> EmptyEnvelope patch_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an item pick list

Applies a JSON Patch document to an item pick list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an item pick list
        api_response = api_instance.patch_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemPickListsApi->patch_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->patch_item_pick_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_item_pick_list_entry_async**
> EmptyEnvelope patch_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a pick list entry

Applies a JSON Patch document to a pick list entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a pick list entry
        api_response = api_instance.patch_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemPickListsApi->patch_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->patch_item_pick_list_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_pick_list_async**
> EmptyEnvelope update_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_update_dto=item_pick_list_update_dto)

Update an item pick list

Updates an existing item pick list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_pick_list_update_dto import ItemPickListUpdateDto
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_update_dto = openapi_client.ItemPickListUpdateDto() # ItemPickListUpdateDto |  (optional)

    try:
        # Update an item pick list
        api_response = api_instance.update_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_update_dto=item_pick_list_update_dto)
        print("The response of ItemPickListsApi->update_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->update_item_pick_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_pick_list_update_dto** | [**ItemPickListUpdateDto**](ItemPickListUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_pick_list_entry_async**
> EmptyEnvelope update_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_update_dto=item_pick_list_entry_update_dto)

Update a pick list entry

Updates an existing pick list entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_pick_list_entry_update_dto import ItemPickListEntryUpdateDto
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
    api_instance = openapi_client.ItemPickListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_entry_update_dto = openapi_client.ItemPickListEntryUpdateDto() # ItemPickListEntryUpdateDto |  (optional)

    try:
        # Update a pick list entry
        api_response = api_instance.update_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_update_dto=item_pick_list_entry_update_dto)
        print("The response of ItemPickListsApi->update_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPickListsApi->update_item_pick_list_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pick_list_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_pick_list_entry_update_dto** | [**ItemPickListEntryUpdateDto**](ItemPickListEntryUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

