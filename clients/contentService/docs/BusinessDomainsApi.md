# openapi_client.BusinessDomainsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_domain_by_id_async**](BusinessDomainsApi.md#get_business_domain_by_id_async) | **GET** /api/v2/ContentService/BusinessDomains/{businessDomainId} | Get business domain by ID
[**get_business_domains_async**](BusinessDomainsApi.md#get_business_domains_async) | **GET** /api/v2/ContentService/BusinessDomains | Get business domains
[**get_business_domains_count_async**](BusinessDomainsApi.md#get_business_domains_count_async) | **GET** /api/v2/ContentService/BusinessDomains/Count | Get business domains count


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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
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

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
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

