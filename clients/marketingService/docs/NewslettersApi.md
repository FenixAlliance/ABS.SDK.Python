# openapi_client.NewslettersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_newsletter_async**](NewslettersApi.md#create_newsletter_async) | **POST** /api/v2/MarketingService/Newsletters | Create a newsletter
[**delete_newsletter_async**](NewslettersApi.md#delete_newsletter_async) | **DELETE** /api/v2/MarketingService/Newsletters/{newsletterId} | Delete a newsletter
[**get_newsletter_details_async**](NewslettersApi.md#get_newsletter_details_async) | **GET** /api/v2/MarketingService/Newsletters/{newsletterId} | Get newsletter by ID
[**get_newsletter_o_data_async**](NewslettersApi.md#get_newsletter_o_data_async) | **GET** /api/v2/MarketingService/Newsletters | Get newsletters
[**get_newsletters_count_async**](NewslettersApi.md#get_newsletters_count_async) | **GET** /api/v2/MarketingService/Newsletters/Count | Get newsletters count
[**update_newsletter_async**](NewslettersApi.md#update_newsletter_async) | **PUT** /api/v2/MarketingService/Newsletters/{newsletterId} | Update a newsletter


# **create_newsletter_async**
> EmptyEnvelope create_newsletter_async(tenant_id, newsletter_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a newsletter

Creates a new newsletter for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.newsletter_create_dto import NewsletterCreateDto
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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    newsletter_create_dto = openapi_client.NewsletterCreateDto() # NewsletterCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a newsletter
        api_response = api_instance.create_newsletter_async(tenant_id, newsletter_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of NewslettersApi->create_newsletter_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewslettersApi->create_newsletter_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **newsletter_create_dto** | [**NewsletterCreateDto**](NewsletterCreateDto.md)|  | 
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

# **delete_newsletter_async**
> EmptyEnvelope delete_newsletter_async(tenant_id, newsletter_id, api_version=api_version, x_api_version=x_api_version)

Delete a newsletter

Deletes a newsletter by its ID.

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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    newsletter_id = 'newsletter_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a newsletter
        api_response = api_instance.delete_newsletter_async(tenant_id, newsletter_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of NewslettersApi->delete_newsletter_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewslettersApi->delete_newsletter_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **newsletter_id** | **str**|  | 
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

# **get_newsletter_details_async**
> NewsletterDtoEnvelope get_newsletter_details_async(tenant_id, newsletter_id, api_version=api_version, x_api_version=x_api_version)

Get newsletter by ID

Retrieves the details of a specific newsletter by its ID.

### Example


```python
import openapi_client
from openapi_client.models.newsletter_dto_envelope import NewsletterDtoEnvelope
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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    newsletter_id = 'newsletter_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get newsletter by ID
        api_response = api_instance.get_newsletter_details_async(tenant_id, newsletter_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of NewslettersApi->get_newsletter_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewslettersApi->get_newsletter_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **newsletter_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NewsletterDtoEnvelope**](NewsletterDtoEnvelope.md)

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

# **get_newsletter_o_data_async**
> get_newsletter_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get newsletters

Retrieves a collection of newsletters for the specified tenant using OData query options.

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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get newsletters
        api_instance.get_newsletter_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling NewslettersApi->get_newsletter_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_newsletters_count_async**
> Int32Envelope get_newsletters_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get newsletters count

Returns the count of newsletters for the specified tenant using OData query options.

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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get newsletters count
        api_response = api_instance.get_newsletters_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of NewslettersApi->get_newsletters_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewslettersApi->get_newsletters_count_async: %s\n" % e)
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

# **update_newsletter_async**
> EmptyEnvelope update_newsletter_async(tenant_id, newsletter_id, newsletter_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a newsletter

Updates an existing newsletter by its ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.newsletter_update_dto import NewsletterUpdateDto
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
    api_instance = openapi_client.NewslettersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    newsletter_id = 'newsletter_id_example' # str | 
    newsletter_update_dto = openapi_client.NewsletterUpdateDto() # NewsletterUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a newsletter
        api_response = api_instance.update_newsletter_async(tenant_id, newsletter_id, newsletter_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of NewslettersApi->update_newsletter_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewslettersApi->update_newsletter_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **newsletter_id** | **str**|  | 
 **newsletter_update_dto** | [**NewsletterUpdateDto**](NewsletterUpdateDto.md)|  | 
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

