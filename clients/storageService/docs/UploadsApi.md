# openapi_client.UploadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_storage_service_uploads_post**](UploadsApi.md#api_v2_storage_service_uploads_post) | **POST** /api/v2/StorageService/Uploads | 


# **api_v2_storage_service_uploads_post**
> EmptyEnvelope api_v2_storage_service_uploads_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file, i_d=i_d, timestamp=timestamp)



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
    api_instance = openapi_client.UploadsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    notes = 'notes_example' # str |  (optional)
    title = 'title_example' # str |  (optional)
    author = 'author_example' # str |  (optional)
    is_folder = True # bool |  (optional)
    file_name = 'file_name_example' # str |  (optional)
    abstract = 'abstract_example' # str |  (optional)
    key_words = 'key_words_example' # str |  (optional)
    valid_response = True # bool |  (optional)
    parent_file_upload_id = 'parent_file_upload_id_example' # str |  (optional)
    file_path = 'file_path_example' # str |  (optional)
    file = None # bytearray |  (optional)
    i_d = 'i_d_example' # str |  (optional)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.api_v2_storage_service_uploads_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file, i_d=i_d, timestamp=timestamp)
        print("The response of UploadsApi->api_v2_storage_service_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->api_v2_storage_service_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **author** | **str**|  | [optional] 
 **is_folder** | **bool**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **abstract** | **str**|  | [optional] 
 **key_words** | **str**|  | [optional] 
 **valid_response** | **bool**|  | [optional] 
 **parent_file_upload_id** | **str**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 
 **i_d** | **str**|  | [optional] 
 **timestamp** | **datetime**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

