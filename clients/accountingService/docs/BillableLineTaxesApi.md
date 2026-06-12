# openapi_client.BillableLineTaxesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billable_line_tax**](BillableLineTaxesApi.md#create_billable_line_tax) | **POST** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes | Create a new tax for a billable line.
[**delete_billable_line_tax**](BillableLineTaxesApi.md#delete_billable_line_tax) | **DELETE** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes/{taxId} | Delete a tax from a billable line.
[**get_billable_line_taxes**](BillableLineTaxesApi.md#get_billable_line_taxes) | **GET** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes | Get taxes for a billable line.
[**get_billable_line_taxes_count**](BillableLineTaxesApi.md#get_billable_line_taxes_count) | **GET** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes/Count | Get the count of taxes for a billable line.
[**patch_billable_line_tax_async**](BillableLineTaxesApi.md#patch_billable_line_tax_async) | **PATCH** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes/{taxId} | Patch a billable line tax
[**update_billable_line_tax**](BillableLineTaxesApi.md#update_billable_line_tax) | **PUT** /api/v2/AccountingService/BillableLines/{billableLineId}/Taxes/{taxId} | Update a tax for a billable line.


# **create_billable_line_tax**
> EmptyEnvelope create_billable_line_tax(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version, applied_item_tax_record_create_dto=applied_item_tax_record_create_dto)

Create a new tax for a billable line.

Creates a new tax entry for the specified billable line.

### Example


```python
import openapi_client
from openapi_client.models.applied_item_tax_record_create_dto import AppliedItemTaxRecordCreateDto
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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    applied_item_tax_record_create_dto = openapi_client.AppliedItemTaxRecordCreateDto() # AppliedItemTaxRecordCreateDto |  (optional)

    try:
        # Create a new tax for a billable line.
        api_response = api_instance.create_billable_line_tax(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version, applied_item_tax_record_create_dto=applied_item_tax_record_create_dto)
        print("The response of BillableLineTaxesApi->create_billable_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->create_billable_line_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **applied_item_tax_record_create_dto** | [**AppliedItemTaxRecordCreateDto**](AppliedItemTaxRecordCreateDto.md)|  | [optional] 

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

# **delete_billable_line_tax**
> EmptyEnvelope delete_billable_line_tax(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version)

Delete a tax from a billable line.

Deletes the specified tax entry from the billable line.

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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    tax_id = 'tax_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tax from a billable line.
        api_response = api_instance.delete_billable_line_tax(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillableLineTaxesApi->delete_billable_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->delete_billable_line_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
 **tax_id** | **str**|  | 
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

# **get_billable_line_taxes**
> AppliedItemTaxRecordDtoIReadOnlyListEnvelope get_billable_line_taxes(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version)

Get taxes for a billable line.

Retrieves the taxes applied to the specified billable line.

### Example


```python
import openapi_client
from openapi_client.models.applied_item_tax_record_dto_i_read_only_list_envelope import AppliedItemTaxRecordDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get taxes for a billable line.
        api_response = api_instance.get_billable_line_taxes(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillableLineTaxesApi->get_billable_line_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->get_billable_line_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppliedItemTaxRecordDtoIReadOnlyListEnvelope**](AppliedItemTaxRecordDtoIReadOnlyListEnvelope.md)

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

# **get_billable_line_taxes_count**
> Int32Envelope get_billable_line_taxes_count(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version)

Get the count of taxes for a billable line.

Retrieves the total count of taxes applied to the specified billable line.

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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of taxes for a billable line.
        api_response = api_instance.get_billable_line_taxes_count(tenant_id, billable_line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillableLineTaxesApi->get_billable_line_taxes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->get_billable_line_taxes_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
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

# **patch_billable_line_tax_async**
> EmptyEnvelope patch_billable_line_tax_async(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a billable line tax

Partially updates a billable line tax.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    tax_id = 'tax_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a billable line tax
        api_response = api_instance.patch_billable_line_tax_async(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of BillableLineTaxesApi->patch_billable_line_tax_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->patch_billable_line_tax_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
 **tax_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **update_billable_line_tax**
> EmptyEnvelope update_billable_line_tax(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version, applied_item_tax_record_update_dto=applied_item_tax_record_update_dto)

Update a tax for a billable line.

Updates the specified tax entry for the billable line.

### Example


```python
import openapi_client
from openapi_client.models.applied_item_tax_record_update_dto import AppliedItemTaxRecordUpdateDto
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
    api_instance = openapi_client.BillableLineTaxesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billable_line_id = 'billable_line_id_example' # str | 
    tax_id = 'tax_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    applied_item_tax_record_update_dto = openapi_client.AppliedItemTaxRecordUpdateDto() # AppliedItemTaxRecordUpdateDto |  (optional)

    try:
        # Update a tax for a billable line.
        api_response = api_instance.update_billable_line_tax(tenant_id, billable_line_id, tax_id, api_version=api_version, x_api_version=x_api_version, applied_item_tax_record_update_dto=applied_item_tax_record_update_dto)
        print("The response of BillableLineTaxesApi->update_billable_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableLineTaxesApi->update_billable_line_tax: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billable_line_id** | **str**|  | 
 **tax_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **applied_item_tax_record_update_dto** | [**AppliedItemTaxRecordUpdateDto**](AppliedItemTaxRecordUpdateDto.md)|  | [optional] 

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

