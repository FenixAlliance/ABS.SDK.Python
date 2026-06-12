# openapi_client.ItemBundlesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_bundle_async**](ItemBundlesApi.md#create_item_bundle_async) | **POST** /api/v2/CatalogService/ItemBundles | Create a new item bundle
[**delete_item_bundle_async**](ItemBundlesApi.md#delete_item_bundle_async) | **DELETE** /api/v2/CatalogService/ItemBundles/{itemBundleId} | Delete an item bundle
[**get_item_bundle_by_id_async**](ItemBundlesApi.md#get_item_bundle_by_id_async) | **GET** /api/v2/CatalogService/ItemBundles/{itemBundleId} | Get item bundle by ID
[**get_item_bundles_async**](ItemBundlesApi.md#get_item_bundles_async) | **GET** /api/v2/CatalogService/ItemBundles | Get all item bundles
[**get_item_bundles_count_async**](ItemBundlesApi.md#get_item_bundles_count_async) | **GET** /api/v2/CatalogService/ItemBundles/Count | Get item bundles count
[**patch_item_bundle_async**](ItemBundlesApi.md#patch_item_bundle_async) | **PATCH** /api/v2/CatalogService/ItemBundles/{itemBundleId} | Patch an item bundle
[**update_item_bundle_async**](ItemBundlesApi.md#update_item_bundle_async) | **PUT** /api/v2/CatalogService/ItemBundles/{itemBundleId} | Update an item bundle


# **create_item_bundle_async**
> ItemBundleDtoEnvelope create_item_bundle_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_bundle_create_dto=item_bundle_create_dto)

Create a new item bundle

Creates a new item bundle for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_bundle_create_dto import ItemBundleCreateDto
from openapi_client.models.item_bundle_dto_envelope import ItemBundleDtoEnvelope
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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_bundle_create_dto = openapi_client.ItemBundleCreateDto() # ItemBundleCreateDto |  (optional)

    try:
        # Create a new item bundle
        api_response = api_instance.create_item_bundle_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_bundle_create_dto=item_bundle_create_dto)
        print("The response of ItemBundlesApi->create_item_bundle_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->create_item_bundle_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_bundle_create_dto** | [**ItemBundleCreateDto**](ItemBundleCreateDto.md)|  | [optional] 

### Return type

[**ItemBundleDtoEnvelope**](ItemBundleDtoEnvelope.md)

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

# **delete_item_bundle_async**
> delete_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version)

Delete an item bundle

Deletes an item bundle for the specified tenant.

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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_bundle_id = 'item_bundle_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item bundle
        api_instance.delete_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->delete_item_bundle_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_bundle_id** | **str**|  | 
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

# **get_item_bundle_by_id_async**
> ItemBundleDtoEnvelope get_item_bundle_by_id_async(item_bundle_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item bundle by ID

Retrieves a specific item bundle by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_bundle_dto_envelope import ItemBundleDtoEnvelope
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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    item_bundle_id = 'item_bundle_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item bundle by ID
        api_response = api_instance.get_item_bundle_by_id_async(item_bundle_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemBundlesApi->get_item_bundle_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->get_item_bundle_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_bundle_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBundleDtoEnvelope**](ItemBundleDtoEnvelope.md)

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

# **get_item_bundles_async**
> ItemBundleDtoListEnvelope get_item_bundles_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item bundles

Retrieves all item bundles for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_bundle_dto_list_envelope import ItemBundleDtoListEnvelope
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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item bundles
        api_response = api_instance.get_item_bundles_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemBundlesApi->get_item_bundles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->get_item_bundles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBundleDtoListEnvelope**](ItemBundleDtoListEnvelope.md)

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

# **get_item_bundles_count_async**
> Int32Envelope get_item_bundles_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item bundles count

Returns the count of item bundles for the specified tenant.

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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item bundles count
        api_response = api_instance.get_item_bundles_count_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemBundlesApi->get_item_bundles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->get_item_bundles_count_async: %s\n" % e)
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

# **patch_item_bundle_async**
> EmptyEnvelope patch_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an item bundle

Partially updates an existing item bundle for the specified tenant using a JSON Patch document.

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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_bundle_id = 'item_bundle_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an item bundle
        api_response = api_instance.patch_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ItemBundlesApi->patch_item_bundle_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->patch_item_bundle_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_bundle_id** | **str**|  | 
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

# **update_item_bundle_async**
> ItemBundleDtoEnvelope update_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version, item_bundle_update_dto=item_bundle_update_dto)

Update an item bundle

Updates an existing item bundle for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_bundle_dto_envelope import ItemBundleDtoEnvelope
from openapi_client.models.item_bundle_update_dto import ItemBundleUpdateDto
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
    api_instance = openapi_client.ItemBundlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_bundle_id = 'item_bundle_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_bundle_update_dto = openapi_client.ItemBundleUpdateDto() # ItemBundleUpdateDto |  (optional)

    try:
        # Update an item bundle
        api_response = api_instance.update_item_bundle_async(tenant_id, item_bundle_id, api_version=api_version, x_api_version=x_api_version, item_bundle_update_dto=item_bundle_update_dto)
        print("The response of ItemBundlesApi->update_item_bundle_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemBundlesApi->update_item_bundle_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_bundle_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_bundle_update_dto** | [**ItemBundleUpdateDto**](ItemBundleUpdateDto.md)|  | [optional] 

### Return type

[**ItemBundleDtoEnvelope**](ItemBundleDtoEnvelope.md)

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

