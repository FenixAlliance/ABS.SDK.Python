# openapi_client.SecurityCertificatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_certificates_async**](SecurityCertificatesApi.md#get_security_certificates_async) | **GET** /api/v2/SecurityService/SecurityCertificates | Get security certificates
[**get_security_certificates_count_async**](SecurityCertificatesApi.md#get_security_certificates_count_async) | **GET** /api/v2/SecurityService/SecurityCertificates/Count | Get security certificates count


# **get_security_certificates_async**
> SecurityCertificateDtoListEnvelope get_security_certificates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get security certificates

Retrieves security certificates for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.security_certificate_dto_list_envelope import SecurityCertificateDtoListEnvelope
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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get security certificates
        api_response = api_instance.get_security_certificates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SecurityCertificatesApi->get_security_certificates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityCertificatesApi->get_security_certificates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SecurityCertificateDtoListEnvelope**](SecurityCertificateDtoListEnvelope.md)

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

# **get_security_certificates_count_async**
> Int32Envelope get_security_certificates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get security certificates count

Retrieves the count of security certificates for the specified tenant.

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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get security certificates count
        api_response = api_instance.get_security_certificates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SecurityCertificatesApi->get_security_certificates_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityCertificatesApi->get_security_certificates_count_async: %s\n" % e)
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

