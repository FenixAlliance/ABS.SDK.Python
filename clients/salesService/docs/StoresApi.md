# openapi_client.StoresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_stores_async**](StoresApi.md#count_stores_async) | **GET** /api/v2/SalesService/Stores/Count | Get stores count
[**create_store_async**](StoresApi.md#create_store_async) | **POST** /api/v2/SalesService/Stores | Create a store
[**delete_store_async**](StoresApi.md#delete_store_async) | **DELETE** /api/v2/SalesService/Stores/{storeId} | Delete a store
[**get_store_async**](StoresApi.md#get_store_async) | **GET** /api/v2/SalesService/Stores/{storeId} | Get store by ID
[**get_stores_async**](StoresApi.md#get_stores_async) | **GET** /api/v2/SalesService/Stores | Get stores
[**update_store_async**](StoresApi.md#update_store_async) | **PUT** /api/v2/SalesService/Stores/{storeId} | Update a store


# **count_stores_async**
> Int32Envelope count_stores_async(tenant_id)

Get stores count

Returns the total count of stores for the specified tenant with OData filter support.

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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get stores count
        api_response = api_instance.count_stores_async(tenant_id)
        print("The response of StoresApi->count_stores_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->count_stores_async: %s\n" % e)
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_store_async**
> EmptyEnvelope create_store_async(tenant_id, store_create_dto=store_create_dto)

Create a store

Creates a new store for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.store_create_dto import StoreCreateDto
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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    store_create_dto = openapi_client.StoreCreateDto() # StoreCreateDto |  (optional)

    try:
        # Create a store
        api_response = api_instance.create_store_async(tenant_id, store_create_dto=store_create_dto)
        print("The response of StoresApi->create_store_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->create_store_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **store_create_dto** | [**StoreCreateDto**](StoreCreateDto.md)|  | [optional] 

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

# **delete_store_async**
> EmptyEnvelope delete_store_async(tenant_id, store_id)

Delete a store

Deletes an existing store by its unique identifier.

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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    store_id = 'store_id_example' # str | 

    try:
        # Delete a store
        api_response = api_instance.delete_store_async(tenant_id, store_id)
        print("The response of StoresApi->delete_store_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->delete_store_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **store_id** | **str**|  | 

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

# **get_store_async**
> StoreDtoEnvelope get_store_async(tenant_id, store_id)

Get store by ID

Retrieves a single store by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.store_dto_envelope import StoreDtoEnvelope
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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    store_id = 'store_id_example' # str | 

    try:
        # Get store by ID
        api_response = api_instance.get_store_async(tenant_id, store_id)
        print("The response of StoresApi->get_store_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_store_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **store_id** | **str**|  | 

### Return type

[**StoreDtoEnvelope**](StoreDtoEnvelope.md)

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

# **get_stores_async**
> StoreDtoListEnvelope get_stores_async(tenant_id)

Get stores

Retrieves a list of stores for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.store_dto_list_envelope import StoreDtoListEnvelope
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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get stores
        api_response = api_instance.get_stores_async(tenant_id)
        print("The response of StoresApi->get_stores_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_stores_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**StoreDtoListEnvelope**](StoreDtoListEnvelope.md)

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

# **update_store_async**
> EmptyEnvelope update_store_async(tenant_id, store_id, store_update_dto=store_update_dto)

Update a store

Updates an existing store by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.store_update_dto import StoreUpdateDto
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
    api_instance = openapi_client.StoresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    store_id = 'store_id_example' # str | 
    store_update_dto = openapi_client.StoreUpdateDto() # StoreUpdateDto |  (optional)

    try:
        # Update a store
        api_response = api_instance.update_store_async(tenant_id, store_id, store_update_dto=store_update_dto)
        print("The response of StoresApi->update_store_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->update_store_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **store_id** | **str**|  | 
 **store_update_dto** | [**StoreUpdateDto**](StoreUpdateDto.md)|  | [optional] 

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

