# openapi_client.ItemRetainSamplesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_retain_sample_async**](ItemRetainSamplesApi.md#create_item_retain_sample_async) | **POST** /api/v2/LogisticsService/ItemRetainSamples | Create an item retain sample
[**delete_item_retain_sample_async**](ItemRetainSamplesApi.md#delete_item_retain_sample_async) | **DELETE** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Delete an item retain sample
[**get_item_retain_sample_by_id_async**](ItemRetainSamplesApi.md#get_item_retain_sample_by_id_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Get item retain sample by ID
[**get_item_retain_samples_async**](ItemRetainSamplesApi.md#get_item_retain_samples_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples | Get all item retain samples
[**get_item_retain_samples_count_async**](ItemRetainSamplesApi.md#get_item_retain_samples_count_async) | **GET** /api/v2/LogisticsService/ItemRetainSamples/Count | Get item retain samples count
[**update_item_retain_sample_async**](ItemRetainSamplesApi.md#update_item_retain_sample_async) | **PUT** /api/v2/LogisticsService/ItemRetainSamples/{retainSampleId} | Update an item retain sample


# **create_item_retain_sample_async**
> EmptyEnvelope create_item_retain_sample_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_create_dto=item_retain_sample_create_dto)

Create an item retain sample

Creates a new item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_retain_sample_create_dto import ItemRetainSampleCreateDto
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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_retain_sample_create_dto = openapi_client.ItemRetainSampleCreateDto() # ItemRetainSampleCreateDto |  (optional)

    try:
        # Create an item retain sample
        api_response = api_instance.create_item_retain_sample_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_create_dto=item_retain_sample_create_dto)
        print("The response of ItemRetainSamplesApi->create_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->create_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_retain_sample_create_dto** | [**ItemRetainSampleCreateDto**](ItemRetainSampleCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_retain_sample_async**
> EmptyEnvelope delete_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)

Delete an item retain sample

Deletes an item retain sample.

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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item retain sample
        api_response = api_instance.delete_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRetainSamplesApi->delete_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->delete_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_retain_sample_by_id_async**
> ItemRetainSampleDtoEnvelope get_item_retain_sample_by_id_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)

Get item retain sample by ID

Retrieves a specific item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.item_retain_sample_dto_envelope import ItemRetainSampleDtoEnvelope
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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item retain sample by ID
        api_response = api_instance.get_item_retain_sample_by_id_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRetainSamplesApi->get_item_retain_sample_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->get_item_retain_sample_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRetainSampleDtoEnvelope**](ItemRetainSampleDtoEnvelope.md)

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

# **get_item_retain_samples_async**
> ItemRetainSampleDtoListEnvelope get_item_retain_samples_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item retain samples

Retrieves all item retain samples for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_retain_sample_dto_list_envelope import ItemRetainSampleDtoListEnvelope
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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item retain samples
        api_response = api_instance.get_item_retain_samples_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRetainSamplesApi->get_item_retain_samples_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->get_item_retain_samples_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRetainSampleDtoListEnvelope**](ItemRetainSampleDtoListEnvelope.md)

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

# **get_item_retain_samples_count_async**
> Int32Envelope get_item_retain_samples_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get item retain samples count

Returns the count of item retain samples.

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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item retain samples count
        api_response = api_instance.get_item_retain_samples_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemRetainSamplesApi->get_item_retain_samples_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->get_item_retain_samples_count_async: %s\n" % e)
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

# **update_item_retain_sample_async**
> EmptyEnvelope update_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_update_dto=item_retain_sample_update_dto)

Update an item retain sample

Updates an existing item retain sample.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_retain_sample_update_dto import ItemRetainSampleUpdateDto
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
    api_instance = openapi_client.ItemRetainSamplesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    retain_sample_id = 'retain_sample_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_retain_sample_update_dto = openapi_client.ItemRetainSampleUpdateDto() # ItemRetainSampleUpdateDto |  (optional)

    try:
        # Update an item retain sample
        api_response = api_instance.update_item_retain_sample_async(tenant_id, retain_sample_id, api_version=api_version, x_api_version=x_api_version, item_retain_sample_update_dto=item_retain_sample_update_dto)
        print("The response of ItemRetainSamplesApi->update_item_retain_sample_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemRetainSamplesApi->update_item_retain_sample_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **retain_sample_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_retain_sample_update_dto** | [**ItemRetainSampleUpdateDto**](ItemRetainSampleUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

