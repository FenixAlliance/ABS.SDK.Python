# openapi_client.CommissionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_commission_async**](CommissionsApi.md#create_commission_async) | **POST** /api/v2/AccountingService/Commissions/Commissions | Create a commission
[**create_payment_commission_async**](CommissionsApi.md#create_payment_commission_async) | **POST** /api/v2/AccountingService/Commissions/PaymentCommissions | Create a payment commission
[**delete_commission_async**](CommissionsApi.md#delete_commission_async) | **DELETE** /api/v2/AccountingService/Commissions/Commissions/{commissionId} | Delete a commission
[**delete_payment_commission_async**](CommissionsApi.md#delete_payment_commission_async) | **DELETE** /api/v2/AccountingService/Commissions/PaymentCommissions/{paymentCommissionId} | Delete a payment commission
[**get_commission_async**](CommissionsApi.md#get_commission_async) | **GET** /api/v2/AccountingService/Commissions/Commissions/{commissionId} | Get a commission by id
[**get_commissions_async**](CommissionsApi.md#get_commissions_async) | **GET** /api/v2/AccountingService/Commissions/Commissions | Get all commissions for a tenant
[**get_commissions_count_async**](CommissionsApi.md#get_commissions_count_async) | **GET** /api/v2/AccountingService/Commissions/Commissions/Count | Get the count of commissions for a tenant
[**get_payment_commission_async**](CommissionsApi.md#get_payment_commission_async) | **GET** /api/v2/AccountingService/Commissions/PaymentCommissions/{paymentCommissionId} | Get a payment commission by id
[**get_payment_commissions_async**](CommissionsApi.md#get_payment_commissions_async) | **GET** /api/v2/AccountingService/Commissions/PaymentCommissions | Get all payment commissions for a tenant
[**get_payment_commissions_count_async**](CommissionsApi.md#get_payment_commissions_count_async) | **GET** /api/v2/AccountingService/Commissions/PaymentCommissions/Count | Get the count of payment commissions for a tenant
[**update_commission_async**](CommissionsApi.md#update_commission_async) | **PUT** /api/v2/AccountingService/Commissions/Commissions/{commissionId} | Update a commission
[**update_payment_commission_async**](CommissionsApi.md#update_payment_commission_async) | **PUT** /api/v2/AccountingService/Commissions/PaymentCommissions/{paymentCommissionId} | Update a payment commission


# **create_commission_async**
> EmptyEnvelope create_commission_async(tenant_id, commission_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a commission

Creates a new commission.

### Example


```python
import openapi_client
from openapi_client.models.commission_create_dto import CommissionCreateDto
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    commission_create_dto = openapi_client.CommissionCreateDto() # CommissionCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a commission
        api_response = api_instance.create_commission_async(tenant_id, commission_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->create_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->create_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **commission_create_dto** | [**CommissionCreateDto**](CommissionCreateDto.md)|  | 
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

# **create_payment_commission_async**
> EmptyEnvelope create_payment_commission_async(tenant_id, payment_commission_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a payment commission

Creates a new payment commission.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_commission_create_dto import PaymentCommissionCreateDto
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_commission_create_dto = openapi_client.PaymentCommissionCreateDto() # PaymentCommissionCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a payment commission
        api_response = api_instance.create_payment_commission_async(tenant_id, payment_commission_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->create_payment_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->create_payment_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_commission_create_dto** | [**PaymentCommissionCreateDto**](PaymentCommissionCreateDto.md)|  | 
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

# **delete_commission_async**
> EmptyEnvelope delete_commission_async(tenant_id, commission_id, api_version=api_version, x_api_version=x_api_version)

Delete a commission

Deletes a commission.

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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    commission_id = 'commission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a commission
        api_response = api_instance.delete_commission_async(tenant_id, commission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->delete_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->delete_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **commission_id** | **str**|  | 
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

# **delete_payment_commission_async**
> EmptyEnvelope delete_payment_commission_async(tenant_id, payment_commission_id, api_version=api_version, x_api_version=x_api_version)

Delete a payment commission

Deletes a payment commission.

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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_commission_id = 'payment_commission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a payment commission
        api_response = api_instance.delete_payment_commission_async(tenant_id, payment_commission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->delete_payment_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->delete_payment_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_commission_id** | **str**|  | 
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

# **get_commission_async**
> CommissionDtoEnvelope get_commission_async(tenant_id, commission_id, api_version=api_version, x_api_version=x_api_version)

Get a commission by id

Retrieves a commission by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.commission_dto_envelope import CommissionDtoEnvelope
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    commission_id = 'commission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a commission by id
        api_response = api_instance.get_commission_async(tenant_id, commission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **commission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CommissionDtoEnvelope**](CommissionDtoEnvelope.md)

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

# **get_commissions_async**
> CommissionDtoListEnvelope get_commissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all commissions for a tenant

Retrieves all commissions for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.commission_dto_list_envelope import CommissionDtoListEnvelope
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all commissions for a tenant
        api_response = api_instance.get_commissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_commissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CommissionDtoListEnvelope**](CommissionDtoListEnvelope.md)

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

# **get_commissions_count_async**
> Int32Envelope get_commissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of commissions for a tenant

Retrieves the count of commissions for the specified tenant using OData query options.

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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of commissions for a tenant
        api_response = api_instance.get_commissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_commissions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commissions_count_async: %s\n" % e)
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

# **get_payment_commission_async**
> PaymentCommissionDtoEnvelope get_payment_commission_async(tenant_id, payment_commission_id, api_version=api_version, x_api_version=x_api_version)

Get a payment commission by id

Retrieves a payment commission by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.payment_commission_dto_envelope import PaymentCommissionDtoEnvelope
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_commission_id = 'payment_commission_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a payment commission by id
        api_response = api_instance.get_payment_commission_async(tenant_id, payment_commission_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_payment_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_payment_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_commission_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentCommissionDtoEnvelope**](PaymentCommissionDtoEnvelope.md)

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

# **get_payment_commissions_async**
> PaymentCommissionDtoListEnvelope get_payment_commissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all payment commissions for a tenant

Retrieves all payment commissions for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.payment_commission_dto_list_envelope import PaymentCommissionDtoListEnvelope
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all payment commissions for a tenant
        api_response = api_instance.get_payment_commissions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_payment_commissions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_payment_commissions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentCommissionDtoListEnvelope**](PaymentCommissionDtoListEnvelope.md)

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

# **get_payment_commissions_count_async**
> Int32Envelope get_payment_commissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of payment commissions for a tenant

Retrieves the count of payment commissions for the specified tenant using OData query options.

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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of payment commissions for a tenant
        api_response = api_instance.get_payment_commissions_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->get_payment_commissions_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_payment_commissions_count_async: %s\n" % e)
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

# **update_commission_async**
> EmptyEnvelope update_commission_async(tenant_id, commission_id, commission_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a commission

Updates an existing commission.

### Example


```python
import openapi_client
from openapi_client.models.commission_update_dto import CommissionUpdateDto
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    commission_id = 'commission_id_example' # str | 
    commission_update_dto = openapi_client.CommissionUpdateDto() # CommissionUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a commission
        api_response = api_instance.update_commission_async(tenant_id, commission_id, commission_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->update_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->update_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **commission_id** | **str**|  | 
 **commission_update_dto** | [**CommissionUpdateDto**](CommissionUpdateDto.md)|  | 
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

# **update_payment_commission_async**
> EmptyEnvelope update_payment_commission_async(tenant_id, payment_commission_id, payment_commission_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a payment commission

Updates an existing payment commission.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_commission_update_dto import PaymentCommissionUpdateDto
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
    api_instance = openapi_client.CommissionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payment_commission_id = 'payment_commission_id_example' # str | 
    payment_commission_update_dto = openapi_client.PaymentCommissionUpdateDto() # PaymentCommissionUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a payment commission
        api_response = api_instance.update_payment_commission_async(tenant_id, payment_commission_id, payment_commission_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CommissionsApi->update_payment_commission_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->update_payment_commission_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payment_commission_id** | **str**|  | 
 **payment_commission_update_dto** | [**PaymentCommissionUpdateDto**](PaymentCommissionUpdateDto.md)|  | 
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

