# openapi_client.ItemRefundPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_refund_policies_async**](ItemRefundPoliciesApi.md#count_item_refund_policies_async) | **GET** /api/v2/CatalogService/ItemRefundPolicies/Count | Count item refund policies
[**get_item_refund_policies_async**](ItemRefundPoliciesApi.md#get_item_refund_policies_async) | **GET** /api/v2/CatalogService/ItemRefundPolicies | Get item refund policies
[**get_item_refund_policy_by_id_async**](ItemRefundPoliciesApi.md#get_item_refund_policy_by_id_async) | **GET** /api/v2/CatalogService/ItemRefundPolicies/{itemRefundPolicyId} | Get item refund policy by ID
[**relate_item_to_refund_policy_async**](ItemRefundPoliciesApi.md#relate_item_to_refund_policy_async) | **POST** /api/v2/CatalogService/ItemRefundPolicies | Relate item to refund policy
[**remove_refund_policy_from_item_async**](ItemRefundPoliciesApi.md#remove_refund_policy_from_item_async) | **DELETE** /api/v2/CatalogService/ItemRefundPolicies/{itemRefundPolicyId} | Remove refund policy from item


# **count_item_refund_policies_async**
> Int32Envelope count_item_refund_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Count item refund policies

Counts all refund policies for a specific item.

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
    api_instance = openapi_client.ItemRefundPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item refund policies
        api_response = api_instance.count_item_refund_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRefundPoliciesApi->count_item_refund_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRefundPoliciesApi->count_item_refund_policies_async: %s\n" % e)
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

# **get_item_refund_policies_async**
> ItemRefundPolicyDtoListEnvelope get_item_refund_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item refund policies

Retrieves all refund policies for a specific item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_list_envelope import ItemRefundPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemRefundPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item refund policies
        api_response = api_instance.get_item_refund_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRefundPoliciesApi->get_item_refund_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRefundPoliciesApi->get_item_refund_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoListEnvelope**](ItemRefundPolicyDtoListEnvelope.md)

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

# **get_item_refund_policy_by_id_async**
> ItemRefundPolicyDtoEnvelope get_item_refund_policy_by_id_async(item_refund_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item refund policy by ID

Retrieves a specific refund policy for an item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_envelope import ItemRefundPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemRefundPoliciesApi(api_client)
    item_refund_policy_id = 'item_refund_policy_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item refund policy by ID
        api_response = api_instance.get_item_refund_policy_by_id_async(item_refund_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRefundPoliciesApi->get_item_refund_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRefundPoliciesApi->get_item_refund_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_refund_policy_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoEnvelope**](ItemRefundPolicyDtoEnvelope.md)

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

# **relate_item_to_refund_policy_async**
> relate_item_to_refund_policy_async(tenant_id, item_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate item to refund policy

Relates an item to an existing refund policy.

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
    api_instance = openapi_client.ItemRefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    refund_policy_id = 'refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate item to refund policy
        api_instance.relate_item_to_refund_policy_async(tenant_id, item_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemRefundPoliciesApi->relate_item_to_refund_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **refund_policy_id** | **str**|  | 
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

# **remove_refund_policy_from_item_async**
> remove_refund_policy_from_item_async(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove refund policy from item

Removes a refund policy from an item.

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
    api_instance = openapi_client.ItemRefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_refund_policy_id = 'item_refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove refund policy from item
        api_instance.remove_refund_policy_from_item_async(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemRefundPoliciesApi->remove_refund_policy_from_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_refund_policy_id** | **str**|  | 
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

