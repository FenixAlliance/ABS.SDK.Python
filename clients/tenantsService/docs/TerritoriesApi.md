# openapi_client.TerritoriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_territory**](TerritoriesApi.md#create_tenant_territory) | **POST** /api/v2/TenantsService/Territories | Create a new tenant territory
[**delete_tenant_territory**](TerritoriesApi.md#delete_tenant_territory) | **DELETE** /api/v2/TenantsService/Territories/{tenantTerritoryId} | Delete a tenant territory
[**get_tenant_territories**](TerritoriesApi.md#get_tenant_territories) | **GET** /api/v2/TenantsService/Territories | Retrieve a list of tenant territories
[**get_tenant_territories_count**](TerritoriesApi.md#get_tenant_territories_count) | **GET** /api/v2/TenantsService/Territories/Count | Get the count of tenant territories
[**get_tenant_territory_by_id**](TerritoriesApi.md#get_tenant_territory_by_id) | **GET** /api/v2/TenantsService/Territories/{tenantTerritoryId} | Retrieve a single tenant territory by its ID
[**update_tenant_territory**](TerritoriesApi.md#update_tenant_territory) | **PUT** /api/v2/TenantsService/Territories/{tenantTerritoryId} | Update a tenant territory


# **create_tenant_territory**
> EmptyEnvelope create_tenant_territory(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_territory_create_dto=tenant_territory_create_dto)

Create a new tenant territory

Create a new tenant territory

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_territory_create_dto import TenantTerritoryCreateDto
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_territory_create_dto = openapi_client.TenantTerritoryCreateDto() # TenantTerritoryCreateDto |  (optional)

    try:
        # Create a new tenant territory
        api_response = api_instance.create_tenant_territory(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_territory_create_dto=tenant_territory_create_dto)
        print("The response of TerritoriesApi->create_tenant_territory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->create_tenant_territory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_territory_create_dto** | [**TenantTerritoryCreateDto**](TenantTerritoryCreateDto.md)|  | [optional] 

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

# **delete_tenant_territory**
> EmptyEnvelope delete_tenant_territory(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant territory

Delete a tenant territory

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_territory_id = 'tenant_territory_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant territory
        api_response = api_instance.delete_tenant_territory(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TerritoriesApi->delete_tenant_territory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->delete_tenant_territory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_territory_id** | **str**|  | 
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

# **get_tenant_territories**
> TenantTerritoryDtoListEnvelope get_tenant_territories(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant territories

Retrieve a list of tenant territories

### Example


```python
import openapi_client
from openapi_client.models.tenant_territory_dto_list_envelope import TenantTerritoryDtoListEnvelope
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant territories
        api_response = api_instance.get_tenant_territories(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TerritoriesApi->get_tenant_territories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->get_tenant_territories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTerritoryDtoListEnvelope**](TenantTerritoryDtoListEnvelope.md)

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

# **get_tenant_territories_count**
> Int32Envelope get_tenant_territories_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant territories

Get the count of tenant territories

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant territories
        api_response = api_instance.get_tenant_territories_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TerritoriesApi->get_tenant_territories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->get_tenant_territories_count: %s\n" % e)
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

# **get_tenant_territory_by_id**
> TenantTerritoryDtoEnvelope get_tenant_territory_by_id(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant territory by its ID

Retrieve a single tenant territory by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_territory_dto_envelope import TenantTerritoryDtoEnvelope
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_territory_id = 'tenant_territory_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant territory by its ID
        api_response = api_instance.get_tenant_territory_by_id(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TerritoriesApi->get_tenant_territory_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->get_tenant_territory_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_territory_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTerritoryDtoEnvelope**](TenantTerritoryDtoEnvelope.md)

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

# **update_tenant_territory**
> EmptyEnvelope update_tenant_territory(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version, tenant_territory_update_dto=tenant_territory_update_dto)

Update a tenant territory

Update a tenant territory

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_territory_update_dto import TenantTerritoryUpdateDto
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
    api_instance = openapi_client.TerritoriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_territory_id = 'tenant_territory_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_territory_update_dto = openapi_client.TenantTerritoryUpdateDto() # TenantTerritoryUpdateDto |  (optional)

    try:
        # Update a tenant territory
        api_response = api_instance.update_tenant_territory(tenant_id, tenant_territory_id, api_version=api_version, x_api_version=x_api_version, tenant_territory_update_dto=tenant_territory_update_dto)
        print("The response of TerritoriesApi->update_tenant_territory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerritoriesApi->update_tenant_territory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_territory_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_territory_update_dto** | [**TenantTerritoryUpdateDto**](TenantTerritoryUpdateDto.md)|  | [optional] 

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

