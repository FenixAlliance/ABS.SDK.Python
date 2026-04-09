# openapi_client.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_async**](PaymentsApi.md#create_payment_async) | **POST** /api/v2/PaymentsService/Payments | Creates a new payment
[**delete_payment_async**](PaymentsApi.md#delete_payment_async) | **DELETE** /api/v2/PaymentsService/Payments/{paymentId} | Deletes a payment
[**get_payment_async**](PaymentsApi.md#get_payment_async) | **GET** /api/v2/PaymentsService/Payments/{paymentId}/Details | Gets a payment by ID (deprecated)
[**get_payment_async_v2**](PaymentsApi.md#get_payment_async_v2) | **GET** /api/v2/PaymentsService/Payments/{paymentId} | Gets a payment by ID
[**get_payments_async**](PaymentsApi.md#get_payments_async) | **GET** /api/v2/PaymentsService/Payments | Retrieves all payments
[**update_payment_async**](PaymentsApi.md#update_payment_async) | **PUT** /api/v2/PaymentsService/Payments/{paymentId} | Updates a payment


# **create_payment_async**
> EmptyEnvelope create_payment_async(tenant_id, payment_create_dto=payment_create_dto)

Creates a new payment

Creates a new payment for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_create_dto import PaymentCreateDto
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
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_create_dto = openapi_client.PaymentCreateDto() # PaymentCreateDto |  (optional)

    try:
        # Creates a new payment
        api_response = api_instance.create_payment_async(tenant_id, payment_create_dto=payment_create_dto)
        print("The response of PaymentsApi->create_payment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_create_dto** | [**PaymentCreateDto**](PaymentCreateDto.md)|  | [optional] 

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

# **delete_payment_async**
> EmptyEnvelope delete_payment_async(tenant_id, payment_id)

Deletes a payment

Deletes the specified payment.

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
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_id = 'payment_id_example' # str | 

    try:
        # Deletes a payment
        api_response = api_instance.delete_payment_async(tenant_id, payment_id)
        print("The response of PaymentsApi->delete_payment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->delete_payment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_id** | **str**|  | 

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

# **get_payment_async**
> PaymentDtoListEnvelope get_payment_async(payment_id)

Gets a payment by ID (deprecated)

Retrieves a payment using the deprecated /Details route. Use GET {paymentId} instead.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 

    try:
        # Gets a payment by ID (deprecated)
        api_response = api_instance.get_payment_async(payment_id)
        print("The response of PaymentsApi->get_payment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **get_payment_async_v2**
> PaymentDtoListEnvelope get_payment_async_v2(payment_id)

Gets a payment by ID

Retrieves the details of a payment using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 

    try:
        # Gets a payment by ID
        api_response = api_instance.get_payment_async_v2(payment_id)
        print("The response of PaymentsApi->get_payment_async_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_async_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **get_payments_async**
> PaymentDtoListEnvelope get_payments_async(tenant_id)

Retrieves all payments

Gets all payments for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves all payments
        api_response = api_instance.get_payments_async(tenant_id)
        print("The response of PaymentsApi->get_payments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **update_payment_async**
> EmptyEnvelope update_payment_async(tenant_id, payment_id, payment_update_dto=payment_update_dto)

Updates a payment

Updates the specified payment.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_update_dto import PaymentUpdateDto
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
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_id = 'payment_id_example' # str | 
    payment_update_dto = openapi_client.PaymentUpdateDto() # PaymentUpdateDto |  (optional)

    try:
        # Updates a payment
        api_response = api_instance.update_payment_async(tenant_id, payment_id, payment_update_dto=payment_update_dto)
        print("The response of PaymentsApi->update_payment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->update_payment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_id** | **str**|  | 
 **payment_update_dto** | [**PaymentUpdateDto**](PaymentUpdateDto.md)|  | [optional] 

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

