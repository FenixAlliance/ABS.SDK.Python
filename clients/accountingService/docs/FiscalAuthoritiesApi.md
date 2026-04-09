# openapi_client.FiscalAuthoritiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_authority**](FiscalAuthoritiesApi.md#create_fiscal_authority) | **POST** /api/v2/AccountingService/Fiscals/Authorities | Create a fiscal authority
[**delete_fiscal_authority**](FiscalAuthoritiesApi.md#delete_fiscal_authority) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/{authorityId} | Delete a fiscal authority
[**get_fiscal_authorities**](FiscalAuthoritiesApi.md#get_fiscal_authorities) | **GET** /api/v2/AccountingService/Fiscals/Authorities | Get fiscal authorities
[**get_fiscal_authorities_count**](FiscalAuthoritiesApi.md#get_fiscal_authorities_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/Count | Get fiscal authorities count
[**get_fiscal_authority**](FiscalAuthoritiesApi.md#get_fiscal_authority) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId} | Get fiscal authority by ID
[**update_fiscal_authority**](FiscalAuthoritiesApi.md#update_fiscal_authority) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/{authorityId} | Update a fiscal authority


# **create_fiscal_authority**
> EmptyEnvelope create_fiscal_authority(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_authority_create_dto=fiscal_authority_create_dto)

Create a fiscal authority

Creates a new fiscal authority for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_authority_create_dto import FiscalAuthorityCreateDto
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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_authority_create_dto = openapi_client.FiscalAuthorityCreateDto() # FiscalAuthorityCreateDto |  (optional)

    try:
        # Create a fiscal authority
        api_response = api_instance.create_fiscal_authority(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_authority_create_dto=fiscal_authority_create_dto)
        print("The response of FiscalAuthoritiesApi->create_fiscal_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->create_fiscal_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_authority_create_dto** | [**FiscalAuthorityCreateDto**](FiscalAuthorityCreateDto.md)|  | [optional] 

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

# **delete_fiscal_authority**
> EmptyEnvelope delete_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal authority

Deletes a fiscal authority identified by its unique identifier.

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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal authority
        api_response = api_instance.delete_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthoritiesApi->delete_fiscal_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->delete_fiscal_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **authority_id** | **str**|  | 
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

# **get_fiscal_authorities**
> FiscalAuthorityDtoListEnvelope get_fiscal_authorities(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal authorities

Retrieves all fiscal authorities for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_authority_dto_list_envelope import FiscalAuthorityDtoListEnvelope
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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal authorities
        api_response = api_instance.get_fiscal_authorities(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthoritiesApi->get_fiscal_authorities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->get_fiscal_authorities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalAuthorityDtoListEnvelope**](FiscalAuthorityDtoListEnvelope.md)

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

# **get_fiscal_authorities_count**
> Int32Envelope get_fiscal_authorities_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal authorities count

Returns the total count of fiscal authorities for the specified tenant.

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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal authorities count
        api_response = api_instance.get_fiscal_authorities_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthoritiesApi->get_fiscal_authorities_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->get_fiscal_authorities_count: %s\n" % e)
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

# **get_fiscal_authority**
> FiscalAuthorityDtoEnvelope get_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal authority by ID

Retrieves a specific fiscal authority by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_authority_dto_envelope import FiscalAuthorityDtoEnvelope
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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal authority by ID
        api_response = api_instance.get_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthoritiesApi->get_fiscal_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->get_fiscal_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalAuthorityDtoEnvelope**](FiscalAuthorityDtoEnvelope.md)

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

# **update_fiscal_authority**
> EmptyEnvelope update_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version, fiscal_authority_update_dto=fiscal_authority_update_dto)

Update a fiscal authority

Updates an existing fiscal authority identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_authority_update_dto import FiscalAuthorityUpdateDto
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
    api_instance = openapi_client.FiscalAuthoritiesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_authority_update_dto = openapi_client.FiscalAuthorityUpdateDto() # FiscalAuthorityUpdateDto |  (optional)

    try:
        # Update a fiscal authority
        api_response = api_instance.update_fiscal_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version, fiscal_authority_update_dto=fiscal_authority_update_dto)
        print("The response of FiscalAuthoritiesApi->update_fiscal_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthoritiesApi->update_fiscal_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_authority_update_dto** | [**FiscalAuthorityUpdateDto**](FiscalAuthorityUpdateDto.md)|  | [optional] 

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

