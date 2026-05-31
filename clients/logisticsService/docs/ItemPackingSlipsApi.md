# openapi_client.ItemPackingSlipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_packing_slip_async**](ItemPackingSlipsApi.md#create_item_packing_slip_async) | **POST** /api/v2/LogisticsService/ItemPackingSlips | Create an item packing slip
[**create_item_packing_slip_entry_async**](ItemPackingSlipsApi.md#create_item_packing_slip_entry_async) | **POST** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries | Create a packing slip entry
[**delete_item_packing_slip_async**](ItemPackingSlipsApi.md#delete_item_packing_slip_async) | **DELETE** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Delete an item packing slip
[**delete_item_packing_slip_entry_async**](ItemPackingSlipsApi.md#delete_item_packing_slip_entry_async) | **DELETE** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Delete a packing slip entry
[**get_item_packing_slip_by_id_async**](ItemPackingSlipsApi.md#get_item_packing_slip_by_id_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Get item packing slip by ID
[**get_item_packing_slip_entries_async**](ItemPackingSlipsApi.md#get_item_packing_slip_entries_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries | Get packing slip entries
[**get_item_packing_slip_entries_count_async**](ItemPackingSlipsApi.md#get_item_packing_slip_entries_count_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/Count | Get packing slip entries count
[**get_item_packing_slip_entry_by_id_async**](ItemPackingSlipsApi.md#get_item_packing_slip_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Get packing slip entry by ID
[**get_item_packing_slips_async**](ItemPackingSlipsApi.md#get_item_packing_slips_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips | Get all item packing slips
[**get_item_packing_slips_count_async**](ItemPackingSlipsApi.md#get_item_packing_slips_count_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/Count | Get item packing slips count
[**update_item_packing_slip_async**](ItemPackingSlipsApi.md#update_item_packing_slip_async) | **PUT** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Update an item packing slip
[**update_item_packing_slip_entry_async**](ItemPackingSlipsApi.md#update_item_packing_slip_entry_async) | **PUT** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Update a packing slip entry


# **create_item_packing_slip_async**
> EmptyEnvelope create_item_packing_slip_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_create_dto=item_packing_slip_create_dto)

Create an item packing slip

Creates a new item packing slip.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_packing_slip_create_dto import ItemPackingSlipCreateDto
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_create_dto = openapi_client.ItemPackingSlipCreateDto() # ItemPackingSlipCreateDto |  (optional)

    try:
        # Create an item packing slip
        api_response = api_instance.create_item_packing_slip_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_create_dto=item_packing_slip_create_dto)
        print("The response of ItemPackingSlipsApi->create_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->create_item_packing_slip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_packing_slip_create_dto** | [**ItemPackingSlipCreateDto**](ItemPackingSlipCreateDto.md)|  | [optional] 

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

# **create_item_packing_slip_entry_async**
> EmptyEnvelope create_item_packing_slip_entry_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_create_dto=item_packing_slip_entry_create_dto)

Create a packing slip entry

Creates a new packing slip entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_packing_slip_entry_create_dto import ItemPackingSlipEntryCreateDto
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_entry_create_dto = openapi_client.ItemPackingSlipEntryCreateDto() # ItemPackingSlipEntryCreateDto |  (optional)

    try:
        # Create a packing slip entry
        api_response = api_instance.create_item_packing_slip_entry_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_create_dto=item_packing_slip_entry_create_dto)
        print("The response of ItemPackingSlipsApi->create_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->create_item_packing_slip_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_packing_slip_entry_create_dto** | [**ItemPackingSlipEntryCreateDto**](ItemPackingSlipEntryCreateDto.md)|  | [optional] 

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

# **delete_item_packing_slip_async**
> EmptyEnvelope delete_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)

Delete an item packing slip

Deletes an item packing slip.

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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item packing slip
        api_response = api_instance.delete_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->delete_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->delete_item_packing_slip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
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

# **delete_item_packing_slip_entry_async**
> EmptyEnvelope delete_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Delete a packing slip entry

Deletes a packing slip entry.

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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a packing slip entry
        api_response = api_instance.delete_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->delete_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->delete_item_packing_slip_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
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

# **get_item_packing_slip_by_id_async**
> ItemPackingSlipDtoEnvelope get_item_packing_slip_by_id_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)

Get item packing slip by ID

Retrieves a specific item packing slip.

### Example


```python
import openapi_client
from openapi_client.models.item_packing_slip_dto_envelope import ItemPackingSlipDtoEnvelope
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item packing slip by ID
        api_response = api_instance.get_item_packing_slip_by_id_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slip_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slip_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPackingSlipDtoEnvelope**](ItemPackingSlipDtoEnvelope.md)

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

# **get_item_packing_slip_entries_async**
> ItemPackingSlipEntryDtoListEnvelope get_item_packing_slip_entries_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)

Get packing slip entries

Retrieves all entries for the specified packing slip.

### Example


```python
import openapi_client
from openapi_client.models.item_packing_slip_entry_dto_list_envelope import ItemPackingSlipEntryDtoListEnvelope
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entries
        api_response = api_instance.get_item_packing_slip_entries_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slip_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slip_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPackingSlipEntryDtoListEnvelope**](ItemPackingSlipEntryDtoListEnvelope.md)

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

# **get_item_packing_slip_entries_count_async**
> Int32Envelope get_item_packing_slip_entries_count_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)

Get packing slip entries count

Returns the count of packing slip entries.

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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entries count
        api_response = api_instance.get_item_packing_slip_entries_count_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slip_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slip_entries_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
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

# **get_item_packing_slip_entry_by_id_async**
> ItemPackingSlipEntryDtoEnvelope get_item_packing_slip_entry_by_id_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Get packing slip entry by ID

Retrieves a specific packing slip entry.

### Example


```python
import openapi_client
from openapi_client.models.item_packing_slip_entry_dto_envelope import ItemPackingSlipEntryDtoEnvelope
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entry by ID
        api_response = api_instance.get_item_packing_slip_entry_by_id_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slip_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slip_entry_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPackingSlipEntryDtoEnvelope**](ItemPackingSlipEntryDtoEnvelope.md)

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

# **get_item_packing_slips_async**
> ItemPackingSlipDtoListEnvelope get_item_packing_slips_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item packing slips

Retrieves all item packing slips for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_packing_slip_dto_list_envelope import ItemPackingSlipDtoListEnvelope
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item packing slips
        api_response = api_instance.get_item_packing_slips_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slips_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slips_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemPackingSlipDtoListEnvelope**](ItemPackingSlipDtoListEnvelope.md)

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

# **get_item_packing_slips_count_async**
> Int32Envelope get_item_packing_slips_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item packing slips count

Returns the count of item packing slips.

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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item packing slips count
        api_response = api_instance.get_item_packing_slips_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemPackingSlipsApi->get_item_packing_slips_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->get_item_packing_slips_count_async: %s\n" % e)
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

# **update_item_packing_slip_async**
> EmptyEnvelope update_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_update_dto=item_packing_slip_update_dto)

Update an item packing slip

Updates an existing item packing slip.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_packing_slip_update_dto import ItemPackingSlipUpdateDto
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_update_dto = openapi_client.ItemPackingSlipUpdateDto() # ItemPackingSlipUpdateDto |  (optional)

    try:
        # Update an item packing slip
        api_response = api_instance.update_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_update_dto=item_packing_slip_update_dto)
        print("The response of ItemPackingSlipsApi->update_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->update_item_packing_slip_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_packing_slip_update_dto** | [**ItemPackingSlipUpdateDto**](ItemPackingSlipUpdateDto.md)|  | [optional] 

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

# **update_item_packing_slip_entry_async**
> EmptyEnvelope update_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_update_dto=item_packing_slip_entry_update_dto)

Update a packing slip entry

Updates an existing packing slip entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_packing_slip_entry_update_dto import ItemPackingSlipEntryUpdateDto
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
    api_instance = openapi_client.ItemPackingSlipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_entry_update_dto = openapi_client.ItemPackingSlipEntryUpdateDto() # ItemPackingSlipEntryUpdateDto |  (optional)

    try:
        # Update a packing slip entry
        api_response = api_instance.update_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_update_dto=item_packing_slip_entry_update_dto)
        print("The response of ItemPackingSlipsApi->update_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemPackingSlipsApi->update_item_packing_slip_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **packing_slip_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_packing_slip_entry_update_dto** | [**ItemPackingSlipEntryUpdateDto**](ItemPackingSlipEntryUpdateDto.md)|  | [optional] 

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

