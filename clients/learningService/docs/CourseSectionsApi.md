# openapi_client.CourseSectionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_section_async**](CourseSectionsApi.md#create_course_section_async) | **POST** /api/v2/LearningService/CourseSections | Create a new course section
[**delete_course_section_async**](CourseSectionsApi.md#delete_course_section_async) | **DELETE** /api/v2/LearningService/CourseSections/{sectionId} | Delete a course section
[**get_course_section_by_id_async**](CourseSectionsApi.md#get_course_section_by_id_async) | **GET** /api/v2/LearningService/CourseSections/{sectionId} | Get course section by ID
[**get_course_sections_async**](CourseSectionsApi.md#get_course_sections_async) | **GET** /api/v2/LearningService/CourseSections | Get all course sections
[**get_course_sections_count_async**](CourseSectionsApi.md#get_course_sections_count_async) | **GET** /api/v2/LearningService/CourseSections/Count | Get course sections count
[**update_course_section_async**](CourseSectionsApi.md#update_course_section_async) | **PUT** /api/v2/LearningService/CourseSections/{sectionId} | Update a course section


# **create_course_section_async**
> create_course_section_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_section_create_dto=course_section_create_dto)

Create a new course section

Creates a new course section for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_section_create_dto import CourseSectionCreateDto
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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_section_create_dto = openapi_client.CourseSectionCreateDto() # CourseSectionCreateDto |  (optional)

    try:
        # Create a new course section
        api_instance.create_course_section_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_section_create_dto=course_section_create_dto)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->create_course_section_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_section_create_dto** | [**CourseSectionCreateDto**](CourseSectionCreateDto.md)|  | [optional] 

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

# **delete_course_section_async**
> delete_course_section_async(tenant_id, section_id, api_version=api_version, x_api_version=x_api_version)

Delete a course section

Deletes a course section for the specified tenant.

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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    section_id = 'section_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course section
        api_instance.delete_course_section_async(tenant_id, section_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->delete_course_section_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **section_id** | **str**|  | 
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

# **get_course_section_by_id_async**
> CourseSectionDto get_course_section_by_id_async(section_id, api_version=api_version, x_api_version=x_api_version)

Get course section by ID

Retrieves a specific course section by its ID.

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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    section_id = 'section_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course section by ID
        api_response = api_instance.get_course_section_by_id_async(section_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseSectionsApi->get_course_section_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->get_course_section_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseSectionDto**](CourseSectionDto.md)

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

# **get_course_sections_async**
> List[CourseSectionDto] get_course_sections_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course sections

Retrieves all course sections for the specified tenant.

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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course sections
        api_response = api_instance.get_course_sections_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseSectionsApi->get_course_sections_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->get_course_sections_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_sections_count_async**
> int get_course_sections_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course sections count

Returns the count of course sections for the specified tenant.

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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course sections count
        api_response = api_instance.get_course_sections_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseSectionsApi->get_course_sections_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->get_course_sections_count_async: %s\n" % e)
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

# **update_course_section_async**
> update_course_section_async(tenant_id, section_id, api_version=api_version, x_api_version=x_api_version, course_section_update_dto=course_section_update_dto)

Update a course section

Updates an existing course section for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_section_update_dto import CourseSectionUpdateDto
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
    api_instance = openapi_client.CourseSectionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    section_id = 'section_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_section_update_dto = openapi_client.CourseSectionUpdateDto() # CourseSectionUpdateDto |  (optional)

    try:
        # Update a course section
        api_instance.update_course_section_async(tenant_id, section_id, api_version=api_version, x_api_version=x_api_version, course_section_update_dto=course_section_update_dto)
    except Exception as e:
        print("Exception when calling CourseSectionsApi->update_course_section_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **section_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_section_update_dto** | [**CourseSectionUpdateDto**](CourseSectionUpdateDto.md)|  | [optional] 

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

