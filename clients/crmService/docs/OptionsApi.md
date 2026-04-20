# openapi_client.OptionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_option**](OptionsApi.md#create_contact_option) | **POST** /api/v2/CrmService/Contacts/{contactId}/Options | Create a new contact option
[**delete_contact_option**](OptionsApi.md#delete_contact_option) | **DELETE** /api/v2/CrmService/Contacts/{contactId}/Options/{optionId} | Delete a contact option
[**get_contact_option_by_id**](OptionsApi.md#get_contact_option_by_id) | **GET** /api/v2/CrmService/Contacts/{contactId}/Options/{optionId} | Retrieve a single contact option by its ID
[**get_contact_option_by_key**](OptionsApi.md#get_contact_option_by_key) | **GET** /api/v2/CrmService/Contacts/{contactId}/Options/Key/{key} | Retrieve a single contact option by its key
[**get_contact_options**](OptionsApi.md#get_contact_options) | **GET** /api/v2/CrmService/Contacts/{contactId}/Options | Retrieve a list of contact options
[**get_contact_options_count**](OptionsApi.md#get_contact_options_count) | **GET** /api/v2/CrmService/Contacts/{contactId}/Options/Count | Get the count of contact options
[**update_contact_option**](OptionsApi.md#update_contact_option) | **PUT** /api/v2/CrmService/Contacts/{contactId}/Options/{optionId} | Update a contact option
[**upsert_contact_option**](OptionsApi.md#upsert_contact_option) | **PUT** /api/v2/CrmService/Contacts/{contactId}/Options/Upsert/{key} | Create or update a contact option by key


# **create_contact_option**
> EmptyEnvelope create_contact_option(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)

Create a new contact option

Create a new option for a contact

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_create_dto import OptionCreateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_create_dto = openapi_client.OptionCreateDto() # OptionCreateDto |  (optional)

    try:
        # Create a new contact option
        api_response = api_instance.create_contact_option(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)
        print("The response of OptionsApi->create_contact_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_contact_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **key** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_create_dto** | [**OptionCreateDto**](OptionCreateDto.md)|  | [optional] 

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

# **delete_contact_option**
> EmptyEnvelope delete_contact_option(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version)

Delete a contact option

Delete a contact option

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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a contact option
        api_response = api_instance.delete_contact_option(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->delete_contact_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_contact_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **option_id** | **str**|  | 
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

# **get_contact_option_by_id**
> OptionDtoEnvelope get_contact_option_by_id(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single contact option by its ID

Retrieve a single contact option by its ID

### Example


```python
import openapi_client
from openapi_client.models.option_dto_envelope import OptionDtoEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single contact option by its ID
        api_response = api_instance.get_contact_option_by_id(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_contact_option_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_contact_option_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoEnvelope**](OptionDtoEnvelope.md)

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

# **get_contact_option_by_key**
> OptionDtoEnvelope get_contact_option_by_key(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single contact option by its key

Retrieve a single contact option by its key

### Example


```python
import openapi_client
from openapi_client.models.option_dto_envelope import OptionDtoEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single contact option by its key
        api_response = api_instance.get_contact_option_by_key(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_contact_option_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_contact_option_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **key** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoEnvelope**](OptionDtoEnvelope.md)

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

# **get_contact_options**
> OptionDtoListEnvelope get_contact_options(tenant_id, contact_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of contact options

Retrieve a list of options for a contact

### Example


```python
import openapi_client
from openapi_client.models.option_dto_list_envelope import OptionDtoListEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of contact options
        api_response = api_instance.get_contact_options(tenant_id, contact_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_contact_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_contact_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoListEnvelope**](OptionDtoListEnvelope.md)

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

# **get_contact_options_count**
> Int32Envelope get_contact_options_count(tenant_id, contact_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)

Get the count of contact options

Get the count of options for a contact

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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of contact options
        api_response = api_instance.get_contact_options_count(tenant_id, contact_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_contact_options_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_contact_options_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
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

# **update_contact_option**
> EmptyEnvelope update_contact_option(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)

Update a contact option

Update a contact option

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_update_dto import OptionUpdateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_update_dto = openapi_client.OptionUpdateDto() # OptionUpdateDto |  (optional)

    try:
        # Update a contact option
        api_response = api_instance.update_contact_option(tenant_id, contact_id, option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)
        print("The response of OptionsApi->update_contact_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->update_contact_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_update_dto** | [**OptionUpdateDto**](OptionUpdateDto.md)|  | [optional] 

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

# **upsert_contact_option**
> EmptyEnvelope upsert_contact_option(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)

Create or update a contact option by key

Create or update a contact option by key

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_update_dto import OptionUpdateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_update_dto = openapi_client.OptionUpdateDto() # OptionUpdateDto |  (optional)

    try:
        # Create or update a contact option by key
        api_response = api_instance.upsert_contact_option(tenant_id, contact_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)
        print("The response of OptionsApi->upsert_contact_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->upsert_contact_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **key** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_update_dto** | [**OptionUpdateDto**](OptionUpdateDto.md)|  | [optional] 

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

