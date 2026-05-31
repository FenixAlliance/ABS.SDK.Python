# openapi_client.EmailTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_template_async**](EmailTemplatesApi.md#create_email_template_async) | **POST** /api/v2/MarketingService/EmailTemplates | Create an email template
[**delete_email_template_async**](EmailTemplatesApi.md#delete_email_template_async) | **DELETE** /api/v2/MarketingService/EmailTemplates/{emailTemplateId} | Delete an email template
[**get_email_template_details_async**](EmailTemplatesApi.md#get_email_template_details_async) | **GET** /api/v2/MarketingService/EmailTemplates/{emailTemplateId} | Get email template by ID
[**get_email_templates_count_async**](EmailTemplatesApi.md#get_email_templates_count_async) | **GET** /api/v2/MarketingService/EmailTemplates/Count | Get email templates count
[**get_email_templates_o_data_async**](EmailTemplatesApi.md#get_email_templates_o_data_async) | **GET** /api/v2/MarketingService/EmailTemplates | Get email templates
[**update_email_template_async**](EmailTemplatesApi.md#update_email_template_async) | **PUT** /api/v2/MarketingService/EmailTemplates/{emailTemplateId} | Update an email template


# **create_email_template_async**
> EmptyEnvelope create_email_template_async(tenant_id, email_template_create_dto, api_version=api_version, x_api_version=x_api_version)

Create an email template

Creates a new email template for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.email_template_create_dto import EmailTemplateCreateDto
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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_template_create_dto = openapi_client.EmailTemplateCreateDto() # EmailTemplateCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create an email template
        api_response = api_instance.create_email_template_async(tenant_id, email_template_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->create_email_template_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->create_email_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_template_create_dto** | [**EmailTemplateCreateDto**](EmailTemplateCreateDto.md)|  | 
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

# **delete_email_template_async**
> EmptyEnvelope delete_email_template_async(tenant_id, email_template_id, api_version=api_version, x_api_version=x_api_version)

Delete an email template

Deletes an email template by its ID.

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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_template_id = 'email_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an email template
        api_response = api_instance.delete_email_template_async(tenant_id, email_template_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->delete_email_template_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->delete_email_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_template_id** | **str**|  | 
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

# **get_email_template_details_async**
> EmailTemplateDtoEnvelope get_email_template_details_async(tenant_id, email_template_id, api_version=api_version, x_api_version=x_api_version)

Get email template by ID

Retrieves the details of a specific email template by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_template_dto_envelope import EmailTemplateDtoEnvelope
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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_template_id = 'email_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email template by ID
        api_response = api_instance.get_email_template_details_async(tenant_id, email_template_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->get_email_template_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->get_email_template_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailTemplateDtoEnvelope**](EmailTemplateDtoEnvelope.md)

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

# **get_email_templates_count_async**
> Int32Envelope get_email_templates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email templates count

Returns the count of email templates for the specified tenant using OData query options.

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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email templates count
        api_response = api_instance.get_email_templates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->get_email_templates_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->get_email_templates_count_async: %s\n" % e)
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

# **get_email_templates_o_data_async**
> EmailTemplateDtoListEnvelope get_email_templates_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get email templates

Retrieves a collection of email templates for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.email_template_dto_list_envelope import EmailTemplateDtoListEnvelope
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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get email templates
        api_response = api_instance.get_email_templates_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->get_email_templates_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->get_email_templates_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmailTemplateDtoListEnvelope**](EmailTemplateDtoListEnvelope.md)

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

# **update_email_template_async**
> EmptyEnvelope update_email_template_async(tenant_id, email_template_id, email_template_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an email template

Updates an existing email template by its ID.

### Example


```python
import openapi_client
from openapi_client.models.email_template_update_dto import EmailTemplateUpdateDto
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
    api_instance = openapi_client.EmailTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    email_template_id = 'email_template_id_example' # str | 
    email_template_update_dto = openapi_client.EmailTemplateUpdateDto() # EmailTemplateUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an email template
        api_response = api_instance.update_email_template_async(tenant_id, email_template_id, email_template_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of EmailTemplatesApi->update_email_template_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplatesApi->update_email_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **email_template_id** | **str**|  | 
 **email_template_update_dto** | [**EmailTemplateUpdateDto**](EmailTemplateUpdateDto.md)|  | 
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

