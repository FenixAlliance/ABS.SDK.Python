# openapi_client.UnitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_unit**](UnitsApi.md#create_tenant_unit) | **POST** /api/v2/TenantsService/Units | Create a new tenant unit
[**delete_tenant_unit**](UnitsApi.md#delete_tenant_unit) | **DELETE** /api/v2/TenantsService/Units/{tenantUnitId} | Delete a tenant unit
[**get_tenant_unit_by_id**](UnitsApi.md#get_tenant_unit_by_id) | **GET** /api/v2/TenantsService/Units/{tenantUnitId} | Retrieve a single tenant unit by its ID
[**get_tenant_units**](UnitsApi.md#get_tenant_units) | **GET** /api/v2/TenantsService/Units | Retrieve a list of tenant units
[**get_tenant_units_count**](UnitsApi.md#get_tenant_units_count) | **GET** /api/v2/TenantsService/Units/Count | Get the count of tenant units
[**update_tenant_unit**](UnitsApi.md#update_tenant_unit) | **PUT** /api/v2/TenantsService/Units/{tenantUnitId} | Update a tenant unit


# **create_tenant_unit**
> EmptyEnvelope create_tenant_unit(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_unit_create_dto=tenant_unit_create_dto)

Create a new tenant unit

Create a new tenant unit

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_unit_create_dto import TenantUnitCreateDto
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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_unit_create_dto = openapi_client.TenantUnitCreateDto() # TenantUnitCreateDto |  (optional)

    try:
        # Create a new tenant unit
        api_response = api_instance.create_tenant_unit(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_unit_create_dto=tenant_unit_create_dto)
        print("The response of UnitsApi->create_tenant_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->create_tenant_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_unit_create_dto** | [**TenantUnitCreateDto**](TenantUnitCreateDto.md)|  | [optional] 

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

# **delete_tenant_unit**
> EmptyEnvelope delete_tenant_unit(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant unit

Delete a tenant unit

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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_unit_id = 'tenant_unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant unit
        api_response = api_instance.delete_tenant_unit(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitsApi->delete_tenant_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->delete_tenant_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_unit_id** | **str**|  | 
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

# **get_tenant_unit_by_id**
> TenantUnitDtoEnvelope get_tenant_unit_by_id(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant unit by its ID

Retrieve a single tenant unit by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_unit_dto_envelope import TenantUnitDtoEnvelope
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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_unit_id = 'tenant_unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant unit by its ID
        api_response = api_instance.get_tenant_unit_by_id(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitsApi->get_tenant_unit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->get_tenant_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantUnitDtoEnvelope**](TenantUnitDtoEnvelope.md)

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

# **get_tenant_units**
> TenantUnitDtoListEnvelope get_tenant_units(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant units

Retrieve a list of tenant units

### Example


```python
import openapi_client
from openapi_client.models.tenant_unit_dto_list_envelope import TenantUnitDtoListEnvelope
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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant units
        api_response = api_instance.get_tenant_units(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitsApi->get_tenant_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->get_tenant_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantUnitDtoListEnvelope**](TenantUnitDtoListEnvelope.md)

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

# **get_tenant_units_count**
> Int32Envelope get_tenant_units_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant units

Get the count of tenant units

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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant units
        api_response = api_instance.get_tenant_units_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitsApi->get_tenant_units_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->get_tenant_units_count: %s\n" % e)
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

# **update_tenant_unit**
> EmptyEnvelope update_tenant_unit(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version, tenant_unit_update_dto=tenant_unit_update_dto)

Update a tenant unit

Update a tenant unit

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_unit_update_dto import TenantUnitUpdateDto
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
    api_instance = openapi_client.UnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_unit_id = 'tenant_unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_unit_update_dto = openapi_client.TenantUnitUpdateDto() # TenantUnitUpdateDto |  (optional)

    try:
        # Update a tenant unit
        api_response = api_instance.update_tenant_unit(tenant_id, tenant_unit_id, api_version=api_version, x_api_version=x_api_version, tenant_unit_update_dto=tenant_unit_update_dto)
        print("The response of UnitsApi->update_tenant_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitsApi->update_tenant_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_unit_update_dto** | [**TenantUnitUpdateDto**](TenantUnitUpdateDto.md)|  | [optional] 

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

