# openapi_client.MarketingCampaignsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_marketing_service_marketing_campaigns_count_get**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_count_get) | **GET** /api/v2/MarketingService/MarketingCampaigns/Count | 
[**api_v2_marketing_service_marketing_campaigns_get**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_get) | **GET** /api/v2/MarketingService/MarketingCampaigns | 
[**api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete) | **DELETE** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | 
[**api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get) | **GET** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | 
[**api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put) | **PUT** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | 
[**api_v2_marketing_service_marketing_campaigns_post**](MarketingCampaignsApi.md#api_v2_marketing_service_marketing_campaigns_post) | **POST** /api/v2/MarketingService/MarketingCampaigns | 


# **api_v2_marketing_service_marketing_campaigns_count_get**
> Int32Envelope api_v2_marketing_service_marketing_campaigns_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_campaigns_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_count_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_campaigns_get**
> api_v2_marketing_service_marketing_campaigns_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_instance.api_v2_marketing_service_marketing_campaigns_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete**
> EmptyEnvelope api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketingcampaign_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get**
> MarketingCampaignDtoEnvelope api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.marketing_campaign_dto_envelope import MarketingCampaignDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketingcampaign_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingCampaignDtoEnvelope**](MarketingCampaignDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put**
> EmptyEnvelope api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put(tenant_id, marketingcampaign_id, marketing_campaign_update_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_campaign_update_dto import MarketingCampaignUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    marketing_campaign_update_dto = openapi_client.MarketingCampaignUpdateDto() # MarketingCampaignUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put(tenant_id, marketingcampaign_id, marketing_campaign_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_marketingcampaign_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketingcampaign_id** | **str**|  | 
 **marketing_campaign_update_dto** | [**MarketingCampaignUpdateDto**](MarketingCampaignUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_campaigns_post**
> EmptyEnvelope api_v2_marketing_service_marketing_campaigns_post(tenant_id, marketing_campaign_create_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_campaign_create_dto import MarketingCampaignCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_campaign_create_dto = openapi_client.MarketingCampaignCreateDto() # MarketingCampaignCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_campaigns_post(tenant_id, marketing_campaign_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->api_v2_marketing_service_marketing_campaigns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_campaign_create_dto** | [**MarketingCampaignCreateDto**](MarketingCampaignCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

