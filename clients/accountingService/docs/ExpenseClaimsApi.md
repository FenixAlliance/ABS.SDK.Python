# openapi_client.ExpenseClaimsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_expense_claim**](ExpenseClaimsApi.md#create_expense_claim) | **POST** /api/v2/AccountingService/ExpenseClaims | Create an expense claim
[**delete_expense_claim**](ExpenseClaimsApi.md#delete_expense_claim) | **DELETE** /api/v2/AccountingService/ExpenseClaims/{expenseClaimId} | Delete an expense claim
[**get_expense_claim**](ExpenseClaimsApi.md#get_expense_claim) | **GET** /api/v2/AccountingService/ExpenseClaims/{expenseClaimId} | Get an expense claim by id
[**get_expense_claims**](ExpenseClaimsApi.md#get_expense_claims) | **GET** /api/v2/AccountingService/ExpenseClaims | Get all expense claims for a tenant
[**get_expense_claims_count**](ExpenseClaimsApi.md#get_expense_claims_count) | **GET** /api/v2/AccountingService/ExpenseClaims/Count | Get the count of expense claims for a tenant
[**patch_expense_claim**](ExpenseClaimsApi.md#patch_expense_claim) | **PATCH** /api/v2/AccountingService/ExpenseClaims/{expenseClaimId} | Patch an expense claim
[**update_expense_claim**](ExpenseClaimsApi.md#update_expense_claim) | **PUT** /api/v2/AccountingService/ExpenseClaims/{expenseClaimId} | Update an expense claim


# **create_expense_claim**
> EmptyEnvelope create_expense_claim(tenant_id, expense_claim_create_dto, api_version=api_version, x_api_version=x_api_version)

Create an expense claim

Creates a new expense claim.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.expense_claim_create_dto import ExpenseClaimCreateDto
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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_claim_create_dto = openapi_client.ExpenseClaimCreateDto() # ExpenseClaimCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create an expense claim
        api_response = api_instance.create_expense_claim(tenant_id, expense_claim_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->create_expense_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->create_expense_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_claim_create_dto** | [**ExpenseClaimCreateDto**](ExpenseClaimCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **delete_expense_claim**
> EmptyEnvelope delete_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version)

Delete an expense claim

Deletes an expense claim.

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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_claim_id = 'expense_claim_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an expense claim
        api_response = api_instance.delete_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->delete_expense_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->delete_expense_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_claim_id** | **str**|  | 
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

# **get_expense_claim**
> ExpenseClaimDtoEnvelope get_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version)

Get an expense claim by id

Retrieves an expense claim by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.expense_claim_dto_envelope import ExpenseClaimDtoEnvelope
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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_claim_id = 'expense_claim_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get an expense claim by id
        api_response = api_instance.get_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->get_expense_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->get_expense_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_claim_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExpenseClaimDtoEnvelope**](ExpenseClaimDtoEnvelope.md)

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

# **get_expense_claims**
> ExpenseClaimDtoListEnvelope get_expense_claims(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all expense claims for a tenant

Retrieves all expense claims for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.expense_claim_dto_list_envelope import ExpenseClaimDtoListEnvelope
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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all expense claims for a tenant
        api_response = api_instance.get_expense_claims(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->get_expense_claims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->get_expense_claims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExpenseClaimDtoListEnvelope**](ExpenseClaimDtoListEnvelope.md)

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

# **get_expense_claims_count**
> Int32Envelope get_expense_claims_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of expense claims for a tenant

Retrieves the count of expense claims for the specified tenant using OData query options.

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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of expense claims for a tenant
        api_response = api_instance.get_expense_claims_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->get_expense_claims_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->get_expense_claims_count: %s\n" % e)
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

# **patch_expense_claim**
> EmptyEnvelope patch_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an expense claim

Partially updates an existing expense claim.

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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_claim_id = 'expense_claim_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an expense claim
        api_response = api_instance.patch_expense_claim(tenant_id, expense_claim_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ExpenseClaimsApi->patch_expense_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->patch_expense_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_claim_id** | **str**|  | 
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

# **update_expense_claim**
> EmptyEnvelope update_expense_claim(tenant_id, expense_claim_id, expense_claim_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an expense claim

Updates an existing expense claim.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.expense_claim_update_dto import ExpenseClaimUpdateDto
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
    api_instance = openapi_client.ExpenseClaimsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_claim_id = 'expense_claim_id_example' # str | 
    expense_claim_update_dto = openapi_client.ExpenseClaimUpdateDto() # ExpenseClaimUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an expense claim
        api_response = api_instance.update_expense_claim(tenant_id, expense_claim_id, expense_claim_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseClaimsApi->update_expense_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseClaimsApi->update_expense_claim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_claim_id** | **str**|  | 
 **expense_claim_update_dto** | [**ExpenseClaimUpdateDto**](ExpenseClaimUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

