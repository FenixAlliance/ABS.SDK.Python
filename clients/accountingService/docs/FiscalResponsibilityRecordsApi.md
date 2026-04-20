# openapi_client.FiscalResponsibilityRecordsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_responsibility_record**](FiscalResponsibilityRecordsApi.md#create_fiscal_responsibility_record) | **POST** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilityRecords | Create a fiscal responsibility record
[**delete_fiscal_responsibility_record**](FiscalResponsibilityRecordsApi.md#delete_fiscal_responsibility_record) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilityRecords/{fiscalResponsibilityRecordId} | Delete a fiscal responsibility record
[**get_fiscal_responsibility_record**](FiscalResponsibilityRecordsApi.md#get_fiscal_responsibility_record) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalResponsibilities/{fiscalResponsibilityId}/FiscalResponsibilityRecords/{fiscalResponsibilityRecordId} | Get fiscal responsibility record by ID
[**get_fiscal_responsibility_records**](FiscalResponsibilityRecordsApi.md#get_fiscal_responsibility_records) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalResponsibilities/{fiscalResponsibilityId}/FiscalResponsibilityRecords | Get fiscal responsibility records
[**get_fiscal_responsibility_records_count**](FiscalResponsibilityRecordsApi.md#get_fiscal_responsibility_records_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalResponsibilities/{fiscalResponsibilityId}/FiscalResponsibilityRecords/Count | Get fiscal responsibility records count
[**update_fiscal_responsibility_record**](FiscalResponsibilityRecordsApi.md#update_fiscal_responsibility_record) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilityRecords/{fiscalResponsibilityRecordId} | Update a fiscal responsibility record


# **create_fiscal_responsibility_record**
> EmptyEnvelope create_fiscal_responsibility_record(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_record_create_dto=fiscal_responsibility_record_create_dto)

Create a fiscal responsibility record

Creates a new fiscal responsibility record for a fiscal responsibility.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_responsibility_record_create_dto import FiscalResponsibilityRecordCreateDto
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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_responsibility_record_create_dto = openapi_client.FiscalResponsibilityRecordCreateDto() # FiscalResponsibilityRecordCreateDto |  (optional)

    try:
        # Create a fiscal responsibility record
        api_response = api_instance.create_fiscal_responsibility_record(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_record_create_dto=fiscal_responsibility_record_create_dto)
        print("The response of FiscalResponsibilityRecordsApi->create_fiscal_responsibility_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->create_fiscal_responsibility_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_responsibility_record_create_dto** | [**FiscalResponsibilityRecordCreateDto**](FiscalResponsibilityRecordCreateDto.md)|  | [optional] 

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

# **delete_fiscal_responsibility_record**
> EmptyEnvelope delete_fiscal_responsibility_record(tenant_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal responsibility record

Deletes a fiscal responsibility record identified by its unique identifier.

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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    fiscal_responsibility_record_id = 'fiscal_responsibility_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal responsibility record
        api_response = api_instance.delete_fiscal_responsibility_record(tenant_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilityRecordsApi->delete_fiscal_responsibility_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->delete_fiscal_responsibility_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_responsibility_record_id** | **str**|  | 
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

# **get_fiscal_responsibility_record**
> FiscalResponsibilityRecordDtoEnvelope get_fiscal_responsibility_record(tenant_id, fiscal_authority_id, fiscal_responsibility_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibility record by ID

Retrieves a specific fiscal responsibility record by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_responsibility_record_dto_envelope import FiscalResponsibilityRecordDtoEnvelope
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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    fiscal_responsibility_record_id = 'fiscal_responsibility_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibility record by ID
        api_response = api_instance.get_fiscal_responsibility_record(tenant_id, fiscal_authority_id, fiscal_responsibility_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilityRecordsApi->get_fiscal_responsibility_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->get_fiscal_responsibility_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_responsibility_id** | **str**|  | 
 **fiscal_responsibility_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalResponsibilityRecordDtoEnvelope**](FiscalResponsibilityRecordDtoEnvelope.md)

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

# **get_fiscal_responsibility_records**
> FiscalResponsibilityRecordDtoListEnvelope get_fiscal_responsibility_records(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibility records

Retrieves all fiscal responsibility records for the specified fiscal responsibility.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_responsibility_record_dto_list_envelope import FiscalResponsibilityRecordDtoListEnvelope
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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibility records
        api_response = api_instance.get_fiscal_responsibility_records(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilityRecordsApi->get_fiscal_responsibility_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->get_fiscal_responsibility_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_responsibility_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalResponsibilityRecordDtoListEnvelope**](FiscalResponsibilityRecordDtoListEnvelope.md)

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

# **get_fiscal_responsibility_records_count**
> Int32Envelope get_fiscal_responsibility_records_count(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibility records count

Returns the total count of fiscal responsibility records for the specified fiscal responsibility.

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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibility records count
        api_response = api_instance.get_fiscal_responsibility_records_count(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilityRecordsApi->get_fiscal_responsibility_records_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->get_fiscal_responsibility_records_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_responsibility_id** | **str**|  | 
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

# **update_fiscal_responsibility_record**
> EmptyEnvelope update_fiscal_responsibility_record(tenant_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_record_update_dto=fiscal_responsibility_record_update_dto)

Update a fiscal responsibility record

Updates an existing fiscal responsibility record identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_responsibility_record_update_dto import FiscalResponsibilityRecordUpdateDto
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
    api_instance = openapi_client.FiscalResponsibilityRecordsApi(api_client)
    tenant_id = None # object | 
    fiscal_responsibility_record_id = 'fiscal_responsibility_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_responsibility_record_update_dto = openapi_client.FiscalResponsibilityRecordUpdateDto() # FiscalResponsibilityRecordUpdateDto |  (optional)

    try:
        # Update a fiscal responsibility record
        api_response = api_instance.update_fiscal_responsibility_record(tenant_id, fiscal_responsibility_record_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_record_update_dto=fiscal_responsibility_record_update_dto)
        print("The response of FiscalResponsibilityRecordsApi->update_fiscal_responsibility_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilityRecordsApi->update_fiscal_responsibility_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_responsibility_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_responsibility_record_update_dto** | [**FiscalResponsibilityRecordUpdateDto**](FiscalResponsibilityRecordUpdateDto.md)|  | [optional] 

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

