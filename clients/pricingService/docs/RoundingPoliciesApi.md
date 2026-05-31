# openapi_client.RoundingPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rounding_policy_async**](RoundingPoliciesApi.md#create_rounding_policy_async) | **POST** /api/v2/PricingService/RoundingPolicies | Creates a rounding policy
[**delete_rounding_policy_async**](RoundingPoliciesApi.md#delete_rounding_policy_async) | **DELETE** /api/v2/PricingService/RoundingPolicies/{roundingPolicyId} | Deletes a rounding policy
[**get_rounding_policies_async**](RoundingPoliciesApi.md#get_rounding_policies_async) | **GET** /api/v2/PricingService/RoundingPolicies | Gets all rounding policies
[**get_rounding_policies_count_async**](RoundingPoliciesApi.md#get_rounding_policies_count_async) | **GET** /api/v2/PricingService/RoundingPolicies/Count | Counts rounding policies
[**get_rounding_policy_by_id_async**](RoundingPoliciesApi.md#get_rounding_policy_by_id_async) | **GET** /api/v2/PricingService/RoundingPolicies/{roundingPolicyId} | Gets a rounding policy by ID
[**update_rounding_policy_async**](RoundingPoliciesApi.md#update_rounding_policy_async) | **PUT** /api/v2/PricingService/RoundingPolicies/{roundingPolicyId} | Updates a rounding policy


# **create_rounding_policy_async**
> EmptyEnvelope create_rounding_policy_async(tenant_id, rounding_policy_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a rounding policy

Creates a new rounding policy for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.rounding_policy_create_dto import RoundingPolicyCreateDto
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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rounding_policy_create_dto = openapi_client.RoundingPolicyCreateDto() # RoundingPolicyCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a rounding policy
        api_response = api_instance.create_rounding_policy_async(tenant_id, rounding_policy_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->create_rounding_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->create_rounding_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rounding_policy_create_dto** | [**RoundingPolicyCreateDto**](RoundingPolicyCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rounding_policy_async**
> EmptyEnvelope delete_rounding_policy_async(tenant_id, rounding_policy_id, api_version=api_version, x_api_version=x_api_version)

Deletes a rounding policy

Deletes the specified rounding policy.

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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rounding_policy_id = 'rounding_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a rounding policy
        api_response = api_instance.delete_rounding_policy_async(tenant_id, rounding_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->delete_rounding_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->delete_rounding_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rounding_policy_id** | **str**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rounding_policies_async**
> RoundingPolicyDtoListEnvelope get_rounding_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all rounding policies

Retrieves all rounding policies for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.rounding_policy_dto_list_envelope import RoundingPolicyDtoListEnvelope
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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all rounding policies
        api_response = api_instance.get_rounding_policies_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->get_rounding_policies_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->get_rounding_policies_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RoundingPolicyDtoListEnvelope**](RoundingPolicyDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rounding_policies_count_async**
> Int32Envelope get_rounding_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts rounding policies

Gets the count of rounding policies for the current tenant.

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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts rounding policies
        api_response = api_instance.get_rounding_policies_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->get_rounding_policies_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->get_rounding_policies_count_async: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rounding_policy_by_id_async**
> RoundingPolicyDtoEnvelope get_rounding_policy_by_id_async(tenant_id, rounding_policy_id, api_version=api_version, x_api_version=x_api_version)

Gets a rounding policy by ID

Retrieves the details of a rounding policy using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.rounding_policy_dto_envelope import RoundingPolicyDtoEnvelope
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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rounding_policy_id = 'rounding_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a rounding policy by ID
        api_response = api_instance.get_rounding_policy_by_id_async(tenant_id, rounding_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->get_rounding_policy_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->get_rounding_policy_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rounding_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RoundingPolicyDtoEnvelope**](RoundingPolicyDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rounding_policy_async**
> EmptyEnvelope update_rounding_policy_async(tenant_id, rounding_policy_id, rounding_policy_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a rounding policy

Updates the specified rounding policy.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.rounding_policy_update_dto import RoundingPolicyUpdateDto
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
    api_instance = openapi_client.RoundingPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rounding_policy_id = 'rounding_policy_id_example' # str | 
    rounding_policy_update_dto = openapi_client.RoundingPolicyUpdateDto() # RoundingPolicyUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a rounding policy
        api_response = api_instance.update_rounding_policy_async(tenant_id, rounding_policy_id, rounding_policy_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of RoundingPoliciesApi->update_rounding_policy_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoundingPoliciesApi->update_rounding_policy_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rounding_policy_id** | **str**|  | 
 **rounding_policy_update_dto** | [**RoundingPolicyUpdateDto**](RoundingPolicyUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

