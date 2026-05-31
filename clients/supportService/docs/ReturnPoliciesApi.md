# openapi_client.ReturnPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_return_policy_async**](ReturnPoliciesApi.md#create_return_policy_async) | **POST** /api/v2/SupportService/ReturnPolicies | Create a new return policy
[**delete_return_policy_async**](ReturnPoliciesApi.md#delete_return_policy_async) | **DELETE** /api/v2/SupportService/ReturnPolicies/{returnPolicyId} | Delete a return policy
[**get_return_policies_async**](ReturnPoliciesApi.md#get_return_policies_async) | **GET** /api/v2/SupportService/ReturnPolicies | Retrieve a list of return policies
[**get_return_policies_count_async**](ReturnPoliciesApi.md#get_return_policies_count_async) | **GET** /api/v2/SupportService/ReturnPolicies/Count | Get the count of return policies
[**get_return_policy_async**](ReturnPoliciesApi.md#get_return_policy_async) | **GET** /api/v2/SupportService/ReturnPolicies/{returnPolicyId} | Retrieve a return policy by ID
[**update_return_policy_async**](ReturnPoliciesApi.md#update_return_policy_async) | **PUT** /api/v2/SupportService/ReturnPolicies/{returnPolicyId} | Update a return policy


# **create_return_policy_async**
> EmptyEnvelope create_return_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_return_policy_create_dto=item_return_policy_create_dto)

Create a new return policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_return_policy_create_dto import ItemReturnPolicyCreateDto
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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_return_policy_create_dto = openapi_client.ItemReturnPolicyCreateDto() # ItemReturnPolicyCreateDto |  (optional)

    try:
        # Create a new return policy
        api_response = api_instance.create_return_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_return_policy_create_dto=item_return_policy_create_dto)
        print("The response of ReturnPoliciesApi->create_return_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->create_return_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_return_policy_create_dto** | [**ItemReturnPolicyCreateDto**](ItemReturnPolicyCreateDto.md)|  | [optional] 

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

# **delete_return_policy_async**
> EmptyEnvelope delete_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)

Delete a return policy

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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_policy_id = 'return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a return policy
        api_response = api_instance.delete_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnPoliciesApi->delete_return_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->delete_return_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_policy_id** | **str**|  | 
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

# **get_return_policies_async**
> ItemReturnPolicyDtoListEnvelope get_return_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of return policies

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_list_envelope import ItemReturnPolicyDtoListEnvelope
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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of return policies
        api_response = api_instance.get_return_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnPoliciesApi->get_return_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->get_return_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_return_policies_count_async**
> Int32Envelope get_return_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of return policies

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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of return policies
        api_response = api_instance.get_return_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnPoliciesApi->get_return_policies_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->get_return_policies_count_async: %s\n" % e)
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

# **get_return_policy_async**
> ItemReturnPolicyDtoEnvelope get_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a return policy by ID

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_envelope import ItemReturnPolicyDtoEnvelope
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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_policy_id = 'return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a return policy by ID
        api_response = api_instance.get_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnPoliciesApi->get_return_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->get_return_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_policy_id** | **str**|  | 
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

# **update_return_policy_async**
> EmptyEnvelope update_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version, item_return_policy_update_dto=item_return_policy_update_dto)

Update a return policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_return_policy_update_dto import ItemReturnPolicyUpdateDto
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
    api_instance = openapi_client.ReturnPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_policy_id = 'return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_return_policy_update_dto = openapi_client.ItemReturnPolicyUpdateDto() # ItemReturnPolicyUpdateDto |  (optional)

    try:
        # Update a return policy
        api_response = api_instance.update_return_policy_async(tenant_id, return_policy_id, api_version=api_version, x_api_version=x_api_version, item_return_policy_update_dto=item_return_policy_update_dto)
        print("The response of ReturnPoliciesApi->update_return_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPoliciesApi->update_return_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_return_policy_update_dto** | [**ItemReturnPolicyUpdateDto**](ItemReturnPolicyUpdateDto.md)|  | [optional] 

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

