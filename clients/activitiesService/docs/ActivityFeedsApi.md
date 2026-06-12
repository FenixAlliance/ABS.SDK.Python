# openapi_client.ActivityFeedsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_activity_types_async**](ActivityFeedsApi.md#count_activity_types_async) | **GET** /api/v2/ActivitiesService/ActivityTypes/Count | Count Activity Types
[**create_activity_async**](ActivityFeedsApi.md#create_activity_async) | **POST** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities | Create an activity
[**create_activity_type_async**](ActivityFeedsApi.md#create_activity_type_async) | **POST** /api/v2/ActivitiesService/ActivityTypes | Create Activity Type
[**delete_activity_async**](ActivityFeedsApi.md#delete_activity_async) | **DELETE** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities/{activityId} | Delete an activity
[**delete_activity_type_async**](ActivityFeedsApi.md#delete_activity_type_async) | **DELETE** /api/v2/ActivitiesService/ActivityTypes/{activityTypeId} | Delete Activity Type
[**get_activities_async**](ActivityFeedsApi.md#get_activities_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities | Get activities
[**get_activities_count_async**](ActivityFeedsApi.md#get_activities_count_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities/Count | Count activities
[**get_activity_async**](ActivityFeedsApi.md#get_activity_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities/{activityId} | Get activity by ID
[**get_activity_feed_async**](ActivityFeedsApi.md#get_activity_feed_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId} | Get activity feed by ID
[**get_activity_feeds_async**](ActivityFeedsApi.md#get_activity_feeds_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds | Get activity feeds
[**get_activity_feeds_count_async**](ActivityFeedsApi.md#get_activity_feeds_count_async) | **GET** /api/v2/ActivitiesService/ActivityFeeds/Count | Count activity feeds
[**get_activity_type_by_id_async**](ActivityFeedsApi.md#get_activity_type_by_id_async) | **GET** /api/v2/ActivitiesService/ActivityTypes/{activityTypeId} | Get Activity Type
[**get_activity_types_async**](ActivityFeedsApi.md#get_activity_types_async) | **GET** /api/v2/ActivitiesService/ActivityTypes | Get Activity Types
[**patch_activity_async**](ActivityFeedsApi.md#patch_activity_async) | **PATCH** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities/{activityId} | Patch an activity
[**patch_activity_type_async**](ActivityFeedsApi.md#patch_activity_type_async) | **PATCH** /api/v2/ActivitiesService/ActivityTypes/{activityTypeId} | Patch Activity Type
[**update_activity_async**](ActivityFeedsApi.md#update_activity_async) | **PUT** /api/v2/ActivitiesService/ActivityFeeds/{activityFeedId}/Activities/{activityId} | Update an activity
[**update_activity_type_async**](ActivityFeedsApi.md#update_activity_type_async) | **PUT** /api/v2/ActivitiesService/ActivityTypes/{activityTypeId} | Update Activity Type


# **count_activity_types_async**
> Int32Envelope count_activity_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count Activity Types

Count activity types for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count Activity Types
        api_response = api_instance.count_activity_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->count_activity_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->count_activity_types_async: %s\n" % e)
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

# **create_activity_async**
> ActivityRecordDtoEnvelope create_activity_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version, activity_record_create_dto=activity_record_create_dto)

Create an activity

Creates a new activity in a specific activity feed.

### Example


```python
import openapi_client
from openapi_client.models.activity_record_create_dto import ActivityRecordCreateDto
from openapi_client.models.activity_record_dto_envelope import ActivityRecordDtoEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    activity_record_create_dto = openapi_client.ActivityRecordCreateDto() # ActivityRecordCreateDto |  (optional)

    try:
        # Create an activity
        api_response = api_instance.create_activity_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version, activity_record_create_dto=activity_record_create_dto)
        print("The response of ActivityFeedsApi->create_activity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->create_activity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **activity_record_create_dto** | [**ActivityRecordCreateDto**](ActivityRecordCreateDto.md)|  | [optional] 

### Return type

[**ActivityRecordDtoEnvelope**](ActivityRecordDtoEnvelope.md)

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

# **create_activity_type_async**
> Envelope create_activity_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, activity_type_create_dto=activity_type_create_dto)

Create Activity Type

Create a new activity type.

### Example


```python
import openapi_client
from openapi_client.models.activity_type_create_dto import ActivityTypeCreateDto
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    activity_type_create_dto = openapi_client.ActivityTypeCreateDto() # ActivityTypeCreateDto |  (optional)

    try:
        # Create Activity Type
        api_response = api_instance.create_activity_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, activity_type_create_dto=activity_type_create_dto)
        print("The response of ActivityFeedsApi->create_activity_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->create_activity_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **activity_type_create_dto** | [**ActivityTypeCreateDto**](ActivityTypeCreateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **delete_activity_async**
> EmptyEnvelope delete_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version)

Delete an activity

Deletes an activity from an activity feed.

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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    activity_id = 'activity_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an activity
        api_response = api_instance.delete_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->delete_activity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->delete_activity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **activity_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_type_async**
> Envelope delete_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version)

Delete Activity Type

Delete an activity type.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_type_id = 'activity_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete Activity Type
        api_response = api_instance.delete_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->delete_activity_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->delete_activity_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **get_activities_async**
> ActivityRecordDtoListEnvelope get_activities_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)

Get activities

Retrieves activities for a specific activity feed.

### Example


```python
import openapi_client
from openapi_client.models.activity_record_dto_list_envelope import ActivityRecordDtoListEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get activities
        api_response = api_instance.get_activities_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activities_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activities_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityRecordDtoListEnvelope**](ActivityRecordDtoListEnvelope.md)

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

# **get_activities_count_async**
> Int32Envelope get_activities_count_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)

Count activities

Returns the count of activities for a specific activity feed.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count activities
        api_response = api_instance.get_activities_count_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activities_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activities_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
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

# **get_activity_async**
> ActivityRecordDtoEnvelope get_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version)

Get activity by ID

Retrieves a specific activity by its ID.

### Example


```python
import openapi_client
from openapi_client.models.activity_record_dto_envelope import ActivityRecordDtoEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    activity_id = 'activity_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get activity by ID
        api_response = api_instance.get_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **activity_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityRecordDtoEnvelope**](ActivityRecordDtoEnvelope.md)

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

# **get_activity_feed_async**
> ActivityFeedDtoEnvelope get_activity_feed_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)

Get activity feed by ID

Retrieves a specific activity feed by its ID.

### Example


```python
import openapi_client
from openapi_client.models.activity_feed_dto_envelope import ActivityFeedDtoEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get activity feed by ID
        api_response = api_instance.get_activity_feed_async(tenant_id, activity_feed_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_feed_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_feed_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityFeedDtoEnvelope**](ActivityFeedDtoEnvelope.md)

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

# **get_activity_feeds_async**
> ActivityFeedDtoListEnvelope get_activity_feeds_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get activity feeds

Retrieves a list of activity feeds for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.activity_feed_dto_list_envelope import ActivityFeedDtoListEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get activity feeds
        api_response = api_instance.get_activity_feeds_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_feeds_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_feeds_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityFeedDtoListEnvelope**](ActivityFeedDtoListEnvelope.md)

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

# **get_activity_feeds_count_async**
> Int32Envelope get_activity_feeds_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count activity feeds

Returns the count of activity feeds for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count activity feeds
        api_response = api_instance.get_activity_feeds_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_feeds_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_feeds_count_async: %s\n" % e)
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

# **get_activity_type_by_id_async**
> ActivityTypeDtoEnvelope get_activity_type_by_id_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version)

Get Activity Type

Get an activity type by ID.

### Example


```python
import openapi_client
from openapi_client.models.activity_type_dto_envelope import ActivityTypeDtoEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_type_id = 'activity_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Activity Type
        api_response = api_instance.get_activity_type_by_id_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityTypeDtoEnvelope**](ActivityTypeDtoEnvelope.md)

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

# **get_activity_types_async**
> ActivityTypeDtoListEnvelope get_activity_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get Activity Types

Get a list of activity types for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.activity_type_dto_list_envelope import ActivityTypeDtoListEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Activity Types
        api_response = api_instance.get_activity_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ActivityFeedsApi->get_activity_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->get_activity_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ActivityTypeDtoListEnvelope**](ActivityTypeDtoListEnvelope.md)

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

# **patch_activity_async**
> EmptyEnvelope patch_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an activity

Patch an activity

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    activity_id = 'activity_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an activity
        api_response = api_instance.patch_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ActivityFeedsApi->patch_activity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->patch_activity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **activity_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **patch_activity_type_async**
> EmptyEnvelope patch_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch Activity Type

Patch an activity type

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_type_id = 'activity_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch Activity Type
        api_response = api_instance.patch_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ActivityFeedsApi->patch_activity_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->patch_activity_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **update_activity_async**
> ActivityRecordDtoEnvelope update_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version, activity_record_update_dto=activity_record_update_dto)

Update an activity

Updates an existing activity.

### Example


```python
import openapi_client
from openapi_client.models.activity_record_dto_envelope import ActivityRecordDtoEnvelope
from openapi_client.models.activity_record_update_dto import ActivityRecordUpdateDto
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_feed_id = 'activity_feed_id_example' # str | 
    activity_id = 'activity_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    activity_record_update_dto = openapi_client.ActivityRecordUpdateDto() # ActivityRecordUpdateDto |  (optional)

    try:
        # Update an activity
        api_response = api_instance.update_activity_async(tenant_id, activity_feed_id, activity_id, api_version=api_version, x_api_version=x_api_version, activity_record_update_dto=activity_record_update_dto)
        print("The response of ActivityFeedsApi->update_activity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->update_activity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_feed_id** | **str**|  | 
 **activity_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **activity_record_update_dto** | [**ActivityRecordUpdateDto**](ActivityRecordUpdateDto.md)|  | [optional] 

### Return type

[**ActivityRecordDtoEnvelope**](ActivityRecordDtoEnvelope.md)

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

# **update_activity_type_async**
> Envelope update_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version, activity_type_update_dto=activity_type_update_dto)

Update Activity Type

Update an existing activity type.

### Example


```python
import openapi_client
from openapi_client.models.activity_type_update_dto import ActivityTypeUpdateDto
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ActivityFeedsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    activity_type_id = 'activity_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    activity_type_update_dto = openapi_client.ActivityTypeUpdateDto() # ActivityTypeUpdateDto |  (optional)

    try:
        # Update Activity Type
        api_response = api_instance.update_activity_type_async(tenant_id, activity_type_id, api_version=api_version, x_api_version=x_api_version, activity_type_update_dto=activity_type_update_dto)
        print("The response of ActivityFeedsApi->update_activity_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFeedsApi->update_activity_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **activity_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **activity_type_update_dto** | [**ActivityTypeUpdateDto**](ActivityTypeUpdateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

