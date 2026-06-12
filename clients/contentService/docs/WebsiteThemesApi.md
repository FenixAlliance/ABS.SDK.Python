# openapi_client.WebsiteThemesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_website_theme_async**](WebsiteThemesApi.md#create_website_theme_async) | **POST** /api/v2/ContentService/WebsiteThemes | Create a new website theme
[**delete_website_theme_async**](WebsiteThemesApi.md#delete_website_theme_async) | **DELETE** /api/v2/ContentService/WebsiteThemes/{id} | Delete a website theme
[**get_website_theme_by_id_async**](WebsiteThemesApi.md#get_website_theme_by_id_async) | **GET** /api/v2/ContentService/WebsiteThemes/{id} | Get website theme by ID
[**get_website_themes_async**](WebsiteThemesApi.md#get_website_themes_async) | **GET** /api/v2/ContentService/WebsiteThemes | Get all website themes
[**get_website_themes_count_async**](WebsiteThemesApi.md#get_website_themes_count_async) | **GET** /api/v2/ContentService/WebsiteThemes/Count | Get website themes count
[**patch_website_theme_async**](WebsiteThemesApi.md#patch_website_theme_async) | **PATCH** /api/v2/ContentService/WebsiteThemes/{id} | Patch a website theme
[**update_website_theme_async**](WebsiteThemesApi.md#update_website_theme_async) | **PUT** /api/v2/ContentService/WebsiteThemes/{id} | Update a website theme


# **create_website_theme_async**
> create_website_theme_async(tenant_id, api_version=api_version, x_api_version=x_api_version, website_theme_create_dto=website_theme_create_dto)

Create a new website theme

Creates a new website theme for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.website_theme_create_dto import WebsiteThemeCreateDto
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    website_theme_create_dto = openapi_client.WebsiteThemeCreateDto() # WebsiteThemeCreateDto |  (optional)

    try:
        # Create a new website theme
        api_instance.create_website_theme_async(tenant_id, api_version=api_version, x_api_version=x_api_version, website_theme_create_dto=website_theme_create_dto)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->create_website_theme_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **website_theme_create_dto** | [**WebsiteThemeCreateDto**](WebsiteThemeCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_theme_async**
> delete_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete a website theme

Deletes a website theme for the specified tenant.

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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a website theme
        api_instance.delete_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->delete_website_theme_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_theme_by_id_async**
> WebsiteThemeDto get_website_theme_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get website theme by ID

Retrieves a specific website theme by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.website_theme_dto import WebsiteThemeDto
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get website theme by ID
        api_response = api_instance.get_website_theme_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebsiteThemesApi->get_website_theme_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->get_website_theme_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebsiteThemeDto**](WebsiteThemeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_themes_async**
> WebsiteThemeDtoListEnvelope get_website_themes_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get all website themes

Retrieves all website themes for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.website_theme_dto_list_envelope import WebsiteThemeDtoListEnvelope
from openapi_client.models.website_theme_dto_o_data_query_options import WebsiteThemeDtoODataQueryOptions
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.WebsiteThemeDtoODataQueryOptions() # WebsiteThemeDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all website themes
        api_response = api_instance.get_website_themes_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebsiteThemesApi->get_website_themes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->get_website_themes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**WebsiteThemeDtoODataQueryOptions**](.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebsiteThemeDtoListEnvelope**](WebsiteThemeDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_themes_count_async**
> Int32Envelope get_website_themes_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get website themes count

Returns the count of website themes for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.models.website_theme_dto_o_data_query_options import WebsiteThemeDtoODataQueryOptions
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.WebsiteThemeDtoODataQueryOptions() # WebsiteThemeDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get website themes count
        api_response = api_instance.get_website_themes_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebsiteThemesApi->get_website_themes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->get_website_themes_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**WebsiteThemeDtoODataQueryOptions**](.md)|  | [optional] 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_theme_async**
> patch_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a website theme

Partially updates an existing website theme for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a website theme
        api_instance.patch_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->patch_website_theme_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_theme_async**
> update_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, website_theme_update_dto=website_theme_update_dto)

Update a website theme

Updates an existing website theme for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.website_theme_update_dto import WebsiteThemeUpdateDto
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
    api_instance = openapi_client.WebsiteThemesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    website_theme_update_dto = openapi_client.WebsiteThemeUpdateDto() # WebsiteThemeUpdateDto |  (optional)

    try:
        # Update a website theme
        api_instance.update_website_theme_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, website_theme_update_dto=website_theme_update_dto)
    except Exception as e:
        print("Exception when calling WebsiteThemesApi->update_website_theme_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **website_theme_update_dto** | [**WebsiteThemeUpdateDto**](WebsiteThemeUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

