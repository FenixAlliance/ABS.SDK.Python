# openapi_client.LanguagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_languages_async**](LanguagesApi.md#count_languages_async) | **GET** /api/v2/GlobeService/Languages/Count | Count languages
[**get_language_by_id_async**](LanguagesApi.md#get_language_by_id_async) | **GET** /api/v2/GlobeService/Languages/{languageId} | Get language by ID
[**get_languages_async**](LanguagesApi.md#get_languages_async) | **GET** /api/v2/GlobeService/Languages | Get all languages


# **count_languages_async**
> Int32Envelope count_languages_async(api_version=api_version, x_api_version=x_api_version)

Count languages

Returns the total number of supported languages, with optional OData filtering.

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
    api_instance = openapi_client.LanguagesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count languages
        api_response = api_instance.count_languages_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of LanguagesApi->count_languages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguagesApi->count_languages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_language_by_id_async**
> CountryLanguageDtoEnvelope get_language_by_id_async(language_id, api_version=api_version, x_api_version=x_api_version)

Get language by ID

Retrieves a single language by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.country_language_dto_envelope import CountryLanguageDtoEnvelope
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
    api_instance = openapi_client.LanguagesApi(api_client)
    language_id = 'language_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get language by ID
        api_response = api_instance.get_language_by_id_async(language_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LanguagesApi->get_language_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguagesApi->get_language_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryLanguageDtoEnvelope**](CountryLanguageDtoEnvelope.md)

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

# **get_languages_async**
> CountryLanguageDtoListEnvelope get_languages_async(api_version=api_version, x_api_version=x_api_version)

Get all languages

Retrieves the list of all supported languages with optional OData pagination and filtering.

### Example


```python
import openapi_client
from openapi_client.models.country_language_dto_list_envelope import CountryLanguageDtoListEnvelope
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
    api_instance = openapi_client.LanguagesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all languages
        api_response = api_instance.get_languages_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of LanguagesApi->get_languages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguagesApi->get_languages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryLanguageDtoListEnvelope**](CountryLanguageDtoListEnvelope.md)

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

