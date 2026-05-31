# openapi_client.PaymentModesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_mode_async**](PaymentModesApi.md#create_payment_mode_async) | **POST** /api/v2/PaymentsService/PaymentModes | Creates a new payment mode
[**delete_payment_mode_async**](PaymentModesApi.md#delete_payment_mode_async) | **DELETE** /api/v2/PaymentsService/PaymentModes/{paymentModeId} | Deletes a payment mode
[**get_payment_mode_details_async**](PaymentModesApi.md#get_payment_mode_details_async) | **GET** /api/v2/PaymentsService/PaymentModes/{paymentModeId} | Gets a payment mode by ID
[**get_payment_modes_async**](PaymentModesApi.md#get_payment_modes_async) | **GET** /api/v2/PaymentsService/PaymentModes | Retrieves all payment modes
[**get_payment_modes_count_async**](PaymentModesApi.md#get_payment_modes_count_async) | **GET** /api/v2/PaymentsService/PaymentModes/Count | Counts payment modes
[**update_payment_mode_async**](PaymentModesApi.md#update_payment_mode_async) | **PUT** /api/v2/PaymentsService/PaymentModes/{paymentModeId} | Updates a payment mode


# **create_payment_mode_async**
> EmptyEnvelope create_payment_mode_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_mode_create_dto=payment_mode_create_dto)

Creates a new payment mode

Creates a new payment mode for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_mode_create_dto import PaymentModeCreateDto
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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_mode_create_dto = openapi_client.PaymentModeCreateDto() # PaymentModeCreateDto |  (optional)

    try:
        # Creates a new payment mode
        api_response = api_instance.create_payment_mode_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payment_mode_create_dto=payment_mode_create_dto)
        print("The response of PaymentModesApi->create_payment_mode_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->create_payment_mode_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_mode_create_dto** | [**PaymentModeCreateDto**](PaymentModeCreateDto.md)|  | [optional] 

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

# **delete_payment_mode_async**
> EmptyEnvelope delete_payment_mode_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version)

Deletes a payment mode

Deletes the specified payment mode.

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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_mode_id = 'payment_mode_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a payment mode
        api_response = api_instance.delete_payment_mode_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentModesApi->delete_payment_mode_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->delete_payment_mode_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_mode_id** | **str**|  | 
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

# **get_payment_mode_details_async**
> PaymentModeDtoEnvelope get_payment_mode_details_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version)

Gets a payment mode by ID

Retrieves the details of a payment mode using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_mode_dto_envelope import PaymentModeDtoEnvelope
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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_mode_id = 'payment_mode_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a payment mode by ID
        api_response = api_instance.get_payment_mode_details_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentModesApi->get_payment_mode_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->get_payment_mode_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_mode_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentModeDtoEnvelope**](PaymentModeDtoEnvelope.md)

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

# **get_payment_modes_async**
> PaymentModeDtoIReadOnlyListEnvelope get_payment_modes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all payment modes

Gets all payment modes for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.payment_mode_dto_i_read_only_list_envelope import PaymentModeDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all payment modes
        api_response = api_instance.get_payment_modes_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentModesApi->get_payment_modes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->get_payment_modes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentModeDtoIReadOnlyListEnvelope**](PaymentModeDtoIReadOnlyListEnvelope.md)

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

# **get_payment_modes_count_async**
> Int32Envelope get_payment_modes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts payment modes

Gets the count of payment modes for the current tenant.

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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts payment modes
        api_response = api_instance.get_payment_modes_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PaymentModesApi->get_payment_modes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->get_payment_modes_count_async: %s\n" % e)
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

# **update_payment_mode_async**
> EmptyEnvelope update_payment_mode_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version, payment_mode_update_dto=payment_mode_update_dto)

Updates a payment mode

Updates the specified payment mode.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_mode_update_dto import PaymentModeUpdateDto
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
    api_instance = openapi_client.PaymentModesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_mode_id = 'payment_mode_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_mode_update_dto = openapi_client.PaymentModeUpdateDto() # PaymentModeUpdateDto |  (optional)

    try:
        # Updates a payment mode
        api_response = api_instance.update_payment_mode_async(tenant_id, payment_mode_id, api_version=api_version, x_api_version=x_api_version, payment_mode_update_dto=payment_mode_update_dto)
        print("The response of PaymentModesApi->update_payment_mode_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentModesApi->update_payment_mode_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_mode_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_mode_update_dto** | [**PaymentModeUpdateDto**](PaymentModeUpdateDto.md)|  | [optional] 

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

