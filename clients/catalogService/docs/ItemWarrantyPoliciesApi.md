# openapi_client.ItemWarrantyPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_warranty_policies_async**](ItemWarrantyPoliciesApi.md#count_item_warranty_policies_async) | **GET** /api/v2/CatalogService/ItemWarrantyPolicies/Count | Count item warranty policies
[**get_item_warranty_policies_async**](ItemWarrantyPoliciesApi.md#get_item_warranty_policies_async) | **GET** /api/v2/CatalogService/ItemWarrantyPolicies | Get item warranty policies
[**get_item_warranty_policy_by_id_async**](ItemWarrantyPoliciesApi.md#get_item_warranty_policy_by_id_async) | **GET** /api/v2/CatalogService/ItemWarrantyPolicies/{itemWarrantyPolicyId} | Get item warranty policy by ID
[**relate_item_to_warranty_policy_async**](ItemWarrantyPoliciesApi.md#relate_item_to_warranty_policy_async) | **POST** /api/v2/CatalogService/ItemWarrantyPolicies | Relate item to warranty policy
[**remove_warranty_policy_from_item_async**](ItemWarrantyPoliciesApi.md#remove_warranty_policy_from_item_async) | **DELETE** /api/v2/CatalogService/ItemWarrantyPolicies/{itemWarrantyPolicyId} | Remove warranty policy from item


# **count_item_warranty_policies_async**
> Int32Envelope count_item_warranty_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Count item warranty policies

Counts all warranty policies for a specific item.

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
    api_instance = openapi_client.ItemWarrantyPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item warranty policies
        api_response = api_instance.count_item_warranty_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemWarrantyPoliciesApi->count_item_warranty_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemWarrantyPoliciesApi->count_item_warranty_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
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

# **get_item_warranty_policies_async**
> ItemWarrantyPolicyDtoListEnvelope get_item_warranty_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item warranty policies

Retrieves all warranty policies for a specific item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_list_envelope import ItemWarrantyPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemWarrantyPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item warranty policies
        api_response = api_instance.get_item_warranty_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemWarrantyPoliciesApi->get_item_warranty_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemWarrantyPoliciesApi->get_item_warranty_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoListEnvelope**](ItemWarrantyPolicyDtoListEnvelope.md)

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

# **get_item_warranty_policy_by_id_async**
> ItemWarrantyPolicyDtoEnvelope get_item_warranty_policy_by_id_async(item_warranty_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item warranty policy by ID

Retrieves a specific warranty policy for an item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_envelope import ItemWarrantyPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemWarrantyPoliciesApi(api_client)
    item_warranty_policy_id = 'item_warranty_policy_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item warranty policy by ID
        api_response = api_instance.get_item_warranty_policy_by_id_async(item_warranty_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemWarrantyPoliciesApi->get_item_warranty_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemWarrantyPoliciesApi->get_item_warranty_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_warranty_policy_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoEnvelope**](ItemWarrantyPolicyDtoEnvelope.md)

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

# **relate_item_to_warranty_policy_async**
> relate_item_to_warranty_policy_async(tenant_id, item_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate item to warranty policy

Relates an item to an existing warranty policy.

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
    api_instance = openapi_client.ItemWarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    warranty_policy_id = 'warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate item to warranty policy
        api_instance.relate_item_to_warranty_policy_async(tenant_id, item_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemWarrantyPoliciesApi->relate_item_to_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **warranty_policy_id** | **str**|  | 
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

# **remove_warranty_policy_from_item_async**
> remove_warranty_policy_from_item_async(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove warranty policy from item

Removes a warranty policy from an item.

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
    api_instance = openapi_client.ItemWarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_warranty_policy_id = 'item_warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove warranty policy from item
        api_instance.remove_warranty_policy_from_item_async(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemWarrantyPoliciesApi->remove_warranty_policy_from_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_warranty_policy_id** | **str**|  | 
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

