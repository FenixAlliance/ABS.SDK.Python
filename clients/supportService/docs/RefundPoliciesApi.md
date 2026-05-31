# openapi_client.RefundPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_refund_policy_async**](RefundPoliciesApi.md#create_refund_policy_async) | **POST** /api/v2/SupportService/RefundPolicies | Create a new refund policy
[**delete_refund_policy_async**](RefundPoliciesApi.md#delete_refund_policy_async) | **DELETE** /api/v2/SupportService/RefundPolicies/{refundPolicyId} | Delete a refund policy
[**get_refund_policies_async**](RefundPoliciesApi.md#get_refund_policies_async) | **GET** /api/v2/SupportService/RefundPolicies | Retrieve a list of refund policies
[**get_refund_policies_count_async**](RefundPoliciesApi.md#get_refund_policies_count_async) | **GET** /api/v2/SupportService/RefundPolicies/Count | Get the count of refund policies
[**get_refund_policy_async**](RefundPoliciesApi.md#get_refund_policy_async) | **GET** /api/v2/SupportService/RefundPolicies/{refundPolicyId} | Retrieve a refund policy by ID
[**update_refund_policy_async**](RefundPoliciesApi.md#update_refund_policy_async) | **PUT** /api/v2/SupportService/RefundPolicies/{refundPolicyId} | Update a refund policy


# **create_refund_policy_async**
> EmptyEnvelope create_refund_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_refund_policy_create_dto=item_refund_policy_create_dto)

Create a new refund policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_refund_policy_create_dto import ItemRefundPolicyCreateDto
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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_refund_policy_create_dto = openapi_client.ItemRefundPolicyCreateDto() # ItemRefundPolicyCreateDto |  (optional)

    try:
        # Create a new refund policy
        api_response = api_instance.create_refund_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_refund_policy_create_dto=item_refund_policy_create_dto)
        print("The response of RefundPoliciesApi->create_refund_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->create_refund_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_refund_policy_create_dto** | [**ItemRefundPolicyCreateDto**](ItemRefundPolicyCreateDto.md)|  | [optional] 

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

# **delete_refund_policy_async**
> EmptyEnvelope delete_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Delete a refund policy

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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_policy_id = 'refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a refund policy
        api_response = api_instance.delete_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundPoliciesApi->delete_refund_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->delete_refund_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_policy_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_policies_async**
> ItemRefundPolicyDtoListEnvelope get_refund_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of refund policies

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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of refund policies
        api_response = api_instance.get_refund_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundPoliciesApi->get_refund_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->get_refund_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_refund_policies_count_async**
> Int32Envelope get_refund_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of refund policies

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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of refund policies
        api_response = api_instance.get_refund_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundPoliciesApi->get_refund_policies_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->get_refund_policies_count_async: %s\n" % e)
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_policy_async**
> ItemRefundPolicyDtoEnvelope get_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a refund policy by ID

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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_policy_id = 'refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a refund policy by ID
        api_response = api_instance.get_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundPoliciesApi->get_refund_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->get_refund_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_policy_id** | **str**|  | 
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

# **update_refund_policy_async**
> EmptyEnvelope update_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version, item_refund_policy_update_dto=item_refund_policy_update_dto)

Update a refund policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_refund_policy_update_dto import ItemRefundPolicyUpdateDto
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
    api_instance = openapi_client.RefundPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_policy_id = 'refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_refund_policy_update_dto = openapi_client.ItemRefundPolicyUpdateDto() # ItemRefundPolicyUpdateDto |  (optional)

    try:
        # Update a refund policy
        api_response = api_instance.update_refund_policy_async(tenant_id, refund_policy_id, api_version=api_version, x_api_version=x_api_version, item_refund_policy_update_dto=item_refund_policy_update_dto)
        print("The response of RefundPoliciesApi->update_refund_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundPoliciesApi->update_refund_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_refund_policy_update_dto** | [**ItemRefundPolicyUpdateDto**](ItemRefundPolicyUpdateDto.md)|  | [optional] 

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

