# openapi_client.SubscriptionPlansApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_plan_async**](SubscriptionPlansApi.md#create_subscription_plan_async) | **POST** /api/v2/SubscriptionsService/SubscriptionPlans | Create a subscription plan
[**delete_subscription_plan_async**](SubscriptionPlansApi.md#delete_subscription_plan_async) | **DELETE** /api/v2/SubscriptionsService/SubscriptionPlans/{planId} | Delete a subscription plan
[**get_subscription_plan_by_id_async**](SubscriptionPlansApi.md#get_subscription_plan_by_id_async) | **GET** /api/v2/SubscriptionsService/SubscriptionPlans/{planId} | Get a subscription plan by ID
[**get_subscription_plans_async**](SubscriptionPlansApi.md#get_subscription_plans_async) | **GET** /api/v2/SubscriptionsService/SubscriptionPlans | Get all subscription plans
[**get_subscription_plans_count_async**](SubscriptionPlansApi.md#get_subscription_plans_count_async) | **GET** /api/v2/SubscriptionsService/SubscriptionPlans/Count | Get subscription plans count
[**update_subscription_plan_async**](SubscriptionPlansApi.md#update_subscription_plan_async) | **PUT** /api/v2/SubscriptionsService/SubscriptionPlans/{planId} | Update a subscription plan


# **create_subscription_plan_async**
> Envelope create_subscription_plan_async(tenant_id, api_version=api_version, x_api_version=x_api_version, subscription_plan_create_dto=subscription_plan_create_dto)

Create a subscription plan

Creates a new subscription plan for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.subscription_plan_create_dto import SubscriptionPlanCreateDto
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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    subscription_plan_create_dto = openapi_client.SubscriptionPlanCreateDto() # SubscriptionPlanCreateDto |  (optional)

    try:
        # Create a subscription plan
        api_response = api_instance.create_subscription_plan_async(tenant_id, api_version=api_version, x_api_version=x_api_version, subscription_plan_create_dto=subscription_plan_create_dto)
        print("The response of SubscriptionPlansApi->create_subscription_plan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->create_subscription_plan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **subscription_plan_create_dto** | [**SubscriptionPlanCreateDto**](SubscriptionPlanCreateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **delete_subscription_plan_async**
> Envelope delete_subscription_plan_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version)

Delete a subscription plan

Deletes a subscription plan by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a subscription plan
        api_response = api_instance.delete_subscription_plan_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionPlansApi->delete_subscription_plan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->delete_subscription_plan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **get_subscription_plan_by_id_async**
> SubscriptionPlanDtoEnvelope get_subscription_plan_by_id_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version)

Get a subscription plan by ID

Retrieves a subscription plan by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.subscription_plan_dto_envelope import SubscriptionPlanDtoEnvelope
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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a subscription plan by ID
        api_response = api_instance.get_subscription_plan_by_id_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionPlansApi->get_subscription_plan_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->get_subscription_plan_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SubscriptionPlanDtoEnvelope**](SubscriptionPlanDtoEnvelope.md)

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

# **get_subscription_plans_async**
> SubscriptionPlanDtoIReadOnlyListEnvelope get_subscription_plans_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all subscription plans

Retrieves all subscription plans for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.subscription_plan_dto_i_read_only_list_envelope import SubscriptionPlanDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all subscription plans
        api_response = api_instance.get_subscription_plans_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionPlansApi->get_subscription_plans_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->get_subscription_plans_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SubscriptionPlanDtoIReadOnlyListEnvelope**](SubscriptionPlanDtoIReadOnlyListEnvelope.md)

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

# **get_subscription_plans_count_async**
> Int32Envelope get_subscription_plans_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get subscription plans count

Returns the count of subscription plans for the specified tenant.

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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get subscription plans count
        api_response = api_instance.get_subscription_plans_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionPlansApi->get_subscription_plans_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->get_subscription_plans_count_async: %s\n" % e)
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

# **update_subscription_plan_async**
> Envelope update_subscription_plan_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version, subscription_plan_update_dto=subscription_plan_update_dto)

Update a subscription plan

Updates an existing subscription plan.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.subscription_plan_update_dto import SubscriptionPlanUpdateDto
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
    api_instance = openapi_client.SubscriptionPlansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    subscription_plan_update_dto = openapi_client.SubscriptionPlanUpdateDto() # SubscriptionPlanUpdateDto |  (optional)

    try:
        # Update a subscription plan
        api_response = api_instance.update_subscription_plan_async(tenant_id, plan_id, api_version=api_version, x_api_version=x_api_version, subscription_plan_update_dto=subscription_plan_update_dto)
        print("The response of SubscriptionPlansApi->update_subscription_plan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPlansApi->update_subscription_plan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **subscription_plan_update_dto** | [**SubscriptionPlanUpdateDto**](SubscriptionPlanUpdateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

