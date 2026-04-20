# openapi_client.CourseCategoriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_category_async**](CourseCategoriesApi.md#create_course_category_async) | **POST** /api/v2/LearningService/CourseCategories | Create a new course category
[**delete_course_category_async**](CourseCategoriesApi.md#delete_course_category_async) | **DELETE** /api/v2/LearningService/CourseCategories/{categoryId} | Delete a course category
[**get_course_categories_async**](CourseCategoriesApi.md#get_course_categories_async) | **GET** /api/v2/LearningService/CourseCategories | Get all course categories
[**get_course_categories_count_async**](CourseCategoriesApi.md#get_course_categories_count_async) | **GET** /api/v2/LearningService/CourseCategories/Count | Get course categories count
[**get_course_category_by_id_async**](CourseCategoriesApi.md#get_course_category_by_id_async) | **GET** /api/v2/LearningService/CourseCategories/{categoryId} | Get course category by ID
[**update_course_category_async**](CourseCategoriesApi.md#update_course_category_async) | **PUT** /api/v2/LearningService/CourseCategories/{categoryId} | Update a course category


# **create_course_category_async**
> create_course_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_category_create_dto=course_category_create_dto)

Create a new course category

Creates a new course category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_category_create_dto import CourseCategoryCreateDto
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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_category_create_dto = openapi_client.CourseCategoryCreateDto() # CourseCategoryCreateDto |  (optional)

    try:
        # Create a new course category
        api_instance.create_course_category_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_category_create_dto=course_category_create_dto)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->create_course_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_category_create_dto** | [**CourseCategoryCreateDto**](CourseCategoryCreateDto.md)|  | [optional] 

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

# **delete_course_category_async**
> delete_course_category_async(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)

Delete a course category

Deletes a course category for the specified tenant.

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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course category
        api_instance.delete_course_category_async(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->delete_course_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_course_categories_async**
> List[CourseCategoryDto] get_course_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course categories

Retrieves all course categories for the specified tenant.

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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course categories
        api_response = api_instance.get_course_categories_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCategoriesApi->get_course_categories_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->get_course_categories_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_categories_count_async**
> int get_course_categories_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course categories count

Returns the count of course categories for the specified tenant.

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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course categories count
        api_response = api_instance.get_course_categories_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCategoriesApi->get_course_categories_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->get_course_categories_count_async: %s\n" % e)
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

# **get_course_category_by_id_async**
> CourseCategoryDto get_course_category_by_id_async(category_id, api_version=api_version, x_api_version=x_api_version)

Get course category by ID

Retrieves a specific course category by its ID.

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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course category by ID
        api_response = api_instance.get_course_category_by_id_async(category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCategoriesApi->get_course_category_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->get_course_category_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseCategoryDto**](CourseCategoryDto.md)

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

# **update_course_category_async**
> update_course_category_async(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version, course_category_update_dto=course_category_update_dto)

Update a course category

Updates an existing course category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_category_update_dto import CourseCategoryUpdateDto
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
    api_instance = openapi_client.CourseCategoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_category_update_dto = openapi_client.CourseCategoryUpdateDto() # CourseCategoryUpdateDto |  (optional)

    try:
        # Update a course category
        api_instance.update_course_category_async(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version, course_category_update_dto=course_category_update_dto)
    except Exception as e:
        print("Exception when calling CourseCategoriesApi->update_course_category_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_category_update_dto** | [**CourseCategoryUpdateDto**](CourseCategoryUpdateDto.md)|  | [optional] 

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

