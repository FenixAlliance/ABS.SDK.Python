# openapi_client.InvoiceEnumerationRangesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice_enumeration_range_async**](InvoiceEnumerationRangesApi.md#create_invoice_enumeration_range_async) | **POST** /api/v2/AccountingService/InvoiceEnumerationRanges | Create a new invoice enumeration range
[**delete_invoice_enumeration_range_async**](InvoiceEnumerationRangesApi.md#delete_invoice_enumeration_range_async) | **DELETE** /api/v2/AccountingService/InvoiceEnumerationRanges/{rangeId} | Delete an invoice enumeration range
[**get_invoice_enumeration_range_details_async**](InvoiceEnumerationRangesApi.md#get_invoice_enumeration_range_details_async) | **GET** /api/v2/AccountingService/InvoiceEnumerationRanges/{rangeId} | Get invoice enumeration range by ID
[**get_invoice_enumeration_ranges_async**](InvoiceEnumerationRangesApi.md#get_invoice_enumeration_ranges_async) | **GET** /api/v2/AccountingService/InvoiceEnumerationRanges | Get all invoice enumeration ranges
[**update_invoice_enumeration_range_async**](InvoiceEnumerationRangesApi.md#update_invoice_enumeration_range_async) | **PUT** /api/v2/AccountingService/InvoiceEnumerationRanges/{rangeId} | Update an invoice enumeration range


# **create_invoice_enumeration_range_async**
> EmptyEnvelope create_invoice_enumeration_range_async(tenant_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_create_dto=invoice_enumeration_range_create_dto)

Create a new invoice enumeration range

Creates a new invoice enumeration range for the tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_enumeration_range_create_dto import InvoiceEnumerationRangeCreateDto
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
    api_instance = openapi_client.InvoiceEnumerationRangesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    invoice_enumeration_range_create_dto = openapi_client.InvoiceEnumerationRangeCreateDto() # InvoiceEnumerationRangeCreateDto |  (optional)

    try:
        # Create a new invoice enumeration range
        api_response = api_instance.create_invoice_enumeration_range_async(tenant_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_create_dto=invoice_enumeration_range_create_dto)
        print("The response of InvoiceEnumerationRangesApi->create_invoice_enumeration_range_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEnumerationRangesApi->create_invoice_enumeration_range_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **invoice_enumeration_range_create_dto** | [**InvoiceEnumerationRangeCreateDto**](InvoiceEnumerationRangeCreateDto.md)|  | [optional] 

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

# **delete_invoice_enumeration_range_async**
> EmptyEnvelope delete_invoice_enumeration_range_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version)

Delete an invoice enumeration range

Deletes an invoice enumeration range by its identifier.

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
    api_instance = openapi_client.InvoiceEnumerationRangesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    range_id = 'range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an invoice enumeration range
        api_response = api_instance.delete_invoice_enumeration_range_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvoiceEnumerationRangesApi->delete_invoice_enumeration_range_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEnumerationRangesApi->delete_invoice_enumeration_range_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **range_id** | **str**|  | 
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

# **get_invoice_enumeration_range_details_async**
> InvoiceEnumerationRangeDtoEnvelope get_invoice_enumeration_range_details_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version)

Get invoice enumeration range by ID

Retrieves the details of a specific invoice enumeration range.

### Example


```python
import openapi_client
from openapi_client.models.invoice_enumeration_range_dto_envelope import InvoiceEnumerationRangeDtoEnvelope
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
    api_instance = openapi_client.InvoiceEnumerationRangesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    range_id = 'range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get invoice enumeration range by ID
        api_response = api_instance.get_invoice_enumeration_range_details_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvoiceEnumerationRangesApi->get_invoice_enumeration_range_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEnumerationRangesApi->get_invoice_enumeration_range_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **range_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InvoiceEnumerationRangeDtoEnvelope**](InvoiceEnumerationRangeDtoEnvelope.md)

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

# **get_invoice_enumeration_ranges_async**
> InvoiceEnumerationRangeDtoListEnvelope get_invoice_enumeration_ranges_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all invoice enumeration ranges

Retrieves all invoice enumeration ranges for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.invoice_enumeration_range_dto_list_envelope import InvoiceEnumerationRangeDtoListEnvelope
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
    api_instance = openapi_client.InvoiceEnumerationRangesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all invoice enumeration ranges
        api_response = api_instance.get_invoice_enumeration_ranges_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InvoiceEnumerationRangesApi->get_invoice_enumeration_ranges_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEnumerationRangesApi->get_invoice_enumeration_ranges_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InvoiceEnumerationRangeDtoListEnvelope**](InvoiceEnumerationRangeDtoListEnvelope.md)

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

# **update_invoice_enumeration_range_async**
> EmptyEnvelope update_invoice_enumeration_range_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_update_dto=invoice_enumeration_range_update_dto)

Update an invoice enumeration range

Updates an existing invoice enumeration range with the provided data.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_enumeration_range_update_dto import InvoiceEnumerationRangeUpdateDto
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
    api_instance = openapi_client.InvoiceEnumerationRangesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    range_id = 'range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    invoice_enumeration_range_update_dto = openapi_client.InvoiceEnumerationRangeUpdateDto() # InvoiceEnumerationRangeUpdateDto |  (optional)

    try:
        # Update an invoice enumeration range
        api_response = api_instance.update_invoice_enumeration_range_async(tenant_id, range_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_update_dto=invoice_enumeration_range_update_dto)
        print("The response of InvoiceEnumerationRangesApi->update_invoice_enumeration_range_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEnumerationRangesApi->update_invoice_enumeration_range_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **range_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **invoice_enumeration_range_update_dto** | [**InvoiceEnumerationRangeUpdateDto**](InvoiceEnumerationRangeUpdateDto.md)|  | [optional] 

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

