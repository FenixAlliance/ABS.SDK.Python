# openapi_client.TeamRecordsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_team_record**](TeamRecordsApi.md#create_tenant_team_record) | **POST** /api/v2/TenantsService/TeamRecords | Create a new tenant team record
[**delete_tenant_team_record**](TeamRecordsApi.md#delete_tenant_team_record) | **DELETE** /api/v2/TenantsService/TeamRecords/{tenantTeamRecordId} | Delete a tenant team record
[**get_tenant_team_record_by_id**](TeamRecordsApi.md#get_tenant_team_record_by_id) | **GET** /api/v2/TenantsService/TeamRecords/{tenantTeamRecordId} | Retrieve a single tenant team record by its ID
[**get_tenant_team_records**](TeamRecordsApi.md#get_tenant_team_records) | **GET** /api/v2/TenantsService/TeamRecords | Retrieve a list of tenant team records
[**get_tenant_team_records_count**](TeamRecordsApi.md#get_tenant_team_records_count) | **GET** /api/v2/TenantsService/TeamRecords/Count | Get the count of tenant team records
[**update_tenant_team_record**](TeamRecordsApi.md#update_tenant_team_record) | **PUT** /api/v2/TenantsService/TeamRecords/{tenantTeamRecordId} | Update a tenant team record


# **create_tenant_team_record**
> EmptyEnvelope create_tenant_team_record(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_record_create_dto=tenant_team_record_create_dto)

Create a new tenant team record

Create a new tenant team record

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_record_create_dto import TenantTeamRecordCreateDto
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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_record_create_dto = openapi_client.TenantTeamRecordCreateDto() # TenantTeamRecordCreateDto |  (optional)

    try:
        # Create a new tenant team record
        api_response = api_instance.create_tenant_team_record(tenant_id, api_version=api_version, x_api_version=x_api_version, tenant_team_record_create_dto=tenant_team_record_create_dto)
        print("The response of TeamRecordsApi->create_tenant_team_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->create_tenant_team_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_record_create_dto** | [**TenantTeamRecordCreateDto**](TenantTeamRecordCreateDto.md)|  | [optional] 

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

# **delete_tenant_team_record**
> EmptyEnvelope delete_tenant_team_record(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version)

Delete a tenant team record

Delete a tenant team record

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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_record_id = 'tenant_team_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a tenant team record
        api_response = api_instance.delete_tenant_team_record(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamRecordsApi->delete_tenant_team_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->delete_tenant_team_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_record_id** | **str**|  | 
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

# **get_tenant_team_record_by_id**
> TenantTeamRecordDtoEnvelope get_tenant_team_record_by_id(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single tenant team record by its ID

Retrieve a single tenant team record by its ID

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_record_dto_envelope import TenantTeamRecordDtoEnvelope
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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_record_id = 'tenant_team_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single tenant team record by its ID
        api_response = api_instance.get_tenant_team_record_by_id(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamRecordsApi->get_tenant_team_record_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->get_tenant_team_record_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamRecordDtoEnvelope**](TenantTeamRecordDtoEnvelope.md)

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

# **get_tenant_team_records**
> TenantTeamRecordDtoListEnvelope get_tenant_team_records(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of tenant team records

Retrieve a list of tenant team records

### Example


```python
import openapi_client
from openapi_client.models.tenant_team_record_dto_list_envelope import TenantTeamRecordDtoListEnvelope
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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of tenant team records
        api_response = api_instance.get_tenant_team_records(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamRecordsApi->get_tenant_team_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->get_tenant_team_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TenantTeamRecordDtoListEnvelope**](TenantTeamRecordDtoListEnvelope.md)

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

# **get_tenant_team_records_count**
> Int32Envelope get_tenant_team_records_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of tenant team records

Get the count of tenant team records

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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of tenant team records
        api_response = api_instance.get_tenant_team_records_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TeamRecordsApi->get_tenant_team_records_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->get_tenant_team_records_count: %s\n" % e)
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

# **update_tenant_team_record**
> EmptyEnvelope update_tenant_team_record(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version, tenant_team_record_update_dto=tenant_team_record_update_dto)

Update a tenant team record

Update a tenant team record

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.tenant_team_record_update_dto import TenantTeamRecordUpdateDto
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
    api_instance = openapi_client.TeamRecordsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_team_record_id = 'tenant_team_record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    tenant_team_record_update_dto = openapi_client.TenantTeamRecordUpdateDto() # TenantTeamRecordUpdateDto |  (optional)

    try:
        # Update a tenant team record
        api_response = api_instance.update_tenant_team_record(tenant_id, tenant_team_record_id, api_version=api_version, x_api_version=x_api_version, tenant_team_record_update_dto=tenant_team_record_update_dto)
        print("The response of TeamRecordsApi->update_tenant_team_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamRecordsApi->update_tenant_team_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_team_record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **tenant_team_record_update_dto** | [**TenantTeamRecordUpdateDto**](TenantTeamRecordUpdateDto.md)|  | [optional] 

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

