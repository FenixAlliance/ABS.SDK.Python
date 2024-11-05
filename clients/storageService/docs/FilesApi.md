# openapi_client.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_async**](FilesApi.md#create_file_async) | **POST** /api/v2/StorageService/Files | 
[**delete_file_async**](FilesApi.md#delete_file_async) | **DELETE** /api/v2/StorageService/Files/{fileId} | 
[**download_file_async**](FilesApi.md#download_file_async) | **GET** /api/v2/StorageService/Files/{fileId}/Raw | 
[**get_file_async**](FilesApi.md#get_file_async) | **GET** /api/v2/StorageService/Files/{fileId} | 
[**get_files_async**](FilesApi.md#get_files_async) | **GET** /api/v2/StorageService/Files | 
[**update_file_async**](FilesApi.md#update_file_async) | **PUT** /api/v2/StorageService/Files/{fileId} | 


# **create_file_async**
> EmptyEnvelope create_file_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, id=id, timestamp=timestamp, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file)



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
    api_instance = openapi_client.FilesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
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

    try:
        api_response = api_instance.create_file_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, id=id, timestamp=timestamp, notes=notes, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file)
        print("The response of FilesApi->create_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **timestamp** | **datetime**|  | [optional] 
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

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_async**
> FileUploadDtoEnvelope delete_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.delete_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FilesApi->delete_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FileUploadDtoEnvelope**](FileUploadDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_async**
> bytearray download_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.download_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FilesApi->download_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->download_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_file_async**
> FileUploadDtoEnvelope get_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FilesApi->get_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FileUploadDtoEnvelope**](FileUploadDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_files_async**
> FileUploadDtoEnvelope get_files_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope
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
    api_instance = openapi_client.FilesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_files_async(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FilesApi->get_files_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_files_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FileUploadDtoEnvelope**](FileUploadDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **update_file_async**
> FileUploadDtoEnvelope update_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, metadata=metadata, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    notes = 'notes_example' # str |  (optional)
    metadata = 'metadata_example' # str |  (optional)
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

    try:
        api_response = api_instance.update_file_async(file_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, notes=notes, metadata=metadata, title=title, author=author, is_folder=is_folder, file_name=file_name, abstract=abstract, key_words=key_words, valid_response=valid_response, parent_file_upload_id=parent_file_upload_id, file_path=file_path, file=file)
        print("The response of FilesApi->update_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **metadata** | **str**|  | [optional] 
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

### Return type

[**FileUploadDtoEnvelope**](FileUploadDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

