# openapi_client.TaxClassesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_class**](TaxClassesApi.md#create_tax_class) | **POST** /api/v2/AccountingService/TaxClasses | Create a tax class
[**delete_tax_class**](TaxClassesApi.md#delete_tax_class) | **DELETE** /api/v2/AccountingService/TaxClasses/{id} | Delete a tax class
[**get_tax_class**](TaxClassesApi.md#get_tax_class) | **GET** /api/v2/AccountingService/TaxClasses/{id} | Get tax class by ID
[**get_tax_classes**](TaxClassesApi.md#get_tax_classes) | **GET** /api/v2/AccountingService/TaxClasses | Get all tax classes for a tenant
[**get_tax_classes_count**](TaxClassesApi.md#get_tax_classes_count) | **GET** /api/v2/AccountingService/TaxClasses/Count | Get tax classes count
[**update_tax_class**](TaxClassesApi.md#update_tax_class) | **PUT** /api/v2/AccountingService/TaxClasses/{id} | Update a tax class


# **create_tax_class**
> EmptyEnvelope create_tax_class(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_class_create_dto=tax_class_create_dto)

Create a tax class

Creates a new tax class for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_class_create_dto import TaxClassCreateDto
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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_class_create_dto = openapi_client.TaxClassCreateDto() # TaxClassCreateDto |  (optional)

    try:
        # Create a tax class
        api_response = api_instance.create_tax_class(tenant_id, api_version=api_version, x_api_version=x_api_version, tax_class_create_dto=tax_class_create_dto)
        print("The response of TaxClassesApi->create_tax_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->create_tax_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_class_create_dto** | [**TaxClassCreateDto**](TaxClassCreateDto.md)|  | [optional] 

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

# **delete_tax_class**
> EmptyEnvelope delete_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete a tax class

Deletes a tax class identified by its unique identifier.

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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tax class
        api_response = api_instance.delete_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxClassesApi->delete_tax_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->delete_tax_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
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

# **get_tax_class**
> TaxClassDtoEnvelope get_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get tax class by ID

Retrieves a specific tax class by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.tax_class_dto_envelope import TaxClassDtoEnvelope
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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax class by ID
        api_response = api_instance.get_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxClassesApi->get_tax_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->get_tax_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxClassDtoEnvelope**](TaxClassDtoEnvelope.md)

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

# **get_tax_classes**
> TaxClassDtoListEnvelope get_tax_classes(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all tax classes for a tenant

Retrieves all tax classes for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.tax_class_dto_list_envelope import TaxClassDtoListEnvelope
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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all tax classes for a tenant
        api_response = api_instance.get_tax_classes(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxClassesApi->get_tax_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->get_tax_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TaxClassDtoListEnvelope**](TaxClassDtoListEnvelope.md)

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

# **get_tax_classes_count**
> Int32Envelope get_tax_classes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get tax classes count

Returns the count of tax classes for the specified tenant.

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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax classes count
        api_response = api_instance.get_tax_classes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TaxClassesApi->get_tax_classes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->get_tax_classes_count: %s\n" % e)
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

# **update_tax_class**
> EmptyEnvelope update_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_class_update_dto=tax_class_update_dto)

Update a tax class

Updates an existing tax class identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tax_class_update_dto import TaxClassUpdateDto
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
    api_instance = openapi_client.TaxClassesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tax_class_update_dto = openapi_client.TaxClassUpdateDto() # TaxClassUpdateDto |  (optional)

    try:
        # Update a tax class
        api_response = api_instance.update_tax_class(tenant_id, id, api_version=api_version, x_api_version=x_api_version, tax_class_update_dto=tax_class_update_dto)
        print("The response of TaxClassesApi->update_tax_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxClassesApi->update_tax_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tax_class_update_dto** | [**TaxClassUpdateDto**](TaxClassUpdateDto.md)|  | [optional] 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

