# openapi_client.SocialPostBucketsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_marketing_service_social_post_buckets_count_get**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_count_get) | **GET** /api/v2/MarketingService/SocialPostBuckets/Count | 
[**api_v2_marketing_service_social_post_buckets_get**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_get) | **GET** /api/v2/MarketingService/SocialPostBuckets | 
[**api_v2_marketing_service_social_post_buckets_post**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_post) | **POST** /api/v2/MarketingService/SocialPostBuckets | 
[**api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete) | **DELETE** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | 
[**api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get) | **GET** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | 
[**api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put**](SocialPostBucketsApi.md#api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put) | **PUT** /api/v2/MarketingService/SocialPostBuckets/{socialpostbucketId} | 


# **api_v2_marketing_service_social_post_buckets_count_get**
> Int32Envelope api_v2_marketing_service_social_post_buckets_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_count_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_marketing_service_social_post_buckets_get**
> SocialPostBucketDtoListEnvelope api_v2_marketing_service_social_post_buckets_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_marketing_service_social_post_buckets_post**
> EmptyEnvelope api_v2_marketing_service_social_post_buckets_post(tenant_id, social_post_bucket_create_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    social_post_bucket_create_dto = openapi_client.SocialPostBucketCreateDto() # SocialPostBucketCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_post(tenant_id, social_post_bucket_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_post: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete**
> EmptyEnvelope api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialpostbucket_id = 'socialpostbucket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_delete: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get**
> SocialPostBucketDtoEnvelope api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SocialPostBucketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    socialpostbucket_id = 'socialpostbucket_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get(tenant_id, socialpostbucket_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put**
> EmptyEnvelope api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put(tenant_id, socialpostbucket_id, social_post_bucket_update_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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
        api_response = api_instance.api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put(tenant_id, socialpostbucket_id, social_post_bucket_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialPostBucketsApi->api_v2_marketing_service_social_post_buckets_socialpostbucket_id_put: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

