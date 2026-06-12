# openapi_client.BusinessDomainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_business_domain**](BusinessDomainsApi.md#delete_system_business_domain) | **DELETE** /api/v2/SystemService/BusinessDomains/{businessDomainId} | Delete a business domain
[**get_system_business_domain_by_id**](BusinessDomainsApi.md#get_system_business_domain_by_id) | **GET** /api/v2/SystemService/BusinessDomains/{businessDomainId} | Retrieve a business domain by its ID
[**get_system_business_domains**](BusinessDomainsApi.md#get_system_business_domains) | **GET** /api/v2/SystemService/BusinessDomains | Retrieve all business domains in the system
[**get_system_business_domains_count**](BusinessDomainsApi.md#get_system_business_domains_count) | **GET** /api/v2/SystemService/BusinessDomains/Count | Get the count of all business domains in the system
[**verify_system_business_domain**](BusinessDomainsApi.md#verify_system_business_domain) | **POST** /api/v2/SystemService/BusinessDomains/{businessDomainId}/Verify | Verify a business domain


# **delete_system_business_domain**
> EmptyEnvelope delete_system_business_domain(business_domain_id, api_version=api_version, x_api_version=x_api_version)

Delete a business domain

Removes any business domain from the system, regardless of owning tenant.

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
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a business domain
        api_response = api_instance.delete_system_business_domain(business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->delete_system_business_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->delete_system_business_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_system_business_domain_by_id**
> BusinessDomainDtoEnvelope get_system_business_domain_by_id(business_domain_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a business domain by its ID

Retrieve any business domain by its ID, regardless of owning tenant.

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
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a business domain by its ID
        api_response = api_instance.get_system_business_domain_by_id(business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_system_business_domain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_system_business_domain_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_system_business_domains**
> BusinessDomainDtoListEnvelope get_system_business_domains(api_version=api_version, x_api_version=x_api_version)

Retrieve all business domains in the system

Retrieve all registered business domains across every tenant (global administrators only).

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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve all business domains in the system
        api_response = api_instance.get_system_business_domains(api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_system_business_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_system_business_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_system_business_domains_count**
> Int32Envelope get_system_business_domains_count(api_version=api_version, x_api_version=x_api_version)

Get the count of all business domains in the system

Get the count of all registered business domains across every tenant.

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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of all business domains in the system
        api_response = api_instance.get_system_business_domains_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->get_system_business_domains_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->get_system_business_domains_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **verify_system_business_domain**
> EmptyEnvelope verify_system_business_domain(business_domain_id, api_version=api_version, x_api_version=x_api_version)

Verify a business domain

Checks the domain's DNS TXT records for the verification token and marks it verified.

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
    business_domain_id = 'business_domain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Verify a business domain
        api_response = api_instance.verify_system_business_domain(business_domain_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BusinessDomainsApi->verify_system_business_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessDomainsApi->verify_system_business_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

