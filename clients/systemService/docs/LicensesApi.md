# openapi_client.LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_licensing_licenses_generate_post**](LicensesApi.md#api_licensing_licenses_generate_post) | **POST** /api/Licensing/Licenses/Generate | 
[**api_licensing_licenses_validate_attributes_get**](LicensesApi.md#api_licensing_licenses_validate_attributes_get) | **GET** /api/Licensing/Licenses/Validate/Attributes | 
[**api_licensing_licenses_validate_errors_get**](LicensesApi.md#api_licensing_licenses_validate_errors_get) | **GET** /api/Licensing/Licenses/Validate/Errors | 
[**api_licensing_licenses_validate_get**](LicensesApi.md#api_licensing_licenses_validate_get) | **GET** /api/Licensing/Licenses/Validate | 


# **api_licensing_licenses_generate_post**
> StringEnvelope api_licensing_licenses_generate_post(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key_request=license_key_request)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.license_key_request import LicenseKeyRequest
from openapi_client.models.string_envelope import StringEnvelope
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
    api_instance = openapi_client.LicensesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    license_key_request = openapi_client.LicenseKeyRequest() # LicenseKeyRequest |  (optional)

    try:
        api_response = api_instance.api_licensing_licenses_generate_post(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key_request=license_key_request)
        print("The response of LicensesApi->api_licensing_licenses_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->api_licensing_licenses_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **license_key_request** | [**LicenseKeyRequest**](LicenseKeyRequest.md)|  | [optional] 

### Return type

[**StringEnvelope**](StringEnvelope.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_licensing_licenses_validate_attributes_get**
> LicenseAttributesListEnvelope api_licensing_licenses_validate_attributes_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.license_attributes_list_envelope import LicenseAttributesListEnvelope
from openapi_client.models.license_key import LicenseKey
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
    api_instance = openapi_client.LicensesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    license_key = openapi_client.LicenseKey() # LicenseKey |  (optional)

    try:
        api_response = api_instance.api_licensing_licenses_validate_attributes_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)
        print("The response of LicensesApi->api_licensing_licenses_validate_attributes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->api_licensing_licenses_validate_attributes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **license_key** | [**LicenseKey**](LicenseKey.md)|  | [optional] 

### Return type

[**LicenseAttributesListEnvelope**](LicenseAttributesListEnvelope.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_licensing_licenses_validate_errors_get**
> LicenseValidationErrorListEnvelope api_licensing_licenses_validate_errors_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.license_key import LicenseKey
from openapi_client.models.license_validation_error_list_envelope import LicenseValidationErrorListEnvelope
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
    api_instance = openapi_client.LicensesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    license_key = openapi_client.LicenseKey() # LicenseKey |  (optional)

    try:
        api_response = api_instance.api_licensing_licenses_validate_errors_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)
        print("The response of LicensesApi->api_licensing_licenses_validate_errors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->api_licensing_licenses_validate_errors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **license_key** | [**LicenseKey**](LicenseKey.md)|  | [optional] 

### Return type

[**LicenseValidationErrorListEnvelope**](LicenseValidationErrorListEnvelope.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_licensing_licenses_validate_get**
> BooleanEnvelope api_licensing_licenses_validate_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
from openapi_client.models.license_key import LicenseKey
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
    api_instance = openapi_client.LicensesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    license_key = openapi_client.LicenseKey() # LicenseKey |  (optional)

    try:
        api_response = api_instance.api_licensing_licenses_validate_get(tenant_id, api_version=api_version, x_api_version=x_api_version, license_key=license_key)
        print("The response of LicensesApi->api_licensing_licenses_validate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->api_licensing_licenses_validate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **license_key** | [**LicenseKey**](LicenseKey.md)|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

