# openapi_client.BusinessDomainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_domain_async**](BusinessDomainsApi.md#create_business_domain_async) | **POST** /api/v2/ContentService/BusinessDomains | Register a business domain
[**delete_business_domain_async**](BusinessDomainsApi.md#delete_business_domain_async) | **DELETE** /api/v2/ContentService/BusinessDomains/{businessDomainId} | Delete a business domain
[**get_business_domain_by_id_async**](BusinessDomainsApi.md#get_business_domain_by_id_async) | **GET** /api/v2/ContentService/BusinessDomains/{businessDomainId} | Get business domain by ID
[**get_business_domains_async**](BusinessDomainsApi.md#get_business_domains_async) | **GET** /api/v2/ContentService/BusinessDomains | Get business domains
[**get_business_domains_count_async**](BusinessDomainsApi.md#get_business_domains_count_async) | **GET** /api/v2/ContentService/BusinessDomains/Count | Get business domains count
[**update_business_domain_async**](BusinessDomainsApi.md#update_business_domain_async) | **PUT** /api/v2/ContentService/BusinessDomains/{businessDomainId} | Update a business domain
[**verify_business_domain_async**](BusinessDomainsApi.md#verify_business_domain_async) | **POST** /api/v2/ContentService/BusinessDomains/{businessDomainId}/Verify | Verify a business domain


# **create_business_domain_async**
> EmptyEnvelope create_business_domain_async(tenant_id, business_domain_create_dto, api_version=api_version, x_api_version=x_api_version)

Register a business domain

Registers a new (unverified) business domain for the tenant and issues a DNS TXT verification token.

### Example


```python
import openapi_client
from openapi_client.models.business_domain_create_dto import BusinessDomainCreateDto
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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_domain_create_dto = openapi_client.BusinessDomainCreateDto() # BusinessDomainCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Register a business domain
        api_response = api_instance.create_business_domain_async(tenant_id, business_domain_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->create_business_domain_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->create_business_domain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_domain_create_dto** | [**BusinessDomainCreateDto**](BusinessDomainCreateDto.md)|  | 
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

# **delete_business_domain_async**
> EmptyEnvelope delete_business_domain_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)

Delete a business domain

Removes a business domain from the tenant.

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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a business domain
        api_response = api_instance.delete_business_domain_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->delete_business_domain_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->delete_business_domain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_domain_id** | **str**|  | 
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

# **get_business_domain_by_id_async**
> BusinessDomainDtoEnvelope get_business_domain_by_id_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)

Get business domain by ID

Retrieves a specific business domain.

### Example


```python
import openapi_client
from openapi_client.models.business_domain_dto_envelope import BusinessDomainDtoEnvelope
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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business domain by ID
        api_response = api_instance.get_business_domain_by_id_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_business_domain_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_business_domain_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_domain_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessDomainDtoEnvelope**](BusinessDomainDtoEnvelope.md)

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

# **get_business_domains_async**
> BusinessDomainDtoListEnvelope get_business_domains_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get business domains

Retrieves business domains for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.business_domain_dto_list_envelope import BusinessDomainDtoListEnvelope
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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business domains
        api_response = api_instance.get_business_domains_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_business_domains_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_business_domains_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BusinessDomainDtoListEnvelope**](BusinessDomainDtoListEnvelope.md)

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

# **get_business_domains_count_async**
> Int32Envelope get_business_domains_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get business domains count

Retrieves the count of business domains for the specified tenant.

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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get business domains count
        api_response = api_instance.get_business_domains_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_business_domains_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_business_domains_count_async: %s\n" % e)
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

# **update_business_domain_async**
> EmptyEnvelope update_business_domain_async(tenant_id, business_domain_id, business_domain_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a business domain

Updates a business domain. Changing the host re-issues the verification token and clears verification.

### Example


```python
import openapi_client
from openapi_client.models.business_domain_update_dto import BusinessDomainUpdateDto
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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_domain_id = 'business_domain_id_example' # str | 
    business_domain_update_dto = openapi_client.BusinessDomainUpdateDto() # BusinessDomainUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a business domain
        api_response = api_instance.update_business_domain_async(tenant_id, business_domain_id, business_domain_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->update_business_domain_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->update_business_domain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_domain_id** | **str**|  | 
 **business_domain_update_dto** | [**BusinessDomainUpdateDto**](BusinessDomainUpdateDto.md)|  | 
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

# **verify_business_domain_async**
> EmptyEnvelope verify_business_domain_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)

Verify a business domain

Checks the domain's DNS TXT records for the verification token and marks the domain verified.

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
    api_instance = openapi_client.BusinessDomainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Verify a business domain
        api_response = api_instance.verify_business_domain_async(tenant_id, business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->verify_business_domain_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->verify_business_domain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **business_domain_id** | **str**|  | 
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

