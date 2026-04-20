# openapi_client.MarketingListsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketing_list_async**](MarketingListsApi.md#create_marketing_list_async) | **POST** /api/v2/MarketingService/MarketingLists | Create a marketing list
[**delete_marketing_list_async**](MarketingListsApi.md#delete_marketing_list_async) | **DELETE** /api/v2/MarketingService/MarketingLists/{marketinglistId} | Delete a marketing list
[**get_marketing_list_details_async**](MarketingListsApi.md#get_marketing_list_details_async) | **GET** /api/v2/MarketingService/MarketingLists/{marketinglistId} | Get marketing list by ID
[**get_marketing_list_o_data_async**](MarketingListsApi.md#get_marketing_list_o_data_async) | **GET** /api/v2/MarketingService/MarketingLists | Get marketing lists
[**get_marketing_lists_count_async**](MarketingListsApi.md#get_marketing_lists_count_async) | **GET** /api/v2/MarketingService/MarketingLists/Count | Get marketing lists count
[**update_marketing_list_async**](MarketingListsApi.md#update_marketing_list_async) | **PUT** /api/v2/MarketingService/MarketingLists/{marketinglistId} | Update a marketing list


# **create_marketing_list_async**
> EmptyEnvelope create_marketing_list_async(tenant_id, marketing_list_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a marketing list

Creates a new marketing list for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_list_create_dto import MarketingListCreateDto
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_list_create_dto = openapi_client.MarketingListCreateDto() # MarketingListCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a marketing list
        api_response = api_instance.create_marketing_list_async(tenant_id, marketing_list_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->create_marketing_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->create_marketing_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_list_create_dto** | [**MarketingListCreateDto**](MarketingListCreateDto.md)|  | 
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

# **delete_marketing_list_async**
> EmptyEnvelope delete_marketing_list_async(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)

Delete a marketing list

Deletes a marketing list by its ID.

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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a marketing list
        api_response = api_instance.delete_marketing_list_async(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->delete_marketing_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->delete_marketing_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
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

# **get_marketing_list_details_async**
> MarketingListDtoEnvelope get_marketing_list_details_async(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)

Get marketing list by ID

Retrieves the details of a specific marketing list by its ID.

### Example


```python
import openapi_client
from openapi_client.models.marketing_list_dto_envelope import MarketingListDtoEnvelope
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing list by ID
        api_response = api_instance.get_marketing_list_details_async(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->get_marketing_list_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->get_marketing_list_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingListDtoEnvelope**](MarketingListDtoEnvelope.md)

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

# **get_marketing_list_o_data_async**
> MarketingListDtoListEnvelope get_marketing_list_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing lists

Retrieves a collection of marketing lists for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.marketing_list_dto_list_envelope import MarketingListDtoListEnvelope
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing lists
        api_response = api_instance.get_marketing_list_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->get_marketing_list_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->get_marketing_list_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingListDtoListEnvelope**](MarketingListDtoListEnvelope.md)

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

# **get_marketing_lists_count_async**
> Int32Envelope get_marketing_lists_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing lists count

Returns the count of marketing lists for the specified tenant using OData query options.

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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing lists count
        api_response = api_instance.get_marketing_lists_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->get_marketing_lists_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->get_marketing_lists_count_async: %s\n" % e)
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

# **update_marketing_list_async**
> EmptyEnvelope update_marketing_list_async(tenant_id, marketinglist_id, marketing_list_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a marketing list

Updates an existing marketing list by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_list_update_dto import MarketingListUpdateDto
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    marketing_list_update_dto = openapi_client.MarketingListUpdateDto() # MarketingListUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a marketing list
        api_response = api_instance.update_marketing_list_async(tenant_id, marketinglist_id, marketing_list_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->update_marketing_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->update_marketing_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
 **marketing_list_update_dto** | [**MarketingListUpdateDto**](MarketingListUpdateDto.md)|  | 
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

