# openapi_client.ItemTaxPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_item_tax_policies_async**](ItemTaxPoliciesApi.md#count_item_tax_policies_async) | **GET** /api/v2/CatalogService/ItemTaxPolicies/Count | Count item tax policies
[**get_item_tax_policies_async**](ItemTaxPoliciesApi.md#get_item_tax_policies_async) | **GET** /api/v2/CatalogService/ItemTaxPolicies | Get item tax policies
[**get_item_tax_policy_by_id_async**](ItemTaxPoliciesApi.md#get_item_tax_policy_by_id_async) | **GET** /api/v2/CatalogService/ItemTaxPolicies/{itemTaxPolicyId} | Get item tax policy by ID
[**relate_item_to_tax_policy_async**](ItemTaxPoliciesApi.md#relate_item_to_tax_policy_async) | **POST** /api/v2/CatalogService/ItemTaxPolicies | Relate item to tax policy
[**remove_tax_policy_from_item_async**](ItemTaxPoliciesApi.md#remove_tax_policy_from_item_async) | **DELETE** /api/v2/CatalogService/ItemTaxPolicies/{itemTaxPolicyId} | Remove tax policy from item


# **count_item_tax_policies_async**
> Int32Envelope count_item_tax_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Count item tax policies

Counts all tax policies for a specific item.

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
    api_instance = openapi_client.ItemTaxPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count item tax policies
        api_response = api_instance.count_item_tax_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTaxPoliciesApi->count_item_tax_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTaxPoliciesApi->count_item_tax_policies_async: %s\n" % e)
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

# **get_item_tax_policies_async**
> ItemTaxPolicyDtoListEnvelope get_item_tax_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item tax policies

Retrieves all tax policies for a specific item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_list_envelope import ItemTaxPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemTaxPoliciesApi(api_client)
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item tax policies
        api_response = api_instance.get_item_tax_policies_async(item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTaxPoliciesApi->get_item_tax_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTaxPoliciesApi->get_item_tax_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoListEnvelope**](ItemTaxPolicyDtoListEnvelope.md)

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

# **get_item_tax_policy_by_id_async**
> ItemTaxPolicyDtoEnvelope get_item_tax_policy_by_id_async(item_tax_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)

Get item tax policy by ID

Retrieves a specific tax policy for an item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_envelope import ItemTaxPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemTaxPoliciesApi(api_client)
    item_tax_policy_id = 'item_tax_policy_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item tax policy by ID
        api_response = api_instance.get_item_tax_policy_by_id_async(item_tax_policy_id, item_id=item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemTaxPoliciesApi->get_item_tax_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemTaxPoliciesApi->get_item_tax_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_tax_policy_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoEnvelope**](ItemTaxPolicyDtoEnvelope.md)

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

# **relate_item_to_tax_policy_async**
> relate_item_to_tax_policy_async(tenant_id, item_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate item to tax policy

Relates an item to an existing tax policy.

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
    api_instance = openapi_client.ItemTaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate item to tax policy
        api_instance.relate_item_to_tax_policy_async(tenant_id, item_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemTaxPoliciesApi->relate_item_to_tax_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
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

# **remove_tax_policy_from_item_async**
> remove_tax_policy_from_item_async(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove tax policy from item

Removes a tax policy from an item.

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
    api_instance = openapi_client.ItemTaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_tax_policy_id = 'item_tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove tax policy from item
        api_instance.remove_tax_policy_from_item_async(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemTaxPoliciesApi->remove_tax_policy_from_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_tax_policy_id** | **str**|  | 
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

