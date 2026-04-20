# openapi_client.UnitGroupsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unit_async**](UnitGroupsApi.md#create_unit_async) | **POST** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units | Create a unit within a unit group
[**create_unit_group_async**](UnitGroupsApi.md#create_unit_group_async) | **POST** /api/v2/TenantsService/UnitGroups | Create a new unit group
[**delete_unit_async**](UnitGroupsApi.md#delete_unit_async) | **DELETE** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units/{unitId} | Delete a unit from a unit group
[**delete_unit_group_async**](UnitGroupsApi.md#delete_unit_group_async) | **DELETE** /api/v2/TenantsService/UnitGroups/{unitGroupId} | Delete a unit group
[**get_unit_async**](UnitGroupsApi.md#get_unit_async) | **GET** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units/{unitId} | Retrieve a unit by ID within a unit group
[**get_unit_group_async**](UnitGroupsApi.md#get_unit_group_async) | **GET** /api/v2/TenantsService/UnitGroups/{unitGroupId} | Retrieve a unit group by ID
[**get_unit_groups_async**](UnitGroupsApi.md#get_unit_groups_async) | **GET** /api/v2/TenantsService/UnitGroups | Retrieve a list of unit groups
[**get_unit_groups_count_async**](UnitGroupsApi.md#get_unit_groups_count_async) | **GET** /api/v2/TenantsService/UnitGroups/Count | Get the count of unit groups
[**get_units_async**](UnitGroupsApi.md#get_units_async) | **GET** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units | Retrieve units for a unit group
[**get_units_count_async**](UnitGroupsApi.md#get_units_count_async) | **GET** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units/Count | Get the count of units in a unit group
[**update_unit_async**](UnitGroupsApi.md#update_unit_async) | **PUT** /api/v2/TenantsService/UnitGroups/{unitGroupId}/Units/{unitId} | Update a unit within a unit group
[**update_unit_group_async**](UnitGroupsApi.md#update_unit_group_async) | **PUT** /api/v2/TenantsService/UnitGroups/{unitGroupId} | Update a unit group


# **create_unit_async**
> EmptyEnvelope create_unit_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version, unit_create_dto=unit_create_dto)

Create a unit within a unit group

Creates a new unit within a specific unit group.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.unit_create_dto import UnitCreateDto
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    unit_create_dto = openapi_client.UnitCreateDto() # UnitCreateDto |  (optional)

    try:
        # Create a unit within a unit group
        api_response = api_instance.create_unit_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version, unit_create_dto=unit_create_dto)
        print("The response of UnitGroupsApi->create_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->create_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **unit_create_dto** | [**UnitCreateDto**](UnitCreateDto.md)|  | [optional] 

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

# **create_unit_group_async**
> EmptyEnvelope create_unit_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, unit_group_create_dto=unit_group_create_dto)

Create a new unit group

Creates a new unit group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.unit_group_create_dto import UnitGroupCreateDto
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    unit_group_create_dto = openapi_client.UnitGroupCreateDto() # UnitGroupCreateDto |  (optional)

    try:
        # Create a new unit group
        api_response = api_instance.create_unit_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, unit_group_create_dto=unit_group_create_dto)
        print("The response of UnitGroupsApi->create_unit_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->create_unit_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **unit_group_create_dto** | [**UnitGroupCreateDto**](UnitGroupCreateDto.md)|  | [optional] 

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

# **delete_unit_async**
> EmptyEnvelope delete_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version)

Delete a unit from a unit group

Deletes a unit from a specific unit group.

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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a unit from a unit group
        api_response = api_instance.delete_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->delete_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->delete_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **unit_id** | **str**|  | 
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

# **delete_unit_group_async**
> EmptyEnvelope delete_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)

Delete a unit group

Deletes a unit group by its unique identifier.

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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a unit group
        api_response = api_instance.delete_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->delete_unit_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->delete_unit_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
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

# **get_unit_async**
> UnitDtoEnvelope get_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a unit by ID within a unit group

Retrieves a single unit by its unique identifier within a specific unit group.

### Example


```python
import openapi_client
from openapi_client.models.unit_dto_envelope import UnitDtoEnvelope
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a unit by ID within a unit group
        api_response = api_instance.get_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UnitDtoEnvelope**](UnitDtoEnvelope.md)

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

# **get_unit_group_async**
> UnitGroupDtoEnvelope get_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a unit group by ID

Retrieves a single unit group by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.unit_group_dto_envelope import UnitGroupDtoEnvelope
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a unit group by ID
        api_response = api_instance.get_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_unit_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_unit_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UnitGroupDtoEnvelope**](UnitGroupDtoEnvelope.md)

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

# **get_unit_groups_async**
> UnitGroupDtoListEnvelope get_unit_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of unit groups

Retrieves a list of unit groups for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.unit_group_dto_list_envelope import UnitGroupDtoListEnvelope
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of unit groups
        api_response = api_instance.get_unit_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_unit_groups_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_unit_groups_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UnitGroupDtoListEnvelope**](UnitGroupDtoListEnvelope.md)

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

# **get_unit_groups_count_async**
> Int32Envelope get_unit_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of unit groups

Returns the total count of unit groups for the specified tenant with OData query support.

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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of unit groups
        api_response = api_instance.get_unit_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_unit_groups_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_unit_groups_count_async: %s\n" % e)
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

# **get_units_async**
> UnitDtoListEnvelope get_units_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)

Retrieve units for a unit group

Retrieves a list of units belonging to a specific unit group.

### Example


```python
import openapi_client
from openapi_client.models.unit_dto_list_envelope import UnitDtoListEnvelope
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve units for a unit group
        api_response = api_instance.get_units_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_units_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_units_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**UnitDtoListEnvelope**](UnitDtoListEnvelope.md)

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

# **get_units_count_async**
> Int32Envelope get_units_count_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)

Get the count of units in a unit group

Returns the total count of units in a specific unit group.

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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of units in a unit group
        api_response = api_instance.get_units_count_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UnitGroupsApi->get_units_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->get_units_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
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

# **update_unit_async**
> EmptyEnvelope update_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version, unit_update_dto=unit_update_dto)

Update a unit within a unit group

Updates an existing unit within a specific unit group.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.unit_update_dto import UnitUpdateDto
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    unit_update_dto = openapi_client.UnitUpdateDto() # UnitUpdateDto |  (optional)

    try:
        # Update a unit within a unit group
        api_response = api_instance.update_unit_async(tenant_id, unit_group_id, unit_id, api_version=api_version, x_api_version=x_api_version, unit_update_dto=unit_update_dto)
        print("The response of UnitGroupsApi->update_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->update_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **unit_update_dto** | [**UnitUpdateDto**](UnitUpdateDto.md)|  | [optional] 

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

# **update_unit_group_async**
> EmptyEnvelope update_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version, unit_group_update_dto=unit_group_update_dto)

Update a unit group

Updates an existing unit group by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.unit_group_update_dto import UnitGroupUpdateDto
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
    api_instance = openapi_client.UnitGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_group_id = 'unit_group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    unit_group_update_dto = openapi_client.UnitGroupUpdateDto() # UnitGroupUpdateDto |  (optional)

    try:
        # Update a unit group
        api_response = api_instance.update_unit_group_async(tenant_id, unit_group_id, api_version=api_version, x_api_version=x_api_version, unit_group_update_dto=unit_group_update_dto)
        print("The response of UnitGroupsApi->update_unit_group_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitGroupsApi->update_unit_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **unit_group_update_dto** | [**UnitGroupUpdateDto**](UnitGroupUpdateDto.md)|  | [optional] 

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

