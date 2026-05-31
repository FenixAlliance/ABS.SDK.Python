# openapi_client.BlobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_blob_async**](BlobsApi.md#get_blob_async) | **GET** /api/v2/StorageService/Blobs/Single | 
[**get_blobs_async**](BlobsApi.md#get_blobs_async) | **GET** /api/v2/StorageService/Blobs | 


# **get_blob_async**
> BlobEnvelope get_blob_async(tenant_id=tenant_id, file_path=file_path, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.blob_envelope import BlobEnvelope
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
    api_instance = openapi_client.BlobsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    file_path = 'file_path_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_blob_async(tenant_id=tenant_id, file_path=file_path, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlobsApi->get_blob_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlobsApi->get_blob_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlobEnvelope**](BlobEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blobs_async**
> BlobEnvelope get_blobs_async(tenant_id=tenant_id, folder_path=folder_path, browse_filter=browse_filter, file_prefix=file_prefix, recurse=recurse, max_results=max_results, include_attributes=include_attributes, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.blob_envelope import BlobEnvelope
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
    api_instance = openapi_client.BlobsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    folder_path = 'folder_path_example' # str |  (optional)
    browse_filter = 'browse_filter_example' # str |  (optional)
    file_prefix = 'file_prefix_example' # str |  (optional)
    recurse = True # bool |  (optional)
    max_results = 56 # int |  (optional)
    include_attributes = True # bool |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_blobs_async(tenant_id=tenant_id, folder_path=folder_path, browse_filter=browse_filter, file_prefix=file_prefix, recurse=recurse, max_results=max_results, include_attributes=include_attributes, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlobsApi->get_blobs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlobsApi->get_blobs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **folder_path** | **str**|  | [optional] 
 **browse_filter** | **str**|  | [optional] 
 **file_prefix** | **str**|  | [optional] 
 **recurse** | **bool**|  | [optional] 
 **max_results** | **int**|  | [optional] 
 **include_attributes** | **bool**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlobEnvelope**](BlobEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

