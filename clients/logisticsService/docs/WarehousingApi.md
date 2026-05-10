# openapi_client.WarehousingApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_packing_slip_async**](WarehousingApi.md#create_item_packing_slip_async) | **POST** /api/v2/LogisticsService/ItemPackingSlips | Create an item packing slip
[**create_item_packing_slip_entry_async**](WarehousingApi.md#create_item_packing_slip_entry_async) | **POST** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries | Create a packing slip entry
[**create_item_pick_list_async**](WarehousingApi.md#create_item_pick_list_async) | **POST** /api/v2/LogisticsService/ItemPickLists | Create an item pick list
[**create_item_pick_list_entry_async**](WarehousingApi.md#create_item_pick_list_entry_async) | **POST** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries | Create a pick list entry
[**create_item_restock_async**](WarehousingApi.md#create_item_restock_async) | **POST** /api/v2/LogisticsService/ItemRestocks | Create an item restock
[**create_item_restock_entry_async**](WarehousingApi.md#create_item_restock_entry_async) | **POST** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries | Create a restock entry
[**create_item_retain_sample_async**](WarehousingApi.md#create_item_retain_sample_async) | **POST** /api/v2/LogisticsService/ItemRetainSamples | Create an item retain sample
[**create_warehouse_async**](WarehousingApi.md#create_warehouse_async) | **POST** /api/v2/LogisticsService/Warehouses | Create a warehouse
[**delete_item_packing_slip_async**](WarehousingApi.md#delete_item_packing_slip_async) | **DELETE** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Delete an item packing slip
[**delete_item_packing_slip_entry_async**](WarehousingApi.md#delete_item_packing_slip_entry_async) | **DELETE** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Delete a packing slip entry
[**delete_item_pick_list_async**](WarehousingApi.md#delete_item_pick_list_async) | **DELETE** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Delete an item pick list
[**delete_item_pick_list_entry_async**](WarehousingApi.md#delete_item_pick_list_entry_async) | **DELETE** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Delete a pick list entry
[**delete_item_restock_async**](WarehousingApi.md#delete_item_restock_async) | **DELETE** /api/v2/LogisticsService/ItemRestocks/{restockId} | Delete an item restock
[**delete_item_restock_entry_async**](WarehousingApi.md#delete_item_restock_entry_async) | **DELETE** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Delete a restock entry
[**delete_item_retain_sample_async**](WarehousingApi.md#delete_item_retain_sample_async) | **DELETE** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Delete an item retain sample
[**delete_warehouse_async**](WarehousingApi.md#delete_warehouse_async) | **DELETE** /api/v2/LogisticsService/Warehouses/{warehouseId} | Delete a warehouse
[**get_item_packing_slip_by_id_async**](WarehousingApi.md#get_item_packing_slip_by_id_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Get item packing slip by ID
[**get_item_packing_slip_entries_async**](WarehousingApi.md#get_item_packing_slip_entries_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries | Get packing slip entries
[**get_item_packing_slip_entries_count_async**](WarehousingApi.md#get_item_packing_slip_entries_count_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/Count | Get packing slip entries count
[**get_item_packing_slip_entry_by_id_async**](WarehousingApi.md#get_item_packing_slip_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Get packing slip entry by ID
[**get_item_packing_slips_async**](WarehousingApi.md#get_item_packing_slips_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips | Get all item packing slips
[**get_item_packing_slips_count_async**](WarehousingApi.md#get_item_packing_slips_count_async) | **GET** /api/v2/LogisticsService/ItemPackingSlips/Count | Get item packing slips count
[**get_item_pick_list_by_id_async**](WarehousingApi.md#get_item_pick_list_by_id_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Get item pick list by ID
[**get_item_pick_list_entries_async**](WarehousingApi.md#get_item_pick_list_entries_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries | Get pick list entries
[**get_item_pick_list_entries_count_async**](WarehousingApi.md#get_item_pick_list_entries_count_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/Count | Get pick list entries count
[**get_item_pick_list_entry_by_id_async**](WarehousingApi.md#get_item_pick_list_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Get pick list entry by ID
[**get_item_pick_lists_async**](WarehousingApi.md#get_item_pick_lists_async) | **GET** /api/v2/LogisticsService/ItemPickLists | Get all item pick lists
[**get_item_pick_lists_count_async**](WarehousingApi.md#get_item_pick_lists_count_async) | **GET** /api/v2/LogisticsService/ItemPickLists/Count | Get item pick lists count
[**get_item_restock_by_id_async**](WarehousingApi.md#get_item_restock_by_id_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId} | Get item restock by ID
[**get_item_restock_entries_async**](WarehousingApi.md#get_item_restock_entries_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries | Get restock entries
[**get_item_restock_entries_count_async**](WarehousingApi.md#get_item_restock_entries_count_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/Count | Get restock entries count
[**get_item_restock_entry_by_id_async**](WarehousingApi.md#get_item_restock_entry_by_id_async) | **GET** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Get restock entry by ID
[**get_item_restocks_async**](WarehousingApi.md#get_item_restocks_async) | **GET** /api/v2/LogisticsService/ItemRestocks | Get all item restocks
[**get_item_restocks_count_async**](WarehousingApi.md#get_item_restocks_count_async) | **GET** /api/v2/LogisticsService/ItemRestocks/Count | Get item restocks count
[**get_item_retain_sample_by_id_async**](WarehousingApi.md#get_item_retain_sample_by_id_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Get item retain sample by ID
[**get_item_retain_samples_async**](WarehousingApi.md#get_item_retain_samples_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples | Get all item retain samples
[**get_item_retain_samples_count_async**](WarehousingApi.md#get_item_retain_samples_count_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples/Count | Get item retain samples count
[**get_warehouse_by_id_async**](WarehousingApi.md#get_warehouse_by_id_async) | **GET** /api/v2/LogisticsService/Warehouses/{warehouseId} | Get warehouse by ID
[**get_warehouses_async**](WarehousingApi.md#get_warehouses_async) | **GET** /api/v2/LogisticsService/Warehouses | Get all warehouses
[**get_warehouses_count_async**](WarehousingApi.md#get_warehouses_count_async) | **GET** /api/v2/LogisticsService/Warehouses/Count | Get warehouses count
[**update_item_packing_slip_async**](WarehousingApi.md#update_item_packing_slip_async) | **PUT** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId} | Update an item packing slip
[**update_item_packing_slip_entry_async**](WarehousingApi.md#update_item_packing_slip_entry_async) | **PUT** /api/v2/LogisticsService/ItemPackingSlips/{packingSlipId}/Entries/{entryId} | Update a packing slip entry
[**update_item_pick_list_async**](WarehousingApi.md#update_item_pick_list_async) | **PUT** /api/v2/LogisticsService/ItemPickLists/{pickListId} | Update an item pick list
[**update_item_pick_list_entry_async**](WarehousingApi.md#update_item_pick_list_entry_async) | **PUT** /api/v2/LogisticsService/ItemPickLists/{pickListId}/Entries/{entryId} | Update a pick list entry
[**update_item_restock_async**](WarehousingApi.md#update_item_restock_async) | **PUT** /api/v2/LogisticsService/ItemRestocks/{restockId} | Update an item restock
[**update_item_restock_entry_async**](WarehousingApi.md#update_item_restock_entry_async) | **PUT** /api/v2/LogisticsService/ItemRestocks/{restockId}/Entries/{entryId} | Update a restock entry
[**update_item_retain_sample_async**](WarehousingApi.md#update_item_retain_sample_async) | **PUT** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Update an item retain sample
[**update_warehouse_async**](WarehousingApi.md#update_warehouse_async) | **PUT** /api/v2/LogisticsService/Warehouses/{warehouseId} | Update a warehouse


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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_create_dto = openapi_client.ItemPackingSlipCreateDto() # ItemPackingSlipCreateDto |  (optional)

    try:
        # Create an item packing slip
        api_response = api_instance.create_item_packing_slip_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_create_dto=item_packing_slip_create_dto)
        print("The response of WarehousingApi->create_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_packing_slip_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_entry_create_dto = openapi_client.ItemPackingSlipEntryCreateDto() # ItemPackingSlipEntryCreateDto |  (optional)

    try:
        # Create a packing slip entry
        api_response = api_instance.create_item_packing_slip_entry_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_create_dto=item_packing_slip_entry_create_dto)
        print("The response of WarehousingApi->create_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_packing_slip_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_create_dto = openapi_client.ItemPickListCreateDto() # ItemPickListCreateDto |  (optional)

    try:
        # Create an item pick list
        api_response = api_instance.create_item_pick_list_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_create_dto=item_pick_list_create_dto)
        print("The response of WarehousingApi->create_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_pick_list_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_entry_create_dto = openapi_client.ItemPickListEntryCreateDto() # ItemPickListEntryCreateDto |  (optional)

    try:
        # Create a pick list entry
        api_response = api_instance.create_item_pick_list_entry_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_create_dto=item_pick_list_entry_create_dto)
        print("The response of WarehousingApi->create_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_pick_list_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_create_dto = openapi_client.ItemRestockCreateDto() # ItemRestockCreateDto |  (optional)

    try:
        # Create an item restock
        api_response = api_instance.create_item_restock_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_restock_create_dto=item_restock_create_dto)
        print("The response of WarehousingApi->create_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_restock_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_entry_create_dto = openapi_client.ItemRestockEntryCreateDto() # ItemRestockEntryCreateDto |  (optional)

    try:
        # Create a restock entry
        api_response = api_instance.create_item_restock_entry_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_create_dto=item_restock_entry_create_dto)
        print("The response of WarehousingApi->create_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_restock_entry_async: %s\n" % e)
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

# **create_item_retain_sample_async**
> EmptyEnvelope create_item_retain_sample_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_create_dto=item_retain_sample_create_dto)

Create an item retain sample

Creates a new item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_retain_sample_create_dto import ItemRetainSampleCreateDto
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_retain_sample_create_dto = openapi_client.ItemRetainSampleCreateDto() # ItemRetainSampleCreateDto |  (optional)

    try:
        # Create an item retain sample
        api_response = api_instance.create_item_retain_sample_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_create_dto=item_retain_sample_create_dto)
        print("The response of WarehousingApi->create_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_retain_sample_create_dto** | [**ItemRetainSampleCreateDto**](ItemRetainSampleCreateDto.md)|  | [optional] 

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

# **create_warehouse_async**
> EmptyEnvelope create_warehouse_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warehouse_create_dto=warehouse_create_dto)

Create a warehouse

Creates a new warehouse.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warehouse_create_dto import WarehouseCreateDto
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warehouse_create_dto = openapi_client.WarehouseCreateDto() # WarehouseCreateDto |  (optional)

    try:
        # Create a warehouse
        api_response = api_instance.create_warehouse_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warehouse_create_dto=warehouse_create_dto)
        print("The response of WarehousingApi->create_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->create_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warehouse_create_dto** | [**WarehouseCreateDto**](WarehouseCreateDto.md)|  | [optional] 

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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item packing slip
        api_response = api_instance.delete_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_packing_slip_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a packing slip entry
        api_response = api_instance.delete_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_packing_slip_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item pick list
        api_response = api_instance.delete_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_pick_list_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a pick list entry
        api_response = api_instance.delete_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_pick_list_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item restock
        api_response = api_instance.delete_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_restock_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a restock entry
        api_response = api_instance.delete_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_restock_entry_async: %s\n" % e)
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

# **delete_item_retain_sample_async**
> EmptyEnvelope delete_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)

Delete an item retain sample

Deletes an item retain sample.

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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item retain sample
        api_response = api_instance.delete_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
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

# **delete_warehouse_async**
> EmptyEnvelope delete_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)

Delete a warehouse

Deletes a warehouse.

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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a warehouse
        api_response = api_instance.delete_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->delete_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->delete_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item packing slip by ID
        api_response = api_instance.get_item_packing_slip_by_id_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slip_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slip_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entries
        api_response = api_instance.get_item_packing_slip_entries_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slip_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slip_entries_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entries count
        api_response = api_instance.get_item_packing_slip_entries_count_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slip_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slip_entries_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get packing slip entry by ID
        api_response = api_instance.get_item_packing_slip_entry_by_id_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slip_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slip_entry_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item packing slips
        api_response = api_instance.get_item_packing_slips_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slips_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slips_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item packing slips count
        api_response = api_instance.get_item_packing_slips_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_packing_slips_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_packing_slips_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item pick list by ID
        api_response = api_instance.get_item_pick_list_by_id_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_list_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_list_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entries
        api_response = api_instance.get_item_pick_list_entries_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_list_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_list_entries_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entries count
        api_response = api_instance.get_item_pick_list_entries_count_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_list_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_list_entries_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pick list entry by ID
        api_response = api_instance.get_item_pick_list_entry_by_id_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_list_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_list_entry_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item pick lists
        api_response = api_instance.get_item_pick_lists_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_lists_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_lists_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item pick lists count
        api_response = api_instance.get_item_pick_lists_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_pick_lists_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_pick_lists_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item restock by ID
        api_response = api_instance.get_item_restock_by_id_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restock_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restock_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entries
        api_response = api_instance.get_item_restock_entries_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restock_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restock_entries_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entries count
        api_response = api_instance.get_item_restock_entries_count_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restock_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restock_entries_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get restock entry by ID
        api_response = api_instance.get_item_restock_entry_by_id_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restock_entry_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restock_entry_by_id_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item restocks
        api_response = api_instance.get_item_restocks_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restocks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restocks_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item restocks count
        api_response = api_instance.get_item_restocks_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_restocks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_restocks_count_async: %s\n" % e)
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

# **get_item_retain_sample_by_id_async**
> ItemRetainSampleDtoEnvelope get_item_retain_sample_by_id_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)

Get item retain sample by ID

Retrieves a specific item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.item_retain_sample_dto_envelope import ItemRetainSampleDtoEnvelope
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item retain sample by ID
        api_response = api_instance.get_item_retain_sample_by_id_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_retain_sample_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_retain_sample_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRetainSampleDtoEnvelope**](ItemRetainSampleDtoEnvelope.md)

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

# **get_item_retain_samples_async**
> ItemRetainSampleDtoListEnvelope get_item_retain_samples_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item retain samples

Retrieves all item retain samples for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_retain_sample_dto_list_envelope import ItemRetainSampleDtoListEnvelope
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item retain samples
        api_response = api_instance.get_item_retain_samples_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_retain_samples_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_retain_samples_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRetainSampleDtoListEnvelope**](ItemRetainSampleDtoListEnvelope.md)

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

# **get_item_retain_samples_count_async**
> Int32Envelope get_item_retain_samples_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item retain samples count

Returns the count of item retain samples.

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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item retain samples count
        api_response = api_instance.get_item_retain_samples_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_item_retain_samples_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_item_retain_samples_count_async: %s\n" % e)
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

# **get_warehouse_by_id_async**
> WarehouseDtoEnvelope get_warehouse_by_id_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)

Get warehouse by ID

Retrieves a specific warehouse.

### Example


```python
import openapi_client
from openapi_client.models.warehouse_dto_envelope import WarehouseDtoEnvelope
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warehouse by ID
        api_response = api_instance.get_warehouse_by_id_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_warehouse_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_warehouse_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarehouseDtoEnvelope**](WarehouseDtoEnvelope.md)

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

# **get_warehouses_async**
> WarehouseDtoListEnvelope get_warehouses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all warehouses

Retrieves all warehouses for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.warehouse_dto_list_envelope import WarehouseDtoListEnvelope
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all warehouses
        api_response = api_instance.get_warehouses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_warehouses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_warehouses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarehouseDtoListEnvelope**](WarehouseDtoListEnvelope.md)

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

# **get_warehouses_count_async**
> Int32Envelope get_warehouses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get warehouses count

Returns the count of warehouses.

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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warehouses count
        api_response = api_instance.get_warehouses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarehousingApi->get_warehouses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->get_warehouses_count_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_update_dto = openapi_client.ItemPackingSlipUpdateDto() # ItemPackingSlipUpdateDto |  (optional)

    try:
        # Update an item packing slip
        api_response = api_instance.update_item_packing_slip_async(tenant_id, packing_slip_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_update_dto=item_packing_slip_update_dto)
        print("The response of WarehousingApi->update_item_packing_slip_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_packing_slip_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    packing_slip_id = 'packing_slip_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_packing_slip_entry_update_dto = openapi_client.ItemPackingSlipEntryUpdateDto() # ItemPackingSlipEntryUpdateDto |  (optional)

    try:
        # Update a packing slip entry
        api_response = api_instance.update_item_packing_slip_entry_async(tenant_id, packing_slip_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_packing_slip_entry_update_dto=item_packing_slip_entry_update_dto)
        print("The response of WarehousingApi->update_item_packing_slip_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_packing_slip_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_update_dto = openapi_client.ItemPickListUpdateDto() # ItemPickListUpdateDto |  (optional)

    try:
        # Update an item pick list
        api_response = api_instance.update_item_pick_list_async(tenant_id, pick_list_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_update_dto=item_pick_list_update_dto)
        print("The response of WarehousingApi->update_item_pick_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_pick_list_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pick_list_id = 'pick_list_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_pick_list_entry_update_dto = openapi_client.ItemPickListEntryUpdateDto() # ItemPickListEntryUpdateDto |  (optional)

    try:
        # Update a pick list entry
        api_response = api_instance.update_item_pick_list_entry_async(tenant_id, pick_list_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_pick_list_entry_update_dto=item_pick_list_entry_update_dto)
        print("The response of WarehousingApi->update_item_pick_list_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_pick_list_entry_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_update_dto = openapi_client.ItemRestockUpdateDto() # ItemRestockUpdateDto |  (optional)

    try:
        # Update an item restock
        api_response = api_instance.update_item_restock_async(tenant_id, restock_id, api_version=api_version, x_api_version=x_api_version, item_restock_update_dto=item_restock_update_dto)
        print("The response of WarehousingApi->update_item_restock_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_restock_async: %s\n" % e)
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    restock_id = 'restock_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_restock_entry_update_dto = openapi_client.ItemRestockEntryUpdateDto() # ItemRestockEntryUpdateDto |  (optional)

    try:
        # Update a restock entry
        api_response = api_instance.update_item_restock_entry_async(tenant_id, restock_id, entry_id, api_version=api_version, x_api_version=x_api_version, item_restock_entry_update_dto=item_restock_entry_update_dto)
        print("The response of WarehousingApi->update_item_restock_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_restock_entry_async: %s\n" % e)
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

# **update_item_retain_sample_async**
> EmptyEnvelope update_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_update_dto=item_retain_sample_update_dto)

Update an item retain sample

Updates an existing item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_retain_sample_update_dto import ItemRetainSampleUpdateDto
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_retain_sample_update_dto = openapi_client.ItemRetainSampleUpdateDto() # ItemRetainSampleUpdateDto |  (optional)

    try:
        # Update an item retain sample
        api_response = api_instance.update_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_update_dto=item_retain_sample_update_dto)
        print("The response of WarehousingApi->update_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_retain_sample_update_dto** | [**ItemRetainSampleUpdateDto**](ItemRetainSampleUpdateDto.md)|  | [optional] 

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

# **update_warehouse_async**
> EmptyEnvelope update_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version, warehouse_update_dto=warehouse_update_dto)

Update a warehouse

Updates an existing warehouse.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warehouse_update_dto import WarehouseUpdateDto
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
    api_instance = openapi_client.WarehousingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warehouse_id = 'warehouse_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warehouse_update_dto = openapi_client.WarehouseUpdateDto() # WarehouseUpdateDto |  (optional)

    try:
        # Update a warehouse
        api_response = api_instance.update_warehouse_async(tenant_id, warehouse_id, api_version=api_version, x_api_version=x_api_version, warehouse_update_dto=warehouse_update_dto)
        print("The response of WarehousingApi->update_warehouse_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousingApi->update_warehouse_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warehouse_update_dto** | [**WarehouseUpdateDto**](WarehouseUpdateDto.md)|  | [optional] 

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

