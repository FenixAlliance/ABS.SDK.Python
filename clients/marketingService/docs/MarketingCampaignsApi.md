# openapi_client.MarketingCampaignsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketing_campaign_async**](MarketingCampaignsApi.md#create_marketing_campaign_async) | **POST** /api/v2/MarketingService/MarketingCampaigns | Create a marketing campaign
[**delete_marketing_campaign_async**](MarketingCampaignsApi.md#delete_marketing_campaign_async) | **DELETE** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | Delete a marketing campaign
[**get_marketing_campaign_details_async**](MarketingCampaignsApi.md#get_marketing_campaign_details_async) | **GET** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | Get marketing campaign by ID
[**get_marketing_campaign_o_data_async**](MarketingCampaignsApi.md#get_marketing_campaign_o_data_async) | **GET** /api/v2/MarketingService/MarketingCampaigns | Get marketing campaigns
[**get_marketing_campaigns_count_async**](MarketingCampaignsApi.md#get_marketing_campaigns_count_async) | **GET** /api/v2/MarketingService/MarketingCampaigns/Count | Get marketing campaigns count
[**update_marketing_campaign_async**](MarketingCampaignsApi.md#update_marketing_campaign_async) | **PUT** /api/v2/MarketingService/MarketingCampaigns/{marketingcampaignId} | Update a marketing campaign


# **create_marketing_campaign_async**
> EmptyEnvelope create_marketing_campaign_async(tenant_id, marketing_campaign_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a marketing campaign

Creates a new marketing campaign for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_campaign_create_dto import MarketingCampaignCreateDto
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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_campaign_create_dto = openapi_client.MarketingCampaignCreateDto() # MarketingCampaignCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a marketing campaign
        api_response = api_instance.create_marketing_campaign_async(tenant_id, marketing_campaign_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->create_marketing_campaign_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->create_marketing_campaign_async: %s\n" % e)
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

No authorization required

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

# **delete_marketing_campaign_async**
> EmptyEnvelope delete_marketing_campaign_async(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)

Delete a marketing campaign

Deletes a marketing campaign by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a marketing campaign
        api_response = api_instance.delete_marketing_campaign_async(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->delete_marketing_campaign_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->delete_marketing_campaign_async: %s\n" % e)
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

No authorization required

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

# **get_marketing_campaign_details_async**
> MarketingCampaignDtoEnvelope get_marketing_campaign_details_async(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)

Get marketing campaign by ID

Retrieves the details of a specific marketing campaign by its ID.

### Example


```python
import openapi_client
from openapi_client.models.marketing_campaign_dto_envelope import MarketingCampaignDtoEnvelope
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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing campaign by ID
        api_response = api_instance.get_marketing_campaign_details_async(tenant_id, marketingcampaign_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->get_marketing_campaign_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->get_marketing_campaign_details_async: %s\n" % e)
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

No authorization required

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

# **get_marketing_campaign_o_data_async**
> get_marketing_campaign_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing campaigns

Retrieves a collection of marketing campaigns for the specified tenant using OData query options.

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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing campaigns
        api_instance.get_marketing_campaign_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->get_marketing_campaign_o_data_async: %s\n" % e)
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

No authorization required

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

# **get_marketing_campaigns_count_async**
> Int32Envelope get_marketing_campaigns_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing campaigns count

Returns the count of marketing campaigns for the specified tenant using OData query options.

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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing campaigns count
        api_response = api_instance.get_marketing_campaigns_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->get_marketing_campaigns_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->get_marketing_campaigns_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marketing_campaign_async**
> EmptyEnvelope update_marketing_campaign_async(tenant_id, marketingcampaign_id, marketing_campaign_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a marketing campaign

Updates an existing marketing campaign by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_campaign_update_dto import MarketingCampaignUpdateDto
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
    api_instance = openapi_client.MarketingCampaignsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketingcampaign_id = 'marketingcampaign_id_example' # str | 
    marketing_campaign_update_dto = openapi_client.MarketingCampaignUpdateDto() # MarketingCampaignUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a marketing campaign
        api_response = api_instance.update_marketing_campaign_async(tenant_id, marketingcampaign_id, marketing_campaign_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingCampaignsApi->update_marketing_campaign_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCampaignsApi->update_marketing_campaign_async: %s\n" % e)
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

No authorization required

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

