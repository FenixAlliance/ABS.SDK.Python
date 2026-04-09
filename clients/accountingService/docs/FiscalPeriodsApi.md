# openapi_client.FiscalPeriodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_period**](FiscalPeriodsApi.md#create_fiscal_period) | **POST** /api/v2/AccountingService/Fiscals/Authorities/FiscalPeriods | Create a fiscal period
[**delete_fiscal_period**](FiscalPeriodsApi.md#delete_fiscal_period) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/FiscalPeriods/{fiscalPeriodId} | Delete a fiscal period
[**get_fiscal_period**](FiscalPeriodsApi.md#get_fiscal_period) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalYears/{fiscalYearId}/FiscalPeriods/{fiscalPeriodId} | Get fiscal period by ID
[**get_fiscal_periods**](FiscalPeriodsApi.md#get_fiscal_periods) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/FiscalYears/{fiscalYearId}/FiscalPeriods | Get fiscal periods for a fiscal year
[**get_fiscal_periods_count**](FiscalPeriodsApi.md#get_fiscal_periods_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalYears/{fiscalYearId}/FiscalPeriods/Count | Get fiscal periods count
[**update_fiscal_period**](FiscalPeriodsApi.md#update_fiscal_period) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/FiscalPeriods/{fiscalPeriodId} | Update a fiscal period


# **create_fiscal_period**
> EmptyEnvelope create_fiscal_period(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_period_create_dto=fiscal_period_create_dto)

Create a fiscal period

Creates a new fiscal period associated with a fiscal year.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_period_create_dto import FiscalPeriodCreateDto
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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_period_create_dto = openapi_client.FiscalPeriodCreateDto() # FiscalPeriodCreateDto |  (optional)

    try:
        # Create a fiscal period
        api_response = api_instance.create_fiscal_period(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_period_create_dto=fiscal_period_create_dto)
        print("The response of FiscalPeriodsApi->create_fiscal_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->create_fiscal_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_period_create_dto** | [**FiscalPeriodCreateDto**](FiscalPeriodCreateDto.md)|  | [optional] 

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

# **delete_fiscal_period**
> EmptyEnvelope delete_fiscal_period(tenant_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal period

Deletes a fiscal period identified by its unique identifier.

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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    fiscal_period_id = 'fiscal_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal period
        api_response = api_instance.delete_fiscal_period(tenant_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalPeriodsApi->delete_fiscal_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->delete_fiscal_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_period_id** | **str**|  | 
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

# **get_fiscal_period**
> FiscalPeriodDtoEnvelope get_fiscal_period(tenant_id, fiscal_authority_id, fiscal_year_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal period by ID

Retrieves a specific fiscal period by its unique identifier within a fiscal year.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_period_dto_envelope import FiscalPeriodDtoEnvelope
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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    fiscal_period_id = 'fiscal_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal period by ID
        api_response = api_instance.get_fiscal_period(tenant_id, fiscal_authority_id, fiscal_year_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalPeriodsApi->get_fiscal_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->get_fiscal_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_year_id** | **str**|  | 
 **fiscal_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalPeriodDtoEnvelope**](FiscalPeriodDtoEnvelope.md)

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

# **get_fiscal_periods**
> FiscalPeriodDtoListEnvelope get_fiscal_periods(tenant_id, fiscal_authority_id, fiscal_year_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal periods for a fiscal year

Retrieves all fiscal periods for the specified fiscal year within a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_period_dto_list_envelope import FiscalPeriodDtoListEnvelope
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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal periods for a fiscal year
        api_response = api_instance.get_fiscal_periods(tenant_id, fiscal_authority_id, fiscal_year_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalPeriodsApi->get_fiscal_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->get_fiscal_periods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_year_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalPeriodDtoListEnvelope**](FiscalPeriodDtoListEnvelope.md)

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

# **get_fiscal_periods_count**
> Int32Envelope get_fiscal_periods_count(tenant_id, fiscal_authority_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal periods count

Returns the total count of fiscal periods for the specified fiscal year.

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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal periods count
        api_response = api_instance.get_fiscal_periods_count(tenant_id, fiscal_authority_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalPeriodsApi->get_fiscal_periods_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->get_fiscal_periods_count: %s\n" % e)
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

# **update_fiscal_period**
> EmptyEnvelope update_fiscal_period(tenant_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version, fiscal_period_update_dto=fiscal_period_update_dto)

Update a fiscal period

Updates an existing fiscal period identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_period_update_dto import FiscalPeriodUpdateDto
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
    api_instance = openapi_client.FiscalPeriodsApi(api_client)
    tenant_id = None # object | 
    fiscal_period_id = 'fiscal_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_period_update_dto = openapi_client.FiscalPeriodUpdateDto() # FiscalPeriodUpdateDto |  (optional)

    try:
        # Update a fiscal period
        api_response = api_instance.update_fiscal_period(tenant_id, fiscal_period_id, api_version=api_version, x_api_version=x_api_version, fiscal_period_update_dto=fiscal_period_update_dto)
        print("The response of FiscalPeriodsApi->update_fiscal_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalPeriodsApi->update_fiscal_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_period_update_dto** | [**FiscalPeriodUpdateDto**](FiscalPeriodUpdateDto.md)|  | [optional] 

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

