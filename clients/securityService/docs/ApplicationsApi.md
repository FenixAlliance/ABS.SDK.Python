# openapi_client.ApplicationsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_application_async**](ApplicationsApi.md#create_business_application_async) | **POST** /api/v2/SecurityService/Applications | Create a new business application
[**delete_business_application_async**](ApplicationsApi.md#delete_business_application_async) | **DELETE** /api/v2/SecurityService/Applications/{applicationId} | Delete a business application
[**get_business_application_by_id_async**](ApplicationsApi.md#get_business_application_by_id_async) | **GET** /api/v2/SecurityService/Applications/{applicationId} | Get business application by ID
[**get_business_applications_async**](ApplicationsApi.md#get_business_applications_async) | **GET** /api/v2/SecurityService/Applications | Get all business applications
[**get_business_applications_count_async**](ApplicationsApi.md#get_business_applications_count_async) | **GET** /api/v2/SecurityService/Applications/Count | Get business applications count
[**update_business_application_async**](ApplicationsApi.md#update_business_application_async) | **PUT** /api/v2/SecurityService/Applications/{applicationId} | Update an existing business application


# **create_business_application_async**
> EmptyEnvelope create_business_application_async(tenant_id, business_application_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a new business application

Creates a new business application for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.business_application_create_dto import BusinessApplicationCreateDto
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_application_create_dto = openapi_client.BusinessApplicationCreateDto() # BusinessApplicationCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a new business application
        api_response = api_instance.create_business_application_async(tenant_id, business_application_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->create_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_application_create_dto** | [**BusinessApplicationCreateDto**](BusinessApplicationCreateDto.md)|  | 
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

# **delete_business_application_async**
> EmptyEnvelope delete_business_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Delete a business application

Deletes an existing business application for the specified tenant.

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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a business application
        api_response = api_instance.delete_business_application_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->delete_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_application_by_id_async**
> BusinessApplicationDtoEnvelope get_business_application_by_id_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)

Get business application by ID

Retrieves a specific business application by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.business_application_dto_envelope import BusinessApplicationDtoEnvelope
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business application by ID
        api_response = api_instance.get_business_application_by_id_async(tenant_id, application_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->get_business_application_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_business_application_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessApplicationDtoEnvelope**](BusinessApplicationDtoEnvelope.md)

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

# **get_business_applications_async**
> BusinessApplicationDtoListEnvelope get_business_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all business applications

Retrieves all business applications for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.business_application_dto_list_envelope import BusinessApplicationDtoListEnvelope
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all business applications
        api_response = api_instance.get_business_applications_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->get_business_applications_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_business_applications_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessApplicationDtoListEnvelope**](BusinessApplicationDtoListEnvelope.md)

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

# **get_business_applications_count_async**
> Int32Envelope get_business_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get business applications count

Retrieves the count of business applications for the specified tenant.

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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business applications count
        api_response = api_instance.get_business_applications_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->get_business_applications_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_business_applications_count_async: %s\n" % e)
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

# **update_business_application_async**
> EmptyEnvelope update_business_application_async(tenant_id, application_id, business_application_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an existing business application

Updates an existing business application for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.business_application_update_dto import BusinessApplicationUpdateDto
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    application_id = 'application_id_example' # str | 
    business_application_update_dto = openapi_client.BusinessApplicationUpdateDto() # BusinessApplicationUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an existing business application
        api_response = api_instance.update_business_application_async(tenant_id, application_id, business_application_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ApplicationsApi->update_business_application_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_business_application_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **application_id** | **str**|  | 
 **business_application_update_dto** | [**BusinessApplicationUpdateDto**](BusinessApplicationUpdateDto.md)|  | 
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

