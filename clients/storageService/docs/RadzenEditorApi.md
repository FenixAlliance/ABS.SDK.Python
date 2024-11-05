# openapi_client.RadzenEditorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_storage_service_radzen_editor_uploads_id_post**](RadzenEditorApi.md#api_v2_storage_service_radzen_editor_uploads_id_post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/{id} | 
[**api_v2_storage_service_radzen_editor_uploads_image_post**](RadzenEditorApi.md#api_v2_storage_service_radzen_editor_uploads_image_post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Image | 
[**api_v2_storage_service_radzen_editor_uploads_multiple_post**](RadzenEditorApi.md#api_v2_storage_service_radzen_editor_uploads_multiple_post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Multiple | 
[**api_v2_storage_service_radzen_editor_uploads_single_post**](RadzenEditorApi.md#api_v2_storage_service_radzen_editor_uploads_single_post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Single | 
[**api_v2_storage_service_radzen_editor_uploads_specific_post**](RadzenEditorApi.md#api_v2_storage_service_radzen_editor_uploads_specific_post) | **POST** /api/v2/StorageService/RadzenEditor/Uploads/Specific | 


# **api_v2_storage_service_radzen_editor_uploads_id_post**
> api_v2_storage_service_radzen_editor_uploads_id_post(id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)



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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    id = 56 # int | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    files = None # List[bytearray] |  (optional)

    try:
        api_instance.api_v2_storage_service_radzen_editor_uploads_id_post(id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->api_v2_storage_service_radzen_editor_uploads_id_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storage_service_radzen_editor_uploads_image_post**
> api_v2_storage_service_radzen_editor_uploads_image_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)



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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_instance.api_v2_storage_service_radzen_editor_uploads_image_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->api_v2_storage_service_radzen_editor_uploads_image_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storage_service_radzen_editor_uploads_multiple_post**
> api_v2_storage_service_radzen_editor_uploads_multiple_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)



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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    files = None # List[bytearray] |  (optional)

    try:
        api_instance.api_v2_storage_service_radzen_editor_uploads_multiple_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, files=files)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->api_v2_storage_service_radzen_editor_uploads_multiple_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storage_service_radzen_editor_uploads_single_post**
> api_v2_storage_service_radzen_editor_uploads_single_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)



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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_instance.api_v2_storage_service_radzen_editor_uploads_single_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->api_v2_storage_service_radzen_editor_uploads_single_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_storage_service_radzen_editor_uploads_specific_post**
> api_v2_storage_service_radzen_editor_uploads_specific_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)



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
    api_instance = openapi_client.RadzenEditorApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_instance.api_v2_storage_service_radzen_editor_uploads_specific_post(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, file=file)
    except Exception as e:
        print("Exception when calling RadzenEditorApi->api_v2_storage_service_radzen_editor_uploads_specific_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

