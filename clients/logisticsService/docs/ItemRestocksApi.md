# openapi_client.ItemRestocksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_restock_async**](ItemRestocksApi.md#create_item_restock_async) | **POST** /api/v2/LogisticsService/ItemRestocks | Create an item restock
[**create_item_restock_entry_async**](ItemRestocksApi.md#create_item_restock_entry_async) | **POST** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries | Create a restock entry
[**delete_item_restock_async**](ItemRestocksApi.md#delete_item_restock_async) | **DELETE** /api/v2/LogisticsService/ItemRestocks/{restockId} | Delete an item restock
[**delete_item_restock_entry_async**](ItemRestocksApi.md#delete_item_restock_entry_async) | **DELETE** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Delete a restock entry
[**get_item_restock_by_id_async**](ItemRestocksApi.md#get_item_restock_by_id_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId} | Get item restock by ID
[**get_item_restock_entries_async**](ItemRestocksApi.md#get_item_restock_entries_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries | Get restock entries
[**get_item_restock_entries_count_async**](ItemRestocksApi.md#get_item_restock_entries_count_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/Count | Get restock entries count
[**get_item_restock_entry_by_id_async**](ItemRestocksApi.md#get_item_restock_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Get restock entry by ID
[**get_item_restocks_async**](ItemRestocksApi.md#get_item_restocks_async) | **GET** /api/v2/LogisticsService/ItemRestocks | Get all item restocks
[**get_item_restocks_count_async**](ItemRestocksApi.md#get_item_restocks_count_async) | **GET** /api/v2/LogisticsService/ItemRestocks/Count | Get item restocks count
[**patch_item_restock_async**](ItemRestocksApi.md#patch_item_restock_async) | **PATCH** /api/v2/LogisticsService/ItemRestocks/{restockId} | Patch an item restock
[**patch_item_restock_entry_async**](ItemRestocksApi.md#patch_item_restock_entry_async) | **PATCH** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Patch a restock entry
[**update_item_restock_async**](ItemRestocksApi.md#update_item_restock_async) | **PUT** /api/v2/LogisticsService/ItemRestocks/{restockId} | Update an item restock
[**update_item_restock_entry_async**](ItemRestocksApi.md#update_item_restock_entry_async) | **PUT** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Update a restock entry


# **create_item_restock_async**
> EmptyEnvelope create_item_restock_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_restock_create_dto=item_restock_create_dto)

Create an item restock

Creates a new item restock.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_restock_create_dto import ItemRestockCreateDto
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_create_dto = openapi_client.ItemRestockCreateDto() # ItemRestockCreateDto |  (optional)

    try:
        # Create an item restock
        api_response = api_instance.create_item_restock_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_restock_create_dto=item_restock_create_dto)
        print("The response of ItemRestocksApi->create_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->create_item_restock_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_restock_create_dto** | [**ItemRestockCreateDto**](ItemRestockCreateDto.md)|  | [optional] 

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

# **create_item_restock_entry_async**
> EmptyEnvelope create_item_restock_entry_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_create_dto=item_restock_entry_create_dto)

Create a restock entry

Creates a new restock entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_restock_entry_create_dto import ItemRestockEntryCreateDto
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_entry_create_dto = openapi_client.ItemRestockEntryCreateDto() # ItemRestockEntryCreateDto |  (optional)

    try:
        # Create a restock entry
        api_response = api_instance.create_item_restock_entry_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_create_dto=item_restock_entry_create_dto)
        print("The response of ItemRestocksApi->create_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->create_item_restock_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_restock_entry_create_dto** | [**ItemRestockEntryCreateDto**](ItemRestockEntryCreateDto.md)|  | [optional] 

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

# **delete_item_restock_async**
> EmptyEnvelope delete_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)

Delete an item restock

Deletes an item restock.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item restock
        api_response = api_instance.delete_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->delete_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->delete_item_restock_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
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

# **delete_item_restock_entry_async**
> EmptyEnvelope delete_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Delete a restock entry

Deletes a restock entry.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a restock entry
        api_response = api_instance.delete_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->delete_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->delete_item_restock_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
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

# **get_item_restock_by_id_async**
> ItemRestockDtoEnvelope get_item_restock_by_id_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)

Get item restock by ID

Retrieves a specific item restock.

### Example


```python
import openapi_client
from openapi_client.models.item_restock_dto_envelope import ItemRestockDtoEnvelope
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item restock by ID
        api_response = api_instance.get_item_restock_by_id_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restock_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restock_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRestockDtoEnvelope**](ItemRestockDtoEnvelope.md)

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

# **get_item_restock_entries_async**
> ItemRestockEntryDtoListEnvelope get_item_restock_entries_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)

Get restock entries

Retrieves all entries for the specified restock.

### Example


```python
import openapi_client
from openapi_client.models.item_restock_entry_dto_list_envelope import ItemRestockEntryDtoListEnvelope
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entries
        api_response = api_instance.get_item_restock_entries_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restock_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restock_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRestockEntryDtoListEnvelope**](ItemRestockEntryDtoListEnvelope.md)

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

# **get_item_restock_entries_count_async**
> Int32Envelope get_item_restock_entries_count_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)

Get restock entries count

Returns the count of restock entries.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entries count
        api_response = api_instance.get_item_restock_entries_count_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restock_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restock_entries_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
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

# **get_item_restock_entry_by_id_async**
> ItemRestockEntryDtoEnvelope get_item_restock_entry_by_id_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Get restock entry by ID

Retrieves a specific restock entry.

### Example


```python
import openapi_client
from openapi_client.models.item_restock_entry_dto_envelope import ItemRestockEntryDtoEnvelope
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entry by ID
        api_response = api_instance.get_item_restock_entry_by_id_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restock_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restock_entry_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRestockEntryDtoEnvelope**](ItemRestockEntryDtoEnvelope.md)

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

# **get_item_restocks_async**
> ItemRestockDtoListEnvelope get_item_restocks_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item restocks

Retrieves all item restocks for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_restock_dto_list_envelope import ItemRestockDtoListEnvelope
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item restocks
        api_response = api_instance.get_item_restocks_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restocks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restocks_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRestockDtoListEnvelope**](ItemRestockDtoListEnvelope.md)

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

# **get_item_restocks_count_async**
> Int32Envelope get_item_restocks_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item restocks count

Returns the count of item restocks.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item restocks count
        api_response = api_instance.get_item_restocks_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRestocksApi->get_item_restocks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->get_item_restocks_count_async: %s\n" % e)
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

# **patch_item_restock_async**
> EmptyEnvelope patch_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an item restock

Applies a JSON Patch document to an item restock.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an item restock
        api_response = api_instance.patch_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemRestocksApi->patch_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->patch_item_restock_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
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

# **patch_item_restock_entry_async**
> EmptyEnvelope patch_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a restock entry

Applies a JSON Patch document to a restock entry.

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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a restock entry
        api_response = api_instance.patch_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemRestocksApi->patch_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->patch_item_restock_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
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

# **update_item_restock_async**
> EmptyEnvelope update_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_update_dto=item_restock_update_dto)

Update an item restock

Updates an existing item restock.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_restock_update_dto import ItemRestockUpdateDto
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_update_dto = openapi_client.ItemRestockUpdateDto() # ItemRestockUpdateDto |  (optional)

    try:
        # Update an item restock
        api_response = api_instance.update_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_update_dto=item_restock_update_dto)
        print("The response of ItemRestocksApi->update_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->update_item_restock_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_restock_update_dto** | [**ItemRestockUpdateDto**](ItemRestockUpdateDto.md)|  | [optional] 

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

# **update_item_restock_entry_async**
> EmptyEnvelope update_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_update_dto=item_restock_entry_update_dto)

Update a restock entry

Updates an existing restock entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_restock_entry_update_dto import ItemRestockEntryUpdateDto
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
    api_instance = openapi_client.ItemRestocksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_entry_update_dto = openapi_client.ItemRestockEntryUpdateDto() # ItemRestockEntryUpdateDto |  (optional)

    try:
        # Update a restock entry
        api_response = api_instance.update_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_update_dto=item_restock_entry_update_dto)
        print("The response of ItemRestocksApi->update_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRestocksApi->update_item_restock_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **restock_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_restock_entry_update_dto** | [**ItemRestockEntryUpdateDto**](ItemRestockEntryUpdateDto.md)|  | [optional] 

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

