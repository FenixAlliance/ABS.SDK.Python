# openapi_client.WebPageCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_page_category_async**](WebPageCategoriesApi.md#create_web_page_category_async) | **POST** /api/v2/ContentService/WebPageCategories | Create a web page category
[**delete_web_page_category_async**](WebPageCategoriesApi.md#delete_web_page_category_async) | **DELETE** /api/v2/ContentService/WebPageCategories/{webPageCategoryId} | Delete a web page category
[**get_web_page_categories_async**](WebPageCategoriesApi.md#get_web_page_categories_async) | **GET** /api/v2/ContentService/WebPageCategories | Get web page categories
[**get_web_page_category_by_id_async**](WebPageCategoriesApi.md#get_web_page_category_by_id_async) | **GET** /api/v2/ContentService/WebPageCategories/{webPageCategoryId} | Get web page category by ID
[**update_web_page_category_async**](WebPageCategoriesApi.md#update_web_page_category_async) | **PUT** /api/v2/ContentService/WebPageCategories/{webPageCategoryId} | Update a web page category


# **create_web_page_category_async**
> EmptyEnvelope create_web_page_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_category_create_dto=web_page_category_create_dto)

Create a web page category

Creates a new web page category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_page_category_create_dto import WebPageCategoryCreateDto
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
    api_instance = openapi_client.WebPageCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_category_create_dto = openapi_client.WebPageCategoryCreateDto() # WebPageCategoryCreateDto |  (optional)

    try:
        # Create a web page category
        api_response = api_instance.create_web_page_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_category_create_dto=web_page_category_create_dto)
        print("The response of WebPageCategoriesApi->create_web_page_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageCategoriesApi->create_web_page_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_category_create_dto** | [**WebPageCategoryCreateDto**](WebPageCategoryCreateDto.md)|  | [optional] 

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

# **delete_web_page_category_async**
> EmptyEnvelope delete_web_page_category_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version)

Delete a web page category

Deletes a web page category for the specified tenant.

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
    api_instance = openapi_client.WebPageCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_category_id = 'web_page_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web page category
        api_response = api_instance.delete_web_page_category_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageCategoriesApi->delete_web_page_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageCategoriesApi->delete_web_page_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_category_id** | **str**|  | 
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

# **get_web_page_categories_async**
> WebPageCategoryDtoListEnvelope get_web_page_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web page categories

Retrieves all web page categories for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_page_category_dto_list_envelope import WebPageCategoryDtoListEnvelope
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
    api_instance = openapi_client.WebPageCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web page categories
        api_response = api_instance.get_web_page_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageCategoriesApi->get_web_page_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageCategoriesApi->get_web_page_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageCategoryDtoListEnvelope**](WebPageCategoryDtoListEnvelope.md)

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

# **get_web_page_category_by_id_async**
> WebPageCategoryDtoEnvelope get_web_page_category_by_id_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version)

Get web page category by ID

Retrieves a specific web page category by its ID.

### Example


```python
import openapi_client
from openapi_client.models.web_page_category_dto_envelope import WebPageCategoryDtoEnvelope
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
    api_instance = openapi_client.WebPageCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_category_id = 'web_page_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web page category by ID
        api_response = api_instance.get_web_page_category_by_id_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPageCategoriesApi->get_web_page_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageCategoriesApi->get_web_page_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageCategoryDtoEnvelope**](WebPageCategoryDtoEnvelope.md)

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

# **update_web_page_category_async**
> EmptyEnvelope update_web_page_category_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version, web_page_category_update_dto=web_page_category_update_dto)

Update a web page category

Updates an existing web page category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_page_category_update_dto import WebPageCategoryUpdateDto
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
    api_instance = openapi_client.WebPageCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_category_id = 'web_page_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_category_update_dto = openapi_client.WebPageCategoryUpdateDto() # WebPageCategoryUpdateDto |  (optional)

    try:
        # Update a web page category
        api_response = api_instance.update_web_page_category_async(tenant_id, web_page_category_id, api_version=api_version, x_api_version=x_api_version, web_page_category_update_dto=web_page_category_update_dto)
        print("The response of WebPageCategoriesApi->update_web_page_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageCategoriesApi->update_web_page_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_category_update_dto** | [**WebPageCategoryUpdateDto**](WebPageCategoryUpdateDto.md)|  | [optional] 

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

