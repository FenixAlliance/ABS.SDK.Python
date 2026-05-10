# openapi_client.ItemShippingPoliciesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_shipping_policy_async**](ItemShippingPoliciesApi.md#create_item_shipping_policy_async) | **POST** /api/v2/ShipmentsService/ItemShippingPolicies | Create an item shipping policy
[**delete_item_shipping_policy_async**](ItemShippingPoliciesApi.md#delete_item_shipping_policy_async) | **DELETE** /api/v2/ShipmentsService/ItemShippingPolicies/{policyId} | Delete an item shipping policy
[**get_item_shipping_policies_async**](ItemShippingPoliciesApi.md#get_item_shipping_policies_async) | **GET** /api/v2/ShipmentsService/ItemShippingPolicies | Get all item shipping policies
[**get_item_shipping_policies_count_async**](ItemShippingPoliciesApi.md#get_item_shipping_policies_count_async) | **GET** /api/v2/ShipmentsService/ItemShippingPolicies/Count | Get item shipping policies count
[**get_item_shipping_policy_by_id_async**](ItemShippingPoliciesApi.md#get_item_shipping_policy_by_id_async) | **GET** /api/v2/ShipmentsService/ItemShippingPolicies/{policyId} | Get item shipping policy by ID
[**update_item_shipping_policy_async**](ItemShippingPoliciesApi.md#update_item_shipping_policy_async) | **PUT** /api/v2/ShipmentsService/ItemShippingPolicies/{policyId} | Update an item shipping policy


# **create_item_shipping_policy_async**
> create_item_shipping_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_shipping_policy_create_dto=item_shipping_policy_create_dto)

Create an item shipping policy

Creates a new item shipping policy.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_create_dto import ItemShippingPolicyCreateDto
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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_shipping_policy_create_dto = openapi_client.ItemShippingPolicyCreateDto() # ItemShippingPolicyCreateDto |  (optional)

    try:
        # Create an item shipping policy
        api_instance.create_item_shipping_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_shipping_policy_create_dto=item_shipping_policy_create_dto)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->create_item_shipping_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_shipping_policy_create_dto** | [**ItemShippingPolicyCreateDto**](ItemShippingPolicyCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_shipping_policy_async**
> delete_item_shipping_policy_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version)

Delete an item shipping policy

Deletes an item shipping policy.

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
    policy_id = 'policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item shipping policy
        api_instance.delete_item_shipping_policy_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->delete_item_shipping_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **policy_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_shipping_policies_async**
> ItemShippingPolicyDtoListEnvelope get_item_shipping_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item shipping policies

Retrieves all item shipping policies for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item shipping policies
        api_response = api_instance.get_item_shipping_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->get_item_shipping_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->get_item_shipping_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_item_shipping_policies_count_async**
> Int32Envelope get_item_shipping_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item shipping policies count

Returns the count of item shipping policies.

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
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item shipping policies count
        api_response = api_instance.get_item_shipping_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->get_item_shipping_policies_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->get_item_shipping_policies_count_async: %s\n" % e)
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

# **get_item_shipping_policy_by_id_async**
> ItemShippingPolicyDtoEnvelope get_item_shipping_policy_by_id_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version)

Get item shipping policy by ID

Retrieves a specific item shipping policy.

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
    tenant_id = 'tenant_id_example' # str | 
    policy_id = 'policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item shipping policy by ID
        api_response = api_instance.get_item_shipping_policy_by_id_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemShippingPoliciesApi->get_item_shipping_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->get_item_shipping_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **policy_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_shipping_policy_async**
> update_item_shipping_policy_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version, item_shipping_policy_update_dto=item_shipping_policy_update_dto)

Update an item shipping policy

Updates an existing item shipping policy.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_update_dto import ItemShippingPolicyUpdateDto
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
    policy_id = 'policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_shipping_policy_update_dto = openapi_client.ItemShippingPolicyUpdateDto() # ItemShippingPolicyUpdateDto |  (optional)

    try:
        # Update an item shipping policy
        api_instance.update_item_shipping_policy_async(tenant_id, policy_id, api_version=api_version, x_api_version=x_api_version, item_shipping_policy_update_dto=item_shipping_policy_update_dto)
    except Exception as e:
        print("Exception when calling ItemShippingPoliciesApi->update_item_shipping_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_shipping_policy_update_dto** | [**ItemShippingPolicyUpdateDto**](ItemShippingPolicyUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

