# openapi_client.FiscalYearsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_year_async**](FiscalYearsApi.md#create_fiscal_year_async) | **POST** /api/v2/AccountingService/FiscalYears | Create fiscal year
[**delete_fiscal_year_async**](FiscalYearsApi.md#delete_fiscal_year_async) | **DELETE** /api/v2/AccountingService/FiscalYears/{fiscalYearId} | Delete fiscal year
[**get_fiscal_year_details_async**](FiscalYearsApi.md#get_fiscal_year_details_async) | **GET** /api/v2/AccountingService/FiscalYears/{fiscalYearId} | Get fiscal year by ID
[**get_fiscal_years_async**](FiscalYearsApi.md#get_fiscal_years_async) | **GET** /api/v2/AccountingService/FiscalYears | Get all fiscal years
[**get_fiscal_years_count_async**](FiscalYearsApi.md#get_fiscal_years_count_async) | **GET** /api/v2/AccountingService/FiscalYears/Count | Count fiscal years
[**update_fiscal_year_async**](FiscalYearsApi.md#update_fiscal_year_async) | **PUT** /api/v2/AccountingService/FiscalYears/{fiscalYearId} | Update fiscal year


# **create_fiscal_year_async**
> EmptyEnvelope create_fiscal_year_async(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_create_dto=fiscal_year_create_dto)

Create fiscal year

Creates a new fiscal year entry for a tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_year_create_dto import FiscalYearCreateDto
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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_year_create_dto = openapi_client.FiscalYearCreateDto() # FiscalYearCreateDto |  (optional)

    try:
        # Create fiscal year
        api_response = api_instance.create_fiscal_year_async(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_create_dto=fiscal_year_create_dto)
        print("The response of FiscalYearsApi->create_fiscal_year_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->create_fiscal_year_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fiscal_year_async**
> EmptyEnvelope delete_fiscal_year_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)

Delete fiscal year

Deletes a fiscal year identified by its ID.

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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete fiscal year
        api_response = api_instance.delete_fiscal_year_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalYearsApi->delete_fiscal_year_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->delete_fiscal_year_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_year_details_async**
> FiscalYearDtoEnvelope get_fiscal_year_details_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal year by ID

Gets details for a specific fiscal year.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_year_dto_envelope import FiscalYearDtoEnvelope
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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal year by ID
        api_response = api_instance.get_fiscal_year_details_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalYearsApi->get_fiscal_year_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->get_fiscal_year_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_years_async**
> FiscalYearDtoIReadOnlyListEnvelope get_fiscal_years_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all fiscal years

Retrieves a list of fiscal years for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_year_dto_i_read_only_list_envelope import FiscalYearDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all fiscal years
        api_response = api_instance.get_fiscal_years_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalYearsApi->get_fiscal_years_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->get_fiscal_years_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalYearDtoIReadOnlyListEnvelope**](FiscalYearDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_years_count_async**
> Int32Envelope get_fiscal_years_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count fiscal years

Returns the number of fiscal years for a tenant.

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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count fiscal years
        api_response = api_instance.get_fiscal_years_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalYearsApi->get_fiscal_years_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->get_fiscal_years_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fiscal_year_async**
> EmptyEnvelope update_fiscal_year_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_update_dto=fiscal_year_update_dto)

Update fiscal year

Updates an existing fiscal year identified by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_year_update_dto import FiscalYearUpdateDto
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
    api_instance = openapi_client.FiscalYearsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    fiscal_year_id = 'fiscal_year_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_year_update_dto = openapi_client.FiscalYearUpdateDto() # FiscalYearUpdateDto |  (optional)

    try:
        # Update fiscal year
        api_response = api_instance.update_fiscal_year_async(tenant_id, fiscal_year_id, api_version=api_version, x_api_version=x_api_version, fiscal_year_update_dto=fiscal_year_update_dto)
        print("The response of FiscalYearsApi->update_fiscal_year_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalYearsApi->update_fiscal_year_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

