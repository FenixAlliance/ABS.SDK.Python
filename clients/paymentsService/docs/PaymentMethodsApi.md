# openapi_client.PaymentMethodsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method_async**](PaymentMethodsApi.md#create_payment_method_async) | **POST** /api/v2/PaymentsService/PaymentMethods | Creates a new payment method
[**delete_payment_method_async**](PaymentMethodsApi.md#delete_payment_method_async) | **DELETE** /api/v2/PaymentsService/PaymentMethods/{paymentMethodId} | Deletes a payment method
[**get_payment_method_details_async**](PaymentMethodsApi.md#get_payment_method_details_async) | **GET** /api/v2/PaymentsService/PaymentMethods/{paymentMethodId} | Gets a payment method by ID
[**get_payment_methods_async**](PaymentMethodsApi.md#get_payment_methods_async) | **GET** /api/v2/PaymentsService/PaymentMethods | Retrieves all payment methods
[**get_payment_methods_count_async**](PaymentMethodsApi.md#get_payment_methods_count_async) | **GET** /api/v2/PaymentsService/PaymentMethods/Count | Counts payment methods
[**update_payment_method_async**](PaymentMethodsApi.md#update_payment_method_async) | **PUT** /api/v2/PaymentsService/PaymentMethods/{paymentMethodId} | Updates a payment method


# **create_payment_method_async**
> EmptyEnvelope create_payment_method_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_method_create_dto=payment_method_create_dto)

Creates a new payment method

Creates a new payment method for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_method_create_dto import PaymentMethodCreateDto
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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_method_create_dto = openapi_client.PaymentMethodCreateDto() # PaymentMethodCreateDto |  (optional)

    try:
        # Creates a new payment method
        api_response = api_instance.create_payment_method_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_method_create_dto=payment_method_create_dto)
        print("The response of PaymentMethodsApi->create_payment_method_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->create_payment_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_method_create_dto** | [**PaymentMethodCreateDto**](PaymentMethodCreateDto.md)|  | [optional] 

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

# **delete_payment_method_async**
> EmptyEnvelope delete_payment_method_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version)

Deletes a payment method

Deletes the specified payment method.

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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a payment method
        api_response = api_instance.delete_payment_method_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentMethodsApi->delete_payment_method_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->delete_payment_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_method_id** | **str**|  | 
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

# **get_payment_method_details_async**
> PaymentMethodDtoEnvelope get_payment_method_details_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version)

Gets a payment method by ID

Retrieves the details of a payment method using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_method_dto_envelope import PaymentMethodDtoEnvelope
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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a payment method by ID
        api_response = api_instance.get_payment_method_details_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentMethodsApi->get_payment_method_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_payment_method_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_method_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentMethodDtoEnvelope**](PaymentMethodDtoEnvelope.md)

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

# **get_payment_methods_async**
> PaymentMethodDtoIReadOnlyListEnvelope get_payment_methods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all payment methods

Gets all payment methods for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.payment_method_dto_i_read_only_list_envelope import PaymentMethodDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all payment methods
        api_response = api_instance.get_payment_methods_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentMethodsApi->get_payment_methods_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_payment_methods_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentMethodDtoIReadOnlyListEnvelope**](PaymentMethodDtoIReadOnlyListEnvelope.md)

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

# **get_payment_methods_count_async**
> Int32Envelope get_payment_methods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts payment methods

Gets the count of payment methods for the current tenant.

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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts payment methods
        api_response = api_instance.get_payment_methods_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentMethodsApi->get_payment_methods_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_payment_methods_count_async: %s\n" % e)
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

# **update_payment_method_async**
> EmptyEnvelope update_payment_method_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version, payment_method_update_dto=payment_method_update_dto)

Updates a payment method

Updates the specified payment method.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_method_update_dto import PaymentMethodUpdateDto
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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_method_update_dto = openapi_client.PaymentMethodUpdateDto() # PaymentMethodUpdateDto |  (optional)

    try:
        # Updates a payment method
        api_response = api_instance.update_payment_method_async(tenant_id, payment_method_id, api_version=api_version, x_api_version=x_api_version, payment_method_update_dto=payment_method_update_dto)
        print("The response of PaymentMethodsApi->update_payment_method_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->update_payment_method_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_method_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_method_update_dto** | [**PaymentMethodUpdateDto**](PaymentMethodUpdateDto.md)|  | [optional] 

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

