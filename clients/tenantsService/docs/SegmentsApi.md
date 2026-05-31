# openapi_client.SegmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_segment**](SegmentsApi.md#create_tenant_segment) | **POST** /api/v2/TenantsService/Segments | Create a new tenant segment
[**delete_tenant_segment**](SegmentsApi.md#delete_tenant_segment) | **DELETE** /api/v2/TenantsService/Segments/{tenantSegmentId} | Delete a tenant segment
[**get_tenant_segment_by_id**](SegmentsApi.md#get_tenant_segment_by_id) | **GET** /api/v2/TenantsService/Segments/{tenantSegmentId} | Retrieve a single tenant segment by its ID
[**get_tenant_segments**](SegmentsApi.md#get_tenant_segments) | **GET** /api/v2/TenantsService/Segments | Retrieve a list of tenant segments
[**get_tenant_segments_count**](SegmentsApi.md#get_tenant_segments_count) | **GET** /api/v2/TenantsService/Segments/Count | Get the count of tenant segments
[**update_tenant_segment**](SegmentsApi.md#update_tenant_segment) | **PUT** /api/v2/TenantsService/Segments/{tenantSegmentId} | Update a tenant segment


# **create_tenant_segment**
> EmptyEnvelope create_tenant_segment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_segment_create_dto=tenant_segment_create_dto)

Create a new tenant segment

Create a new tenant segment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_segment_create_dto import TenantSegmentCreateDto
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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_segment_create_dto = openapi_client.TenantSegmentCreateDto() # TenantSegmentCreateDto |  (optional)

    try:
        # Create a new tenant segment
        api_response = api_instance.create_tenant_segment(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_segment_create_dto=tenant_segment_create_dto)
        print("The response of SegmentsApi->create_tenant_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->create_tenant_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_segment_create_dto** | [**TenantSegmentCreateDto**](TenantSegmentCreateDto.md)|  | [optional] 

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

# **delete_tenant_segment**
> EmptyEnvelope delete_tenant_segment(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant segment

Delete a tenant segment

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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_segment_id = 'tenant_segment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant segment
        api_response = api_instance.delete_tenant_segment(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SegmentsApi->delete_tenant_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_tenant_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_segment_id** | **str**|  | 
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

# **get_tenant_segment_by_id**
> TenantSegmentDtoEnvelope get_tenant_segment_by_id(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant segment by its ID

Retrieve a single tenant segment by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_segment_dto_envelope import TenantSegmentDtoEnvelope
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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_segment_id = 'tenant_segment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant segment by its ID
        api_response = api_instance.get_tenant_segment_by_id(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SegmentsApi->get_tenant_segment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_tenant_segment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_segment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantSegmentDtoEnvelope**](TenantSegmentDtoEnvelope.md)

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

# **get_tenant_segments**
> TenantSegmentDtoListEnvelope get_tenant_segments(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant segments

Retrieve a list of tenant segments

### Example


```python
import openapi_client
from openapi_client.models.tenant_segment_dto_list_envelope import TenantSegmentDtoListEnvelope
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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant segments
        api_response = api_instance.get_tenant_segments(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SegmentsApi->get_tenant_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_tenant_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantSegmentDtoListEnvelope**](TenantSegmentDtoListEnvelope.md)

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

# **get_tenant_segments_count**
> Int32Envelope get_tenant_segments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant segments

Get the count of tenant segments

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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant segments
        api_response = api_instance.get_tenant_segments_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SegmentsApi->get_tenant_segments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_tenant_segments_count: %s\n" % e)
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

# **update_tenant_segment**
> EmptyEnvelope update_tenant_segment(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version, tenant_segment_update_dto=tenant_segment_update_dto)

Update a tenant segment

Update a tenant segment

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_segment_update_dto import TenantSegmentUpdateDto
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
    api_instance = openapi_client.SegmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_segment_id = 'tenant_segment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_segment_update_dto = openapi_client.TenantSegmentUpdateDto() # TenantSegmentUpdateDto |  (optional)

    try:
        # Update a tenant segment
        api_response = api_instance.update_tenant_segment(tenant_id, tenant_segment_id, api_version=api_version, x_api_version=x_api_version, tenant_segment_update_dto=tenant_segment_update_dto)
        print("The response of SegmentsApi->update_tenant_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->update_tenant_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_segment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_segment_update_dto** | [**TenantSegmentUpdateDto**](TenantSegmentUpdateDto.md)|  | [optional] 

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

