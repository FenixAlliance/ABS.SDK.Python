# openapi_client.CostCentresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_centre**](CostCentresApi.md#create_cost_centre) | **POST** /api/v2/AccountingService/CostCentres | Create a cost centre
[**create_cost_centre_budget**](CostCentresApi.md#create_cost_centre_budget) | **POST** /api/v2/AccountingService/CostCentres/CostCentreBudgets | Create a cost centre budget
[**create_cost_centre_group**](CostCentresApi.md#create_cost_centre_group) | **POST** /api/v2/AccountingService/CostCentres/CostCentreGroups | Create a cost centre group
[**delete_cost_centre**](CostCentresApi.md#delete_cost_centre) | **DELETE** /api/v2/AccountingService/CostCentres/{costCentreId} | Delete a cost centre
[**delete_cost_centre_budget**](CostCentresApi.md#delete_cost_centre_budget) | **DELETE** /api/v2/AccountingService/CostCentres/CostCentreBudgets/{budgetId} | Delete a cost centre budget
[**delete_cost_centre_group**](CostCentresApi.md#delete_cost_centre_group) | **DELETE** /api/v2/AccountingService/CostCentres/CostCentreGroups/{groupId} | Delete a cost centre group
[**get_cost_centre**](CostCentresApi.md#get_cost_centre) | **GET** /api/v2/AccountingService/CostCentres/{costCentreId} | Get a cost centre by id
[**get_cost_centre_budget**](CostCentresApi.md#get_cost_centre_budget) | **GET** /api/v2/AccountingService/CostCentres/CostCentreBudgets/{budgetId} | Get a cost centre budget by id
[**get_cost_centre_budgets**](CostCentresApi.md#get_cost_centre_budgets) | **GET** /api/v2/AccountingService/CostCentres/CostCentreBudgets | Get all cost centre budgets for a tenant
[**get_cost_centre_group**](CostCentresApi.md#get_cost_centre_group) | **GET** /api/v2/AccountingService/CostCentres/CostCentreGroups/{groupId} | Get a cost centre group by id
[**get_cost_centre_groups**](CostCentresApi.md#get_cost_centre_groups) | **GET** /api/v2/AccountingService/CostCentres/CostCentreGroups | Get all cost centre groups for a tenant
[**get_cost_centre_groups_count**](CostCentresApi.md#get_cost_centre_groups_count) | **GET** /api/v2/AccountingService/CostCentres/CostCentreGroups/Count | Get the count of cost centre groups for a tenant
[**get_cost_centres**](CostCentresApi.md#get_cost_centres) | **GET** /api/v2/AccountingService/CostCentres | Get all cost centres for a tenant
[**get_cost_centres_count**](CostCentresApi.md#get_cost_centres_count) | **GET** /api/v2/AccountingService/CostCentres/Count | Get the count of cost centres for a tenant
[**update_cost_centre**](CostCentresApi.md#update_cost_centre) | **PUT** /api/v2/AccountingService/CostCentres/{costCentreId} | Update a cost centre
[**update_cost_centre_budget**](CostCentresApi.md#update_cost_centre_budget) | **PUT** /api/v2/AccountingService/CostCentres/CostCentreBudgets/{budgetId} | Update a cost centre budget
[**update_cost_centre_group**](CostCentresApi.md#update_cost_centre_group) | **PUT** /api/v2/AccountingService/CostCentres/CostCentreGroups/{groupId} | Update a cost centre group


# **create_cost_centre**
> EmptyEnvelope create_cost_centre(tenant_id, cost_centre_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a cost centre

Creates a new cost centre.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_create_dto import CostCentreCreateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_create_dto = openapi_client.CostCentreCreateDto() # CostCentreCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a cost centre
        api_response = api_instance.create_cost_centre(tenant_id, cost_centre_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->create_cost_centre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->create_cost_centre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_create_dto** | [**CostCentreCreateDto**](CostCentreCreateDto.md)|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cost_centre_budget**
> EmptyEnvelope create_cost_centre_budget(tenant_id, cost_centre_budget_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a cost centre budget

Creates a new cost centre budget.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_budget_create_dto import CostCentreBudgetCreateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_budget_create_dto = openapi_client.CostCentreBudgetCreateDto() # CostCentreBudgetCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a cost centre budget
        api_response = api_instance.create_cost_centre_budget(tenant_id, cost_centre_budget_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->create_cost_centre_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->create_cost_centre_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_budget_create_dto** | [**CostCentreBudgetCreateDto**](CostCentreBudgetCreateDto.md)|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cost_centre_group**
> EmptyEnvelope create_cost_centre_group(tenant_id, cost_centre_group_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a cost centre group

Creates a new cost centre group.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_group_create_dto import CostCentreGroupCreateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_group_create_dto = openapi_client.CostCentreGroupCreateDto() # CostCentreGroupCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a cost centre group
        api_response = api_instance.create_cost_centre_group(tenant_id, cost_centre_group_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->create_cost_centre_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->create_cost_centre_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_group_create_dto** | [**CostCentreGroupCreateDto**](CostCentreGroupCreateDto.md)|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cost_centre**
> EmptyEnvelope delete_cost_centre(tenant_id, cost_centre_id, api_version=api_version, x_api_version=x_api_version)

Delete a cost centre

Deletes a cost centre.

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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_id = 'cost_centre_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a cost centre
        api_response = api_instance.delete_cost_centre(tenant_id, cost_centre_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->delete_cost_centre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->delete_cost_centre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_id** | **str**|  | 
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

# **delete_cost_centre_budget**
> EmptyEnvelope delete_cost_centre_budget(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)

Delete a cost centre budget

Deletes a cost centre budget.

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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a cost centre budget
        api_response = api_instance.delete_cost_centre_budget(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->delete_cost_centre_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->delete_cost_centre_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
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

# **delete_cost_centre_group**
> EmptyEnvelope delete_cost_centre_group(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)

Delete a cost centre group

Deletes a cost centre group.

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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    group_id = 'group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a cost centre group
        api_response = api_instance.delete_cost_centre_group(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->delete_cost_centre_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->delete_cost_centre_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **group_id** | **str**|  | 
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

# **get_cost_centre**
> CostCentreDtoEnvelope get_cost_centre(tenant_id, cost_centre_id, api_version=api_version, x_api_version=x_api_version)

Get a cost centre by id

Retrieves a cost centre by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_dto_envelope import CostCentreDtoEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_id = 'cost_centre_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a cost centre by id
        api_response = api_instance.get_cost_centre(tenant_id, cost_centre_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreDtoEnvelope**](CostCentreDtoEnvelope.md)

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

# **get_cost_centre_budget**
> CostCentreBudgetDtoEnvelope get_cost_centre_budget(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)

Get a cost centre budget by id

Retrieves a cost centre budget by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_budget_dto_envelope import CostCentreBudgetDtoEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a cost centre budget by id
        api_response = api_instance.get_cost_centre_budget(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreBudgetDtoEnvelope**](CostCentreBudgetDtoEnvelope.md)

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

# **get_cost_centre_budgets**
> CostCentreBudgetDtoListEnvelope get_cost_centre_budgets(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all cost centre budgets for a tenant

Retrieves all cost centre budgets for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_budget_dto_list_envelope import CostCentreBudgetDtoListEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all cost centre budgets for a tenant
        api_response = api_instance.get_cost_centre_budgets(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreBudgetDtoListEnvelope**](CostCentreBudgetDtoListEnvelope.md)

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

# **get_cost_centre_group**
> CostCentreGroupDtoEnvelope get_cost_centre_group(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)

Get a cost centre group by id

Retrieves a cost centre group by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_group_dto_envelope import CostCentreGroupDtoEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    group_id = 'group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a cost centre group by id
        api_response = api_instance.get_cost_centre_group(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreGroupDtoEnvelope**](CostCentreGroupDtoEnvelope.md)

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

# **get_cost_centre_groups**
> CostCentreGroupDtoListEnvelope get_cost_centre_groups(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all cost centre groups for a tenant

Retrieves all cost centre groups for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_group_dto_list_envelope import CostCentreGroupDtoListEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all cost centre groups for a tenant
        api_response = api_instance.get_cost_centre_groups(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreGroupDtoListEnvelope**](CostCentreGroupDtoListEnvelope.md)

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

# **get_cost_centre_groups_count**
> Int32Envelope get_cost_centre_groups_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of cost centre groups for a tenant

Retrieves the count of cost centre groups for the specified tenant using OData query options.

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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of cost centre groups for a tenant
        api_response = api_instance.get_cost_centre_groups_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centre_groups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centre_groups_count: %s\n" % e)
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

# **get_cost_centres**
> CostCentreDtoListEnvelope get_cost_centres(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all cost centres for a tenant

Retrieves all cost centres for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_dto_list_envelope import CostCentreDtoListEnvelope
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all cost centres for a tenant
        api_response = api_instance.get_cost_centres(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CostCentreDtoListEnvelope**](CostCentreDtoListEnvelope.md)

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

# **get_cost_centres_count**
> Int32Envelope get_cost_centres_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of cost centres for a tenant

Retrieves the count of cost centres for the specified tenant using OData query options.

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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of cost centres for a tenant
        api_response = api_instance.get_cost_centres_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->get_cost_centres_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->get_cost_centres_count: %s\n" % e)
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

# **update_cost_centre**
> EmptyEnvelope update_cost_centre(tenant_id, cost_centre_id, cost_centre_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a cost centre

Updates an existing cost centre.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_update_dto import CostCentreUpdateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cost_centre_id = 'cost_centre_id_example' # str | 
    cost_centre_update_dto = openapi_client.CostCentreUpdateDto() # CostCentreUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a cost centre
        api_response = api_instance.update_cost_centre(tenant_id, cost_centre_id, cost_centre_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->update_cost_centre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->update_cost_centre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cost_centre_id** | **str**|  | 
 **cost_centre_update_dto** | [**CostCentreUpdateDto**](CostCentreUpdateDto.md)|  | 
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

# **update_cost_centre_budget**
> EmptyEnvelope update_cost_centre_budget(tenant_id, budget_id, cost_centre_budget_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a cost centre budget

Updates an existing cost centre budget.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_budget_update_dto import CostCentreBudgetUpdateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    cost_centre_budget_update_dto = openapi_client.CostCentreBudgetUpdateDto() # CostCentreBudgetUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a cost centre budget
        api_response = api_instance.update_cost_centre_budget(tenant_id, budget_id, cost_centre_budget_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->update_cost_centre_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->update_cost_centre_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **cost_centre_budget_update_dto** | [**CostCentreBudgetUpdateDto**](CostCentreBudgetUpdateDto.md)|  | 
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

# **update_cost_centre_group**
> EmptyEnvelope update_cost_centre_group(tenant_id, group_id, cost_centre_group_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a cost centre group

Updates an existing cost centre group.

### Example


```python
import openapi_client
from openapi_client.models.cost_centre_group_update_dto import CostCentreGroupUpdateDto
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
    api_instance = openapi_client.CostCentresApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    group_id = 'group_id_example' # str | 
    cost_centre_group_update_dto = openapi_client.CostCentreGroupUpdateDto() # CostCentreGroupUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a cost centre group
        api_response = api_instance.update_cost_centre_group(tenant_id, group_id, cost_centre_group_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of CostCentresApi->update_cost_centre_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCentresApi->update_cost_centre_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **group_id** | **str**|  | 
 **cost_centre_group_update_dto** | [**CostCentreGroupUpdateDto**](CostCentreGroupUpdateDto.md)|  | 
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

