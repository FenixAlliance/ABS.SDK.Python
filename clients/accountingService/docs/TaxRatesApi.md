# openapi_client.TaxRatesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_rate**](TaxRatesApi.md#create_tax_rate) | **POST** /api/v2/AccountingService/TaxRates | Create a tax rate
[**delete_tax_rate**](TaxRatesApi.md#delete_tax_rate) | **DELETE** /api/v2/AccountingService/TaxRates/{id} | Delete a tax rate
[**get_tax_rate**](TaxRatesApi.md#get_tax_rate) | **GET** /api/v2/AccountingService/TaxRates/{id} | Get tax rate by ID
[**get_tax_rates**](TaxRatesApi.md#get_tax_rates) | **GET** /api/v2/AccountingService/TaxRates | Get all tax rates for a tenant
[**get_tax_rates_count**](TaxRatesApi.md#get_tax_rates_count) | **GET** /api/v2/AccountingService/TaxRates/Count | Get tax rates count
[**update_tax_rate**](TaxRatesApi.md#update_tax_rate) | **PUT** /api/v2/AccountingService/TaxRates/{id} | Update a tax rate


# **create_tax_rate**
> EmptyEnvelope create_tax_rate(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_rate_create_dto=tax_rate_create_dto)

Create a tax rate

Creates a new tax rate for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_rate_create_dto import TaxRateCreateDto
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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_rate_create_dto = openapi_client.TaxRateCreateDto() # TaxRateCreateDto |  (optional)

    try:
        # Create a tax rate
        api_response = api_instance.create_tax_rate(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_rate_create_dto=tax_rate_create_dto)
        print("The response of TaxRatesApi->create_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->create_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_rate_create_dto** | [**TaxRateCreateDto**](TaxRateCreateDto.md)|  | [optional] 

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

# **delete_tax_rate**
> EmptyEnvelope delete_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete a tax rate

Deletes a tax rate identified by its unique identifier.

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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tax rate
        api_response = api_instance.delete_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxRatesApi->delete_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->delete_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
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

# **get_tax_rate**
> TaxRateDtoEnvelope get_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get tax rate by ID

Retrieves a specific tax rate by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.tax_rate_dto_envelope import TaxRateDtoEnvelope
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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax rate by ID
        api_response = api_instance.get_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxRatesApi->get_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->get_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxRateDtoEnvelope**](TaxRateDtoEnvelope.md)

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

# **get_tax_rates**
> TaxRateDtoListEnvelope get_tax_rates(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all tax rates for a tenant

Retrieves all tax rates for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.tax_rate_dto_list_envelope import TaxRateDtoListEnvelope
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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all tax rates for a tenant
        api_response = api_instance.get_tax_rates(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxRatesApi->get_tax_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->get_tax_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxRateDtoListEnvelope**](TaxRateDtoListEnvelope.md)

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

# **get_tax_rates_count**
> Int32Envelope get_tax_rates_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get tax rates count

Returns the count of tax rates for the specified tenant.

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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax rates count
        api_response = api_instance.get_tax_rates_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxRatesApi->get_tax_rates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->get_tax_rates_count: %s\n" % e)
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

# **update_tax_rate**
> EmptyEnvelope update_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_rate_update_dto=tax_rate_update_dto)

Update a tax rate

Updates an existing tax rate identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_rate_update_dto import TaxRateUpdateDto
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
    api_instance = openapi_client.TaxRatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_rate_update_dto = openapi_client.TaxRateUpdateDto() # TaxRateUpdateDto |  (optional)

    try:
        # Update a tax rate
        api_response = api_instance.update_tax_rate(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_rate_update_dto=tax_rate_update_dto)
        print("The response of TaxRatesApi->update_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->update_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_rate_update_dto** | [**TaxRateUpdateDto**](TaxRateUpdateDto.md)|  | [optional] 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

