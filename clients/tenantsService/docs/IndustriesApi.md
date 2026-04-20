# openapi_client.IndustriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_industry**](IndustriesApi.md#create_tenant_industry) | **POST** /api/v2/TenantsService/Industries | Create a new tenant industry
[**delete_tenant_industry**](IndustriesApi.md#delete_tenant_industry) | **DELETE** /api/v2/TenantsService/Industries/{tenantIndustryId} | Delete a tenant industry
[**get_tenant_industries**](IndustriesApi.md#get_tenant_industries) | **GET** /api/v2/TenantsService/Industries | Retrieve a list of tenant industries
[**get_tenant_industries_count**](IndustriesApi.md#get_tenant_industries_count) | **GET** /api/v2/TenantsService/Industries/Count | Get the count of tenant industries
[**get_tenant_industry_by_id**](IndustriesApi.md#get_tenant_industry_by_id) | **GET** /api/v2/TenantsService/Industries/{tenantIndustryId} | Retrieve a single tenant industry by its ID
[**update_tenant_industry**](IndustriesApi.md#update_tenant_industry) | **PUT** /api/v2/TenantsService/Industries/{tenantIndustryId} | Update a tenant industry


# **create_tenant_industry**
> EmptyEnvelope create_tenant_industry(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_industry_create_dto=tenant_industry_create_dto)

Create a new tenant industry

Create a new tenant industry

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_industry_create_dto import TenantIndustryCreateDto
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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_industry_create_dto = openapi_client.TenantIndustryCreateDto() # TenantIndustryCreateDto |  (optional)

    try:
        # Create a new tenant industry
        api_response = api_instance.create_tenant_industry(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_industry_create_dto=tenant_industry_create_dto)
        print("The response of IndustriesApi->create_tenant_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->create_tenant_industry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_industry_create_dto** | [**TenantIndustryCreateDto**](TenantIndustryCreateDto.md)|  | [optional] 

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

# **delete_tenant_industry**
> EmptyEnvelope delete_tenant_industry(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant industry

Delete a tenant industry

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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_industry_id = 'tenant_industry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant industry
        api_response = api_instance.delete_tenant_industry(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IndustriesApi->delete_tenant_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->delete_tenant_industry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_industry_id** | **str**|  | 
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

# **get_tenant_industries**
> TenantIndustryDtoListEnvelope get_tenant_industries(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant industries

Retrieve a list of tenant industries

### Example


```python
import openapi_client
from openapi_client.models.tenant_industry_dto_list_envelope import TenantIndustryDtoListEnvelope
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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant industries
        api_response = api_instance.get_tenant_industries(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IndustriesApi->get_tenant_industries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->get_tenant_industries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantIndustryDtoListEnvelope**](TenantIndustryDtoListEnvelope.md)

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

# **get_tenant_industries_count**
> Int32Envelope get_tenant_industries_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant industries

Get the count of tenant industries

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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant industries
        api_response = api_instance.get_tenant_industries_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IndustriesApi->get_tenant_industries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->get_tenant_industries_count: %s\n" % e)
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

# **get_tenant_industry_by_id**
> TenantIndustryDtoEnvelope get_tenant_industry_by_id(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant industry by its ID

Retrieve a single tenant industry by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_industry_dto_envelope import TenantIndustryDtoEnvelope
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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_industry_id = 'tenant_industry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant industry by its ID
        api_response = api_instance.get_tenant_industry_by_id(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IndustriesApi->get_tenant_industry_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->get_tenant_industry_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_industry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantIndustryDtoEnvelope**](TenantIndustryDtoEnvelope.md)

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

# **update_tenant_industry**
> EmptyEnvelope update_tenant_industry(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version, tenant_industry_update_dto=tenant_industry_update_dto)

Update a tenant industry

Update a tenant industry

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_industry_update_dto import TenantIndustryUpdateDto
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
    api_instance = openapi_client.IndustriesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_industry_id = 'tenant_industry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_industry_update_dto = openapi_client.TenantIndustryUpdateDto() # TenantIndustryUpdateDto |  (optional)

    try:
        # Update a tenant industry
        api_response = api_instance.update_tenant_industry(tenant_id, tenant_industry_id, api_version=api_version, x_api_version=x_api_version, tenant_industry_update_dto=tenant_industry_update_dto)
        print("The response of IndustriesApi->update_tenant_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->update_tenant_industry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_industry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_industry_update_dto** | [**TenantIndustryUpdateDto**](TenantIndustryUpdateDto.md)|  | [optional] 

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

