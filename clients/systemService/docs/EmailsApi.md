# openapi_client.EmailsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_preview_basic_email_template**](EmailsApi.md#admin_preview_basic_email_template) | **POST** /api/v2/SystemService/Emails/Preview | Preview a rendered basic email template.
[**admin_send_basic_email**](EmailsApi.md#admin_send_basic_email) | **POST** /api/v2/SystemService/Emails/SendBasic | Send a basic transactional email to recipients.


# **admin_preview_basic_email_template**
> admin_preview_basic_email_template(api_version=api_version, x_api_version=x_api_version, object_email_dispatch_request=object_email_dispatch_request)

Preview a rendered basic email template.

This action is only available for global administrators (business_owner role).

### Example


```python
import openapi_client
from openapi_client.models.object_email_dispatch_request import ObjectEmailDispatchRequest
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
    api_instance = openapi_client.EmailsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    object_email_dispatch_request = openapi_client.ObjectEmailDispatchRequest() # ObjectEmailDispatchRequest |  (optional)

    try:
        # Preview a rendered basic email template.
        api_instance.admin_preview_basic_email_template(api_version=api_version, x_api_version=x_api_version, object_email_dispatch_request=object_email_dispatch_request)
    except Exception as e:
        print("Exception when calling EmailsApi->admin_preview_basic_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **object_email_dispatch_request** | [**ObjectEmailDispatchRequest**](ObjectEmailDispatchRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_send_basic_email**
> TenantDtoListEnvelope admin_send_basic_email(api_version=api_version, x_api_version=x_api_version, object_email_dispatch_request=object_email_dispatch_request)

Send a basic transactional email to recipients.

This action is only available for global administrators (business_owner role).

### Example


```python
import openapi_client
from openapi_client.models.object_email_dispatch_request import ObjectEmailDispatchRequest
from openapi_client.models.tenant_dto_list_envelope import TenantDtoListEnvelope
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
    api_instance = openapi_client.EmailsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    object_email_dispatch_request = openapi_client.ObjectEmailDispatchRequest() # ObjectEmailDispatchRequest |  (optional)

    try:
        # Send a basic transactional email to recipients.
        api_response = api_instance.admin_send_basic_email(api_version=api_version, x_api_version=x_api_version, object_email_dispatch_request=object_email_dispatch_request)
        print("The response of EmailsApi->admin_send_basic_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->admin_send_basic_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **object_email_dispatch_request** | [**ObjectEmailDispatchRequest**](ObjectEmailDispatchRequest.md)|  | [optional] 

### Return type

[**TenantDtoListEnvelope**](TenantDtoListEnvelope.md)

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

