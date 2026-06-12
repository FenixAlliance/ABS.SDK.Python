# openapi_client.MaintenanceVisitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_maintenance_visit_async**](MaintenanceVisitsApi.md#create_maintenance_visit_async) | **POST** /api/v2/SupportService/MaintenanceVisits | Create a maintenance visit
[**delete_maintenance_visit_async**](MaintenanceVisitsApi.md#delete_maintenance_visit_async) | **DELETE** /api/v2/SupportService/MaintenanceVisits/{maintenanceVisitId} | Delete a maintenance visit
[**get_maintenance_visit_async**](MaintenanceVisitsApi.md#get_maintenance_visit_async) | **GET** /api/v2/SupportService/MaintenanceVisits/{maintenanceVisitId} | Retrieve a maintenance visit by ID
[**get_maintenance_visits_async**](MaintenanceVisitsApi.md#get_maintenance_visits_async) | **GET** /api/v2/SupportService/MaintenanceVisits | Retrieve maintenance visits
[**get_maintenance_visits_count_async**](MaintenanceVisitsApi.md#get_maintenance_visits_count_async) | **GET** /api/v2/SupportService/MaintenanceVisits/Count | Get maintenance visits count
[**patch_maintenance_visit_async**](MaintenanceVisitsApi.md#patch_maintenance_visit_async) | **PATCH** /api/v2/SupportService/MaintenanceVisits/{maintenanceVisitId} | Patch a maintenance visit
[**update_maintenance_visit_async**](MaintenanceVisitsApi.md#update_maintenance_visit_async) | **PUT** /api/v2/SupportService/MaintenanceVisits/{maintenanceVisitId} | Update a maintenance visit


# **create_maintenance_visit_async**
> EmptyEnvelope create_maintenance_visit_async(tenant_id, api_version=api_version, x_api_version=x_api_version, maintenance_visit_create_dto=maintenance_visit_create_dto)

Create a maintenance visit

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.maintenance_visit_create_dto import MaintenanceVisitCreateDto
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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    maintenance_visit_create_dto = openapi_client.MaintenanceVisitCreateDto() # MaintenanceVisitCreateDto |  (optional)

    try:
        # Create a maintenance visit
        api_response = api_instance.create_maintenance_visit_async(tenant_id, api_version=api_version, x_api_version=x_api_version, maintenance_visit_create_dto=maintenance_visit_create_dto)
        print("The response of MaintenanceVisitsApi->create_maintenance_visit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->create_maintenance_visit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **maintenance_visit_create_dto** | [**MaintenanceVisitCreateDto**](MaintenanceVisitCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_maintenance_visit_async**
> EmptyEnvelope delete_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version)

Delete a maintenance visit

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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    maintenance_visit_id = 'maintenance_visit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a maintenance visit
        api_response = api_instance.delete_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MaintenanceVisitsApi->delete_maintenance_visit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->delete_maintenance_visit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **maintenance_visit_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_visit_async**
> MaintenanceVisitDtoEnvelope get_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a maintenance visit by ID

### Example


```python
import openapi_client
from openapi_client.models.maintenance_visit_dto_envelope import MaintenanceVisitDtoEnvelope
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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    maintenance_visit_id = 'maintenance_visit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a maintenance visit by ID
        api_response = api_instance.get_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MaintenanceVisitsApi->get_maintenance_visit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->get_maintenance_visit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **maintenance_visit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MaintenanceVisitDtoEnvelope**](MaintenanceVisitDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_visits_async**
> MaintenanceVisitDtoListEnvelope get_maintenance_visits_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve maintenance visits

### Example


```python
import openapi_client
from openapi_client.models.maintenance_visit_dto_list_envelope import MaintenanceVisitDtoListEnvelope
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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve maintenance visits
        api_response = api_instance.get_maintenance_visits_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MaintenanceVisitsApi->get_maintenance_visits_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->get_maintenance_visits_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MaintenanceVisitDtoListEnvelope**](MaintenanceVisitDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_visits_count_async**
> Int32Envelope get_maintenance_visits_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get maintenance visits count

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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get maintenance visits count
        api_response = api_instance.get_maintenance_visits_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MaintenanceVisitsApi->get_maintenance_visits_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->get_maintenance_visits_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_maintenance_visit_async**
> EmptyEnvelope patch_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a maintenance visit

Partially updates an existing maintenance visit by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    maintenance_visit_id = 'maintenance_visit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a maintenance visit
        api_response = api_instance.patch_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of MaintenanceVisitsApi->patch_maintenance_visit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->patch_maintenance_visit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **maintenance_visit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **update_maintenance_visit_async**
> EmptyEnvelope update_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version, body=body)

Update a maintenance visit

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
    api_instance = openapi_client.MaintenanceVisitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    maintenance_visit_id = 'maintenance_visit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update a maintenance visit
        api_response = api_instance.update_maintenance_visit_async(tenant_id, maintenance_visit_id, api_version=api_version, x_api_version=x_api_version, body=body)
        print("The response of MaintenanceVisitsApi->update_maintenance_visit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceVisitsApi->update_maintenance_visit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **maintenance_visit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

