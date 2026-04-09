# openapi_client.PricingRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_rule**](PricingRulesApi.md#create_pricing_rule) | **POST** /api/v2/CatalogService/PricingRules | Create a new pricing rule
[**delete_pricing_rule**](PricingRulesApi.md#delete_pricing_rule) | **DELETE** /api/v2/CatalogService/PricingRules/{pricingRuleId} | Delete a pricing rule
[**get_pricing_rule_by_id**](PricingRulesApi.md#get_pricing_rule_by_id) | **GET** /api/v2/CatalogService/PricingRules/{pricingRuleId} | Get pricing rule by ID
[**get_pricing_rules**](PricingRulesApi.md#get_pricing_rules) | **GET** /api/v2/CatalogService/PricingRules | Get all pricing rules
[**update_pricing_rule**](PricingRulesApi.md#update_pricing_rule) | **PUT** /api/v2/CatalogService/PricingRules/Update | Update a pricing rule


# **create_pricing_rule**
> PricingRuleDtoEnvelope create_pricing_rule(tenant_id, api_version=api_version, x_api_version=x_api_version, pricing_rule_create_dto=pricing_rule_create_dto)

Create a new pricing rule

Creates a new pricing rule for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_create_dto import PricingRuleCreateDto
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope
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
    api_instance = openapi_client.PricingRulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    pricing_rule_create_dto = openapi_client.PricingRuleCreateDto() # PricingRuleCreateDto |  (optional)

    try:
        # Create a new pricing rule
        api_response = api_instance.create_pricing_rule(tenant_id, api_version=api_version, x_api_version=x_api_version, pricing_rule_create_dto=pricing_rule_create_dto)
        print("The response of PricingRulesApi->create_pricing_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingRulesApi->create_pricing_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **pricing_rule_create_dto** | [**PricingRuleCreateDto**](PricingRuleCreateDto.md)|  | [optional] 

### Return type

[**PricingRuleDtoEnvelope**](PricingRuleDtoEnvelope.md)

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

# **delete_pricing_rule**
> delete_pricing_rule(tenant_id, pricing_rule_id, api_version=api_version, x_api_version=x_api_version)

Delete a pricing rule

Deletes a pricing rule for the specified tenant and rule ID.

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
    api_instance = openapi_client.PricingRulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pricing_rule_id = 'pricing_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a pricing rule
        api_instance.delete_pricing_rule(tenant_id, pricing_rule_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling PricingRulesApi->delete_pricing_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pricing_rule_id** | **str**|  | 
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

# **get_pricing_rule_by_id**
> PricingRuleDtoEnvelope get_pricing_rule_by_id(pricing_rule_id, api_version=api_version, x_api_version=x_api_version)

Get pricing rule by ID

Retrieves a pricing rule by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope
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
    api_instance = openapi_client.PricingRulesApi(api_client)
    pricing_rule_id = 'pricing_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get pricing rule by ID
        api_response = api_instance.get_pricing_rule_by_id(pricing_rule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricingRulesApi->get_pricing_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingRulesApi->get_pricing_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_rule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PricingRuleDtoEnvelope**](PricingRuleDtoEnvelope.md)

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

# **get_pricing_rules**
> PricingRuleDtoListEnvelope get_pricing_rules(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all pricing rules

Retrieves all pricing rules for the specified tenant, with optional OData query options.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_list_envelope import PricingRuleDtoListEnvelope
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
    api_instance = openapi_client.PricingRulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all pricing rules
        api_response = api_instance.get_pricing_rules(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PricingRulesApi->get_pricing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingRulesApi->get_pricing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PricingRuleDtoListEnvelope**](PricingRuleDtoListEnvelope.md)

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

# **update_pricing_rule**
> update_pricing_rule(tenant_id, pricing_rule_id, api_version=api_version, x_api_version=x_api_version, pricing_rule_update_dto=pricing_rule_update_dto)

Update a pricing rule

Updates an existing pricing rule for the specified tenant and rule ID.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_update_dto import PricingRuleUpdateDto
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
    api_instance = openapi_client.PricingRulesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pricing_rule_id = 'pricing_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    pricing_rule_update_dto = openapi_client.PricingRuleUpdateDto() # PricingRuleUpdateDto |  (optional)

    try:
        # Update a pricing rule
        api_instance.update_pricing_rule(tenant_id, pricing_rule_id, api_version=api_version, x_api_version=x_api_version, pricing_rule_update_dto=pricing_rule_update_dto)
    except Exception as e:
        print("Exception when calling PricingRulesApi->update_pricing_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pricing_rule_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **pricing_rule_update_dto** | [**PricingRuleUpdateDto**](PricingRuleUpdateDto.md)|  | [optional] 

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

