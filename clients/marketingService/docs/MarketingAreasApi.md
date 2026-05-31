# openapi_client.MarketingAreasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketing_area_async**](MarketingAreasApi.md#create_marketing_area_async) | **POST** /api/v2/MarketingService/MarketingAreas | Create a marketing area
[**delete_marketing_area_async**](MarketingAreasApi.md#delete_marketing_area_async) | **DELETE** /api/v2/MarketingService/MarketingAreas/{marketingAreaId} | Delete a marketing area
[**get_marketing_area_by_id_async**](MarketingAreasApi.md#get_marketing_area_by_id_async) | **GET** /api/v2/MarketingService/MarketingAreas/{marketingAreaId} | Get marketing area by ID
[**get_marketing_areas_async**](MarketingAreasApi.md#get_marketing_areas_async) | **GET** /api/v2/MarketingService/MarketingAreas | Get marketing areas
[**get_marketing_areas_count_async**](MarketingAreasApi.md#get_marketing_areas_count_async) | **GET** /api/v2/MarketingService/MarketingAreas/Count | Count marketing areas
[**update_marketing_area_async**](MarketingAreasApi.md#update_marketing_area_async) | **PUT** /api/v2/MarketingService/MarketingAreas/{marketingAreaId} | Update a marketing area


# **create_marketing_area_async**
> EmptyEnvelope create_marketing_area_async(tenant_id, api_version=api_version, x_api_version=x_api_version, marketing_area_create_dto=marketing_area_create_dto)

Create a marketing area

Creates a new marketing area for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_area_create_dto import MarketingAreaCreateDto
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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    marketing_area_create_dto = openapi_client.MarketingAreaCreateDto() # MarketingAreaCreateDto |  (optional)

    try:
        # Create a marketing area
        api_response = api_instance.create_marketing_area_async(tenant_id, api_version=api_version, x_api_version=x_api_version, marketing_area_create_dto=marketing_area_create_dto)
        print("The response of MarketingAreasApi->create_marketing_area_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->create_marketing_area_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **marketing_area_create_dto** | [**MarketingAreaCreateDto**](MarketingAreaCreateDto.md)|  | [optional] 

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

# **delete_marketing_area_async**
> EmptyEnvelope delete_marketing_area_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version)

Delete a marketing area

Deletes a marketing area for the specified tenant.

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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_area_id = 'marketing_area_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a marketing area
        api_response = api_instance.delete_marketing_area_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingAreasApi->delete_marketing_area_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->delete_marketing_area_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_area_id** | **str**|  | 
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

# **get_marketing_area_by_id_async**
> MarketingAreaDtoEnvelope get_marketing_area_by_id_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version)

Get marketing area by ID

Retrieves a specific marketing area by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.marketing_area_dto_envelope import MarketingAreaDtoEnvelope
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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_area_id = 'marketing_area_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing area by ID
        api_response = api_instance.get_marketing_area_by_id_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingAreasApi->get_marketing_area_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->get_marketing_area_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_area_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingAreaDtoEnvelope**](MarketingAreaDtoEnvelope.md)

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

# **get_marketing_areas_async**
> MarketingAreaDtoListEnvelope get_marketing_areas_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing areas

Retrieves marketing areas for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.marketing_area_dto_list_envelope import MarketingAreaDtoListEnvelope
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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing areas
        api_response = api_instance.get_marketing_areas_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingAreasApi->get_marketing_areas_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->get_marketing_areas_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingAreaDtoListEnvelope**](MarketingAreaDtoListEnvelope.md)

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

# **get_marketing_areas_count_async**
> Int32Envelope get_marketing_areas_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count marketing areas

Counts marketing areas for the specified tenant.

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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count marketing areas
        api_response = api_instance.get_marketing_areas_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingAreasApi->get_marketing_areas_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->get_marketing_areas_count_async: %s\n" % e)
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

# **update_marketing_area_async**
> EmptyEnvelope update_marketing_area_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version, marketing_area_update_dto=marketing_area_update_dto)

Update a marketing area

Updates an existing marketing area for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_area_update_dto import MarketingAreaUpdateDto
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
    api_instance = openapi_client.MarketingAreasApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_area_id = 'marketing_area_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    marketing_area_update_dto = openapi_client.MarketingAreaUpdateDto() # MarketingAreaUpdateDto |  (optional)

    try:
        # Update a marketing area
        api_response = api_instance.update_marketing_area_async(tenant_id, marketing_area_id, api_version=api_version, x_api_version=x_api_version, marketing_area_update_dto=marketing_area_update_dto)
        print("The response of MarketingAreasApi->update_marketing_area_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingAreasApi->update_marketing_area_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_area_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **marketing_area_update_dto** | [**MarketingAreaUpdateDto**](MarketingAreaUpdateDto.md)|  | [optional] 

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

