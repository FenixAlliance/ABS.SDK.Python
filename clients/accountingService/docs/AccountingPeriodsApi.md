# openapi_client.AccountingPeriodsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_accounting_period**](AccountingPeriodsApi.md#create_accounting_period) | **POST** /api/v2/AccountingService/AccountingPeriods | Creates a new accounting period
[**delete_accounting_period**](AccountingPeriodsApi.md#delete_accounting_period) | **DELETE** /api/v2/AccountingService/AccountingPeriods/{accountingPeriodId} | Deletes an existing accounting period
[**get_accounting_period**](AccountingPeriodsApi.md#get_accounting_period) | **GET** /api/v2/AccountingService/AccountingPeriods/{accountingPeriodId} | Gets the current tenant accounting period
[**get_accounting_periods**](AccountingPeriodsApi.md#get_accounting_periods) | **GET** /api/v2/AccountingService/AccountingPeriods | Get all accounting periods for a tenant
[**get_accounting_periods_count_async**](AccountingPeriodsApi.md#get_accounting_periods_count_async) | **GET** /api/v2/AccountingService/AccountingPeriods/Count | Gets the current tenant accounting periods count
[**update_accounting_period**](AccountingPeriodsApi.md#update_accounting_period) | **PUT** /api/v2/AccountingService/AccountingPeriods/{accountingPeriodId} | Updates an existing accounting period


# **create_accounting_period**
> EmptyEnvelope create_accounting_period(tenant_id, api_version=api_version, x_api_version=x_api_version, accounting_period_create_dto=accounting_period_create_dto)

Creates a new accounting period

Creates a new accounting period.

### Example


```python
import openapi_client
from openapi_client.models.accounting_period_create_dto import AccountingPeriodCreateDto
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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_period_create_dto = openapi_client.AccountingPeriodCreateDto() # AccountingPeriodCreateDto |  (optional)

    try:
        # Creates a new accounting period
        api_response = api_instance.create_accounting_period(tenant_id, api_version=api_version, x_api_version=x_api_version, accounting_period_create_dto=accounting_period_create_dto)
        print("The response of AccountingPeriodsApi->create_accounting_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->create_accounting_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_period_create_dto** | [**AccountingPeriodCreateDto**](AccountingPeriodCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounting_period**
> EmptyEnvelope delete_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing accounting period

Deletes an existing accounting period.

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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    accounting_period_id = 'accounting_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing accounting period
        api_response = api_instance.delete_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountingPeriodsApi->delete_accounting_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->delete_accounting_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **accounting_period_id** | **str**|  | 
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

# **get_accounting_period**
> AccountingPeriodDtoEnvelope get_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant accounting period

Get the currently acting tenant accounting period.

### Example


```python
import openapi_client
from openapi_client.models.accounting_period_dto_envelope import AccountingPeriodDtoEnvelope
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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    accounting_period_id = 'accounting_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant accounting period
        api_response = api_instance.get_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountingPeriodsApi->get_accounting_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->get_accounting_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **accounting_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingPeriodDtoEnvelope**](AccountingPeriodDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_periods**
> AccountingPeriodDtoListEnvelope get_accounting_periods(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all accounting periods for a tenant

Retrieves all accounting periods for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.accounting_period_dto_list_envelope import AccountingPeriodDtoListEnvelope
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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all accounting periods for a tenant
        api_response = api_instance.get_accounting_periods(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountingPeriodsApi->get_accounting_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->get_accounting_periods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingPeriodDtoListEnvelope**](AccountingPeriodDtoListEnvelope.md)

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

# **get_accounting_periods_count_async**
> Int32Envelope get_accounting_periods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant accounting periods count

Get the currently acting tenant accounting periods count.

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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant accounting periods count
        api_response = api_instance.get_accounting_periods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountingPeriodsApi->get_accounting_periods_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->get_accounting_periods_count_async: %s\n" % e)
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

# **update_accounting_period**
> EmptyEnvelope update_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version, accounting_period_update_dto=accounting_period_update_dto)

Updates an existing accounting period

Updates an existing accounting period.

### Example


```python
import openapi_client
from openapi_client.models.accounting_period_update_dto import AccountingPeriodUpdateDto
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
    api_instance = openapi_client.AccountingPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    accounting_period_id = 'accounting_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_period_update_dto = openapi_client.AccountingPeriodUpdateDto() # AccountingPeriodUpdateDto |  (optional)

    try:
        # Updates an existing accounting period
        api_response = api_instance.update_accounting_period(tenant_id, accounting_period_id, api_version=api_version, x_api_version=x_api_version, accounting_period_update_dto=accounting_period_update_dto)
        print("The response of AccountingPeriodsApi->update_accounting_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPeriodsApi->update_accounting_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **accounting_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_period_update_dto** | [**AccountingPeriodUpdateDto**](AccountingPeriodUpdateDto.md)|  | [optional] 

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

