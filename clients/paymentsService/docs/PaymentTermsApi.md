# openapi_client.PaymentTermsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_term_async**](PaymentTermsApi.md#create_payment_term_async) | **POST** /api/v2/PaymentsService/PaymentTerms | Creates a new payment term
[**delete_payment_term_async**](PaymentTermsApi.md#delete_payment_term_async) | **DELETE** /api/v2/PaymentsService/PaymentTerms/{paymentTermId} | Deletes a payment term
[**get_payment_term_details_async**](PaymentTermsApi.md#get_payment_term_details_async) | **GET** /api/v2/PaymentsService/PaymentTerms/{paymentTermId} | Gets a payment term by ID
[**get_payment_terms_async**](PaymentTermsApi.md#get_payment_terms_async) | **GET** /api/v2/PaymentsService/PaymentTerms | Retrieves all payment terms
[**get_payment_terms_count_async**](PaymentTermsApi.md#get_payment_terms_count_async) | **GET** /api/v2/PaymentsService/PaymentTerms/Count | Counts payment terms
[**update_payment_term_async**](PaymentTermsApi.md#update_payment_term_async) | **PUT** /api/v2/PaymentsService/PaymentTerms/{paymentTermId} | Updates a payment term


# **create_payment_term_async**
> EmptyEnvelope create_payment_term_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_term_create_dto=payment_term_create_dto)

Creates a new payment term

Creates a new payment term for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_term_create_dto import PaymentTermCreateDto
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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_term_create_dto = openapi_client.PaymentTermCreateDto() # PaymentTermCreateDto |  (optional)

    try:
        # Creates a new payment term
        api_response = api_instance.create_payment_term_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_term_create_dto=payment_term_create_dto)
        print("The response of PaymentTermsApi->create_payment_term_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->create_payment_term_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_term_create_dto** | [**PaymentTermCreateDto**](PaymentTermCreateDto.md)|  | [optional] 

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

# **delete_payment_term_async**
> EmptyEnvelope delete_payment_term_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version)

Deletes a payment term

Deletes the specified payment term.

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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_term_id = 'payment_term_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a payment term
        api_response = api_instance.delete_payment_term_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentTermsApi->delete_payment_term_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->delete_payment_term_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_term_id** | **str**|  | 
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

# **get_payment_term_details_async**
> PaymentTermDtoEnvelope get_payment_term_details_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version)

Gets a payment term by ID

Retrieves the details of a payment term using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_term_dto_envelope import PaymentTermDtoEnvelope
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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_term_id = 'payment_term_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a payment term by ID
        api_response = api_instance.get_payment_term_details_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentTermsApi->get_payment_term_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->get_payment_term_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_term_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentTermDtoEnvelope**](PaymentTermDtoEnvelope.md)

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

# **get_payment_terms_async**
> PaymentTermDtoIReadOnlyListEnvelope get_payment_terms_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all payment terms

Gets all payment terms for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.payment_term_dto_i_read_only_list_envelope import PaymentTermDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all payment terms
        api_response = api_instance.get_payment_terms_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentTermsApi->get_payment_terms_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->get_payment_terms_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentTermDtoIReadOnlyListEnvelope**](PaymentTermDtoIReadOnlyListEnvelope.md)

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

# **get_payment_terms_count_async**
> Int32Envelope get_payment_terms_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts payment terms

Gets the count of payment terms for the current tenant.

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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts payment terms
        api_response = api_instance.get_payment_terms_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentTermsApi->get_payment_terms_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->get_payment_terms_count_async: %s\n" % e)
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

# **update_payment_term_async**
> EmptyEnvelope update_payment_term_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version, payment_term_update_dto=payment_term_update_dto)

Updates a payment term

Updates the specified payment term.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_term_update_dto import PaymentTermUpdateDto
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
    api_instance = openapi_client.PaymentTermsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_term_id = 'payment_term_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_term_update_dto = openapi_client.PaymentTermUpdateDto() # PaymentTermUpdateDto |  (optional)

    try:
        # Updates a payment term
        api_response = api_instance.update_payment_term_async(tenant_id, payment_term_id, api_version=api_version, x_api_version=x_api_version, payment_term_update_dto=payment_term_update_dto)
        print("The response of PaymentTermsApi->update_payment_term_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTermsApi->update_payment_term_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_term_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_term_update_dto** | [**PaymentTermUpdateDto**](PaymentTermUpdateDto.md)|  | [optional] 

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

