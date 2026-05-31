# openapi_client.TaxPoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_applied_tax_policy_record**](TaxPoliciesApi.md#create_applied_tax_policy_record) | **POST** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords | Create an applied tax policy record
[**create_item_tax_policy_record**](TaxPoliciesApi.md#create_item_tax_policy_record) | **POST** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/ItemTaxPolicyRecords | Create an item tax policy record
[**create_tax_policy**](TaxPoliciesApi.md#create_tax_policy) | **POST** /api/v2/AccountingService/TaxPolicies | Create a tax policy
[**delete_applied_tax_policy_record**](TaxPoliciesApi.md#delete_applied_tax_policy_record) | **DELETE** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords/{appliedTaxPolicyRecordId} | Delete an applied tax policy record
[**delete_item_tax_policy_record**](TaxPoliciesApi.md#delete_item_tax_policy_record) | **DELETE** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/ItemTaxPolicyRecords/{itemTaxPolicyRecordId} | Delete an item tax policy record
[**delete_tax_policy**](TaxPoliciesApi.md#delete_tax_policy) | **DELETE** /api/v2/AccountingService/TaxPolicies/{id} | Delete a tax policy
[**get_applied_tax_policy_record**](TaxPoliciesApi.md#get_applied_tax_policy_record) | **GET** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords/{appliedTaxPolicyRecordId} | Get applied tax policy record by ID
[**get_applied_tax_policy_records**](TaxPoliciesApi.md#get_applied_tax_policy_records) | **GET** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords | Get applied tax policy records
[**get_applied_tax_policy_records_count**](TaxPoliciesApi.md#get_applied_tax_policy_records_count) | **GET** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords/Count | Get applied tax policy records count
[**get_item_tax_policy_record**](TaxPoliciesApi.md#get_item_tax_policy_record) | **GET** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/ItemTaxPolicyRecords/{itemTaxPolicyRecordId} | Get item tax policy record by ID
[**get_item_tax_policy_records**](TaxPoliciesApi.md#get_item_tax_policy_records) | **GET** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/ItemTaxPolicyRecords | Get item tax policy records
[**get_tax_policies**](TaxPoliciesApi.md#get_tax_policies) | **GET** /api/v2/AccountingService/TaxPolicies | Get all tax policies for a tenant
[**get_tax_policies_by_authority**](TaxPoliciesApi.md#get_tax_policies_by_authority) | **GET** /api/v2/AccountingService/TaxPolicies/ByAuthority/{authorityId} | Get tax policies by fiscal authority
[**get_tax_policies_count**](TaxPoliciesApi.md#get_tax_policies_count) | **GET** /api/v2/AccountingService/TaxPolicies/Count | Get tax policies count
[**get_tax_policy**](TaxPoliciesApi.md#get_tax_policy) | **GET** /api/v2/AccountingService/TaxPolicies/{id} | Get tax policy by ID
[**update_applied_tax_policy_record**](TaxPoliciesApi.md#update_applied_tax_policy_record) | **PUT** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/AppliedTaxPolicyRecords/{appliedTaxPolicyRecordId} | Update an applied tax policy record
[**update_item_tax_policy_record**](TaxPoliciesApi.md#update_item_tax_policy_record) | **PUT** /api/v2/AccountingService/TaxPolicies/{taxPolicyId}/ItemTaxPolicyRecords/{itemTaxPolicyRecordId} | Update an item tax policy record
[**update_tax_policy**](TaxPoliciesApi.md#update_tax_policy) | **PUT** /api/v2/AccountingService/TaxPolicies/{id} | Update a tax policy


# **create_applied_tax_policy_record**
> EmptyEnvelope create_applied_tax_policy_record(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version, applied_tax_policy_record_create_dto=applied_tax_policy_record_create_dto)

Create an applied tax policy record

Creates a new applied tax policy record for the specified tax policy.

### Example


```python
import openapi_client
from openapi_client.models.applied_tax_policy_record_create_dto import AppliedTaxPolicyRecordCreateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    applied_tax_policy_record_create_dto = openapi_client.AppliedTaxPolicyRecordCreateDto() # AppliedTaxPolicyRecordCreateDto |  (optional)

    try:
        # Create an applied tax policy record
        api_response = api_instance.create_applied_tax_policy_record(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version, applied_tax_policy_record_create_dto=applied_tax_policy_record_create_dto)
        print("The response of TaxPoliciesApi->create_applied_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->create_applied_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **applied_tax_policy_record_create_dto** | [**AppliedTaxPolicyRecordCreateDto**](AppliedTaxPolicyRecordCreateDto.md)|  | [optional] 

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

# **create_item_tax_policy_record**
> EmptyEnvelope create_item_tax_policy_record(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version, item_tax_policy_record_create_dto=item_tax_policy_record_create_dto)

Create an item tax policy record

Creates a new item tax policy record for the specified tax policy.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_tax_policy_record_create_dto import ItemTaxPolicyRecordCreateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_tax_policy_record_create_dto = openapi_client.ItemTaxPolicyRecordCreateDto() # ItemTaxPolicyRecordCreateDto |  (optional)

    try:
        # Create an item tax policy record
        api_response = api_instance.create_item_tax_policy_record(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version, item_tax_policy_record_create_dto=item_tax_policy_record_create_dto)
        print("The response of TaxPoliciesApi->create_item_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->create_item_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_tax_policy_record_create_dto** | [**ItemTaxPolicyRecordCreateDto**](ItemTaxPolicyRecordCreateDto.md)|  | [optional] 

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

# **create_tax_policy**
> EmptyEnvelope create_tax_policy(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_policy_create_dto=tax_policy_create_dto)

Create a tax policy

Creates a new tax policy for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_policy_create_dto import TaxPolicyCreateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_policy_create_dto = openapi_client.TaxPolicyCreateDto() # TaxPolicyCreateDto |  (optional)

    try:
        # Create a tax policy
        api_response = api_instance.create_tax_policy(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_policy_create_dto=tax_policy_create_dto)
        print("The response of TaxPoliciesApi->create_tax_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->create_tax_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_policy_create_dto** | [**TaxPolicyCreateDto**](TaxPolicyCreateDto.md)|  | [optional] 

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

# **delete_applied_tax_policy_record**
> EmptyEnvelope delete_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)

Delete an applied tax policy record

Deletes an applied tax policy record identified by its unique identifier.

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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    applied_tax_policy_record_id = 'applied_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an applied tax policy record
        api_response = api_instance.delete_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->delete_applied_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->delete_applied_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **applied_tax_policy_record_id** | **str**|  | 
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

# **delete_item_tax_policy_record**
> EmptyEnvelope delete_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)

Delete an item tax policy record

Deletes an item tax policy record identified by its unique identifier.

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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    item_tax_policy_record_id = 'item_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item tax policy record
        api_response = api_instance.delete_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->delete_item_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->delete_item_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **item_tax_policy_record_id** | **str**|  | 
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

# **delete_tax_policy**
> EmptyEnvelope delete_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete a tax policy

Deletes a tax policy identified by its unique identifier.

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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tax policy
        api_response = api_instance.delete_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->delete_tax_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->delete_tax_policy: %s\n" % e)
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

# **get_applied_tax_policy_record**
> AppliedTaxPolicyRecordDtoEnvelope get_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)

Get applied tax policy record by ID

Retrieves a specific applied tax policy record by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.applied_tax_policy_record_dto_envelope import AppliedTaxPolicyRecordDtoEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    applied_tax_policy_record_id = 'applied_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get applied tax policy record by ID
        api_response = api_instance.get_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_applied_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_applied_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **applied_tax_policy_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppliedTaxPolicyRecordDtoEnvelope**](AppliedTaxPolicyRecordDtoEnvelope.md)

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

# **get_applied_tax_policy_records**
> AppliedTaxPolicyRecordDtoListEnvelope get_applied_tax_policy_records(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Get applied tax policy records

Retrieves all applied tax policy records for the specified tax policy.

### Example


```python
import openapi_client
from openapi_client.models.applied_tax_policy_record_dto_list_envelope import AppliedTaxPolicyRecordDtoListEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get applied tax policy records
        api_response = api_instance.get_applied_tax_policy_records(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_applied_tax_policy_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_applied_tax_policy_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppliedTaxPolicyRecordDtoListEnvelope**](AppliedTaxPolicyRecordDtoListEnvelope.md)

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

# **get_applied_tax_policy_records_count**
> Int32Envelope get_applied_tax_policy_records_count(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Get applied tax policy records count

Returns the total count of applied tax policy records for the specified tax policy.

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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get applied tax policy records count
        api_response = api_instance.get_applied_tax_policy_records_count(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_applied_tax_policy_records_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_applied_tax_policy_records_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
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

# **get_item_tax_policy_record**
> ItemTaxPolicyRecordDtoEnvelope get_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)

Get item tax policy record by ID

Retrieves a specific item tax policy record by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_record_dto_envelope import ItemTaxPolicyRecordDtoEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    item_tax_policy_record_id = 'item_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item tax policy record by ID
        api_response = api_instance.get_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_item_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_item_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **item_tax_policy_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyRecordDtoEnvelope**](ItemTaxPolicyRecordDtoEnvelope.md)

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

# **get_item_tax_policy_records**
> ItemTaxPolicyRecordDtoListEnvelope get_item_tax_policy_records(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Get item tax policy records

Retrieves all item tax policy records for the specified tax policy.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_record_dto_list_envelope import ItemTaxPolicyRecordDtoListEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item tax policy records
        api_response = api_instance.get_item_tax_policy_records(tenant_id, tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_item_tax_policy_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_item_tax_policy_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyRecordDtoListEnvelope**](ItemTaxPolicyRecordDtoListEnvelope.md)

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

# **get_tax_policies**
> TaxPolicyDtoListEnvelope get_tax_policies(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all tax policies for a tenant

Retrieves all tax policies for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.tax_policy_dto_list_envelope import TaxPolicyDtoListEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all tax policies for a tenant
        api_response = api_instance.get_tax_policies(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_tax_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_tax_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxPolicyDtoListEnvelope**](TaxPolicyDtoListEnvelope.md)

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

# **get_tax_policies_by_authority**
> TaxPolicyDtoListEnvelope get_tax_policies_by_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get tax policies by fiscal authority

Retrieves all tax policies associated with the specified fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.tax_policy_dto_list_envelope import TaxPolicyDtoListEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax policies by fiscal authority
        api_response = api_instance.get_tax_policies_by_authority(tenant_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_tax_policies_by_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_tax_policies_by_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxPolicyDtoListEnvelope**](TaxPolicyDtoListEnvelope.md)

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

# **get_tax_policies_count**
> Int32Envelope get_tax_policies_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get tax policies count

Returns the count of tax policies for the specified tenant.

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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax policies count
        api_response = api_instance.get_tax_policies_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_tax_policies_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_tax_policies_count: %s\n" % e)
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

# **get_tax_policy**
> TaxPolicyDtoEnvelope get_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get tax policy by ID

Retrieves a specific tax policy by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.tax_policy_dto_envelope import TaxPolicyDtoEnvelope
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax policy by ID
        api_response = api_instance.get_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxPoliciesApi->get_tax_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->get_tax_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxPolicyDtoEnvelope**](TaxPolicyDtoEnvelope.md)

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

# **update_applied_tax_policy_record**
> EmptyEnvelope update_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version, applied_tax_policy_record_update_dto=applied_tax_policy_record_update_dto)

Update an applied tax policy record

Updates an existing applied tax policy record identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.applied_tax_policy_record_update_dto import AppliedTaxPolicyRecordUpdateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    applied_tax_policy_record_id = 'applied_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    applied_tax_policy_record_update_dto = openapi_client.AppliedTaxPolicyRecordUpdateDto() # AppliedTaxPolicyRecordUpdateDto |  (optional)

    try:
        # Update an applied tax policy record
        api_response = api_instance.update_applied_tax_policy_record(tenant_id, tax_policy_id, applied_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version, applied_tax_policy_record_update_dto=applied_tax_policy_record_update_dto)
        print("The response of TaxPoliciesApi->update_applied_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->update_applied_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **applied_tax_policy_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **applied_tax_policy_record_update_dto** | [**AppliedTaxPolicyRecordUpdateDto**](AppliedTaxPolicyRecordUpdateDto.md)|  | [optional] 

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

# **update_item_tax_policy_record**
> EmptyEnvelope update_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version, item_tax_policy_record_update_dto=item_tax_policy_record_update_dto)

Update an item tax policy record

Updates an existing item tax policy record identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_tax_policy_record_update_dto import ItemTaxPolicyRecordUpdateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tax_policy_id = 'tax_policy_id_example' # str | 
    item_tax_policy_record_id = 'item_tax_policy_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_tax_policy_record_update_dto = openapi_client.ItemTaxPolicyRecordUpdateDto() # ItemTaxPolicyRecordUpdateDto |  (optional)

    try:
        # Update an item tax policy record
        api_response = api_instance.update_item_tax_policy_record(tenant_id, tax_policy_id, item_tax_policy_record_id, api_version=api_version, x_api_version=x_api_version, item_tax_policy_record_update_dto=item_tax_policy_record_update_dto)
        print("The response of TaxPoliciesApi->update_item_tax_policy_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->update_item_tax_policy_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tax_policy_id** | **str**|  | 
 **item_tax_policy_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_tax_policy_record_update_dto** | [**ItemTaxPolicyRecordUpdateDto**](ItemTaxPolicyRecordUpdateDto.md)|  | [optional] 

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

# **update_tax_policy**
> EmptyEnvelope update_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_policy_update_dto=tax_policy_update_dto)

Update a tax policy

Updates an existing tax policy identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_policy_update_dto import TaxPolicyUpdateDto
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
    api_instance = openapi_client.TaxPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_policy_update_dto = openapi_client.TaxPolicyUpdateDto() # TaxPolicyUpdateDto |  (optional)

    try:
        # Update a tax policy
        api_response = api_instance.update_tax_policy(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_policy_update_dto=tax_policy_update_dto)
        print("The response of TaxPoliciesApi->update_tax_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxPoliciesApi->update_tax_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_policy_update_dto** | [**TaxPolicyUpdateDto**](TaxPolicyUpdateDto.md)|  | [optional] 

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

