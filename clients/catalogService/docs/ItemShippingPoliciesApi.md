# openapi_client.ItemShippingPoliciesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_shipping_policies_async**](ItemShippingPoliciesApi.md#count_item_shipping_policies_async) | **GET** /api/v2/CatalogService/ItemShippingPolicies/Count | Count item shipping policies
[**get_item_shipping_policies_async**](ItemShippingPoliciesApi.md#get_item_shipping_policies_async) | **GET** /api/v2/CatalogService/ItemShippingPolicies | Get item shipping policies
[**get_item_shipping_policy_by_id_async**](ItemShippingPoliciesApi.md#get_item_shipping_policy_by_id_async) | **GET** /api/v2/CatalogService/ItemShippingPolicies/{itemShippingPolicyId} | Get item shipping policy by ID
[**relate_item_to_shipping_policy_async**](ItemShippingPoliciesApi.md#relate_item_to_shipping_policy_async) | **POST** /api/v2/CatalogService/ItemShippingPolicies | Relate item to shipping policy
[**remove_shipping_policy_from_item_async**](ItemShippingPoliciesApi.md#remove_shipping_policy_from_item_async) | **DELETE** /api/v2/CatalogService/ItemShippingPolicies/{itemShippingPolicyId} | Remove shipping policy from item


# **count_item_shipping_policies_async**
> Int32Envelope count_item_shipping_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Count item shipping policies

Counts all shipping policies for a specific item.

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
    api_instance = openapi_client.ItemShippingPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item shipping policies
        api_response = api_instance.count_item_shipping_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->count_item_shipping_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->count_item_shipping_policies_async: %s\n" % e)
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

# **get_item_shipping_policies_async**
> ItemShippingPolicyDtoListEnvelope get_item_shipping_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item shipping policies

Retrieves all shipping policies for a specific item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_list_envelope import ItemShippingPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemShippingPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item shipping policies
        api_response = api_instance.get_item_shipping_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->get_item_shipping_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->get_item_shipping_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoListEnvelope**](ItemShippingPolicyDtoListEnvelope.md)

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

# **get_item_shipping_policy_by_id_async**
> ItemShippingPolicyDtoEnvelope get_item_shipping_policy_by_id_async(item_shipping_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item shipping policy by ID

Retrieves a specific shipping policy for an item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_envelope import ItemShippingPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemShippingPoliciesApi(api_client)
    item_shipping_policy_id = 'item_shipping_policy_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item shipping policy by ID
        api_response = api_instance.get_item_shipping_policy_by_id_async(item_shipping_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->get_item_shipping_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->get_item_shipping_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_shipping_policy_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoEnvelope**](ItemShippingPolicyDtoEnvelope.md)

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

# **relate_item_to_shipping_policy_async**
> relate_item_to_shipping_policy_async(tenant_id, item_id, shipping_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate item to shipping policy

Relates an item to an existing shipping policy.

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
    api_instance = openapi_client.ItemShippingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    shipping_policy_id = 'shipping_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate item to shipping policy
        api_instance.relate_item_to_shipping_policy_async(tenant_id, item_id, shipping_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->relate_item_to_shipping_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **shipping_policy_id** | **str**|  | 
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

# **remove_shipping_policy_from_item_async**
> remove_shipping_policy_from_item_async(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove shipping policy from item

Removes a shipping policy from an item.

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
    api_instance = openapi_client.ItemShippingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_shipping_policy_id = 'item_shipping_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove shipping policy from item
        api_instance.remove_shipping_policy_from_item_async(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->remove_shipping_policy_from_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_shipping_policy_id** | **str**|  | 
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

