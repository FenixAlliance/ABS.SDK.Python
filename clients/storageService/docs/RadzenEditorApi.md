# openapi_client.RadzenEditorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image**](RadzenEditorApi.md#image) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Image | Upload an image file
[**multiple**](RadzenEditorApi.md#multiple) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Multiple | Upload multiple files
[**post**](RadzenEditorApi.md#post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/{id} | Upload files by ID
[**single**](RadzenEditorApi.md#single) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Single | Upload a single file
[**specific**](RadzenEditorApi.md#specific) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Specific | Upload a specific file


# **image**
> image(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)

Upload an image file

Uploads an image file and returns its URL for editor embedding.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Upload an image file
        api_instance.image(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multiple**
> multiple(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)

Upload multiple files

Uploads multiple files to tenant or user storage.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    files = None # List[bytearray] |  (optional)

    try:
        # Upload multiple files
        api_instance.multiple(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> post(id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)

Upload files by ID

Uploads files associated with a specific resource ID.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    id = 56 # int | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    files = None # List[bytearray] |  (optional)

    try:
        # Upload files by ID
        api_instance.post(id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **single**
> single(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)

Upload a single file

Uploads a single file to tenant or user storage.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Upload a single file
        api_instance.single(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specific**
> specific(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)

Upload a specific file

Uploads a specific file to tenant or user storage.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Upload a specific file
        api_instance.specific(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->specific: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

