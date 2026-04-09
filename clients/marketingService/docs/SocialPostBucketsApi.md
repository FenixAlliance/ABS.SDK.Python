# openapi_client.SocialPostBucketsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_social_post_bucket_async**](SocialPostBucketsApi.md#create_social_post_bucket_async) | **POST** /api/v2/MarketingService/SocialPostBuckets | Create a social post bucket
[**delete_social_post_bucket_async**](SocialPostBucketsApi.md#delete_social_post_bucket_async) | **DELETE** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | Delete a social post bucket
[**get_social_post_bucket_details_async**](SocialPostBucketsApi.md#get_social_post_bucket_details_async) | **GET** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | Get social post bucket by ID
[**get_social_post_buckets_count_async**](SocialPostBucketsApi.md#get_social_post_buckets_count_async) | **GET** /api/v2/MarketingService/SocialPostBuckets/Count | Get social post buckets count
[**get_social_post_buckets_o_data_async**](SocialPostBucketsApi.md#get_social_post_buckets_o_data_async) | **GET** /api/v2/MarketingService/SocialPostBuckets | Get social post buckets
[**update_social_post_bucket_async**](SocialPostBucketsApi.md#update_social_post_bucket_async) | **PUT** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | Update a social post bucket


# **create_social_post_bucket_async**
> EmptyEnvelope create_social_post_bucket_async(tenant_id, social_post_bucket_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a social post bucket

Creates a new social post bucket for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_bucket_create_dto import SocialPostBucketCreateDto
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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_post_bucket_create_dto = openapi_client.SocialPostBucketCreateDto() # SocialPostBucketCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a social post bucket
        api_response = api_instance.create_social_post_bucket_async(tenant_id, social_post_bucket_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->create_social_post_bucket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->create_social_post_bucket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **social_post_bucket_create_dto** | [**SocialPostBucketCreateDto**](SocialPostBucketCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_social_post_bucket_async**
> EmptyEnvelope delete_social_post_bucket_async(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)

Delete a social post bucket

Deletes a social post bucket by its ID.

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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialpostbucket_id = 'socialpostbucket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a social post bucket
        api_response = api_instance.delete_social_post_bucket_async(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->delete_social_post_bucket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->delete_social_post_bucket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialpostbucket_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_post_bucket_details_async**
> SocialPostBucketDtoEnvelope get_social_post_bucket_details_async(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)

Get social post bucket by ID

Retrieves the details of a specific social post bucket by its ID.

### Example


```python
import openapi_client
from openapi_client.models.social_post_bucket_dto_envelope import SocialPostBucketDtoEnvelope
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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialpostbucket_id = 'socialpostbucket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post bucket by ID
        api_response = api_instance.get_social_post_bucket_details_async(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->get_social_post_bucket_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->get_social_post_bucket_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialpostbucket_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostBucketDtoEnvelope**](SocialPostBucketDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_post_buckets_count_async**
> Int32Envelope get_social_post_buckets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get social post buckets count

Returns the count of social post buckets for the specified tenant using OData query options.

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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post buckets count
        api_response = api_instance.get_social_post_buckets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->get_social_post_buckets_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->get_social_post_buckets_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_post_buckets_o_data_async**
> SocialPostBucketDtoListEnvelope get_social_post_buckets_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get social post buckets

Retrieves a collection of social post buckets for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.social_post_bucket_dto_list_envelope import SocialPostBucketDtoListEnvelope
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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get social post buckets
        api_response = api_instance.get_social_post_buckets_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->get_social_post_buckets_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->get_social_post_buckets_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialPostBucketDtoListEnvelope**](SocialPostBucketDtoListEnvelope.md)

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

# **update_social_post_bucket_async**
> EmptyEnvelope update_social_post_bucket_async(tenant_id, socialpostbucket_id, social_post_bucket_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a social post bucket

Updates an existing social post bucket by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.social_post_bucket_update_dto import SocialPostBucketUpdateDto
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
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialpostbucket_id = 'socialpostbucket_id_example' # str | 
    social_post_bucket_update_dto = openapi_client.SocialPostBucketUpdateDto() # SocialPostBucketUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a social post bucket
        api_response = api_instance.update_social_post_bucket_async(tenant_id, socialpostbucket_id, social_post_bucket_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->update_social_post_bucket_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->update_social_post_bucket_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **socialpostbucket_id** | **str**|  | 
 **social_post_bucket_update_dto** | [**SocialPostBucketUpdateDto**](SocialPostBucketUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

