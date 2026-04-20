# openapi_client.CoursesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_async**](CoursesApi.md#create_course_async) | **POST** /api/v2/LearningService/Courses | Create a new course
[**delete_course_async**](CoursesApi.md#delete_course_async) | **DELETE** /api/v2/LearningService/Courses/{courseId} | Delete a course
[**get_course_articles_by_course_wiki_async**](CoursesApi.md#get_course_articles_by_course_wiki_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Articles/{wikiId} | Get course articles by course wiki
[**get_course_articles_by_course_wiki_count_async**](CoursesApi.md#get_course_articles_by_course_wiki_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Articles/{wikiId}/Count | Get course articles by course wiki count
[**get_course_assignments_by_course_async**](CoursesApi.md#get_course_assignments_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Assignments | Get course assignments by course
[**get_course_assignments_by_course_count_async**](CoursesApi.md#get_course_assignments_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Assignments/Count | Get course assignments by course count
[**get_course_by_id_async**](CoursesApi.md#get_course_by_id_async) | **GET** /api/v2/LearningService/Courses/{courseId} | Get course by ID
[**get_course_categories_by_course_async**](CoursesApi.md#get_course_categories_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Categories | Get course categories by course
[**get_course_categories_by_course_count_async**](CoursesApi.md#get_course_categories_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Categories/Count | Get course categories by course count
[**get_course_cohorts_by_course_async**](CoursesApi.md#get_course_cohorts_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Cohorts | Get course cohorts by course
[**get_course_cohorts_by_course_count_async**](CoursesApi.md#get_course_cohorts_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Cohorts/Count | Get course cohorts by course count
[**get_course_enrollments_by_course_async**](CoursesApi.md#get_course_enrollments_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Enrollments | Get enrollments by course
[**get_course_files_by_course_async**](CoursesApi.md#get_course_files_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Files | Get course files by course
[**get_course_files_by_course_count_async**](CoursesApi.md#get_course_files_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Files/Count | Get course files by course count
[**get_course_forums_by_course_async**](CoursesApi.md#get_course_forums_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Forums | Get course forums by course
[**get_course_forums_by_course_count_async**](CoursesApi.md#get_course_forums_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Forums/Count | Get course forums by course count
[**get_course_handouts_by_course_async**](CoursesApi.md#get_course_handouts_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Handouts | Get course handouts by course
[**get_course_handouts_by_course_count_async**](CoursesApi.md#get_course_handouts_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Handouts/Count | Get course handouts by course count
[**get_course_libraries_by_course_async**](CoursesApi.md#get_course_libraries_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Libraries | Get course libraries by course
[**get_course_libraries_by_course_count_async**](CoursesApi.md#get_course_libraries_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Libraries/Count | Get course libraries by course count
[**get_course_pages_by_course_async**](CoursesApi.md#get_course_pages_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Pages | Get course pages by course
[**get_course_pages_by_course_count_async**](CoursesApi.md#get_course_pages_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Pages/Count | Get course pages by course count
[**get_course_problem_sets_by_course_async**](CoursesApi.md#get_course_problem_sets_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/ProblemSets | Get course problem sets by course
[**get_course_problem_sets_by_course_count_async**](CoursesApi.md#get_course_problem_sets_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/ProblemSets/Count | Get course problem sets by course count
[**get_course_sections_by_course_async**](CoursesApi.md#get_course_sections_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Sections | Get course sections by course
[**get_course_sections_by_course_count_async**](CoursesApi.md#get_course_sections_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Sections/Count | Get course sections by course count
[**get_course_unit_components_by_course_async**](CoursesApi.md#get_course_unit_components_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/UnitComponents | Get course unit components by course
[**get_course_unit_components_by_course_count_async**](CoursesApi.md#get_course_unit_components_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/UnitComponents/Count | Get course unit components by course count
[**get_course_units_by_section_async**](CoursesApi.md#get_course_units_by_section_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Units/{sectionId} | Get course units by section
[**get_course_units_by_section_count_async**](CoursesApi.md#get_course_units_by_section_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Units/{sectionId}/Count | Get course units by section count
[**get_course_updates_by_course_async**](CoursesApi.md#get_course_updates_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Updates | Get course updates by course
[**get_course_updates_by_course_count_async**](CoursesApi.md#get_course_updates_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Updates/Count | Get course updates by course count
[**get_course_wikis_by_course_async**](CoursesApi.md#get_course_wikis_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Wikis | Get course wikis by course
[**get_course_wikis_by_course_count_async**](CoursesApi.md#get_course_wikis_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Wikis/Count | Get course wikis by course count
[**get_courses_async**](CoursesApi.md#get_courses_async) | **GET** /api/v2/LearningService/Courses | Get courses
[**get_courses_count_async**](CoursesApi.md#get_courses_count_async) | **GET** /api/v2/LearningService/Courses/Count | Get courses count
[**get_instructor_profiles_by_course_async**](CoursesApi.md#get_instructor_profiles_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Instructors | Get instructor profiles by course
[**get_instructor_profiles_by_course_count_async**](CoursesApi.md#get_instructor_profiles_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Instructors/Count | Get instructor profiles by course count
[**get_student_profiles_by_course_async**](CoursesApi.md#get_student_profiles_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Students | Get student profiles by course
[**get_student_profiles_by_course_count_async**](CoursesApi.md#get_student_profiles_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/Students/Count | Get student profiles by course count
[**update_course_async**](CoursesApi.md#update_course_async) | **PUT** /api/v2/LearningService/Courses/{courseId} | Update a course


# **create_course_async**
> create_course_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_create_dto=course_create_dto)

Create a new course

Creates a new course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_create_dto import CourseCreateDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_create_dto = openapi_client.CourseCreateDto() # CourseCreateDto |  (optional)

    try:
        # Create a new course
        api_instance.create_course_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_create_dto=course_create_dto)
    except Exception as e:
        print("Exception when calling CoursesApi->create_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_create_dto** | [**CourseCreateDto**](CourseCreateDto.md)|  | [optional] 

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

# **delete_course_async**
> delete_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)

Delete a course

Deletes a course for the specified tenant.

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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course
        api_instance.delete_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CoursesApi->delete_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
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

# **get_course_articles_by_course_wiki_async**
> List[CourseArticleDto] get_course_articles_by_course_wiki_async(course_id, wiki_id, api_version=api_version, x_api_version=x_api_version)

Get course articles by course wiki

Retrieves all course articles for a specific course wiki.

### Example


```python
import openapi_client
from openapi_client.models.course_article_dto import CourseArticleDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    wiki_id = 'wiki_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course articles by course wiki
        api_response = api_instance.get_course_articles_by_course_wiki_async(course_id, wiki_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_articles_by_course_wiki_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_articles_by_course_wiki_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **wiki_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_articles_by_course_wiki_count_async**
> int get_course_articles_by_course_wiki_count_async(course_id, wiki_id, api_version=api_version, x_api_version=x_api_version)

Get course articles by course wiki count

Returns the count of course articles for a specific course wiki.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    wiki_id = 'wiki_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course articles by course wiki count
        api_response = api_instance.get_course_articles_by_course_wiki_count_async(course_id, wiki_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_articles_by_course_wiki_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_articles_by_course_wiki_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **wiki_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_assignments_by_course_async**
> List[CourseAssignmentDto] get_course_assignments_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course assignments by course

Retrieves all course assignments for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_dto import CourseAssignmentDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignments by course
        api_response = api_instance.get_course_assignments_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_assignments_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_assignments_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseAssignmentDto]**](CourseAssignmentDto.md)

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

# **get_course_assignments_by_course_count_async**
> int get_course_assignments_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course assignments by course count

Returns the count of course assignments for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignments by course count
        api_response = api_instance.get_course_assignments_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_assignments_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_assignments_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_by_id_async**
> CourseDto get_course_by_id_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)

Get course by ID

Retrieves a specific course by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_dto import CourseDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course by ID
        api_response = api_instance.get_course_by_id_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseDto**](CourseDto.md)

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

# **get_course_categories_by_course_async**
> List[CourseCategoryDto] get_course_categories_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course categories by course

Retrieves all course categories for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_category_dto import CourseCategoryDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course categories by course
        api_response = api_instance.get_course_categories_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_categories_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_categories_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseCategoryDto]**](CourseCategoryDto.md)

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

# **get_course_categories_by_course_count_async**
> int get_course_categories_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course categories by course count

Returns the count of course categories for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course categories by course count
        api_response = api_instance.get_course_categories_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_categories_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_categories_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_cohorts_by_course_async**
> List[CourseCohortDto] get_course_cohorts_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course cohorts by course

Retrieves all course cohorts for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_cohort_dto import CourseCohortDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course cohorts by course
        api_response = api_instance.get_course_cohorts_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_cohorts_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_cohorts_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseCohortDto]**](CourseCohortDto.md)

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

# **get_course_cohorts_by_course_count_async**
> int get_course_cohorts_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course cohorts by course count

Returns the count of course cohorts for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course cohorts by course count
        api_response = api_instance.get_course_cohorts_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_cohorts_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_cohorts_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_enrollments_by_course_async**
> List[CourseEnrollmentDto] get_course_enrollments_by_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)

Get enrollments by course

Retrieves all enrollments for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_dto import CourseEnrollmentDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get enrollments by course
        api_response = api_instance.get_course_enrollments_by_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_enrollments_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_enrollments_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseEnrollmentDto]**](CourseEnrollmentDto.md)

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

# **get_course_files_by_course_async**
> List[CourseFileDto] get_course_files_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course files by course

Retrieves all course files for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_file_dto import CourseFileDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course files by course
        api_response = api_instance.get_course_files_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_files_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_files_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseFileDto]**](CourseFileDto.md)

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

# **get_course_files_by_course_count_async**
> int get_course_files_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course files by course count

Returns the count of course files for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course files by course count
        api_response = api_instance.get_course_files_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_files_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_files_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_forums_by_course_async**
> List[CourseForumDto] get_course_forums_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course forums by course

Retrieves all course forums for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_forum_dto import CourseForumDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course forums by course
        api_response = api_instance.get_course_forums_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_forums_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_forums_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseForumDto]**](CourseForumDto.md)

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

# **get_course_forums_by_course_count_async**
> int get_course_forums_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course forums by course count

Returns the count of course forums for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course forums by course count
        api_response = api_instance.get_course_forums_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_forums_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_forums_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_handouts_by_course_async**
> List[CourseHandoutDto] get_course_handouts_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course handouts by course

Retrieves all course handouts for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_handout_dto import CourseHandoutDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course handouts by course
        api_response = api_instance.get_course_handouts_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_handouts_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_handouts_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseHandoutDto]**](CourseHandoutDto.md)

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

# **get_course_handouts_by_course_count_async**
> int get_course_handouts_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course handouts by course count

Returns the count of course handouts for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course handouts by course count
        api_response = api_instance.get_course_handouts_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_handouts_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_handouts_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_libraries_by_course_async**
> List[CourseLibraryDto] get_course_libraries_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course libraries by course

Retrieves all course libraries for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_library_dto import CourseLibraryDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course libraries by course
        api_response = api_instance.get_course_libraries_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_libraries_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_libraries_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseLibraryDto]**](CourseLibraryDto.md)

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

# **get_course_libraries_by_course_count_async**
> int get_course_libraries_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course libraries by course count

Returns the count of course libraries for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course libraries by course count
        api_response = api_instance.get_course_libraries_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_libraries_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_libraries_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_pages_by_course_async**
> List[CoursePageDto] get_course_pages_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course pages by course

Retrieves all course pages for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_page_dto import CoursePageDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course pages by course
        api_response = api_instance.get_course_pages_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_pages_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_pages_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CoursePageDto]**](CoursePageDto.md)

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

# **get_course_pages_by_course_count_async**
> int get_course_pages_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course pages by course count

Returns the count of course pages for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course pages by course count
        api_response = api_instance.get_course_pages_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_pages_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_pages_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_problem_sets_by_course_async**
> List[CourseProblemSetDto] get_course_problem_sets_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course problem sets by course

Retrieves all course problem sets for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_problem_set_dto import CourseProblemSetDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course problem sets by course
        api_response = api_instance.get_course_problem_sets_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_problem_sets_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_problem_sets_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseProblemSetDto]**](CourseProblemSetDto.md)

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

# **get_course_problem_sets_by_course_count_async**
> int get_course_problem_sets_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course problem sets by course count

Returns the count of course problem sets for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course problem sets by course count
        api_response = api_instance.get_course_problem_sets_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_problem_sets_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_problem_sets_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_sections_by_course_async**
> List[CourseSectionDto] get_course_sections_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course sections by course

Retrieves all course sections for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_section_dto import CourseSectionDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course sections by course
        api_response = api_instance.get_course_sections_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_sections_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_sections_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseSectionDto]**](CourseSectionDto.md)

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

# **get_course_sections_by_course_count_async**
> int get_course_sections_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course sections by course count

Returns the count of course sections for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course sections by course count
        api_response = api_instance.get_course_sections_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_sections_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_sections_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_unit_components_by_course_async**
> List[CourseUnitComponentDto] get_course_unit_components_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course unit components by course

Retrieves all course unit components for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_component_dto import CourseUnitComponentDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course unit components by course
        api_response = api_instance.get_course_unit_components_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_unit_components_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_unit_components_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseUnitComponentDto]**](CourseUnitComponentDto.md)

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

# **get_course_unit_components_by_course_count_async**
> int get_course_unit_components_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course unit components by course count

Returns the count of course unit components for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course unit components by course count
        api_response = api_instance.get_course_unit_components_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_unit_components_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_unit_components_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_units_by_section_async**
> List[CourseUnitDto] get_course_units_by_section_async(course_id, section_id, api_version=api_version, x_api_version=x_api_version)

Get course units by section

Retrieves all course units for a specific course section.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_dto import CourseUnitDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    section_id = 'section_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course units by section
        api_response = api_instance.get_course_units_by_section_async(course_id, section_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_units_by_section_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_units_by_section_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **section_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseUnitDto]**](CourseUnitDto.md)

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

# **get_course_units_by_section_count_async**
> int get_course_units_by_section_count_async(course_id, section_id, api_version=api_version, x_api_version=x_api_version)

Get course units by section count

Returns the count of course units for a specific course section.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    section_id = 'section_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course units by section count
        api_response = api_instance.get_course_units_by_section_count_async(course_id, section_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_units_by_section_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_units_by_section_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **section_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_updates_by_course_async**
> List[CourseNewsDto] get_course_updates_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course updates by course

Retrieves all course updates for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_news_dto import CourseNewsDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course updates by course
        api_response = api_instance.get_course_updates_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_updates_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_updates_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseNewsDto]**](CourseNewsDto.md)

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

# **get_course_updates_by_course_count_async**
> int get_course_updates_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course updates by course count

Returns the count of course updates for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course updates by course count
        api_response = api_instance.get_course_updates_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_updates_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_updates_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_wikis_by_course_async**
> List[CourseWikiDto] get_course_wikis_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course wikis by course

Retrieves all course wikis for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course wikis by course
        api_response = api_instance.get_course_wikis_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_wikis_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_wikis_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_wikis_by_course_count_async**
> int get_course_wikis_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course wikis by course count

Returns the count of course wikis for a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course wikis by course count
        api_response = api_instance.get_course_wikis_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_course_wikis_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_course_wikis_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses_async**
> List[CourseDto] get_courses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get courses

Retrieves courses. When tenantId is provided, returns tenant-scoped courses; otherwise returns all courses.

### Example


```python
import openapi_client
from openapi_client.models.course_dto import CourseDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get courses
        api_response = api_instance.get_courses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_courses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_courses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseDto]**](CourseDto.md)

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

# **get_courses_count_async**
> int get_courses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get courses count

Returns the count of courses. When tenantId is provided, returns tenant-scoped count; otherwise returns global count.

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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get courses count
        api_response = api_instance.get_courses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_courses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_courses_count_async: %s\n" % e)
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instructor_profiles_by_course_async**
> List[InstructorProfileDto] get_instructor_profiles_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get instructor profiles by course

Retrieves all instructor profiles teaching a specific course.

### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_dto import InstructorProfileDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get instructor profiles by course
        api_response = api_instance.get_instructor_profiles_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_instructor_profiles_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_instructor_profiles_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[InstructorProfileDto]**](InstructorProfileDto.md)

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

# **get_instructor_profiles_by_course_count_async**
> int get_instructor_profiles_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get instructor profiles by course count

Returns the count of instructor profiles teaching a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get instructor profiles by course count
        api_response = api_instance.get_instructor_profiles_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_instructor_profiles_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_instructor_profiles_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_student_profiles_by_course_async**
> List[StudentProfileDto] get_student_profiles_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get student profiles by course

Retrieves all student profiles enrolled in a specific course.

### Example


```python
import openapi_client
from openapi_client.models.student_profile_dto import StudentProfileDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get student profiles by course
        api_response = api_instance.get_student_profiles_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_student_profiles_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_student_profiles_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[StudentProfileDto]**](StudentProfileDto.md)

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

# **get_student_profiles_by_course_count_async**
> int get_student_profiles_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get student profiles by course count

Returns the count of student profiles enrolled in a specific course.

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
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get student profiles by course count
        api_response = api_instance.get_student_profiles_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursesApi->get_student_profiles_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->get_student_profiles_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_course_async**
> update_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, course_update_dto=course_update_dto)

Update a course

Updates an existing course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_update_dto import CourseUpdateDto
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
    api_instance = openapi_client.CoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_update_dto = openapi_client.CourseUpdateDto() # CourseUpdateDto |  (optional)

    try:
        # Update a course
        api_instance.update_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, course_update_dto=course_update_dto)
    except Exception as e:
        print("Exception when calling CoursesApi->update_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_update_dto** | [**CourseUpdateDto**](CourseUpdateDto.md)|  | [optional] 

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

