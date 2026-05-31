# openapi_client.AirwayBillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_airway_bill_line_async**](AirwayBillsApi.md#add_airway_bill_line_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/Lines | Add a line to airway bill
[**cancel_airway_bill_async**](AirwayBillsApi.md#cancel_airway_bill_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/Cancel | Cancel an airway bill
[**create_airway_bill_async**](AirwayBillsApi.md#create_airway_bill_async) | **POST** /api/v2/LogisticsService/AirwayBills | Create an airway bill
[**delete_airway_bill_async**](AirwayBillsApi.md#delete_airway_bill_async) | **DELETE** /api/v2/LogisticsService/AirwayBills/{billId} | Delete an airway bill
[**get_airway_bill_by_id_async**](AirwayBillsApi.md#get_airway_bill_by_id_async) | **GET** /api/v2/LogisticsService/AirwayBills/{billId} | Get airway bill by ID
[**get_airway_bill_lines_async**](AirwayBillsApi.md#get_airway_bill_lines_async) | **GET** /api/v2/LogisticsService/AirwayBills/{billId}/Lines | Get airway bill lines
[**get_airway_bill_lines_count_async**](AirwayBillsApi.md#get_airway_bill_lines_count_async) | **GET** /api/v2/LogisticsService/AirwayBills/{billId}/Lines/Count | Get airway bill lines count
[**get_airway_bills_async**](AirwayBillsApi.md#get_airway_bills_async) | **GET** /api/v2/LogisticsService/AirwayBills | Get all airway bills
[**get_airway_bills_count_async**](AirwayBillsApi.md#get_airway_bills_count_async) | **GET** /api/v2/LogisticsService/AirwayBills/Count | Get airway bills count
[**issue_airway_bill_async**](AirwayBillsApi.md#issue_airway_bill_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/Issue | Issue an airway bill
[**mark_airway_bill_arrived_async**](AirwayBillsApi.md#mark_airway_bill_arrived_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/MarkArrived | Mark airway bill arrived
[**mark_airway_bill_delivered_async**](AirwayBillsApi.md#mark_airway_bill_delivered_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/MarkDelivered | Mark airway bill delivered
[**mark_airway_bill_in_transit_async**](AirwayBillsApi.md#mark_airway_bill_in_transit_async) | **POST** /api/v2/LogisticsService/AirwayBills/{billId}/MarkInTransit | Mark airway bill in transit
[**remove_airway_bill_line_async**](AirwayBillsApi.md#remove_airway_bill_line_async) | **DELETE** /api/v2/LogisticsService/AirwayBills/{billId}/Lines/{lineId} | Remove an airway bill line
[**update_airway_bill_async**](AirwayBillsApi.md#update_airway_bill_async) | **PUT** /api/v2/LogisticsService/AirwayBills/{billId} | Update an airway bill
[**update_airway_bill_line_async**](AirwayBillsApi.md#update_airway_bill_line_async) | **PUT** /api/v2/LogisticsService/AirwayBills/{billId}/Lines/{lineId} | Update an airway bill line


# **add_airway_bill_line_async**
> EmptyEnvelope add_airway_bill_line_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)

Add a line to airway bill

Adds a new line to an airway bill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_create_dto import WaybillLineCreateDto
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_create_dto = openapi_client.WaybillLineCreateDto() # WaybillLineCreateDto |  (optional)

    try:
        # Add a line to airway bill
        api_response = api_instance.add_airway_bill_line_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)
        print("The response of AirwayBillsApi->add_airway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->add_airway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_create_dto** | [**WaybillLineCreateDto**](WaybillLineCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_airway_bill_async**
> EmptyEnvelope cancel_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Cancel an airway bill

Cancels an airway bill.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel an airway bill
        api_response = api_instance.cancel_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->cancel_airway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->cancel_airway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_airway_bill_async**
> EmptyEnvelope create_airway_bill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, airway_bill_create_dto=airway_bill_create_dto)

Create an airway bill

Creates a new airway bill for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.airway_bill_create_dto import AirwayBillCreateDto
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    airway_bill_create_dto = openapi_client.AirwayBillCreateDto() # AirwayBillCreateDto |  (optional)

    try:
        # Create an airway bill
        api_response = api_instance.create_airway_bill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, airway_bill_create_dto=airway_bill_create_dto)
        print("The response of AirwayBillsApi->create_airway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->create_airway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **airway_bill_create_dto** | [**AirwayBillCreateDto**](AirwayBillCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_airway_bill_async**
> EmptyEnvelope delete_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Delete an airway bill

Deletes an airway bill.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an airway bill
        api_response = api_instance.delete_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->delete_airway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->delete_airway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airway_bill_by_id_async**
> AirwayBillDtoEnvelope get_airway_bill_by_id_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get airway bill by ID

Retrieves a specific airway bill by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.airway_bill_dto_envelope import AirwayBillDtoEnvelope
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get airway bill by ID
        api_response = api_instance.get_airway_bill_by_id_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->get_airway_bill_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->get_airway_bill_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AirwayBillDtoEnvelope**](AirwayBillDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airway_bill_lines_async**
> WaybillLineDtoListEnvelope get_airway_bill_lines_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get airway bill lines

Retrieves all lines for a specific airway bill.

### Example


```python
import openapi_client
from openapi_client.models.waybill_line_dto_list_envelope import WaybillLineDtoListEnvelope
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get airway bill lines
        api_response = api_instance.get_airway_bill_lines_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->get_airway_bill_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->get_airway_bill_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WaybillLineDtoListEnvelope**](WaybillLineDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airway_bill_lines_count_async**
> Int32Envelope get_airway_bill_lines_count_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get airway bill lines count

Returns the count of lines for a specific airway bill.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get airway bill lines count
        api_response = api_instance.get_airway_bill_lines_count_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->get_airway_bill_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->get_airway_bill_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airway_bills_async**
> AirwayBillDtoListEnvelope get_airway_bills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all airway bills

Retrieves all airway bills for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.airway_bill_dto_list_envelope import AirwayBillDtoListEnvelope
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all airway bills
        api_response = api_instance.get_airway_bills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->get_airway_bills_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->get_airway_bills_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AirwayBillDtoListEnvelope**](AirwayBillDtoListEnvelope.md)

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

# **get_airway_bills_count_async**
> Int32Envelope get_airway_bills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get airway bills count

Returns the count of airway bills for the specified tenant.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get airway bills count
        api_response = api_instance.get_airway_bills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->get_airway_bills_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->get_airway_bills_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_airway_bill_async**
> EmptyEnvelope issue_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Issue an airway bill

Issues an airway bill.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Issue an airway bill
        api_response = api_instance.issue_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->issue_airway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->issue_airway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_airway_bill_arrived_async**
> EmptyEnvelope mark_airway_bill_arrived_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Mark airway bill arrived

Marks an airway bill as arrived.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark airway bill arrived
        api_response = api_instance.mark_airway_bill_arrived_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->mark_airway_bill_arrived_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->mark_airway_bill_arrived_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_airway_bill_delivered_async**
> EmptyEnvelope mark_airway_bill_delivered_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Mark airway bill delivered

Marks an airway bill as delivered.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark airway bill delivered
        api_response = api_instance.mark_airway_bill_delivered_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->mark_airway_bill_delivered_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->mark_airway_bill_delivered_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_airway_bill_in_transit_async**
> EmptyEnvelope mark_airway_bill_in_transit_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Mark airway bill in transit

Marks an airway bill as in transit.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark airway bill in transit
        api_response = api_instance.mark_airway_bill_in_transit_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->mark_airway_bill_in_transit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->mark_airway_bill_in_transit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_airway_bill_line_async**
> EmptyEnvelope remove_airway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove an airway bill line

Removes a line from an airway bill.

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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove an airway bill line
        api_response = api_instance.remove_airway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AirwayBillsApi->remove_airway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->remove_airway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **line_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_airway_bill_async**
> EmptyEnvelope update_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, airway_bill_update_dto=airway_bill_update_dto)

Update an airway bill

Updates an existing airway bill.

### Example


```python
import openapi_client
from openapi_client.models.airway_bill_update_dto import AirwayBillUpdateDto
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    airway_bill_update_dto = openapi_client.AirwayBillUpdateDto() # AirwayBillUpdateDto |  (optional)

    try:
        # Update an airway bill
        api_response = api_instance.update_airway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, airway_bill_update_dto=airway_bill_update_dto)
        print("The response of AirwayBillsApi->update_airway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->update_airway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **airway_bill_update_dto** | [**AirwayBillUpdateDto**](AirwayBillUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_airway_bill_line_async**
> EmptyEnvelope update_airway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)

Update an airway bill line

Updates an existing line on an airway bill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_update_dto import WaybillLineUpdateDto
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
    api_instance = openapi_client.AirwayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_update_dto = openapi_client.WaybillLineUpdateDto() # WaybillLineUpdateDto |  (optional)

    try:
        # Update an airway bill line
        api_response = api_instance.update_airway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)
        print("The response of AirwayBillsApi->update_airway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwayBillsApi->update_airway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_update_dto** | [**WaybillLineUpdateDto**](WaybillLineUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

