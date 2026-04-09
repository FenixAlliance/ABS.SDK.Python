# openapi_client.LoansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_application_async**](LoansApi.md#create_loan_application_async) | **POST** /api/v2/AccountingService/Loans/Applications | Creates a loan application
[**create_loan_async**](LoansApi.md#create_loan_async) | **POST** /api/v2/AccountingService/Loans | Creates a new loan
[**delete_loan_application_async**](LoansApi.md#delete_loan_application_async) | **DELETE** /api/v2/AccountingService/Loans/Applications/{applicationId} | Deletes a loan application
[**delete_loan_async**](LoansApi.md#delete_loan_async) | **DELETE** /api/v2/AccountingService/Loans/{loanId} | Deletes a loan
[**get_loan_application_details_async**](LoansApi.md#get_loan_application_details_async) | **GET** /api/v2/AccountingService/Loans/Applications/{applicationId} | Gets a loan application by ID
[**get_loan_applications_async**](LoansApi.md#get_loan_applications_async) | **GET** /api/v2/AccountingService/Loans/Applications | Gets all loan applications
[**get_loan_applications_count_async**](LoansApi.md#get_loan_applications_count_async) | **GET** /api/v2/AccountingService/Loans/Applications/Count | Counts loan applications
[**get_loan_details_async**](LoansApi.md#get_loan_details_async) | **GET** /api/v2/AccountingService/Loans/{loanId} | Gets a loan by ID
[**get_loans_async**](LoansApi.md#get_loans_async) | **GET** /api/v2/AccountingService/Loans | Gets all loans
[**get_loans_count_async**](LoansApi.md#get_loans_count_async) | **GET** /api/v2/AccountingService/Loans/Count | Counts loans
[**update_loan_application_async**](LoansApi.md#update_loan_application_async) | **PUT** /api/v2/AccountingService/Loans/Applications/{applicationId} | Updates a loan application
[**update_loan_async**](LoansApi.md#update_loan_async) | **PUT** /api/v2/AccountingService/Loans/{loanId} | Updates a loan


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

# **update_loan_application_async**
> EmptyEnvelope update_loan_application_async(tenant_id, application_id, loan_application_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a loan application

Updates the specified loan application.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loan_application_update_dto import LoanApplicationUpdateDto
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
    loan_application_update_dto = openapi_client.LoanApplicationUpdateDto() # LoanApplicationUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a loan application
        api_response = api_instance.update_loan_application_async(tenant_id, application_id, loan_application_update_dto, api_version=api_version, x_api_version=x_api_version)
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
 **loan_application_update_dto** | [**LoanApplicationUpdateDto**](LoanApplicationUpdateDto.md)|  | 
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

