# openapi_client.PositionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_position**](PositionsApi.md#create_tenant_position) | **POST** /api/v2/TenantsService/Positions | Create a new tenant position
[**delete_tenant_position**](PositionsApi.md#delete_tenant_position) | **DELETE** /api/v2/TenantsService/Positions/{tenantPositionId} | Delete a tenant position
[**get_tenant_position_by_id**](PositionsApi.md#get_tenant_position_by_id) | **GET** /api/v2/TenantsService/Positions/{tenantPositionId} | Retrieve a single tenant position by its ID
[**get_tenant_positions**](PositionsApi.md#get_tenant_positions) | **GET** /api/v2/TenantsService/Positions | Retrieve a list of tenant positions
[**get_tenant_positions_count**](PositionsApi.md#get_tenant_positions_count) | **GET** /api/v2/TenantsService/Positions/Count | Get the count of tenant positions
[**update_tenant_position**](PositionsApi.md#update_tenant_position) | **PUT** /api/v2/TenantsService/Positions/{tenantPositionId} | Update a tenant position


# **create_tenant_position**
> EmptyEnvelope create_tenant_position(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_position_create_dto=tenant_position_create_dto)

Create a new tenant position

Create a new tenant position

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_position_create_dto import TenantPositionCreateDto
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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_position_create_dto = openapi_client.TenantPositionCreateDto() # TenantPositionCreateDto |  (optional)

    try:
        # Create a new tenant position
        api_response = api_instance.create_tenant_position(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_position_create_dto=tenant_position_create_dto)
        print("The response of PositionsApi->create_tenant_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->create_tenant_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_position_create_dto** | [**TenantPositionCreateDto**](TenantPositionCreateDto.md)|  | [optional] 

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

# **delete_tenant_position**
> EmptyEnvelope delete_tenant_position(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant position

Delete a tenant position

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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_position_id = 'tenant_position_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant position
        api_response = api_instance.delete_tenant_position(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PositionsApi->delete_tenant_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->delete_tenant_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_position_id** | **str**|  | 
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

# **get_tenant_position_by_id**
> TenantPositionDtoEnvelope get_tenant_position_by_id(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant position by its ID

Retrieve a single tenant position by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_position_dto_envelope import TenantPositionDtoEnvelope
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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_position_id = 'tenant_position_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant position by its ID
        api_response = api_instance.get_tenant_position_by_id(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PositionsApi->get_tenant_position_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_tenant_position_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_position_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantPositionDtoEnvelope**](TenantPositionDtoEnvelope.md)

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

# **get_tenant_positions**
> TenantPositionDtoListEnvelope get_tenant_positions(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant positions

Retrieve a list of tenant positions

### Example


```python
import openapi_client
from openapi_client.models.tenant_position_dto_list_envelope import TenantPositionDtoListEnvelope
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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant positions
        api_response = api_instance.get_tenant_positions(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PositionsApi->get_tenant_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_tenant_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantPositionDtoListEnvelope**](TenantPositionDtoListEnvelope.md)

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

# **get_tenant_positions_count**
> Int32Envelope get_tenant_positions_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant positions

Get the count of tenant positions

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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant positions
        api_response = api_instance.get_tenant_positions_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PositionsApi->get_tenant_positions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_tenant_positions_count: %s\n" % e)
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

# **update_tenant_position**
> EmptyEnvelope update_tenant_position(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version, tenant_position_update_dto=tenant_position_update_dto)

Update a tenant position

Update a tenant position

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_position_update_dto import TenantPositionUpdateDto
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
    api_instance = openapi_client.PositionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_position_id = 'tenant_position_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_position_update_dto = openapi_client.TenantPositionUpdateDto() # TenantPositionUpdateDto |  (optional)

    try:
        # Update a tenant position
        api_response = api_instance.update_tenant_position(tenant_id, tenant_position_id, api_version=api_version, x_api_version=x_api_version, tenant_position_update_dto=tenant_position_update_dto)
        print("The response of PositionsApi->update_tenant_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->update_tenant_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_position_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_position_update_dto** | [**TenantPositionUpdateDto**](TenantPositionUpdateDto.md)|  | [optional] 

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

