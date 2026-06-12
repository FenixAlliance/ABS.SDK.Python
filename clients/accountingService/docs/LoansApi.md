# openapi_client.LoansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_application_async**](LoansApi.md#create_loan_application_async) | **POST** /api/v2/AccountingService/Loans/Applications | Creates a loan application
[**create_loan_async**](LoansApi.md#create_loan_async) | **POST** /api/v2/AccountingService/Loans | Creates a new loan
[**create_loan_type_async**](LoansApi.md#create_loan_type_async) | **POST** /api/v2/AccountingService/Loans/Types | Creates a loan type
[**delete_loan_application_async**](LoansApi.md#delete_loan_application_async) | **DELETE** /api/v2/AccountingService/Loans/Applications/{applicationId} | Deletes a loan application
[**delete_loan_async**](LoansApi.md#delete_loan_async) | **DELETE** /api/v2/AccountingService/Loans/{loanId} | Deletes a loan
[**delete_loan_type_async**](LoansApi.md#delete_loan_type_async) | **DELETE** /api/v2/AccountingService/Loans/Types/{loanTypeId} | Deletes a loan type
[**get_loan_application_details_async**](LoansApi.md#get_loan_application_details_async) | **GET** /api/v2/AccountingService/Loans/Applications/{applicationId} | Gets a loan application by ID
[**get_loan_applications_async**](LoansApi.md#get_loan_applications_async) | **GET** /api/v2/AccountingService/Loans/Applications | Gets all loan applications
[**get_loan_applications_count_async**](LoansApi.md#get_loan_applications_count_async) | **GET** /api/v2/AccountingService/Loans/Applications/Count | Counts loan applications
[**get_loan_details_async**](LoansApi.md#get_loan_details_async) | **GET** /api/v2/AccountingService/Loans/{loanId} | Gets a loan by ID
[**get_loan_type_by_id_async**](LoansApi.md#get_loan_type_by_id_async) | **GET** /api/v2/AccountingService/Loans/Types/{loanTypeId} | Gets a loan type by ID
[**get_loan_types_async**](LoansApi.md#get_loan_types_async) | **GET** /api/v2/AccountingService/Loans/Types | Gets all loan types
[**get_loan_types_count_async**](LoansApi.md#get_loan_types_count_async) | **GET** /api/v2/AccountingService/Loans/Types/Count | Counts loan types
[**get_loans_async**](LoansApi.md#get_loans_async) | **GET** /api/v2/AccountingService/Loans | Gets all loans
[**get_loans_count_async**](LoansApi.md#get_loans_count_async) | **GET** /api/v2/AccountingService/Loans/Count | Counts loans
[**patch_loan_application_async**](LoansApi.md#patch_loan_application_async) | **PATCH** /api/v2/AccountingService/Loans/Applications/{applicationId} | Patches a loan application
[**patch_loan_async**](LoansApi.md#patch_loan_async) | **PATCH** /api/v2/AccountingService/Loans/{loanId} | Patches a loan
[**patch_loan_type_async**](LoansApi.md#patch_loan_type_async) | **PATCH** /api/v2/AccountingService/Loans/Types/{loanTypeId} | Patches a loan type
[**update_loan_application_async**](LoansApi.md#update_loan_application_async) | **PUT** /api/v2/AccountingService/Loans/Applications/{applicationId} | Updates a loan application
[**update_loan_async**](LoansApi.md#update_loan_async) | **PUT** /api/v2/AccountingService/Loans/{loanId} | Updates a loan
[**update_loan_type_async**](LoansApi.md#update_loan_type_async) | **PUT** /api/v2/AccountingService/Loans/Types/{loanTypeId} | Updates a loan type


# **create_loan_application_async**
> EmptyEnvelope create_loan_application_async(tenant_id, loan_application_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a loan application

Creates a new loan application.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_application_create_dto import LoanApplicationCreateDto
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_application_create_dto = openapi_client.LoanApplicationCreateDto() # LoanApplicationCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a loan application
        api_response = api_instance.create_loan_application_async(tenant_id, loan_application_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->create_loan_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->create_loan_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_application_create_dto** | [**LoanApplicationCreateDto**](LoanApplicationCreateDto.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_async**
> EmptyEnvelope create_loan_async(tenant_id, loan_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a new loan

Creates a new loan for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_create_dto import LoanCreateDto
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_create_dto = openapi_client.LoanCreateDto() # LoanCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a new loan
        api_response = api_instance.create_loan_async(tenant_id, loan_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->create_loan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->create_loan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_create_dto** | [**LoanCreateDto**](LoanCreateDto.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_type_async**
> EmptyEnvelope create_loan_type_async(tenant_id, loan_type_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a loan type

Creates a new loan type for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_type_create_dto import LoanTypeCreateDto
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_type_create_dto = openapi_client.LoanTypeCreateDto() # LoanTypeCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a loan type
        api_response = api_instance.create_loan_type_async(tenant_id, loan_type_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->create_loan_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->create_loan_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_type_create_dto** | [**LoanTypeCreateDto**](LoanTypeCreateDto.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_application_async**
> EmptyEnvelope delete_loan_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Deletes a loan application

Deletes the specified loan application.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a loan application
        api_response = api_instance.delete_loan_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->delete_loan_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->delete_loan_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_async**
> EmptyEnvelope delete_loan_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version)

Deletes a loan

Deletes the specified loan.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_id = 'loan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a loan
        api_response = api_instance.delete_loan_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->delete_loan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->delete_loan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_type_async**
> EmptyEnvelope delete_loan_type_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version)

Deletes a loan type

Deletes the specified loan type.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_type_id = 'loan_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a loan type
        api_response = api_instance.delete_loan_type_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->delete_loan_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->delete_loan_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_type_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_application_details_async**
> LoanApplicationDtoEnvelope get_loan_application_details_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Gets a loan application by ID

Retrieves the details of a loan application.

### Example


```python
import openapi_client
from openapi_client.models.loan_application_dto_envelope import LoanApplicationDtoEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a loan application by ID
        api_response = api_instance.get_loan_application_details_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_application_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_application_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanApplicationDtoEnvelope**](LoanApplicationDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_applications_async**
> LoanApplicationDtoIReadOnlyListEnvelope get_loan_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all loan applications

Retrieves all loan applications for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.loan_application_dto_i_read_only_list_envelope import LoanApplicationDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all loan applications
        api_response = api_instance.get_loan_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_applications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_applications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanApplicationDtoIReadOnlyListEnvelope**](LoanApplicationDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_applications_count_async**
> Int32Envelope get_loan_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts loan applications

Gets the count of loan applications for the current tenant.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts loan applications
        api_response = api_instance.get_loan_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_applications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_applications_count_async: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_details_async**
> LoanDtoEnvelope get_loan_details_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version)

Gets a loan by ID

Retrieves the details of a loan using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.loan_dto_envelope import LoanDtoEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_id = 'loan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a loan by ID
        api_response = api_instance.get_loan_details_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanDtoEnvelope**](LoanDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_type_by_id_async**
> LoanTypeDtoEnvelope get_loan_type_by_id_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version)

Gets a loan type by ID

Retrieves the details of a loan type using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.loan_type_dto_envelope import LoanTypeDtoEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_type_id = 'loan_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a loan type by ID
        api_response = api_instance.get_loan_type_by_id_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanTypeDtoEnvelope**](LoanTypeDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_types_async**
> LoanTypeDtoIReadOnlyListEnvelope get_loan_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all loan types

Retrieves all loan types for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.loan_type_dto_i_read_only_list_envelope import LoanTypeDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all loan types
        api_response = api_instance.get_loan_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanTypeDtoIReadOnlyListEnvelope**](LoanTypeDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_types_count_async**
> Int32Envelope get_loan_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts loan types

Gets the count of loan types for the current tenant.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts loan types
        api_response = api_instance.get_loan_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loan_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loan_types_count_async: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loans_async**
> LoanDtoIReadOnlyListEnvelope get_loans_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all loans

Retrieves all loans for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.loan_dto_i_read_only_list_envelope import LoanDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all loans
        api_response = api_instance.get_loans_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loans_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loans_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LoanDtoIReadOnlyListEnvelope**](LoanDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loans_count_async**
> Int32Envelope get_loans_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts loans

Gets the count of loans for the current tenant.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts loans
        api_response = api_instance.get_loans_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->get_loans_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->get_loans_count_async: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_loan_application_async**
> EmptyEnvelope patch_loan_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patches a loan application

Partially updates the specified loan application using a JSON Patch document.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patches a loan application
        api_response = api_instance.patch_loan_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of LoansApi->patch_loan_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->patch_loan_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_loan_async**
> EmptyEnvelope patch_loan_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patches a loan

Partially updates the specified loan using a JSON Patch document.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_id = 'loan_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patches a loan
        api_response = api_instance.patch_loan_async(tenant_id, loan_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of LoansApi->patch_loan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->patch_loan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_id** | **str**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_loan_type_async**
> EmptyEnvelope patch_loan_type_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patches a loan type

Partially updates the specified loan type using a JSON Patch document.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_type_id = 'loan_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patches a loan type
        api_response = api_instance.patch_loan_type_async(tenant_id, loan_type_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of LoansApi->patch_loan_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->patch_loan_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_type_id** | **str**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_application_async**
> EmptyEnvelope update_loan_application_async(tenant_id, application_id, body, api_version=api_version, x_api_version=x_api_version)

Updates a loan application

Updates the specified loan application.

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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    body = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a loan application
        api_response = api_instance.update_loan_application_async(tenant_id, application_id, body, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->update_loan_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->update_loan_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **body** | **object**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_async**
> EmptyEnvelope update_loan_async(tenant_id, loan_id, loan_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a loan

Updates the specified loan.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_update_dto import LoanUpdateDto
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_id = 'loan_id_example' # str | 
    loan_update_dto = openapi_client.LoanUpdateDto() # LoanUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a loan
        api_response = api_instance.update_loan_async(tenant_id, loan_id, loan_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->update_loan_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->update_loan_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_id** | **str**|  | 
 **loan_update_dto** | [**LoanUpdateDto**](LoanUpdateDto.md)|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_type_async**
> EmptyEnvelope update_loan_type_async(tenant_id, loan_type_id, loan_type_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a loan type

Updates the specified loan type.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_type_update_dto import LoanTypeUpdateDto
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
    api_instance = openapi_client.LoansApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loan_type_id = 'loan_type_id_example' # str | 
    loan_type_update_dto = openapi_client.LoanTypeUpdateDto() # LoanTypeUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a loan type
        api_response = api_instance.update_loan_type_async(tenant_id, loan_type_id, loan_type_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of LoansApi->update_loan_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoansApi->update_loan_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loan_type_id** | **str**|  | 
 **loan_type_update_dto** | [**LoanTypeUpdateDto**](LoanTypeUpdateDto.md)|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

