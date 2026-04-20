# openapi_client.FiscalAuthorityYearsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_year**](FiscalAuthorityYearsApi.md#create_fiscal_year) | **POST** /api/v2/AccountingService/Fiscals/Authorities/FiscalYears | Create a fiscal year
[**delete_fiscal_year**](FiscalAuthorityYearsApi.md#delete_fiscal_year) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/FiscalYears/{fiscalYearId} | Delete a fiscal year
[**get_fiscal_year**](FiscalAuthorityYearsApi.md#get_fiscal_year) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalYears/{fiscalYearId} | Get fiscal year by ID for an authority
[**get_fiscal_years**](FiscalAuthorityYearsApi.md#get_fiscal_years) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/FiscalYears | Get fiscal years for an authority
[**get_fiscal_years_count**](FiscalAuthorityYearsApi.md#get_fiscal_years_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalYears/Count | Get fiscal years count for an authority
[**update_fiscal_year**](FiscalAuthorityYearsApi.md#update_fiscal_year) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/FiscalYears/{fiscalYearId} | Update a fiscal year


# **create_fiscal_year**
> EmptyEnvelope create_fiscal_year(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_create_dto=fiscal_year_create_dto)

Create a fiscal year

Creates a new fiscal year associated with a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_year_create_dto import FiscalYearCreateDto
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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_year_create_dto = openapi_client.FiscalYearCreateDto() # FiscalYearCreateDto |  (optional)

    try:
        # Create a fiscal year
        api_response = api_instance.create_fiscal_year(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_create_dto=fiscal_year_create_dto)
        print("The response of FiscalAuthorityYearsApi->create_fiscal_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->create_fiscal_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_year_create_dto** | [**FiscalYearCreateDto**](FiscalYearCreateDto.md)|  | [optional] 

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

# **delete_fiscal_year**
> EmptyEnvelope delete_fiscal_year(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal year

Deletes a fiscal year identified by its unique identifier.

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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal year
        api_response = api_instance.delete_fiscal_year(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthorityYearsApi->delete_fiscal_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->delete_fiscal_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_year_id** | **str**|  | 
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

# **get_fiscal_year**
> FiscalYearDtoEnvelope get_fiscal_year(tenant_id, fiscal_authority_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal year by ID for an authority

Retrieves a specific fiscal year by its unique identifier within a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_year_dto_envelope import FiscalYearDtoEnvelope
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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal year by ID for an authority
        api_response = api_instance.get_fiscal_year(tenant_id, fiscal_authority_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthorityYearsApi->get_fiscal_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->get_fiscal_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_year_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalYearDtoEnvelope**](FiscalYearDtoEnvelope.md)

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

# **get_fiscal_years**
> FiscalYearDtoListEnvelope get_fiscal_years(tenant_id, fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal years for an authority

Retrieves all fiscal years associated with the specified fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_year_dto_list_envelope import FiscalYearDtoListEnvelope
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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal years for an authority
        api_response = api_instance.get_fiscal_years(tenant_id, fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthorityYearsApi->get_fiscal_years:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->get_fiscal_years: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalYearDtoListEnvelope**](FiscalYearDtoListEnvelope.md)

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

# **get_fiscal_years_count**
> Int32Envelope get_fiscal_years_count(tenant_id, fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal years count for an authority

Returns the total count of fiscal years for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal years count for an authority
        api_response = api_instance.get_fiscal_years_count(tenant_id, fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalAuthorityYearsApi->get_fiscal_years_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->get_fiscal_years_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
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

# **update_fiscal_year**
> EmptyEnvelope update_fiscal_year(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_update_dto=fiscal_year_update_dto)

Update a fiscal year

Updates an existing fiscal year identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_year_update_dto import FiscalYearUpdateDto
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
    api_instance = openapi_client.FiscalAuthorityYearsApi(api_client)
    tenant_id = None # object | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_year_update_dto = openapi_client.FiscalYearUpdateDto() # FiscalYearUpdateDto |  (optional)

    try:
        # Update a fiscal year
        api_response = api_instance.update_fiscal_year(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_update_dto=fiscal_year_update_dto)
        print("The response of FiscalAuthorityYearsApi->update_fiscal_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalAuthorityYearsApi->update_fiscal_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_year_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_year_update_dto** | [**FiscalYearUpdateDto**](FiscalYearUpdateDto.md)|  | [optional] 

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

