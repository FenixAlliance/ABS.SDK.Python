# openapi_client.ItemFamiliesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_family_async**](ItemFamiliesApi.md#create_item_family_async) | **POST** /api/v2/CatalogService/ItemFamilies | Create a new item family
[**delete_item_family_async**](ItemFamiliesApi.md#delete_item_family_async) | **DELETE** /api/v2/CatalogService/ItemFamilies/{itemFamilyId} | Delete an item family
[**get_item_families_async**](ItemFamiliesApi.md#get_item_families_async) | **GET** /api/v2/CatalogService/ItemFamilies | Get all item families
[**get_item_families_count_async**](ItemFamiliesApi.md#get_item_families_count_async) | **GET** /api/v2/CatalogService/ItemFamilies/Count | Get item families count
[**get_item_family_by_id_async**](ItemFamiliesApi.md#get_item_family_by_id_async) | **GET** /api/v2/CatalogService/ItemFamilies/{itemFamilyId} | Get item family by ID
[**patch_item_family_async**](ItemFamiliesApi.md#patch_item_family_async) | **PATCH** /api/v2/CatalogService/ItemFamilies/{itemFamilyId} | Patch an item family
[**update_item_family_async**](ItemFamiliesApi.md#update_item_family_async) | **PUT** /api/v2/CatalogService/ItemFamilies/{itemFamilyId} | Update an item family


# **create_item_family_async**
> ItemFamilyDtoEnvelope create_item_family_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_family_create_dto=item_family_create_dto)

Create a new item family

Creates a new item family for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_family_create_dto import ItemFamilyCreateDto
from openapi_client.models.item_family_dto_envelope import ItemFamilyDtoEnvelope
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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_family_create_dto = openapi_client.ItemFamilyCreateDto() # ItemFamilyCreateDto |  (optional)

    try:
        # Create a new item family
        api_response = api_instance.create_item_family_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_family_create_dto=item_family_create_dto)
        print("The response of ItemFamiliesApi->create_item_family_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->create_item_family_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_family_create_dto** | [**ItemFamilyCreateDto**](ItemFamilyCreateDto.md)|  | [optional] 

### Return type

[**ItemFamilyDtoEnvelope**](ItemFamilyDtoEnvelope.md)

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

# **delete_item_family_async**
> delete_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version)

Delete an item family

Deletes an item family for the specified tenant.

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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_family_id = 'item_family_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item family
        api_instance.delete_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->delete_item_family_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_family_id** | **str**|  | 
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

# **get_item_families_async**
> ItemFamilyDtoListEnvelope get_item_families_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item families

Retrieves all item families for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_family_dto_list_envelope import ItemFamilyDtoListEnvelope
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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item families
        api_response = api_instance.get_item_families_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemFamiliesApi->get_item_families_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->get_item_families_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemFamilyDtoListEnvelope**](ItemFamilyDtoListEnvelope.md)

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

# **get_item_families_count_async**
> Int32Envelope get_item_families_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item families count

Returns the count of item families for the specified tenant.

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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item families count
        api_response = api_instance.get_item_families_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemFamiliesApi->get_item_families_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->get_item_families_count_async: %s\n" % e)
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

# **get_item_family_by_id_async**
> ItemFamilyDtoEnvelope get_item_family_by_id_async(item_family_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item family by ID

Retrieves a specific item family by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_family_dto_envelope import ItemFamilyDtoEnvelope
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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    item_family_id = 'item_family_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item family by ID
        api_response = api_instance.get_item_family_by_id_async(item_family_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemFamiliesApi->get_item_family_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->get_item_family_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_family_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemFamilyDtoEnvelope**](ItemFamilyDtoEnvelope.md)

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

# **patch_item_family_async**
> EmptyEnvelope patch_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an item family

Partially updates an existing item family for the specified tenant using a JSON Patch document.

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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_family_id = 'item_family_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an item family
        api_response = api_instance.patch_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemFamiliesApi->patch_item_family_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->patch_item_family_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_family_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_family_async**
> ItemFamilyDtoEnvelope update_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version, item_family_update_dto=item_family_update_dto)

Update an item family

Updates an existing item family for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_family_dto_envelope import ItemFamilyDtoEnvelope
from openapi_client.models.item_family_update_dto import ItemFamilyUpdateDto
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
    api_instance = openapi_client.ItemFamiliesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_family_id = 'item_family_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_family_update_dto = openapi_client.ItemFamilyUpdateDto() # ItemFamilyUpdateDto |  (optional)

    try:
        # Update an item family
        api_response = api_instance.update_item_family_async(tenant_id, item_family_id, api_version=api_version, x_api_version=x_api_version, item_family_update_dto=item_family_update_dto)
        print("The response of ItemFamiliesApi->update_item_family_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemFamiliesApi->update_item_family_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_family_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_family_update_dto** | [**ItemFamilyUpdateDto**](ItemFamilyUpdateDto.md)|  | [optional] 

### Return type

[**ItemFamilyDtoEnvelope**](ItemFamilyDtoEnvelope.md)

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

