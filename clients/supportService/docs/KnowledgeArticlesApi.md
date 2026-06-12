# openapi_client.KnowledgeArticlesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_knowledge_article_async**](KnowledgeArticlesApi.md#create_knowledge_article_async) | **POST** /api/v2/SupportService/KnowledgeArticles | Create a knowledge article
[**delete_knowledge_article_async**](KnowledgeArticlesApi.md#delete_knowledge_article_async) | **DELETE** /api/v2/SupportService/KnowledgeArticles/{knowledgeArticleId} | Delete a knowledge article
[**get_knowledge_article_async**](KnowledgeArticlesApi.md#get_knowledge_article_async) | **GET** /api/v2/SupportService/KnowledgeArticles/{knowledgeArticleId} | Retrieve a knowledge article by ID
[**get_knowledge_articles_async**](KnowledgeArticlesApi.md#get_knowledge_articles_async) | **GET** /api/v2/SupportService/KnowledgeArticles | Retrieve knowledge articles
[**get_knowledge_articles_count_async**](KnowledgeArticlesApi.md#get_knowledge_articles_count_async) | **GET** /api/v2/SupportService/KnowledgeArticles/Count | Get knowledge articles count
[**patch_knowledge_article_async**](KnowledgeArticlesApi.md#patch_knowledge_article_async) | **PATCH** /api/v2/SupportService/KnowledgeArticles/{knowledgeArticleId} | Patch a knowledge article
[**update_knowledge_article_async**](KnowledgeArticlesApi.md#update_knowledge_article_async) | **PUT** /api/v2/SupportService/KnowledgeArticles/{knowledgeArticleId} | Update a knowledge article


# **create_knowledge_article_async**
> EmptyEnvelope create_knowledge_article_async(tenant_id, api_version=api_version, x_api_version=x_api_version, knowledge_article_create_dto=knowledge_article_create_dto)

Create a knowledge article

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.knowledge_article_create_dto import KnowledgeArticleCreateDto
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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    knowledge_article_create_dto = openapi_client.KnowledgeArticleCreateDto() # KnowledgeArticleCreateDto |  (optional)

    try:
        # Create a knowledge article
        api_response = api_instance.create_knowledge_article_async(tenant_id, api_version=api_version, x_api_version=x_api_version, knowledge_article_create_dto=knowledge_article_create_dto)
        print("The response of KnowledgeArticlesApi->create_knowledge_article_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->create_knowledge_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **knowledge_article_create_dto** | [**KnowledgeArticleCreateDto**](KnowledgeArticleCreateDto.md)|  | [optional] 

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

# **delete_knowledge_article_async**
> EmptyEnvelope delete_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version)

Delete a knowledge article

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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    knowledge_article_id = 'knowledge_article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a knowledge article
        api_response = api_instance.delete_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of KnowledgeArticlesApi->delete_knowledge_article_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->delete_knowledge_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **knowledge_article_id** | **str**|  | 
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

# **get_knowledge_article_async**
> KnowledgeArticleDtoEnvelope get_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a knowledge article by ID

### Example


```python
import openapi_client
from openapi_client.models.knowledge_article_dto_envelope import KnowledgeArticleDtoEnvelope
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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    knowledge_article_id = 'knowledge_article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a knowledge article by ID
        api_response = api_instance.get_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of KnowledgeArticlesApi->get_knowledge_article_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->get_knowledge_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **knowledge_article_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**KnowledgeArticleDtoEnvelope**](KnowledgeArticleDtoEnvelope.md)

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

# **get_knowledge_articles_async**
> KnowledgeArticleDtoListEnvelope get_knowledge_articles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve knowledge articles

### Example


```python
import openapi_client
from openapi_client.models.knowledge_article_dto_list_envelope import KnowledgeArticleDtoListEnvelope
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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve knowledge articles
        api_response = api_instance.get_knowledge_articles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of KnowledgeArticlesApi->get_knowledge_articles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->get_knowledge_articles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**KnowledgeArticleDtoListEnvelope**](KnowledgeArticleDtoListEnvelope.md)

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

# **get_knowledge_articles_count_async**
> Int32Envelope get_knowledge_articles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get knowledge articles count

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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get knowledge articles count
        api_response = api_instance.get_knowledge_articles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of KnowledgeArticlesApi->get_knowledge_articles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->get_knowledge_articles_count_async: %s\n" % e)
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

# **patch_knowledge_article_async**
> EmptyEnvelope patch_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a knowledge article

Partially updates an existing knowledge article by its unique identifier.

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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    knowledge_article_id = 'knowledge_article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a knowledge article
        api_response = api_instance.patch_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of KnowledgeArticlesApi->patch_knowledge_article_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->patch_knowledge_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **knowledge_article_id** | **str**|  | 
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

# **update_knowledge_article_async**
> EmptyEnvelope update_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version, knowledge_article_update_dto=knowledge_article_update_dto)

Update a knowledge article

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.knowledge_article_update_dto import KnowledgeArticleUpdateDto
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
    api_instance = openapi_client.KnowledgeArticlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    knowledge_article_id = 'knowledge_article_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    knowledge_article_update_dto = openapi_client.KnowledgeArticleUpdateDto() # KnowledgeArticleUpdateDto |  (optional)

    try:
        # Update a knowledge article
        api_response = api_instance.update_knowledge_article_async(tenant_id, knowledge_article_id, api_version=api_version, x_api_version=x_api_version, knowledge_article_update_dto=knowledge_article_update_dto)
        print("The response of KnowledgeArticlesApi->update_knowledge_article_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeArticlesApi->update_knowledge_article_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **knowledge_article_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **knowledge_article_update_dto** | [**KnowledgeArticleUpdateDto**](KnowledgeArticleUpdateDto.md)|  | [optional] 

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

