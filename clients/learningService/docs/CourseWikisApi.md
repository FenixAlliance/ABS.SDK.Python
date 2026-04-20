# openapi_client.CourseWikisApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_wiki_async**](CourseWikisApi.md#create_course_wiki_async) | **POST** /api/v2/LearningService/CourseWikis | Create a new course wiki
[**delete_course_wiki_async**](CourseWikisApi.md#delete_course_wiki_async) | **DELETE** /api/v2/LearningService/CourseWikis/{wikiId} | Delete a course wiki
[**get_course_wiki_by_id_async**](CourseWikisApi.md#get_course_wiki_by_id_async) | **GET** /api/v2/LearningService/CourseWikis/{wikiId} | Get course wiki by ID
[**get_course_wikis_async**](CourseWikisApi.md#get_course_wikis_async) | **GET** /api/v2/LearningService/CourseWikis | Get all course wikis
[**get_course_wikis_count_async**](CourseWikisApi.md#get_course_wikis_count_async) | **GET** /api/v2/LearningService/CourseWikis/Count | Get course wikis count
[**update_course_wiki_async**](CourseWikisApi.md#update_course_wiki_async) | **PUT** /api/v2/LearningService/CourseWikis/{wikiId} | Update a course wiki


# **create_course_wiki_async**
> create_course_wiki_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_wiki_create_dto=course_wiki_create_dto)

Create a new course wiki

Creates a new course wiki for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_wiki_create_dto import CourseWikiCreateDto
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
    api_instance = openapi_client.CourseWikisApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_wiki_create_dto = openapi_client.CourseWikiCreateDto() # CourseWikiCreateDto |  (optional)

    try:
        # Create a new course wiki
        api_instance.create_course_wiki_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_wiki_create_dto=course_wiki_create_dto)
    except Exception as e:
        print("Exception when calling CourseWikisApi->create_course_wiki_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_wiki_create_dto** | [**CourseWikiCreateDto**](CourseWikiCreateDto.md)|  | [optional] 

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

# **delete_course_wiki_async**
> delete_course_wiki_async(tenant_id, wiki_id, api_version=api_version, x_api_version=x_api_version)

Delete a course wiki

Deletes a course wiki for the specified tenant.

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
    api_instance = openapi_client.CourseWikisApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    wiki_id = 'wiki_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course wiki
        api_instance.delete_course_wiki_async(tenant_id, wiki_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseWikisApi->delete_course_wiki_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **wiki_id** | **str**|  | 
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

# **get_course_wiki_by_id_async**
> CourseWikiDto get_course_wiki_by_id_async(wiki_id, api_version=api_version, x_api_version=x_api_version)

Get course wiki by ID

Retrieves a specific course wiki by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_wiki_dto import CourseWikiDto
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
    api_instance = openapi_client.CourseWikisApi(api_client)
    wiki_id = 'wiki_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course wiki by ID
        api_response = api_instance.get_course_wiki_by_id_async(wiki_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseWikisApi->get_course_wiki_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseWikisApi->get_course_wiki_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseWikiDto**](CourseWikiDto.md)

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

# **get_course_wikis_async**
> List[CourseWikiDto] get_course_wikis_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course wikis

Retrieves all course wikis for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_wiki_dto import CourseWikiDto
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
    api_instance = openapi_client.CourseWikisApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course wikis
        api_response = api_instance.get_course_wikis_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseWikisApi->get_course_wikis_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseWikisApi->get_course_wikis_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseWikiDto]**](CourseWikiDto.md)

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

# **get_course_wikis_count_async**
> int get_course_wikis_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course wikis count

Returns the count of course wikis for the specified tenant.

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
    api_instance = openapi_client.CourseWikisApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course wikis count
        api_response = api_instance.get_course_wikis_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseWikisApi->get_course_wikis_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseWikisApi->get_course_wikis_count_async: %s\n" % e)
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

# **update_course_wiki_async**
> update_course_wiki_async(tenant_id, wiki_id, api_version=api_version, x_api_version=x_api_version, course_wiki_update_dto=course_wiki_update_dto)

Update a course wiki

Updates an existing course wiki for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_wiki_update_dto import CourseWikiUpdateDto
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
    api_instance = openapi_client.CourseWikisApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    wiki_id = 'wiki_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_wiki_update_dto = openapi_client.CourseWikiUpdateDto() # CourseWikiUpdateDto |  (optional)

    try:
        # Update a course wiki
        api_instance.update_course_wiki_async(tenant_id, wiki_id, api_version=api_version, x_api_version=x_api_version, course_wiki_update_dto=course_wiki_update_dto)
    except Exception as e:
        print("Exception when calling CourseWikisApi->update_course_wiki_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **wiki_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_wiki_update_dto** | [**CourseWikiUpdateDto**](CourseWikiUpdateDto.md)|  | [optional] 

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

