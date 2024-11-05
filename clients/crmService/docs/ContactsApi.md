# openapi_client.ContactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_async**](ContactsApi.md#create_contact_async) | **POST** /api/v2/CrmService/Contacts | Create a new contact
[**delete_contact_async**](ContactsApi.md#delete_contact_async) | **DELETE** /api/v2/CrmService/Contacts/{contactId} | Delete a contact
[**get_business_owned_individual_async**](ContactsApi.md#get_business_owned_individual_async) | **GET** /api/v2/CrmService/Contacts/Individuals/{contactId} | Get a Contact of type Individual by ID
[**get_business_owned_individuals_async**](ContactsApi.md#get_business_owned_individuals_async) | **GET** /api/v2/CrmService/Contacts/Individuals | Get all contacts of type individual
[**get_business_owned_individuals_count_async**](ContactsApi.md#get_business_owned_individuals_count_async) | **GET** /api/v2/CrmService/Contacts/Individuals/Count | Get all contacts of type individual count
[**get_business_owned_organization_async**](ContactsApi.md#get_business_owned_organization_async) | **GET** /api/v2/CrmService/Contacts/Organizations/{contactId} | Get a Contact of type Organization by ID
[**get_business_owned_organizations_async**](ContactsApi.md#get_business_owned_organizations_async) | **GET** /api/v2/CrmService/Contacts/Organizations | Get all contacts of type organization
[**get_business_owned_organizations_count_async**](ContactsApi.md#get_business_owned_organizations_count_async) | **GET** /api/v2/CrmService/Contacts/Organizations/Count | Get all contacts of type organization count
[**get_contact_async**](ContactsApi.md#get_contact_async) | **GET** /api/v2/CrmService/Contacts/{contactId} | Get a contact by ID
[**get_contact_avatar_async**](ContactsApi.md#get_contact_avatar_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/Avatar | Get a contact&#39;s avatar
[**get_contact_cart_async**](ContactsApi.md#get_contact_cart_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/Cart | Get a contact&#39;s cart
[**get_contact_profiles_async**](ContactsApi.md#get_contact_profiles_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/Profiles | Get a contact&#39;s social profiles
[**get_contact_social_profile_async**](ContactsApi.md#get_contact_social_profile_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/SocialProfile | Get a contact&#39;s social profile
[**get_contact_wallet_async**](ContactsApi.md#get_contact_wallet_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/Wallet | Get a contact&#39;s wallet
[**get_contacts_async**](ContactsApi.md#get_contacts_async) | **GET** /api/v2/CrmService/Contacts | Get all business owned contacts
[**get_contacts_count_async**](ContactsApi.md#get_contacts_count_async) | **GET** /api/v2/CrmService/Contacts/Count | Get all business owned contacts count
[**get_extended_business_owned_individuals_async**](ContactsApi.md#get_extended_business_owned_individuals_async) | **GET** /api/v2/CrmService/Contacts/Individuals/Extended | Get all contacts of type individual
[**get_extended_business_owned_organizations_async**](ContactsApi.md#get_extended_business_owned_organizations_async) | **GET** /api/v2/CrmService/Contacts/Organizations/Extended | Get all contacts of type organization
[**get_extended_contact_async**](ContactsApi.md#get_extended_contact_async) | **GET** /api/v2/CrmService/Contacts/{contactId}/Extended | Get a contact by ID
[**get_extended_contacts_async**](ContactsApi.md#get_extended_contacts_async) | **GET** /api/v2/CrmService/Contacts/Extended | Get all business owned contacts
[**get_individual_related_individuals_async**](ContactsApi.md#get_individual_related_individuals_async) | **GET** /api/v2/CrmService/Contacts/Individuals/{contactId}/Individuals | Get individual related individuals
[**get_individual_related_organizations_async**](ContactsApi.md#get_individual_related_organizations_async) | **GET** /api/v2/CrmService/Contacts/Individuals/{contactId}/Organizations | Get individual related organizations
[**get_organization_related_individuals_async**](ContactsApi.md#get_organization_related_individuals_async) | **GET** /api/v2/CrmService/Contacts/Organizations/{contactId}/Individuals | Get organization related individuals
[**get_organization_related_organizations_async**](ContactsApi.md#get_organization_related_organizations_async) | **GET** /api/v2/CrmService/Contacts/Organizations/{contactId}/Organizations | Get organization related organizations
[**patch_contact_async**](ContactsApi.md#patch_contact_async) | **PATCH** /api/v2/CrmService/Contacts/{contactId} | Patch a contact
[**update_contact_async**](ContactsApi.md#update_contact_async) | **PUT** /api/v2/CrmService/Contacts/{contactId} | Update a contact
[**update_contact_avatar_async**](ContactsApi.md#update_contact_avatar_async) | **POST** /api/v2/CrmService/Contacts/{contactId}/Avatar | Update a contact&#39;s avatar
[**upsert_tenant_onto_another_tenant_contact_list_async**](ContactsApi.md#upsert_tenant_onto_another_tenant_contact_list_async) | **POST** /api/v2/CrmService/Contacts/Organizations/Upsert | Upsert a tenant onto another tenant&#39;s contact list
[**upsert_user_onto_another_tenant_contact_list_async**](ContactsApi.md#upsert_user_onto_another_tenant_contact_list_async) | **POST** /api/v2/CrmService/Contacts/Individuals/Upsert | Upsert a user onto a tenant&#39;s contact list


# **create_contact_async**
> EmptyEnvelope create_contact_async(tenant_id, api_version=api_version, x_api_version=x_api_version, contact_create_dto=contact_create_dto)

Create a new contact

Create a new contact

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_create_dto import ContactCreateDto
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    contact_create_dto = openapi_client.ContactCreateDto() # ContactCreateDto |  (optional)

    try:
        # Create a new contact
        api_response = api_instance.create_contact_async(tenant_id, api_version=api_version, x_api_version=x_api_version, contact_create_dto=contact_create_dto)
        print("The response of ContactsApi->create_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **contact_create_dto** | [**ContactCreateDto**](ContactCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **delete_contact_async**
> EmptyEnvelope delete_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Delete a contact

Delete a contact

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a contact
        api_response = api_instance.delete_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->delete_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->delete_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_business_owned_individual_async**
> ContactDtoEnvelope get_business_owned_individual_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a Contact of type Individual by ID

Get a Contact of type Individual by ID

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a Contact of type Individual by ID
        api_response = api_instance.get_business_owned_individual_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_individual_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_individual_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoEnvelope**](ContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_owned_individuals_async**
> ContactDtoListEnvelope get_business_owned_individuals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type individual

Get all contacts of type individual

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type individual
        api_response = api_instance.get_business_owned_individuals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_individuals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_individuals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_business_owned_individuals_count_async**
> ContactDtoListEnvelope get_business_owned_individuals_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type individual count

Get all contacts of type individual count

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type individual count
        api_response = api_instance.get_business_owned_individuals_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_individuals_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_individuals_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_business_owned_organization_async**
> ContactDtoEnvelope get_business_owned_organization_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a Contact of type Organization by ID

Get a Contact of type Organization by ID

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a Contact of type Organization by ID
        api_response = api_instance.get_business_owned_organization_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_organization_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_organization_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoEnvelope**](ContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_owned_organizations_async**
> List[ContactDto] get_business_owned_organizations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type organization

Get all contacts of type organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto import ContactDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type organization
        api_response = api_instance.get_business_owned_organizations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_organizations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_organizations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[ContactDto]**](ContactDto.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_business_owned_organizations_count_async**
> ContactDtoListEnvelope get_business_owned_organizations_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type organization count

Get all contacts of type organization count

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type organization count
        api_response = api_instance.get_business_owned_organizations_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_business_owned_organizations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_business_owned_organizations_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_contact_async**
> ContactDtoEnvelope get_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact by ID

Get a contact by ID

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact by ID
        api_response = api_instance.get_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoEnvelope**](ContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_contact_avatar_async**
> EmptyEnvelope get_contact_avatar_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact's avatar

Get a contact's avatar

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact's avatar
        api_response = api_instance.get_contact_avatar_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_cart_async**
> CartDtoEnvelope get_contact_cart_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact's cart

Get a contact's cart

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact's cart
        api_response = api_instance.get_contact_cart_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_profiles_async**
> ContactProfileDtoListEnvelope get_contact_profiles_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact's social profiles

Get a contact's social profiles

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_profile_dto_list_envelope import ContactProfileDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact's social profiles
        api_response = api_instance.get_contact_profiles_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactProfileDtoListEnvelope**](ContactProfileDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_social_profile_async**
> SocialProfileDtoEnvelope get_contact_social_profile_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact's social profile

Get a contact's social profile

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.social_profile_dto_envelope import SocialProfileDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact's social profile
        api_response = api_instance.get_contact_social_profile_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_social_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_social_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SocialProfileDtoEnvelope**](SocialProfileDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_wallet_async**
> WalletDtoEnvelope get_contact_wallet_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact's wallet

Get a contact's wallet

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.wallet_dto_envelope import WalletDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact's wallet
        api_response = api_instance.get_contact_wallet_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contact_wallet_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_wallet_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletDtoEnvelope**](WalletDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_async**
> ContactDtoListEnvelope get_contacts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all business owned contacts

Get all business owned contacts

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all business owned contacts
        api_response = api_instance.get_contacts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contacts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contacts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_contacts_count_async**
> ContactDtoListEnvelope get_contacts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all business owned contacts count

Get all business owned contacts count

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all business owned contacts count
        api_response = api_instance.get_contacts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_contacts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contacts_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_extended_business_owned_individuals_async**
> ExtendedContactDtoListEnvelope get_extended_business_owned_individuals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type individual

Get all contacts of type individual

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_contact_dto_list_envelope import ExtendedContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type individual
        api_response = api_instance.get_extended_business_owned_individuals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_extended_business_owned_individuals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_extended_business_owned_individuals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedContactDtoListEnvelope**](ExtendedContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_extended_business_owned_organizations_async**
> ExtendedContactDtoListEnvelope get_extended_business_owned_organizations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all contacts of type organization

Get all contacts of type organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_contact_dto_list_envelope import ExtendedContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all contacts of type organization
        api_response = api_instance.get_extended_business_owned_organizations_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_extended_business_owned_organizations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_extended_business_owned_organizations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedContactDtoListEnvelope**](ExtendedContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_extended_contact_async**
> ExtendedContactDtoEnvelope get_extended_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get a contact by ID

Get a contact by ID

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_contact_dto_envelope import ExtendedContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a contact by ID
        api_response = api_instance.get_extended_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_extended_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_extended_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedContactDtoEnvelope**](ExtendedContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_extended_contacts_async**
> ExtendedContactDtoListEnvelope get_extended_contacts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all business owned contacts

Get all business owned contacts

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_contact_dto_list_envelope import ExtendedContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all business owned contacts
        api_response = api_instance.get_extended_contacts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_extended_contacts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_extended_contacts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedContactDtoListEnvelope**](ExtendedContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_individual_related_individuals_async**
> ContactDtoListEnvelope get_individual_related_individuals_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get individual related individuals

Get individual related individuals

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get individual related individuals
        api_response = api_instance.get_individual_related_individuals_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_individual_related_individuals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_individual_related_individuals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_individual_related_organizations_async**
> ContactDtoListEnvelope get_individual_related_organizations_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get individual related organizations

Get individual related organizations

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get individual related organizations
        api_response = api_instance.get_individual_related_organizations_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_individual_related_organizations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_individual_related_organizations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_organization_related_individuals_async**
> ContactDtoListEnvelope get_organization_related_individuals_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get organization related individuals

Get organization related individuals

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get organization related individuals
        api_response = api_instance.get_organization_related_individuals_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_organization_related_individuals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_organization_related_individuals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **get_organization_related_organizations_async**
> ContactDtoListEnvelope get_organization_related_organizations_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)

Get organization related organizations

Get organization related organizations

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get organization related organizations
        api_response = api_instance.get_organization_related_organizations_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->get_organization_related_organizations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_organization_related_organizations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoListEnvelope**](ContactDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **patch_contact_async**
> EmptyEnvelope patch_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a contact

Patch a contact

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a contact
        api_response = api_instance.patch_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ContactsApi->patch_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->patch_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **update_contact_async**
> EmptyEnvelope update_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version, contact_update_dto=contact_update_dto)

Update a contact

Update a contact

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_update_dto import ContactUpdateDto
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    contact_id = 'contact_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    contact_update_dto = openapi_client.ContactUpdateDto() # ContactUpdateDto |  (optional)

    try:
        # Update a contact
        api_response = api_instance.update_contact_async(tenant_id, contact_id, api_version=api_version, x_api_version=x_api_version, contact_update_dto=contact_update_dto)
        print("The response of ContactsApi->update_contact_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contact_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **contact_update_dto** | [**ContactUpdateDto**](ContactUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **update_contact_avatar_async**
> EmptyEnvelope update_contact_avatar_async(contact_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, avatar=avatar)

Update a contact's avatar

Update a contact's avatar

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    avatar = None # bytearray |  (optional)

    try:
        # Update a contact's avatar
        api_response = api_instance.update_contact_avatar_async(contact_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, avatar=avatar)
        print("The response of ContactsApi->update_contact_avatar_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contact_avatar_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **avatar** | **bytearray**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_tenant_onto_another_tenant_contact_list_async**
> ContactDtoEnvelope upsert_tenant_onto_another_tenant_contact_list_async(tenant_id, related_tenant_id, api_version=api_version, x_api_version=x_api_version)

Upsert a tenant onto another tenant's contact list

Upsert a tenant onto another tenant's contact list

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    related_tenant_id = 'related_tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Upsert a tenant onto another tenant's contact list
        api_response = api_instance.upsert_tenant_onto_another_tenant_contact_list_async(tenant_id, related_tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->upsert_tenant_onto_another_tenant_contact_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->upsert_tenant_onto_another_tenant_contact_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **related_tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoEnvelope**](ContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **upsert_user_onto_another_tenant_contact_list_async**
> ContactDtoEnvelope upsert_user_onto_another_tenant_contact_list_async(tenant_id, related_user_id, api_version=api_version, x_api_version=x_api_version)

Upsert a user onto a tenant's contact list

Upsert a user onto a tenant's contact list

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContactsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    related_user_id = 'related_user_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Upsert a user onto a tenant's contact list
        api_response = api_instance.upsert_user_onto_another_tenant_contact_list_async(tenant_id, related_user_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ContactsApi->upsert_user_onto_another_tenant_contact_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->upsert_user_onto_another_tenant_contact_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **related_user_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ContactDtoEnvelope**](ContactDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

