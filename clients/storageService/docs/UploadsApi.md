# openapi_client.UploadsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_file_async**](UploadsApi.md#save_file_async) | **POST** /api/v2/StorageService/Uploads | Upload a file


# **save_file_async**
> EmptyEnvelope save_file_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, app_file_content=app_file_content, app_file_sha256=app_file_sha256, app_file_created_at_utc=app_file_created_at_utc, app_file_user_id_value=app_file_user_id_value, app_file_tenant_id_value=app_file_tenant_id_value, app_file_enrollment_id_value=app_file_enrollment_id_value, app_file_source=app_file_source, app_file_length=app_file_length, app_file_name=app_file_name, app_file_file_name=app_file_file_name, app_file_last_modified=app_file_last_modified, app_file_size=app_file_size, app_file_content_type=app_file_content_type, app_file_content_disposition=app_file_content_disposition, app_file_headers=app_file_headers, id=id, timestamp=timestamp)

Upload a file

Uploads a file to tenant or user storage.

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
    app_file_content = None # bytearray |  (optional)
    app_file_sha256 = 'app_file_sha256_example' # str |  (optional)
    app_file_created_at_utc = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    app_file_user_id_value = 'app_file_user_id_value_example' # str |  (optional)
    app_file_tenant_id_value = 'app_file_tenant_id_value_example' # str |  (optional)
    app_file_enrollment_id_value = 'app_file_enrollment_id_value_example' # str |  (optional)
    app_file_source = 'app_file_source_example' # str |  (optional)
    app_file_length = 56 # int |  (optional)
    app_file_name = 'app_file_name_example' # str |  (optional)
    app_file_file_name = 'app_file_file_name_example' # str |  (optional)
    app_file_last_modified = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    app_file_size = 56 # int |  (optional)
    app_file_content_type = 'app_file_content_type_example' # str |  (optional)
    app_file_content_disposition = 'app_file_content_disposition_example' # str |  (optional)
    app_file_headers = None # Dict[str, str] |  (optional)
    id = 'id_example' # str |  (optional)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Upload a file
        api_response = api_instance.save_file_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, app_file_content=app_file_content, app_file_sha256=app_file_sha256, app_file_created_at_utc=app_file_created_at_utc, app_file_user_id_value=app_file_user_id_value, app_file_tenant_id_value=app_file_tenant_id_value, app_file_enrollment_id_value=app_file_enrollment_id_value, app_file_source=app_file_source, app_file_length=app_file_length, app_file_name=app_file_name, app_file_file_name=app_file_file_name, app_file_last_modified=app_file_last_modified, app_file_size=app_file_size, app_file_content_type=app_file_content_type, app_file_content_disposition=app_file_content_disposition, app_file_headers=app_file_headers, id=id, timestamp=timestamp)
        print("The response of UploadsApi->save_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->save_file_async: %s\n" % e)
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
 **app_file_content** | **bytearray**|  | [optional] 
 **app_file_sha256** | **str**|  | [optional] 
 **app_file_created_at_utc** | **datetime**|  | [optional] 
 **app_file_user_id_value** | **str**|  | [optional] 
 **app_file_tenant_id_value** | **str**|  | [optional] 
 **app_file_enrollment_id_value** | **str**|  | [optional] 
 **app_file_source** | **str**|  | [optional] 
 **app_file_length** | **int**|  | [optional] 
 **app_file_name** | **str**|  | [optional] 
 **app_file_file_name** | **str**|  | [optional] 
 **app_file_last_modified** | **datetime**|  | [optional] 
 **app_file_size** | **int**|  | [optional] 
 **app_file_content_type** | **str**|  | [optional] 
 **app_file_content_disposition** | **str**|  | [optional] 
 **app_file_headers** | [**Dict[str, str]**](Dict.md)|  | [optional] 
 **id** | **str**|  | [optional] 
 **timestamp** | **datetime**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

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

