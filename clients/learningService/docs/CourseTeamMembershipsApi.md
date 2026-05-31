# openapi_client.CourseTeamMembershipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_team_membership_async**](CourseTeamMembershipsApi.md#create_course_team_membership_async) | **POST** /api/v2/LearningService/CourseTeamMemberships | Create a course team membership
[**delete_course_team_membership_async**](CourseTeamMembershipsApi.md#delete_course_team_membership_async) | **DELETE** /api/v2/LearningService/CourseTeamMemberships/{membershipId} | Delete a course team membership
[**get_course_team_membership_by_id_async**](CourseTeamMembershipsApi.md#get_course_team_membership_by_id_async) | **GET** /api/v2/LearningService/CourseTeamMemberships/{membershipId} | Get course team membership by ID
[**get_course_team_memberships_async**](CourseTeamMembershipsApi.md#get_course_team_memberships_async) | **GET** /api/v2/LearningService/CourseTeamMemberships | Get all course team memberships
[**get_course_team_memberships_count_async**](CourseTeamMembershipsApi.md#get_course_team_memberships_count_async) | **GET** /api/v2/LearningService/CourseTeamMemberships/Count | Get course team memberships count
[**update_course_team_membership_async**](CourseTeamMembershipsApi.md#update_course_team_membership_async) | **PUT** /api/v2/LearningService/CourseTeamMemberships/{membershipId} | Update a course team membership


# **create_course_team_membership_async**
> create_course_team_membership_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_team_membership_create_dto=course_team_membership_create_dto)

Create a course team membership

Creates a new course team membership for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_team_membership_create_dto import CourseTeamMembershipCreateDto
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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_team_membership_create_dto = openapi_client.CourseTeamMembershipCreateDto() # CourseTeamMembershipCreateDto |  (optional)

    try:
        # Create a course team membership
        api_instance.create_course_team_membership_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_team_membership_create_dto=course_team_membership_create_dto)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->create_course_team_membership_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_team_membership_create_dto** | [**CourseTeamMembershipCreateDto**](CourseTeamMembershipCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_team_membership_async**
> delete_course_team_membership_async(tenant_id, membership_id, api_version=api_version, x_api_version=x_api_version)

Delete a course team membership

Deletes a course team membership by its ID.

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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    membership_id = 'membership_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course team membership
        api_instance.delete_course_team_membership_async(tenant_id, membership_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->delete_course_team_membership_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **membership_id** | **str**|  | 
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

# **get_course_team_membership_by_id_async**
> CourseTeamMembershipDto get_course_team_membership_by_id_async(membership_id, api_version=api_version, x_api_version=x_api_version)

Get course team membership by ID

Retrieves a specific course team membership by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_team_membership_dto import CourseTeamMembershipDto
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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    membership_id = 'membership_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course team membership by ID
        api_response = api_instance.get_course_team_membership_by_id_async(membership_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseTeamMembershipsApi->get_course_team_membership_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->get_course_team_membership_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseTeamMembershipDto**](CourseTeamMembershipDto.md)

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

# **get_course_team_memberships_async**
> List[CourseTeamMembershipDto] get_course_team_memberships_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course team memberships

Retrieves all course team memberships for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_team_membership_dto import CourseTeamMembershipDto
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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course team memberships
        api_response = api_instance.get_course_team_memberships_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseTeamMembershipsApi->get_course_team_memberships_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->get_course_team_memberships_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseTeamMembershipDto]**](CourseTeamMembershipDto.md)

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

# **get_course_team_memberships_count_async**
> int get_course_team_memberships_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course team memberships count

Returns the count of course team memberships for the specified tenant.

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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course team memberships count
        api_response = api_instance.get_course_team_memberships_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseTeamMembershipsApi->get_course_team_memberships_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->get_course_team_memberships_count_async: %s\n" % e)
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

# **update_course_team_membership_async**
> update_course_team_membership_async(tenant_id, membership_id, api_version=api_version, x_api_version=x_api_version, course_team_membership_update_dto=course_team_membership_update_dto)

Update a course team membership

Updates an existing course team membership.

### Example


```python
import openapi_client
from openapi_client.models.course_team_membership_update_dto import CourseTeamMembershipUpdateDto
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
    api_instance = openapi_client.CourseTeamMembershipsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    membership_id = 'membership_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_team_membership_update_dto = openapi_client.CourseTeamMembershipUpdateDto() # CourseTeamMembershipUpdateDto |  (optional)

    try:
        # Update a course team membership
        api_instance.update_course_team_membership_async(tenant_id, membership_id, api_version=api_version, x_api_version=x_api_version, course_team_membership_update_dto=course_team_membership_update_dto)
    except Exception as e:
        print("Exception when calling CourseTeamMembershipsApi->update_course_team_membership_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **membership_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_team_membership_update_dto** | [**CourseTeamMembershipUpdateDto**](CourseTeamMembershipUpdateDto.md)|  | [optional] 

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

