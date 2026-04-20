# openapi_client.ItemReturnPoliciesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_return_policies_async**](ItemReturnPoliciesApi.md#count_item_return_policies_async) | **GET** /api/v2/CatalogService/ItemReturnPolicies/Count | Count item return policies
[**get_item_return_policies_async**](ItemReturnPoliciesApi.md#get_item_return_policies_async) | **GET** /api/v2/CatalogService/ItemReturnPolicies | Get item return policies
[**get_item_return_policy_by_id_async**](ItemReturnPoliciesApi.md#get_item_return_policy_by_id_async) | **GET** /api/v2/CatalogService/ItemReturnPolicies/{itemReturnPolicyId} | Get item return policy by ID
[**relate_item_to_return_policy_async**](ItemReturnPoliciesApi.md#relate_item_to_return_policy_async) | **POST** /api/v2/CatalogService/ItemReturnPolicies | Relate item to return policy
[**remove_return_policy_from_item_async**](ItemReturnPoliciesApi.md#remove_return_policy_from_item_async) | **DELETE** /api/v2/CatalogService/ItemReturnPolicies/{itemReturnPolicyId} | Remove return policy from item


# **count_item_return_policies_async**
> Int32Envelope count_item_return_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Count item return policies

Counts all return policies for a specific item.

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
    api_instance = openapi_client.ItemReturnPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item return policies
        api_response = api_instance.count_item_return_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemReturnPoliciesApi->count_item_return_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReturnPoliciesApi->count_item_return_policies_async: %s\n" % e)
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

# **get_item_return_policies_async**
> ItemReturnPolicyDtoListEnvelope get_item_return_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item return policies

Retrieves all return policies for a specific item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_list_envelope import ItemReturnPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemReturnPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item return policies
        api_response = api_instance.get_item_return_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemReturnPoliciesApi->get_item_return_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReturnPoliciesApi->get_item_return_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoListEnvelope**](ItemReturnPolicyDtoListEnvelope.md)

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

# **get_item_return_policy_by_id_async**
> ItemReturnPolicyDtoEnvelope get_item_return_policy_by_id_async(item_return_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item return policy by ID

Retrieves a specific return policy for an item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_envelope import ItemReturnPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemReturnPoliciesApi(api_client)
    item_return_policy_id = 'item_return_policy_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item return policy by ID
        api_response = api_instance.get_item_return_policy_by_id_async(item_return_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemReturnPoliciesApi->get_item_return_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemReturnPoliciesApi->get_item_return_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_return_policy_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoEnvelope**](ItemReturnPolicyDtoEnvelope.md)

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

# **relate_item_to_return_policy_async**
> relate_item_to_return_policy_async(tenant_id, item_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate item to return policy

Relates an item to an existing return policy.

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
    api_instance = openapi_client.ItemReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    return_policy_id = 'return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate item to return policy
        api_instance.relate_item_to_return_policy_async(tenant_id, item_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemReturnPoliciesApi->relate_item_to_return_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **return_policy_id** | **str**|  | 
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

# **remove_return_policy_from_item_async**
> remove_return_policy_from_item_async(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove return policy from item

Removes a return policy from an item.

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
    api_instance = openapi_client.ItemReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_return_policy_id = 'item_return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove return policy from item
        api_instance.remove_return_policy_from_item_async(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemReturnPoliciesApi->remove_return_policy_from_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_return_policy_id** | **str**|  | 
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

