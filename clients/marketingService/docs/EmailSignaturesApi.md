# openapi_client.EmailSignaturesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_signature_async**](EmailSignaturesApi.md#create_email_signature_async) | **POST** /api/v2/MarketingService/EmailSignatures | Create an email signature
[**delete_email_signature_async**](EmailSignaturesApi.md#delete_email_signature_async) | **DELETE** /api/v2/MarketingService/EmailSignatures/{emailsignatureId} | Delete an email signature
[**get_email_signature_details_async**](EmailSignaturesApi.md#get_email_signature_details_async) | **GET** /api/v2/MarketingService/EmailSignatures/{emailsignatureId} | Get email signature by ID
[**get_email_signatures_count_async**](EmailSignaturesApi.md#get_email_signatures_count_async) | **GET** /api/v2/MarketingService/EmailSignatures/Count | Get email signatures count
[**get_email_signatures_o_data_async**](EmailSignaturesApi.md#get_email_signatures_o_data_async) | **GET** /api/v2/MarketingService/EmailSignatures | Get email signatures
[**update_email_signature_async**](EmailSignaturesApi.md#update_email_signature_async) | **PUT** /api/v2/MarketingService/EmailSignatures/{emailsignatureId} | Update an email signature


# **create_email_signature_async**
> EmptyEnvelope create_email_signature_async(tenant_id, email_signature_create_dto, api_version=api_version, x_api_version=x_api_version)

Create an email signature

Creates a new email signature for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.email_signature_create_dto import EmailSignatureCreateDto
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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_signature_create_dto = openapi_client.EmailSignatureCreateDto() # EmailSignatureCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create an email signature
        api_response = api_instance.create_email_signature_async(tenant_id, email_signature_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->create_email_signature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->create_email_signature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_signature_create_dto** | [**EmailSignatureCreateDto**](EmailSignatureCreateDto.md)|  | 
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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_signature_async**
> EmptyEnvelope delete_email_signature_async(tenant_id, emailsignature_id, api_version=api_version, x_api_version=x_api_version)

Delete an email signature

Deletes an email signature by its ID.

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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailsignature_id = 'emailsignature_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an email signature
        api_response = api_instance.delete_email_signature_async(tenant_id, emailsignature_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->delete_email_signature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->delete_email_signature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailsignature_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_signature_details_async**
> EmailSignatureDtoEnvelope get_email_signature_details_async(tenant_id, emailsignature_id, api_version=api_version, x_api_version=x_api_version)

Get email signature by ID

Retrieves the details of a specific email signature by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_signature_dto_envelope import EmailSignatureDtoEnvelope
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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailsignature_id = 'emailsignature_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email signature by ID
        api_response = api_instance.get_email_signature_details_async(tenant_id, emailsignature_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->get_email_signature_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->get_email_signature_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailsignature_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailSignatureDtoEnvelope**](EmailSignatureDtoEnvelope.md)

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

# **get_email_signatures_count_async**
> Int32Envelope get_email_signatures_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email signatures count

Returns the count of email signatures for the specified tenant using OData query options.

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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email signatures count
        api_response = api_instance.get_email_signatures_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->get_email_signatures_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->get_email_signatures_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_signatures_o_data_async**
> EmailSignatureDtoListEnvelope get_email_signatures_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email signatures

Retrieves a collection of email signatures for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.email_signature_dto_list_envelope import EmailSignatureDtoListEnvelope
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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email signatures
        api_response = api_instance.get_email_signatures_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->get_email_signatures_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->get_email_signatures_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailSignatureDtoListEnvelope**](EmailSignatureDtoListEnvelope.md)

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

# **update_email_signature_async**
> EmptyEnvelope update_email_signature_async(tenant_id, emailsignature_id, email_signature_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an email signature

Updates an existing email signature by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_signature_update_dto import EmailSignatureUpdateDto
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
    api_instance = openapi_client.EmailSignaturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    emailsignature_id = 'emailsignature_id_example' # str | 
    email_signature_update_dto = openapi_client.EmailSignatureUpdateDto() # EmailSignatureUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an email signature
        api_response = api_instance.update_email_signature_async(tenant_id, emailsignature_id, email_signature_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailSignaturesApi->update_email_signature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSignaturesApi->update_email_signature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **emailsignature_id** | **str**|  | 
 **email_signature_update_dto** | [**EmailSignatureUpdateDto**](EmailSignatureUpdateDto.md)|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

