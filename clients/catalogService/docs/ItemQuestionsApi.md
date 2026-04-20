# openapi_client.ItemQuestionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_question_async**](ItemQuestionsApi.md#create_item_question_async) | **POST** /api/v2/CatalogService/ItemQuestions | Create a new item question
[**delete_item_question_async**](ItemQuestionsApi.md#delete_item_question_async) | **DELETE** /api/v2/CatalogService/ItemQuestions/{itemQuestionId} | Delete an item question
[**get_item_question_by_id_async**](ItemQuestionsApi.md#get_item_question_by_id_async) | **GET** /api/v2/CatalogService/ItemQuestions/{itemQuestionId} | Get item question by ID
[**get_item_questions_async**](ItemQuestionsApi.md#get_item_questions_async) | **GET** /api/v2/CatalogService/ItemQuestions | Get all item questions
[**update_item_question_async**](ItemQuestionsApi.md#update_item_question_async) | **PUT** /api/v2/CatalogService/ItemQuestions/{itemQuestionId} | Update an item question


# **create_item_question_async**
> ItemQuestionDtoEnvelope create_item_question_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_question_create_dto=item_question_create_dto)

Create a new item question

Creates a new item question for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_question_create_dto import ItemQuestionCreateDto
from openapi_client.models.item_question_dto_envelope import ItemQuestionDtoEnvelope
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
    api_instance = openapi_client.ItemQuestionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_question_create_dto = openapi_client.ItemQuestionCreateDto() # ItemQuestionCreateDto |  (optional)

    try:
        # Create a new item question
        api_response = api_instance.create_item_question_async(tenant_id, api_version=api_version, x_api_version=x_api_version, item_question_create_dto=item_question_create_dto)
        print("The response of ItemQuestionsApi->create_item_question_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemQuestionsApi->create_item_question_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_question_create_dto** | [**ItemQuestionCreateDto**](ItemQuestionCreateDto.md)|  | [optional] 

### Return type

[**ItemQuestionDtoEnvelope**](ItemQuestionDtoEnvelope.md)

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

# **delete_item_question_async**
> delete_item_question_async(tenant_id, item_question_id, api_version=api_version, x_api_version=x_api_version)

Delete an item question

Deletes an item question for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ItemQuestionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_question_id = 'item_question_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an item question
        api_instance.delete_item_question_async(tenant_id, item_question_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemQuestionsApi->delete_item_question_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_question_id** | **str**|  | 
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

# **get_item_question_by_id_async**
> ItemQuestionDtoEnvelope get_item_question_by_id_async(item_question_id, api_version=api_version, x_api_version=x_api_version)

Get item question by ID

Retrieves a specific item question by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item_question_dto_envelope import ItemQuestionDtoEnvelope
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
    api_instance = openapi_client.ItemQuestionsApi(api_client)
    item_question_id = 'item_question_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item question by ID
        api_response = api_instance.get_item_question_by_id_async(item_question_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemQuestionsApi->get_item_question_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemQuestionsApi->get_item_question_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_question_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemQuestionDtoEnvelope**](ItemQuestionDtoEnvelope.md)

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

# **get_item_questions_async**
> ItemQuestionDtoListEnvelope get_item_questions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all item questions

Retrieves all item questions for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.item_question_dto_list_envelope import ItemQuestionDtoListEnvelope
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
    api_instance = openapi_client.ItemQuestionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all item questions
        api_response = api_instance.get_item_questions_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemQuestionsApi->get_item_questions_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemQuestionsApi->get_item_questions_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemQuestionDtoListEnvelope**](ItemQuestionDtoListEnvelope.md)

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

# **update_item_question_async**
> update_item_question_async(tenant_id, item_question_id, api_version=api_version, x_api_version=x_api_version, item_question_update_dto=item_question_update_dto)

Update an item question

Updates an existing item question for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.item_question_update_dto import ItemQuestionUpdateDto
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
    api_instance = openapi_client.ItemQuestionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_question_id = 'item_question_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_question_update_dto = openapi_client.ItemQuestionUpdateDto() # ItemQuestionUpdateDto |  (optional)

    try:
        # Update an item question
        api_instance.update_item_question_async(tenant_id, item_question_id, api_version=api_version, x_api_version=x_api_version, item_question_update_dto=item_question_update_dto)
    except Exception as e:
        print("Exception when calling ItemQuestionsApi->update_item_question_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_question_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_question_update_dto** | [**ItemQuestionUpdateDto**](ItemQuestionUpdateDto.md)|  | [optional] 

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

