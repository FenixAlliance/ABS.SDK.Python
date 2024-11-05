# openapi_client.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_payments_service_payments_get**](PaymentsApi.md#api_v2_payments_service_payments_get) | **GET** /api/v2/PaymentsService/Payments | 
[**api_v2_payments_service_payments_payment_id_delete**](PaymentsApi.md#api_v2_payments_service_payments_payment_id_delete) | **DELETE** /api/v2/PaymentsService/Payments/{paymentId} | 
[**api_v2_payments_service_payments_payment_id_details_get**](PaymentsApi.md#api_v2_payments_service_payments_payment_id_details_get) | **GET** /api/v2/PaymentsService/Payments/{paymentId}/Details | 
[**api_v2_payments_service_payments_payment_id_get**](PaymentsApi.md#api_v2_payments_service_payments_payment_id_get) | **GET** /api/v2/PaymentsService/Payments/{paymentId} | 
[**api_v2_payments_service_payments_payment_id_put**](PaymentsApi.md#api_v2_payments_service_payments_payment_id_put) | **PUT** /api/v2/PaymentsService/Payments/{paymentId} | 
[**api_v2_payments_service_payments_post**](PaymentsApi.md#api_v2_payments_service_payments_post) | **POST** /api/v2/PaymentsService/Payments | 


# **api_v2_payments_service_payments_get**
> PaymentDtoListEnvelope api_v2_payments_service_payments_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_payments_service_payments_get(tenant_id)
        print("The response of PaymentsApi->api_v2_payments_service_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_payments_service_payments_payment_id_delete**
> EmptyEnvelope api_v2_payments_service_payments_payment_id_delete(tenant_id, payment_id)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_id = 'payment_id_example' # str | 

    try:
        api_response = api_instance.api_v2_payments_service_payments_payment_id_delete(tenant_id, payment_id)
        print("The response of PaymentsApi->api_v2_payments_service_payments_payment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_payment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_id** | **str**|  | 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_payments_service_payments_payment_id_details_get**
> PaymentDtoListEnvelope api_v2_payments_service_payments_payment_id_details_get(payment_id)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 

    try:
        api_response = api_instance.api_v2_payments_service_payments_payment_id_details_get(payment_id)
        print("The response of PaymentsApi->api_v2_payments_service_payments_payment_id_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_payment_id_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_payments_service_payments_payment_id_get**
> PaymentDtoListEnvelope api_v2_payments_service_payments_payment_id_get(payment_id)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 

    try:
        api_response = api_instance.api_v2_payments_service_payments_payment_id_get(payment_id)
        print("The response of PaymentsApi->api_v2_payments_service_payments_payment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_payment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_payments_service_payments_payment_id_put**
> EmptyEnvelope api_v2_payments_service_payments_payment_id_put(tenant_id, payment_id, payment_update_dto=payment_update_dto)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_id = 'payment_id_example' # str | 
    payment_update_dto = openapi_client.PaymentUpdateDto() # PaymentUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_payments_service_payments_payment_id_put(tenant_id, payment_id, payment_update_dto=payment_update_dto)
        print("The response of PaymentsApi->api_v2_payments_service_payments_payment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_payment_id_put: %s\n" % e)
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

[Bearer](../README.md#Bearer)

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

# **api_v2_payments_service_payments_post**
> EmptyEnvelope api_v2_payments_service_payments_post(tenant_id, payment_create_dto=payment_create_dto)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_create_dto = openapi_client.PaymentCreateDto() # PaymentCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_payments_service_payments_post(tenant_id, payment_create_dto=payment_create_dto)
        print("The response of PaymentsApi->api_v2_payments_service_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->api_v2_payments_service_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_create_dto** | [**PaymentCreateDto**](PaymentCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

