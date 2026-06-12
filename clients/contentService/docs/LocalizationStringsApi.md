# openapi_client.LocalizationStringsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_localization_strings_async**](LocalizationStringsApi.md#count_localization_strings_async) | **GET** /api/v2/ContentService/LocalizationStrings/Count | Count localization strings
[**create_localization_string_async**](LocalizationStringsApi.md#create_localization_string_async) | **POST** /api/v2/ContentService/LocalizationStrings | Create a localization string
[**delete_localization_string_async**](LocalizationStringsApi.md#delete_localization_string_async) | **DELETE** /api/v2/ContentService/LocalizationStrings/{localizationStringId} | Delete a localization string
[**get_localization_string_by_id_async**](LocalizationStringsApi.md#get_localization_string_by_id_async) | **GET** /api/v2/ContentService/LocalizationStrings/{localizationStringId} | Get localization string by ID
[**get_localization_strings_async**](LocalizationStringsApi.md#get_localization_strings_async) | **GET** /api/v2/ContentService/LocalizationStrings | Get localization strings
[**update_localization_string_async**](LocalizationStringsApi.md#update_localization_string_async) | **PUT** /api/v2/ContentService/LocalizationStrings/{localizationStringId} | Update a localization string


# **count_localization_strings_async**
> Int32Envelope count_localization_strings_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count localization strings

Counts all localization strings for the specified tenant.

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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count localization strings
        api_response = api_instance.count_localization_strings_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->count_localization_strings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->count_localization_strings_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localization_string_async**
> EmptyEnvelope create_localization_string_async(tenant_id, localization_string_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a localization string

Creates a new localization string for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.localization_string_create_dto import LocalizationStringCreateDto
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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    localization_string_create_dto = openapi_client.LocalizationStringCreateDto() # LocalizationStringCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a localization string
        api_response = api_instance.create_localization_string_async(tenant_id, localization_string_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->create_localization_string_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->create_localization_string_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **localization_string_create_dto** | [**LocalizationStringCreateDto**](LocalizationStringCreateDto.md)|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localization_string_async**
> EmptyEnvelope delete_localization_string_async(tenant_id, localization_string_id, api_version=api_version, x_api_version=x_api_version)

Delete a localization string

Deletes a localization string for the specified tenant.

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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    localization_string_id = 'localization_string_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a localization string
        api_response = api_instance.delete_localization_string_async(tenant_id, localization_string_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->delete_localization_string_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->delete_localization_string_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **localization_string_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_string_by_id_async**
> LocalizationStringDtoEnvelope get_localization_string_by_id_async(tenant_id, localization_string_id, api_version=api_version, x_api_version=x_api_version)

Get localization string by ID

Retrieves a specific localization string by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.localization_string_dto_envelope import LocalizationStringDtoEnvelope
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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    localization_string_id = 'localization_string_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get localization string by ID
        api_response = api_instance.get_localization_string_by_id_async(tenant_id, localization_string_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->get_localization_string_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->get_localization_string_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **localization_string_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LocalizationStringDtoEnvelope**](LocalizationStringDtoEnvelope.md)

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

# **get_localization_strings_async**
> LocalizationStringDtoListEnvelope get_localization_strings_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get localization strings

Retrieves all localization strings for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.localization_string_dto_list_envelope import LocalizationStringDtoListEnvelope
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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get localization strings
        api_response = api_instance.get_localization_strings_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->get_localization_strings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->get_localization_strings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LocalizationStringDtoListEnvelope**](LocalizationStringDtoListEnvelope.md)

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

# **update_localization_string_async**
> EmptyEnvelope update_localization_string_async(tenant_id, localization_string_id, localization_string_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a localization string

Updates an existing localization string for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.localization_string_update_dto import LocalizationStringUpdateDto
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
    api_instance = openapi_client.LocalizationStringsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    localization_string_id = 'localization_string_id_example' # str | 
    localization_string_update_dto = openapi_client.LocalizationStringUpdateDto() # LocalizationStringUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a localization string
        api_response = api_instance.update_localization_string_async(tenant_id, localization_string_id, localization_string_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LocalizationStringsApi->update_localization_string_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalizationStringsApi->update_localization_string_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **localization_string_id** | **str**|  | 
 **localization_string_update_dto** | [**LocalizationStringUpdateDto**](LocalizationStringUpdateDto.md)|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

