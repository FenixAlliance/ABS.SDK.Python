# openapi_client.PayrollPeriodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payroll_period_async**](PayrollPeriodsApi.md#create_payroll_period_async) | **POST** /api/v2/HrmsService/PayrollPeriods | Create a payroll period
[**delete_payroll_period_async**](PayrollPeriodsApi.md#delete_payroll_period_async) | **DELETE** /api/v2/HrmsService/PayrollPeriods/{periodId} | Delete a payroll period
[**get_payroll_period_by_id_async**](PayrollPeriodsApi.md#get_payroll_period_by_id_async) | **GET** /api/v2/HrmsService/PayrollPeriods/{periodId} | Get payroll period by ID
[**get_payroll_periods_async**](PayrollPeriodsApi.md#get_payroll_periods_async) | **GET** /api/v2/HrmsService/PayrollPeriods | Get payroll periods
[**get_payroll_periods_count_async**](PayrollPeriodsApi.md#get_payroll_periods_count_async) | **GET** /api/v2/HrmsService/PayrollPeriods/Count | Count payroll periods
[**update_payroll_period_async**](PayrollPeriodsApi.md#update_payroll_period_async) | **PUT** /api/v2/HrmsService/PayrollPeriods/{periodId} | Update a payroll period


# **create_payroll_period_async**
> EmptyEnvelope create_payroll_period_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payroll_period_create_dto=payroll_period_create_dto)

Create a payroll period

Creates a new payroll period for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payroll_period_create_dto import PayrollPeriodCreateDto
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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payroll_period_create_dto = openapi_client.PayrollPeriodCreateDto() # PayrollPeriodCreateDto |  (optional)

    try:
        # Create a payroll period
        api_response = api_instance.create_payroll_period_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payroll_period_create_dto=payroll_period_create_dto)
        print("The response of PayrollPeriodsApi->create_payroll_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->create_payroll_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payroll_period_create_dto** | [**PayrollPeriodCreateDto**](PayrollPeriodCreateDto.md)|  | [optional] 

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

# **delete_payroll_period_async**
> EmptyEnvelope delete_payroll_period_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version)

Delete a payroll period

Deletes a payroll period for the specified tenant.

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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    period_id = 'period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a payroll period
        api_response = api_instance.delete_payroll_period_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollPeriodsApi->delete_payroll_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->delete_payroll_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **period_id** | **str**|  | 
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

# **get_payroll_period_by_id_async**
> PayrollPeriodDtoEnvelope get_payroll_period_by_id_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version)

Get payroll period by ID

Retrieves a specific payroll period by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.payroll_period_dto_envelope import PayrollPeriodDtoEnvelope
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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    period_id = 'period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get payroll period by ID
        api_response = api_instance.get_payroll_period_by_id_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollPeriodsApi->get_payroll_period_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->get_payroll_period_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PayrollPeriodDtoEnvelope**](PayrollPeriodDtoEnvelope.md)

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

# **get_payroll_periods_async**
> PayrollPeriodDtoListEnvelope get_payroll_periods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get payroll periods

Retrieves payroll periods for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.payroll_period_dto_list_envelope import PayrollPeriodDtoListEnvelope
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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get payroll periods
        api_response = api_instance.get_payroll_periods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollPeriodsApi->get_payroll_periods_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->get_payroll_periods_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PayrollPeriodDtoListEnvelope**](PayrollPeriodDtoListEnvelope.md)

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

# **get_payroll_periods_count_async**
> Int32Envelope get_payroll_periods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count payroll periods

Counts payroll periods for the specified tenant.

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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count payroll periods
        api_response = api_instance.get_payroll_periods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollPeriodsApi->get_payroll_periods_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->get_payroll_periods_count_async: %s\n" % e)
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

# **update_payroll_period_async**
> EmptyEnvelope update_payroll_period_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version, payroll_period_update_dto=payroll_period_update_dto)

Update a payroll period

Updates an existing payroll period for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payroll_period_update_dto import PayrollPeriodUpdateDto
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
    api_instance = openapi_client.PayrollPeriodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    period_id = 'period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payroll_period_update_dto = openapi_client.PayrollPeriodUpdateDto() # PayrollPeriodUpdateDto |  (optional)

    try:
        # Update a payroll period
        api_response = api_instance.update_payroll_period_async(tenant_id, period_id, api_version=api_version, x_api_version=x_api_version, payroll_period_update_dto=payroll_period_update_dto)
        print("The response of PayrollPeriodsApi->update_payroll_period_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollPeriodsApi->update_payroll_period_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payroll_period_update_dto** | [**PayrollPeriodUpdateDto**](PayrollPeriodUpdateDto.md)|  | [optional] 

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

