# openapi_client.WarrantyPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_warranty_policy_async**](WarrantyPoliciesApi.md#create_warranty_policy_async) | **POST** /api/v2/SupportService/WarrantyPolicies | Create a new warranty policy
[**delete_warranty_policy_async**](WarrantyPoliciesApi.md#delete_warranty_policy_async) | **DELETE** /api/v2/SupportService/WarrantyPolicies/{warrantyPolicyId} | Delete a warranty policy
[**get_warranty_policies_async**](WarrantyPoliciesApi.md#get_warranty_policies_async) | **GET** /api/v2/SupportService/WarrantyPolicies | Retrieve a list of warranty policies
[**get_warranty_policies_count_async**](WarrantyPoliciesApi.md#get_warranty_policies_count_async) | **GET** /api/v2/SupportService/WarrantyPolicies/Count | Get the count of warranty policies
[**get_warranty_policy_async**](WarrantyPoliciesApi.md#get_warranty_policy_async) | **GET** /api/v2/SupportService/WarrantyPolicies/{warrantyPolicyId} | Retrieve a warranty policy by ID
[**patch_warranty_policy_async**](WarrantyPoliciesApi.md#patch_warranty_policy_async) | **PATCH** /api/v2/SupportService/WarrantyPolicies/{warrantyPolicyId} | Patch a warranty policy
[**update_warranty_policy_async**](WarrantyPoliciesApi.md#update_warranty_policy_async) | **PUT** /api/v2/SupportService/WarrantyPolicies/{warrantyPolicyId} | Update a warranty policy


# **create_warranty_policy_async**
> EmptyEnvelope create_warranty_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_warranty_policy_create_dto=item_warranty_policy_create_dto)

Create a new warranty policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_warranty_policy_create_dto import ItemWarrantyPolicyCreateDto
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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_warranty_policy_create_dto = openapi_client.ItemWarrantyPolicyCreateDto() # ItemWarrantyPolicyCreateDto |  (optional)

    try:
        # Create a new warranty policy
        api_response = api_instance.create_warranty_policy_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_warranty_policy_create_dto=item_warranty_policy_create_dto)
        print("The response of WarrantyPoliciesApi->create_warranty_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->create_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_warranty_policy_create_dto** | [**ItemWarrantyPolicyCreateDto**](ItemWarrantyPolicyCreateDto.md)|  | [optional] 

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

# **delete_warranty_policy_async**
> EmptyEnvelope delete_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Delete a warranty policy

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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_policy_id = 'warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a warranty policy
        api_response = api_instance.delete_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyPoliciesApi->delete_warranty_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->delete_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_policy_id** | **str**|  | 
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

# **get_warranty_policies_async**
> ItemWarrantyPolicyDtoListEnvelope get_warranty_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of warranty policies

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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of warranty policies
        api_response = api_instance.get_warranty_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyPoliciesApi->get_warranty_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->get_warranty_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_warranty_policies_count_async**
> Int32Envelope get_warranty_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of warranty policies

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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of warranty policies
        api_response = api_instance.get_warranty_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyPoliciesApi->get_warranty_policies_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->get_warranty_policies_count_async: %s\n" % e)
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

# **get_warranty_policy_async**
> ItemWarrantyPolicyDtoEnvelope get_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a warranty policy by ID

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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_policy_id = 'warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a warranty policy by ID
        api_response = api_instance.get_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyPoliciesApi->get_warranty_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->get_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_policy_id** | **str**|  | 
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

# **patch_warranty_policy_async**
> EmptyEnvelope patch_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a warranty policy

Partially updates an existing warranty policy by its unique identifier.

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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_policy_id = 'warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a warranty policy
        api_response = api_instance.patch_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of WarrantyPoliciesApi->patch_warranty_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->patch_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_policy_id** | **str**|  | 
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

# **update_warranty_policy_async**
> EmptyEnvelope update_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version, item_warranty_policy_update_dto=item_warranty_policy_update_dto)

Update a warranty policy

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_warranty_policy_update_dto import ItemWarrantyPolicyUpdateDto
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
    api_instance = openapi_client.WarrantyPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_policy_id = 'warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_warranty_policy_update_dto = openapi_client.ItemWarrantyPolicyUpdateDto() # ItemWarrantyPolicyUpdateDto |  (optional)

    try:
        # Update a warranty policy
        api_response = api_instance.update_warranty_policy_async(tenant_id, warranty_policy_id, api_version=api_version, x_api_version=x_api_version, item_warranty_policy_update_dto=item_warranty_policy_update_dto)
        print("The response of WarrantyPoliciesApi->update_warranty_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyPoliciesApi->update_warranty_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_warranty_policy_update_dto** | [**ItemWarrantyPolicyUpdateDto**](ItemWarrantyPolicyUpdateDto.md)|  | [optional] 

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

