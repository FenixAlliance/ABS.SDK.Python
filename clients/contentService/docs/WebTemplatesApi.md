# openapi_client.WebTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_web_templates_async**](WebTemplatesApi.md#count_web_templates_async) | **GET** /api/v2/ContentService/WebTemplates/Count | Count web templates
[**create_web_template_async**](WebTemplatesApi.md#create_web_template_async) | **POST** /api/v2/ContentService/WebTemplates | Create a web template
[**delete_web_template_async**](WebTemplatesApi.md#delete_web_template_async) | **DELETE** /api/v2/ContentService/WebTemplates/{webTemplateId} | Delete a web template
[**get_web_template_by_id_async**](WebTemplatesApi.md#get_web_template_by_id_async) | **GET** /api/v2/ContentService/WebTemplates/{webTemplateId} | Get web template by ID
[**get_web_templates_async**](WebTemplatesApi.md#get_web_templates_async) | **GET** /api/v2/ContentService/WebTemplates | Get web templates
[**update_web_template_async**](WebTemplatesApi.md#update_web_template_async) | **PUT** /api/v2/ContentService/WebTemplates/{webTemplateId} | Update a web template


# **count_web_templates_async**
> Int32Envelope count_web_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count web templates

Counts all web templates for the specified tenant.

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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count web templates
        api_response = api_instance.count_web_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebTemplatesApi->count_web_templates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->count_web_templates_async: %s\n" % e)
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

# **create_web_template_async**
> create_web_template_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_template_create_dto=web_template_create_dto)

Create a web template

Creates a new web template for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_template_create_dto import WebTemplateCreateDto
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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_template_create_dto = openapi_client.WebTemplateCreateDto() # WebTemplateCreateDto |  (optional)

    try:
        # Create a web template
        api_instance.create_web_template_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_template_create_dto=web_template_create_dto)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->create_web_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_template_create_dto** | [**WebTemplateCreateDto**](WebTemplateCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

# **delete_web_template_async**
> delete_web_template_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version)

Delete a web template

Deletes a web template for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_template_id = 'web_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web template
        api_instance.delete_web_template_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->delete_web_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **get_web_template_by_id_async**
> WebTemplateDtoEnvelope get_web_template_by_id_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version)

Get web template by ID

Retrieves a specific web template by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.web_template_dto_envelope import WebTemplateDtoEnvelope
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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_template_id = 'web_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web template by ID
        api_response = api_instance.get_web_template_by_id_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebTemplatesApi->get_web_template_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->get_web_template_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebTemplateDtoEnvelope**](WebTemplateDtoEnvelope.md)

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

# **get_web_templates_async**
> WebTemplateDtoListEnvelope get_web_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get web templates

Retrieves all web templates for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_template_dto_list_envelope import WebTemplateDtoListEnvelope
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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get web templates
        api_response = api_instance.get_web_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WebTemplatesApi->get_web_templates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->get_web_templates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebTemplateDtoListEnvelope**](WebTemplateDtoListEnvelope.md)

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

# **update_web_template_async**
> update_web_template_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version, web_template_update_dto=web_template_update_dto)

Update a web template

Updates an existing web template for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.web_template_update_dto import WebTemplateUpdateDto
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
    api_instance = openapi_client.WebTemplatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    web_template_id = 'web_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_template_update_dto = openapi_client.WebTemplateUpdateDto() # WebTemplateUpdateDto |  (optional)

    try:
        # Update a web template
        api_instance.update_web_template_async(tenant_id, web_template_id, api_version=api_version, x_api_version=x_api_version, web_template_update_dto=web_template_update_dto)
    except Exception as e:
        print("Exception when calling WebTemplatesApi->update_web_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **web_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_template_update_dto** | [**WebTemplateUpdateDto**](WebTemplateUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

