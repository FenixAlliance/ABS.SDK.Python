# openapi_client.CourseArticlesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_article_async**](CourseArticlesApi.md#create_course_article_async) | **POST** /api/v2/LearningService/CourseArticles | Create a new course article
[**delete_course_article_async**](CourseArticlesApi.md#delete_course_article_async) | **DELETE** /api/v2/LearningService/CourseArticles/{articleId} | Delete a course article
[**get_course_article_by_id_async**](CourseArticlesApi.md#get_course_article_by_id_async) | **GET** /api/v2/LearningService/CourseArticles/{articleId} | Get course article by ID
[**get_course_articles_async**](CourseArticlesApi.md#get_course_articles_async) | **GET** /api/v2/LearningService/CourseArticles | Get all course articles
[**get_course_articles_count_async**](CourseArticlesApi.md#get_course_articles_count_async) | **GET** /api/v2/LearningService/CourseArticles/Count | Get course articles count
[**update_course_article_async**](CourseArticlesApi.md#update_course_article_async) | **PUT** /api/v2/LearningService/CourseArticles/{articleId} | Update a course article


# **create_course_article_async**
> create_course_article_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_article_create_dto=course_article_create_dto)

Create a new course article

Creates a new course article for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_article_create_dto import CourseArticleCreateDto
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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_article_create_dto = openapi_client.CourseArticleCreateDto() # CourseArticleCreateDto |  (optional)

    try:
        # Create a new course article
        api_instance.create_course_article_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_article_create_dto=course_article_create_dto)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->create_course_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_article_create_dto** | [**CourseArticleCreateDto**](CourseArticleCreateDto.md)|  | [optional] 

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

# **delete_course_article_async**
> delete_course_article_async(tenant_id, article_id, api_version=api_version, x_api_version=x_api_version)

Delete a course article

Deletes a course article for the specified tenant.

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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    article_id = 'article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course article
        api_instance.delete_course_article_async(tenant_id, article_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->delete_course_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **article_id** | **str**|  | 
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

# **get_course_article_by_id_async**
> CourseArticleDto get_course_article_by_id_async(article_id, api_version=api_version, x_api_version=x_api_version)

Get course article by ID

Retrieves a specific course article by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_article_dto import CourseArticleDto
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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    article_id = 'article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course article by ID
        api_response = api_instance.get_course_article_by_id_async(article_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseArticlesApi->get_course_article_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->get_course_article_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseArticleDto**](CourseArticleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_articles_async**
> List[CourseArticleDto] get_course_articles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course articles

Retrieves all course articles for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_article_dto import CourseArticleDto
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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course articles
        api_response = api_instance.get_course_articles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseArticlesApi->get_course_articles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->get_course_articles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseArticleDto]**](CourseArticleDto.md)

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

# **get_course_articles_count_async**
> int get_course_articles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course articles count

Returns the count of course articles for the specified tenant.

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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course articles count
        api_response = api_instance.get_course_articles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseArticlesApi->get_course_articles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->get_course_articles_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**int**

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

# **update_course_article_async**
> update_course_article_async(tenant_id, article_id, api_version=api_version, x_api_version=x_api_version, course_article_update_dto=course_article_update_dto)

Update a course article

Updates an existing course article for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_article_update_dto import CourseArticleUpdateDto
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
    api_instance = openapi_client.CourseArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    article_id = 'article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_article_update_dto = openapi_client.CourseArticleUpdateDto() # CourseArticleUpdateDto |  (optional)

    try:
        # Update a course article
        api_instance.update_course_article_async(tenant_id, article_id, api_version=api_version, x_api_version=x_api_version, course_article_update_dto=course_article_update_dto)
    except Exception as e:
        print("Exception when calling CourseArticlesApi->update_course_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **article_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_article_update_dto** | [**CourseArticleUpdateDto**](CourseArticleUpdateDto.md)|  | [optional] 

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

