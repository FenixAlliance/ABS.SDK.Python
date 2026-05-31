# openapi_client.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_async**](SubscriptionsApi.md#create_subscription_async) | **POST** /api/v2/SubscriptionsService/Subscriptions | Create a subscription
[**delete_subscription_async**](SubscriptionsApi.md#delete_subscription_async) | **DELETE** /api/v2/SubscriptionsService/Subscriptions/{subscriptionId} | Delete a subscription
[**get_subscription_by_id_async**](SubscriptionsApi.md#get_subscription_by_id_async) | **GET** /api/v2/SubscriptionsService/Subscriptions/{subscriptionId} | Get a subscription by ID
[**get_subscriptions_async**](SubscriptionsApi.md#get_subscriptions_async) | **GET** /api/v2/SubscriptionsService/Subscriptions | Get all subscriptions
[**get_subscriptions_count_async**](SubscriptionsApi.md#get_subscriptions_count_async) | **GET** /api/v2/SubscriptionsService/Subscriptions/Count | Get subscriptions count
[**update_subscription_async**](SubscriptionsApi.md#update_subscription_async) | **PUT** /api/v2/SubscriptionsService/Subscriptions/{subscriptionId} | Update a subscription


# **create_subscription_async**
> Envelope create_subscription_async(tenant_id, api_version=api_version, x_api_version=x_api_version, subscription_create_dto=subscription_create_dto)

Create a subscription

Creates a new subscription for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.subscription_create_dto import SubscriptionCreateDto
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    subscription_create_dto = openapi_client.SubscriptionCreateDto() # SubscriptionCreateDto |  (optional)

    try:
        # Create a subscription
        api_response = api_instance.create_subscription_async(tenant_id, api_version=api_version, x_api_version=x_api_version, subscription_create_dto=subscription_create_dto)
        print("The response of SubscriptionsApi->create_subscription_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->create_subscription_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **subscription_create_dto** | [**SubscriptionCreateDto**](SubscriptionCreateDto.md)|  | [optional] 

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

# **delete_subscription_async**
> Envelope delete_subscription_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version)

Delete a subscription

Deletes a subscription by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a subscription
        api_response = api_instance.delete_subscription_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionsApi->delete_subscription_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_subscription_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **subscription_id** | **str**|  | 
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

# **get_subscription_by_id_async**
> SubscriptionDtoEnvelope get_subscription_by_id_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version)

Get a subscription by ID

Retrieves a subscription by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.subscription_dto_envelope import SubscriptionDtoEnvelope
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a subscription by ID
        api_response = api_instance.get_subscription_by_id_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionsApi->get_subscription_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SubscriptionDtoEnvelope**](SubscriptionDtoEnvelope.md)

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

# **get_subscriptions_async**
> SubscriptionDtoIReadOnlyListEnvelope get_subscriptions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all subscriptions

Retrieves all subscriptions for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.subscription_dto_i_read_only_list_envelope import SubscriptionDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all subscriptions
        api_response = api_instance.get_subscriptions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionsApi->get_subscriptions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscriptions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SubscriptionDtoIReadOnlyListEnvelope**](SubscriptionDtoIReadOnlyListEnvelope.md)

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

# **get_subscriptions_count_async**
> Int32Envelope get_subscriptions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get subscriptions count

Returns the count of subscriptions for the specified tenant.

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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get subscriptions count
        api_response = api_instance.get_subscriptions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SubscriptionsApi->get_subscriptions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscriptions_count_async: %s\n" % e)
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

# **update_subscription_async**
> Envelope update_subscription_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version, subscription_update_dto=subscription_update_dto)

Update a subscription

Updates an existing subscription.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.subscription_update_dto import SubscriptionUpdateDto
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    subscription_update_dto = openapi_client.SubscriptionUpdateDto() # SubscriptionUpdateDto |  (optional)

    try:
        # Update a subscription
        api_response = api_instance.update_subscription_async(tenant_id, subscription_id, api_version=api_version, x_api_version=x_api_version, subscription_update_dto=subscription_update_dto)
        print("The response of SubscriptionsApi->update_subscription_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_subscription_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **subscription_update_dto** | [**SubscriptionUpdateDto**](SubscriptionUpdateDto.md)|  | [optional] 

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

