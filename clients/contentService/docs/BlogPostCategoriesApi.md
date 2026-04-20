# openapi_client.BlogPostCategoriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_blog_post_categories_async**](BlogPostCategoriesApi.md#count_blog_post_categories_async) | **GET** /api/v2/ContentService/BlogPostCategories/Count | Count blog post categories
[**create_blog_post_category_async**](BlogPostCategoriesApi.md#create_blog_post_category_async) | **POST** /api/v2/ContentService/BlogPostCategories | Create a blog post category
[**delete_blog_post_category_async**](BlogPostCategoriesApi.md#delete_blog_post_category_async) | **DELETE** /api/v2/ContentService/BlogPostCategories/{blogPostCategoryId} | Delete a blog post category
[**get_blog_post_categories_async**](BlogPostCategoriesApi.md#get_blog_post_categories_async) | **GET** /api/v2/ContentService/BlogPostCategories | Get blog post categories
[**get_blog_post_category_by_id_async**](BlogPostCategoriesApi.md#get_blog_post_category_by_id_async) | **GET** /api/v2/ContentService/BlogPostCategories/{blogPostCategoryId} | Get blog post category by ID
[**update_blog_post_category_async**](BlogPostCategoriesApi.md#update_blog_post_category_async) | **PUT** /api/v2/ContentService/BlogPostCategories/{blogPostCategoryId} | Update a blog post category


# **count_blog_post_categories_async**
> Int32Envelope count_blog_post_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count blog post categories

Counts all blog post categories for the specified tenant.

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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count blog post categories
        api_response = api_instance.count_blog_post_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostCategoriesApi->count_blog_post_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->count_blog_post_categories_async: %s\n" % e)
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

# **create_blog_post_category_async**
> EmptyEnvelope create_blog_post_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blog_post_category_create_dto=blog_post_category_create_dto)

Create a blog post category

Creates a new blog post category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_create_dto import BlogPostCategoryCreateDto
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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blog_post_category_create_dto = openapi_client.BlogPostCategoryCreateDto() # BlogPostCategoryCreateDto |  (optional)

    try:
        # Create a blog post category
        api_response = api_instance.create_blog_post_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blog_post_category_create_dto=blog_post_category_create_dto)
        print("The response of BlogPostCategoriesApi->create_blog_post_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->create_blog_post_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blog_post_category_create_dto** | [**BlogPostCategoryCreateDto**](BlogPostCategoryCreateDto.md)|  | [optional] 

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

# **delete_blog_post_category_async**
> EmptyEnvelope delete_blog_post_category_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version)

Delete a blog post category

Deletes a blog post category for the specified tenant.

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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_category_id = 'blog_post_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a blog post category
        api_response = api_instance.delete_blog_post_category_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostCategoriesApi->delete_blog_post_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->delete_blog_post_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_category_id** | **str**|  | 
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

# **get_blog_post_categories_async**
> BlogPostCategoryDtoListEnvelope get_blog_post_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get blog post categories

Retrieves all blog post categories for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_dto_list_envelope import BlogPostCategoryDtoListEnvelope
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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog post categories
        api_response = api_instance.get_blog_post_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostCategoriesApi->get_blog_post_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->get_blog_post_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogPostCategoryDtoListEnvelope**](BlogPostCategoryDtoListEnvelope.md)

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

# **get_blog_post_category_by_id_async**
> BlogPostCategoryDtoEnvelope get_blog_post_category_by_id_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version)

Get blog post category by ID

Retrieves a specific blog post category by its ID.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_dto_envelope import BlogPostCategoryDtoEnvelope
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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_category_id = 'blog_post_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blog post category by ID
        api_response = api_instance.get_blog_post_category_by_id_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlogPostCategoriesApi->get_blog_post_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->get_blog_post_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlogPostCategoryDtoEnvelope**](BlogPostCategoryDtoEnvelope.md)

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

# **update_blog_post_category_async**
> EmptyEnvelope update_blog_post_category_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version, blog_post_category_update_dto=blog_post_category_update_dto)

Update a blog post category

Updates an existing blog post category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blog_post_category_update_dto import BlogPostCategoryUpdateDto
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
    api_instance = openapi_client.BlogPostCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blog_post_category_id = 'blog_post_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blog_post_category_update_dto = openapi_client.BlogPostCategoryUpdateDto() # BlogPostCategoryUpdateDto |  (optional)

    try:
        # Update a blog post category
        api_response = api_instance.update_blog_post_category_async(tenant_id, blog_post_category_id, api_version=api_version, x_api_version=x_api_version, blog_post_category_update_dto=blog_post_category_update_dto)
        print("The response of BlogPostCategoriesApi->update_blog_post_category_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlogPostCategoriesApi->update_blog_post_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blog_post_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blog_post_category_update_dto** | [**BlogPostCategoryUpdateDto**](BlogPostCategoryUpdateDto.md)|  | [optional] 

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

