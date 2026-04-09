# openapi_client.FiscalEnumerationRangesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice_enumeration_range**](FiscalEnumerationRangesApi.md#create_invoice_enumeration_range) | **POST** /api/v2/AccountingService/Fiscals/Authorities/EnumerationRanges | Create an invoice enumeration range
[**delete_invoice_enumeration_range**](FiscalEnumerationRangesApi.md#delete_invoice_enumeration_range) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/EnumerationRanges/{enumerationRangeId} | Delete an invoice enumeration range
[**get_invoice_enumeration_range**](FiscalEnumerationRangesApi.md#get_invoice_enumeration_range) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/EnumerationRanges/{enumerationRangeId} | Get invoice enumeration range by ID
[**get_invoice_enumeration_ranges**](FiscalEnumerationRangesApi.md#get_invoice_enumeration_ranges) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/EnumerationRanges | Get invoice enumeration ranges for an authority
[**get_invoice_enumeration_ranges_count**](FiscalEnumerationRangesApi.md#get_invoice_enumeration_ranges_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/EnumerationRanges/Count | Get invoice enumeration ranges count
[**update_invoice_enumeration_range**](FiscalEnumerationRangesApi.md#update_invoice_enumeration_range) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/EnumerationRanges/{enumerationRangeId} | Update an invoice enumeration range


# **create_invoice_enumeration_range**
> EmptyEnvelope create_invoice_enumeration_range(tenant_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_create_dto=invoice_enumeration_range_create_dto)

Create an invoice enumeration range

Creates a new invoice enumeration range for a fiscal authority.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    invoice_enumeration_range_create_dto = openapi_client.InvoiceEnumerationRangeCreateDto() # InvoiceEnumerationRangeCreateDto |  (optional)

    try:
        # Create an invoice enumeration range
        api_response = api_instance.create_invoice_enumeration_range(tenant_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_create_dto=invoice_enumeration_range_create_dto)
        print("The response of FiscalEnumerationRangesApi->create_invoice_enumeration_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->create_invoice_enumeration_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_enumeration_range**
> EmptyEnvelope delete_invoice_enumeration_range(tenant_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version)

Delete an invoice enumeration range

Deletes an invoice enumeration range identified by its unique identifier.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    tenant_id = None # object | 
    enumeration_range_id = 'enumeration_range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an invoice enumeration range
        api_response = api_instance.delete_invoice_enumeration_range(tenant_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalEnumerationRangesApi->delete_invoice_enumeration_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->delete_invoice_enumeration_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **enumeration_range_id** | **str**|  | 
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

# **get_invoice_enumeration_range**
> InvoiceEnumerationRangeDtoEnvelope get_invoice_enumeration_range(tenant_id, fiscal_authority_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version)

Get invoice enumeration range by ID

Retrieves a specific invoice enumeration range by its unique identifier.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    enumeration_range_id = 'enumeration_range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get invoice enumeration range by ID
        api_response = api_instance.get_invoice_enumeration_range(tenant_id, fiscal_authority_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalEnumerationRangesApi->get_invoice_enumeration_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->get_invoice_enumeration_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **enumeration_range_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_enumeration_ranges**
> InvoiceEnumerationRangeDtoListEnvelope get_invoice_enumeration_ranges(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get invoice enumeration ranges for an authority

Retrieves all invoice enumeration ranges for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get invoice enumeration ranges for an authority
        api_response = api_instance.get_invoice_enumeration_ranges(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalEnumerationRangesApi->get_invoice_enumeration_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->get_invoice_enumeration_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiscal_authority_id** | **str**|  | 
 **authority_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_enumeration_ranges_count**
> Int32Envelope get_invoice_enumeration_ranges_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)

Get invoice enumeration ranges count

Returns the total count of invoice enumeration ranges for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get invoice enumeration ranges count
        api_response = api_instance.get_invoice_enumeration_ranges_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalEnumerationRangesApi->get_invoice_enumeration_ranges_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->get_invoice_enumeration_ranges_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_invoice_enumeration_range**
> EmptyEnvelope update_invoice_enumeration_range(tenant_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_update_dto=invoice_enumeration_range_update_dto)

Update an invoice enumeration range

Updates an existing invoice enumeration range identified by its unique identifier.

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
    api_instance = openapi_client.FiscalEnumerationRangesApi(api_client)
    tenant_id = None # object | 
    enumeration_range_id = 'enumeration_range_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    invoice_enumeration_range_update_dto = openapi_client.InvoiceEnumerationRangeUpdateDto() # InvoiceEnumerationRangeUpdateDto |  (optional)

    try:
        # Update an invoice enumeration range
        api_response = api_instance.update_invoice_enumeration_range(tenant_id, enumeration_range_id, api_version=api_version, x_api_version=x_api_version, invoice_enumeration_range_update_dto=invoice_enumeration_range_update_dto)
        print("The response of FiscalEnumerationRangesApi->update_invoice_enumeration_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalEnumerationRangesApi->update_invoice_enumeration_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **enumeration_range_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

