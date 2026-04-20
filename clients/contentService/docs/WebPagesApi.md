# openapi_client.WebPagesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_web_pages_async**](WebPagesApi.md#count_web_pages_async) | **GET** /api/v2/ContentService/WebPages/Count | Count web pages
[**create_web_page_async**](WebPagesApi.md#create_web_page_async) | **POST** /api/v2/ContentService/WebPages | Create a web page
[**create_web_page_category_relation_async**](WebPagesApi.md#create_web_page_category_relation_async) | **POST** /api/v2/ContentService/WebPages/{webPageId}/Categories | Create a web page category relation
[**create_web_page_tag_relation_async**](WebPagesApi.md#create_web_page_tag_relation_async) | **POST** /api/v2/ContentService/WebPages/{webPageId}/Tags | Create a web page tag relation
[**delete_web_page_async**](WebPagesApi.md#delete_web_page_async) | **DELETE** /api/v2/ContentService/WebPages/{webPageId} | Delete a web page
[**get_categories_by_web_page_async**](WebPagesApi.md#get_categories_by_web_page_async) | **GET** /api/v2/ContentService/WebPages/{webPageId}/Categories | Get categories by web page
[**get_tags_by_web_page_async**](WebPagesApi.md#get_tags_by_web_page_async) | **GET** /api/v2/ContentService/WebPages/{webPageId}/Tags | Get tags by web page
[**get_web_page_by_id_async**](WebPagesApi.md#get_web_page_by_id_async) | **GET** /api/v2/ContentService/WebPages/{webPageId} | Get web page by ID
[**get_web_pages_async**](WebPagesApi.md#get_web_pages_async) | **GET** /api/v2/ContentService/WebPages | Get web pages
[**relate_web_page_to_category_async**](WebPagesApi.md#relate_web_page_to_category_async) | **POST** /api/v2/ContentService/WebPages/{webPageId}/Categories/{categoryId} | Relate web page to category
[**relate_web_page_to_tag_async**](WebPagesApi.md#relate_web_page_to_tag_async) | **POST** /api/v2/ContentService/WebPages/{webPageId}/Tags/{tagId} | Relate web page to tag
[**unrelate_web_page_category_async**](WebPagesApi.md#unrelate_web_page_category_async) | **DELETE** /api/v2/ContentService/WebPages/{webPageId}/Categories/{categoryId} | Unrelate web page from category
[**unrelate_web_page_tag_async**](WebPagesApi.md#unrelate_web_page_tag_async) | **DELETE** /api/v2/ContentService/WebPages/{webPageId}/Tags/{tagId} | Unrelate web page from tag
[**update_web_page_async**](WebPagesApi.md#update_web_page_async) | **PUT** /api/v2/ContentService/WebPages/{webPageId} | Update a web page


# **count_web_pages_async**
> Int32Envelope count_web_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count web pages

Counts all web pages for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count web pages
        api_response = api_instance.count_web_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPagesApi->count_web_pages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->count_web_pages_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_page_async**
> create_web_page_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_create_dto=web_page_create_dto)

Create a web page

Creates a new web page for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_page_create_dto import WebPageCreateDto
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_create_dto = openapi_client.WebPageCreateDto() # WebPageCreateDto |  (optional)

    try:
        # Create a web page
        api_instance.create_web_page_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_page_create_dto=web_page_create_dto)
    except Exception as e:
        print("Exception when calling WebPagesApi->create_web_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_create_dto** | [**WebPageCreateDto**](WebPageCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_page_category_relation_async**
> create_web_page_category_relation_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_category_create_dto=web_page_category_create_dto)

Create a web page category relation

Creates a new category and relates it to a web page.

### Example


```python
import openapi_client
from openapi_client.models.web_page_category_create_dto import WebPageCategoryCreateDto
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_category_create_dto = openapi_client.WebPageCategoryCreateDto() # WebPageCategoryCreateDto |  (optional)

    try:
        # Create a web page category relation
        api_instance.create_web_page_category_relation_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_category_create_dto=web_page_category_create_dto)
    except Exception as e:
        print("Exception when calling WebPagesApi->create_web_page_category_relation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_category_create_dto** | [**WebPageCategoryCreateDto**](WebPageCategoryCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_page_tag_relation_async**
> create_web_page_tag_relation_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_create_dto=web_page_tag_create_dto)

Create a web page tag relation

Creates a new tag and relates it to a web page.

### Example


```python
import openapi_client
from openapi_client.models.web_page_tag_create_dto import WebPageTagCreateDto
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_tag_create_dto = openapi_client.WebPageTagCreateDto() # WebPageTagCreateDto |  (optional)

    try:
        # Create a web page tag relation
        api_instance.create_web_page_tag_relation_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_tag_create_dto=web_page_tag_create_dto)
    except Exception as e:
        print("Exception when calling WebPagesApi->create_web_page_tag_relation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_tag_create_dto** | [**WebPageTagCreateDto**](WebPageTagCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_page_async**
> delete_web_page_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version)

Delete a web page

Deletes a web page for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web page
        api_instance.delete_web_page_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebPagesApi->delete_web_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_by_web_page_async**
> WebPageCategoryDtoListEnvelope get_categories_by_web_page_async(web_page_id, api_version=api_version, x_api_version=x_api_version)

Get categories by web page

Retrieves all categories related to a specific web page.

### Example


```python
import openapi_client
from openapi_client.models.web_page_category_dto_list_envelope import WebPageCategoryDtoListEnvelope
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
    api_instance = openapi_client.WebPagesApi(api_client)
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get categories by web page
        api_response = api_instance.get_categories_by_web_page_async(web_page_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPagesApi->get_categories_by_web_page_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->get_categories_by_web_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_page_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_by_web_page_async**
> WebPageTagDtoListEnvelope get_tags_by_web_page_async(web_page_id, api_version=api_version, x_api_version=x_api_version)

Get tags by web page

Retrieves all tags related to a specific web page.

### Example


```python
import openapi_client
from openapi_client.models.web_page_tag_dto_list_envelope import WebPageTagDtoListEnvelope
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
    api_instance = openapi_client.WebPagesApi(api_client)
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tags by web page
        api_response = api_instance.get_tags_by_web_page_async(web_page_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPagesApi->get_tags_by_web_page_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->get_tags_by_web_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageTagDtoListEnvelope**](WebPageTagDtoListEnvelope.md)

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

# **get_web_page_by_id_async**
> WebPageDtoEnvelope get_web_page_by_id_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version)

Get web page by ID

Retrieves a specific web page by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.web_page_dto_envelope import WebPageDtoEnvelope
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web page by ID
        api_response = api_instance.get_web_page_by_id_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPagesApi->get_web_page_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->get_web_page_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageDtoEnvelope**](WebPageDtoEnvelope.md)

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

# **get_web_pages_async**
> WebPageDtoListEnvelope get_web_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web pages

Retrieves all web pages for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_page_dto_list_envelope import WebPageDtoListEnvelope
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web pages
        api_response = api_instance.get_web_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebPagesApi->get_web_pages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->get_web_pages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPageDtoListEnvelope**](WebPageDtoListEnvelope.md)

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

# **relate_web_page_to_category_async**
> relate_web_page_to_category_async(tenant_id, web_page_id, category_id, api_version=api_version, x_api_version=x_api_version)

Relate web page to category

Relates an existing category to a web page.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate web page to category
        api_instance.relate_web_page_to_category_async(tenant_id, web_page_id, category_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebPagesApi->relate_web_page_to_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **category_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relate_web_page_to_tag_async**
> relate_web_page_to_tag_async(tenant_id, web_page_id, tag_id, api_version=api_version, x_api_version=x_api_version)

Relate web page to tag

Relates an existing tag to a web page.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    tag_id = 'tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate web page to tag
        api_instance.relate_web_page_to_tag_async(tenant_id, web_page_id, tag_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebPagesApi->relate_web_page_to_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **tag_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unrelate_web_page_category_async**
> unrelate_web_page_category_async(tenant_id, web_page_id, category_id, api_version=api_version, x_api_version=x_api_version)

Unrelate web page from category

Removes the relationship between a web page and a category.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Unrelate web page from category
        api_instance.unrelate_web_page_category_async(tenant_id, web_page_id, category_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebPagesApi->unrelate_web_page_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **category_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unrelate_web_page_tag_async**
> unrelate_web_page_tag_async(tenant_id, web_page_id, tag_id, api_version=api_version, x_api_version=x_api_version)

Unrelate web page from tag

Removes the relationship between a web page and a tag.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    tag_id = 'tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Unrelate web page from tag
        api_instance.unrelate_web_page_tag_async(tenant_id, web_page_id, tag_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebPagesApi->unrelate_web_page_tag_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **tag_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_page_async**
> update_web_page_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_update_dto=web_page_update_dto)

Update a web page

Updates an existing web page for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_page_update_dto import WebPageUpdateDto
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
    api_instance = openapi_client.WebPagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_page_id = 'web_page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_page_update_dto = openapi_client.WebPageUpdateDto() # WebPageUpdateDto |  (optional)

    try:
        # Update a web page
        api_instance.update_web_page_async(tenant_id, web_page_id, api_version=api_version, x_api_version=x_api_version, web_page_update_dto=web_page_update_dto)
    except Exception as e:
        print("Exception when calling WebPagesApi->update_web_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_page_update_dto** | [**WebPageUpdateDto**](WebPageUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

