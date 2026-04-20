# openapi_client.ItemsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_stock_item_tags_by_item_id**](ItemsApi.md#count_stock_item_tags_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Tags/Count | Count tags for a stock item
[**count_stock_items_by_business**](ItemsApi.md#count_stock_items_by_business) | **GET** /api/v2/CatalogService/Items/Count | Count stock items by business
[**create_stock_item**](ItemsApi.md#create_stock_item) | **POST** /api/v2/CatalogService/Items | Create a new stock item
[**delete_stock_item**](ItemsApi.md#delete_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId} | Delete a stock item
[**get_extended_stock_item_by_id**](ItemsApi.md#get_extended_stock_item_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Extended | Get extended stock item by ID
[**get_product_primary_image_async**](ItemsApi.md#get_product_primary_image_async) | **GET** /api/v2/CatalogService/Items/{itemId}/Images/Primary | Get item primary image
[**get_stock_item_attachment_by_id**](ItemsApi.md#get_stock_item_attachment_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Attachments/{itemAttachmentId} | Get attachment by ID for a stock item
[**get_stock_item_attachments_by_item_id**](ItemsApi.md#get_stock_item_attachments_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Attachments | Get attachments for a stock item
[**get_stock_item_attribute_option_by_id**](ItemsApi.md#get_stock_item_attribute_option_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/AttributeOptions/{itemAttributeOptionId} | Get attribute option by ID for a stock item
[**get_stock_item_attribute_options_by_item_id**](ItemsApi.md#get_stock_item_attribute_options_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/AttributeOptions | Get attribute options for a stock item
[**get_stock_item_brand_by_id**](ItemsApi.md#get_stock_item_brand_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Brands/{itemBrandId} | Get brand by ID for a stock item
[**get_stock_item_brands_by_item_id**](ItemsApi.md#get_stock_item_brands_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Brands | Get brands for a stock item
[**get_stock_item_by_id**](ItemsApi.md#get_stock_item_by_id) | **GET** /api/v2/CatalogService/Items/{itemId} | Get stock item by ID
[**get_stock_item_categories_by_item_id**](ItemsApi.md#get_stock_item_categories_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Categories | Get categories for a stock item
[**get_stock_item_category_by_id**](ItemsApi.md#get_stock_item_category_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Categories/{itemCategoryId} | Get category by ID for a stock item
[**get_stock_item_google_categories_by_item_id**](ItemsApi.md#get_stock_item_google_categories_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/GoogleCategories | Get Google categories for a stock item
[**get_stock_item_google_category_by_id**](ItemsApi.md#get_stock_item_google_category_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/GoogleCategories/{itemGoogleCategoryId} | Get Google category by ID for a stock item
[**get_stock_item_image_by_id**](ItemsApi.md#get_stock_item_image_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Images/{itemImageId} | Get image by ID for a stock item
[**get_stock_item_images_by_item_id**](ItemsApi.md#get_stock_item_images_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Images | Get images for a stock item
[**get_stock_item_price_rule_by_id**](ItemsApi.md#get_stock_item_price_rule_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/PriceRules/{itemPriceRuleId} | Get price rule by ID for a stock item
[**get_stock_item_price_rules_by_item_id**](ItemsApi.md#get_stock_item_price_rules_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/PriceRules | Get price rules for a stock item
[**get_stock_item_question_by_id**](ItemsApi.md#get_stock_item_question_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Questions/{itemQuestionId} | Get question by ID for a stock item
[**get_stock_item_questions_by_item_id**](ItemsApi.md#get_stock_item_questions_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Questions | Get questions for a stock item
[**get_stock_item_refund_policies_by_item_id**](ItemsApi.md#get_stock_item_refund_policies_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/RefundPolicies | Get refund policies for a stock item
[**get_stock_item_refund_policy_by_id**](ItemsApi.md#get_stock_item_refund_policy_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/RefundPolicies/{itemRefundPolicyId} | Get refund policy by ID for a stock item
[**get_stock_item_return_policies_by_item_id**](ItemsApi.md#get_stock_item_return_policies_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/ReturnPolicies | Get return policies for a stock item
[**get_stock_item_return_policy_by_id**](ItemsApi.md#get_stock_item_return_policy_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/ReturnPolicies/{itemReturnPolicyId} | Get return policy by ID for a stock item
[**get_stock_item_review_by_id**](ItemsApi.md#get_stock_item_review_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Reviews/{itemReviewId} | Get review by ID for a stock item
[**get_stock_item_reviews_by_item_id**](ItemsApi.md#get_stock_item_reviews_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Reviews | Get reviews for a stock item
[**get_stock_item_shipping_policies_by_item_id**](ItemsApi.md#get_stock_item_shipping_policies_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/ShippingPolicies | Get shipping policies for a stock item
[**get_stock_item_shipping_policy_by_id**](ItemsApi.md#get_stock_item_shipping_policy_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/ShippingPolicies/{itemShippingPolicyId} | Get shipping policy by ID for a stock item
[**get_stock_item_tag_by_id**](ItemsApi.md#get_stock_item_tag_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Tags/{itemTagId} | Get tag by ID for a stock item
[**get_stock_item_tags_by_item_id**](ItemsApi.md#get_stock_item_tags_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Tags | Get tags for a stock item
[**get_stock_item_tax_policies_by_item_id**](ItemsApi.md#get_stock_item_tax_policies_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/TaxPolicies | Get tax policies for a stock item
[**get_stock_item_tax_policy_by_id**](ItemsApi.md#get_stock_item_tax_policy_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/TaxPolicies/{itemTaxPolicyId} | Get tax policy by ID for a stock item
[**get_stock_item_type_by_id**](ItemsApi.md#get_stock_item_type_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Types/{itemTypeId} | Get type by ID for a stock item
[**get_stock_item_types_by_item_id**](ItemsApi.md#get_stock_item_types_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/Types | Get types for a stock item
[**get_stock_item_warranty_policies_by_item_id**](ItemsApi.md#get_stock_item_warranty_policies_by_item_id) | **GET** /api/v2/CatalogService/Items/{itemId}/WarrantyPolicies | Get warranty policies for a stock item
[**get_stock_item_warranty_policy_by_id**](ItemsApi.md#get_stock_item_warranty_policy_by_id) | **GET** /api/v2/CatalogService/Items/{itemId}/WarrantyPolicies/{itemWarrantyPolicyId} | Get warranty policy by ID for a stock item
[**get_stock_items_odata_max_price**](ItemsApi.md#get_stock_items_odata_max_price) | **GET** /api/v2/CatalogService/Items/MaxPrice | Get max price of stock items
[**get_stock_items_odata_min_price**](ItemsApi.md#get_stock_items_odata_min_price) | **GET** /api/v2/CatalogService/Items/MinPrice | Get min price of stock items
[**get_stock_items_query**](ItemsApi.md#get_stock_items_query) | **GET** /api/v2/CatalogService/Items | Get all stock items
[**relate_attachment_to_stock_item**](ItemsApi.md#relate_attachment_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Attachments/{itemAttachmentId} | Relate attachment to stock item
[**relate_attribute_option_to_stock_item**](ItemsApi.md#relate_attribute_option_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/AttributeOptions/{itemAttributeOptionId} | Relate attribute option to stock item
[**relate_brand_to_stock_item**](ItemsApi.md#relate_brand_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Brands/{itemBrandId} | Relate brand to stock item
[**relate_category_to_stock_item**](ItemsApi.md#relate_category_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Categories/{itemCategoryId} | Relate category to stock item
[**relate_google_category_to_stock_item**](ItemsApi.md#relate_google_category_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/GoogleCategories/{itemGoogleCategoryId} | Relate Google category to stock item
[**relate_image_to_stock_item**](ItemsApi.md#relate_image_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Images/{itemImageId} | Relate image to stock item
[**relate_price_rule_to_stock_item**](ItemsApi.md#relate_price_rule_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/PriceRules/{itemPriceRuleId} | Relate price rule to stock item
[**relate_question_to_stock_item**](ItemsApi.md#relate_question_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Questions | Create question for stock item
[**relate_refund_policy_to_stock_item**](ItemsApi.md#relate_refund_policy_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/RefundPolicies/{itemRefundPolicyId} | Relate refund policy to stock item
[**relate_return_policy_to_stock_item**](ItemsApi.md#relate_return_policy_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/ReturnPolicies/{itemReturnPolicyId} | Relate return policy to stock item
[**relate_review_to_stock_item**](ItemsApi.md#relate_review_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Reviews | Create review for stock item
[**relate_shipping_policy_to_stock_item**](ItemsApi.md#relate_shipping_policy_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/ShippingPolicies/{itemShippingPolicyId} | Relate shipping policy to stock item
[**relate_tag_to_stock_item**](ItemsApi.md#relate_tag_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Tags/{itemTagId} | Relate tag to stock item
[**relate_tax_policy_to_stock_item**](ItemsApi.md#relate_tax_policy_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/TaxPolicies/{itemTaxPolicyId} | Relate tax policy to stock item
[**relate_type_to_stock_item**](ItemsApi.md#relate_type_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/Types/{itemTypeId} | Relate type to stock item
[**relate_warranty_policy_to_stock_item**](ItemsApi.md#relate_warranty_policy_to_stock_item) | **POST** /api/v2/CatalogService/Items/{itemId}/WarrantyPolicies/{itemWarrantyPolicyId} | Relate warranty policy to stock item
[**remove_attachment_from_stock_item**](ItemsApi.md#remove_attachment_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Attachments/{itemAttachmentId} | Remove attachment from stock item
[**remove_attribute_option_from_stock_item**](ItemsApi.md#remove_attribute_option_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/AttributeOptions/{itemAttributeOptionId} | Remove attribute option from stock item
[**remove_brand_from_stock_item**](ItemsApi.md#remove_brand_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Brands/{itemBrandId} | Remove brand from stock item
[**remove_category_from_stock_item**](ItemsApi.md#remove_category_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Categories/{itemCategoryId} | Remove category from stock item
[**remove_google_category_from_stock_item**](ItemsApi.md#remove_google_category_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/GoogleCategories/{itemGoogleCategoryId} | Remove Google category from stock item
[**remove_image_from_stock_item**](ItemsApi.md#remove_image_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Images/{itemImageId} | Remove image from stock item
[**remove_price_rule_from_stock_item**](ItemsApi.md#remove_price_rule_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/PriceRules/{itemPriceRuleId} | Remove price rule from stock item
[**remove_question_from_stock_item**](ItemsApi.md#remove_question_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Questions/{itemQuestionId} | Remove question from stock item
[**remove_refund_policy_from_stock_item**](ItemsApi.md#remove_refund_policy_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/RefundPolicies/{itemRefundPolicyId} | Remove refund policy from stock item
[**remove_return_policy_from_stock_item**](ItemsApi.md#remove_return_policy_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/ReturnPolicies/{itemReturnPolicyId} | Remove return policy from stock item
[**remove_review_from_stock_item**](ItemsApi.md#remove_review_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Reviews/{itemReviewId} | Remove review from stock item
[**remove_shipping_policy_from_stock_item**](ItemsApi.md#remove_shipping_policy_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/ShippingPolicies/{itemShippingPolicyId} | Remove shipping policy from stock item
[**remove_tag_from_stock_item**](ItemsApi.md#remove_tag_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Tags/{itemTagId} | Remove tag from stock item
[**remove_tax_policy_from_stock_item**](ItemsApi.md#remove_tax_policy_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/TaxPolicies/{itemTaxPolicyId} | Remove tax policy from stock item
[**remove_type_from_stock_item**](ItemsApi.md#remove_type_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/Types/{itemTypeId} | Remove type from stock item
[**remove_warranty_policy_from_stock_item**](ItemsApi.md#remove_warranty_policy_from_stock_item) | **DELETE** /api/v2/CatalogService/Items/{itemId}/WarrantyPolicies/{itemWarrantyPolicyId} | Remove warranty policy from stock item
[**update_product_primary_image_async**](ItemsApi.md#update_product_primary_image_async) | **POST** /api/v2/CatalogService/Items/{itemId}/Images/Primary | Update item primary image
[**update_stock_item**](ItemsApi.md#update_stock_item) | **PUT** /api/v2/CatalogService/Items/{itemId} | Update a stock item


# **count_stock_item_tags_by_item_id**
> Int32Envelope count_stock_item_tags_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Count tags for a stock item

Counts the number of tags associated with a specific stock item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count tags for a stock item
        api_response = api_instance.count_stock_item_tags_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->count_stock_item_tags_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->count_stock_item_tags_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
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

# **count_stock_items_by_business**
> Int32Envelope count_stock_items_by_business(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Count stock items by business

Counts the number of stock items for a business, optionally filtered by tenant and OData query options.

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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count stock items by business
        api_response = api_instance.count_stock_items_by_business(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->count_stock_items_by_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->count_stock_items_by_business: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
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

# **create_stock_item**
> create_stock_item(tenant_id, api_version=api_version, x_api_version=x_api_version, catalog_item_create_dto=catalog_item_create_dto)

Create a new stock item

Creates a new stock item for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.catalog_item_create_dto import CatalogItemCreateDto
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    catalog_item_create_dto = openapi_client.CatalogItemCreateDto() # CatalogItemCreateDto |  (optional)

    try:
        # Create a new stock item
        api_instance.create_stock_item(tenant_id, api_version=api_version, x_api_version=x_api_version, catalog_item_create_dto=catalog_item_create_dto)
    except Exception as e:
        print("Exception when calling ItemsApi->create_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **catalog_item_create_dto** | [**CatalogItemCreateDto**](CatalogItemCreateDto.md)|  | [optional] 

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

# **delete_stock_item**
> delete_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version)

Delete a stock item

Deletes a stock item for the specified tenant and item ID.

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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a stock item
        api_instance.delete_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **get_extended_stock_item_by_id**
> CatalogItemDtoEnvelope get_extended_stock_item_by_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get extended stock item by ID

Retrieves extended information for a stock item by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.catalog_item_dto_envelope import CatalogItemDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get extended stock item by ID
        api_response = api_instance.get_extended_stock_item_by_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_extended_stock_item_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_extended_stock_item_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CatalogItemDtoEnvelope**](CatalogItemDtoEnvelope.md)

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

# **get_product_primary_image_async**
> EmptyEnvelope get_product_primary_image_async(item_id, api_version=api_version, x_api_version=x_api_version)

Get item primary image

Retrieves the primary image for a specific catalog item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get item primary image
        api_response = api_instance.get_product_primary_image_async(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_product_primary_image_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_product_primary_image_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_item_attachment_by_id**
> ItemAttachmentDtoEnvelope get_stock_item_attachment_by_id(item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)

Get attachment by ID for a stock item

Retrieves a specific attachment by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_dto_envelope import ItemAttachmentDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get attachment by ID for a stock item
        api_response = api_instance.get_stock_item_attachment_by_id(item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttachmentDtoEnvelope**](ItemAttachmentDtoEnvelope.md)

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

# **get_stock_item_attachments_by_item_id**
> ItemAttachmentDtoListEnvelope get_stock_item_attachments_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get attachments for a stock item

Retrieves all attachments associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_dto_list_envelope import ItemAttachmentDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get attachments for a stock item
        api_response = api_instance.get_stock_item_attachments_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_attachments_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_attachments_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttachmentDtoListEnvelope**](ItemAttachmentDtoListEnvelope.md)

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

# **get_stock_item_attribute_option_by_id**
> ItemAttributeOptionDtoEnvelope get_stock_item_attribute_option_by_id(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)

Get attribute option by ID for a stock item

Retrieves a specific attribute option by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get attribute option by ID for a stock item
        api_response = api_instance.get_stock_item_attribute_option_by_id(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_attribute_option_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_attribute_option_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_attribute_option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

# **get_stock_item_attribute_options_by_item_id**
> ItemAttributeOptionDtoListEnvelope get_stock_item_attribute_options_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get attribute options for a stock item

Retrieves all attribute options associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_list_envelope import ItemAttributeOptionDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get attribute options for a stock item
        api_response = api_instance.get_stock_item_attribute_options_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_attribute_options_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_attribute_options_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoListEnvelope**](ItemAttributeOptionDtoListEnvelope.md)

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

# **get_stock_item_brand_by_id**
> ItemBrandDtoEnvelope get_stock_item_brand_by_id(item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)

Get brand by ID for a stock item

Retrieves a specific brand by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get brand by ID for a stock item
        api_response = api_instance.get_stock_item_brand_by_id(item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_brand_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_brand_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_brand_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

# **get_stock_item_brands_by_item_id**
> ItemBrandDtoListEnvelope get_stock_item_brands_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get brands for a stock item

Retrieves all brands associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_list_envelope import ItemBrandDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get brands for a stock item
        api_response = api_instance.get_stock_item_brands_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_brands_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_brands_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoListEnvelope**](ItemBrandDtoListEnvelope.md)

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

# **get_stock_item_by_id**
> CatalogItemDtoEnvelope get_stock_item_by_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get stock item by ID

Retrieves a stock item by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.catalog_item_dto_envelope import CatalogItemDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get stock item by ID
        api_response = api_instance.get_stock_item_by_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CatalogItemDtoEnvelope**](CatalogItemDtoEnvelope.md)

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

# **get_stock_item_categories_by_item_id**
> ItemCategoryDtoListEnvelope get_stock_item_categories_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get categories for a stock item

Retrieves all categories associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_list_envelope import ItemCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get categories for a stock item
        api_response = api_instance.get_stock_item_categories_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_categories_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_categories_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoListEnvelope**](ItemCategoryDtoListEnvelope.md)

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

# **get_stock_item_category_by_id**
> ItemCategoryDtoEnvelope get_stock_item_category_by_id(item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)

Get category by ID for a stock item

Retrieves a specific category by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_envelope import ItemCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get category by ID for a stock item
        api_response = api_instance.get_stock_item_category_by_id(item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoEnvelope**](ItemCategoryDtoEnvelope.md)

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

# **get_stock_item_google_categories_by_item_id**
> ItemGoogleCategoryDtoListEnvelope get_stock_item_google_categories_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get Google categories for a stock item

Retrieves all Google categories associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Google categories for a stock item
        api_response = api_instance.get_stock_item_google_categories_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_google_categories_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_google_categories_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoListEnvelope**](ItemGoogleCategoryDtoListEnvelope.md)

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

# **get_stock_item_google_category_by_id**
> ItemGoogleCategoryDtoEnvelope get_stock_item_google_category_by_id(item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)

Get Google category by ID for a stock item

Retrieves a specific Google category by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_envelope import ItemGoogleCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_google_category_id = 'item_google_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Google category by ID for a stock item
        api_response = api_instance.get_stock_item_google_category_by_id(item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_google_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_google_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_google_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoEnvelope**](ItemGoogleCategoryDtoEnvelope.md)

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

# **get_stock_item_image_by_id**
> ItemImageDtoEnvelope get_stock_item_image_by_id(item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)

Get image by ID for a stock item

Retrieves a specific image by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_envelope import ItemImageDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get image by ID for a stock item
        api_response = api_instance.get_stock_item_image_by_id(item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_image_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_image_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_image_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoEnvelope**](ItemImageDtoEnvelope.md)

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

# **get_stock_item_images_by_item_id**
> ItemImageDtoListEnvelope get_stock_item_images_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get images for a stock item

Retrieves all images associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_list_envelope import ItemImageDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get images for a stock item
        api_response = api_instance.get_stock_item_images_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_images_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_images_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoListEnvelope**](ItemImageDtoListEnvelope.md)

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

# **get_stock_item_price_rule_by_id**
> PricingRuleDtoEnvelope get_stock_item_price_rule_by_id(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)

Get price rule by ID for a stock item

Retrieves a specific pricing rule by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_price_rule_id = 'item_price_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get price rule by ID for a stock item
        api_response = api_instance.get_stock_item_price_rule_by_id(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_price_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_price_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_price_rule_id** | **str**|  | 
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

# **get_stock_item_price_rules_by_item_id**
> PricingRuleDtoListEnvelope get_stock_item_price_rules_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get price rules for a stock item

Retrieves all pricing rules associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_list_envelope import PricingRuleDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get price rules for a stock item
        api_response = api_instance.get_stock_item_price_rules_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_price_rules_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_price_rules_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
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

# **get_stock_item_question_by_id**
> ItemQuestionDtoEnvelope get_stock_item_question_by_id(item_id, item_question_id, api_version=api_version, x_api_version=x_api_version)

Get question by ID for a stock item

Retrieves a specific question by ID for a stock item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_question_id = 'item_question_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get question by ID for a stock item
        api_response = api_instance.get_stock_item_question_by_id(item_id, item_question_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_question_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_question_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
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

# **get_stock_item_questions_by_item_id**
> ItemQuestionDtoListEnvelope get_stock_item_questions_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get questions for a stock item

Retrieves all questions associated with a specific stock item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get questions for a stock item
        api_response = api_instance.get_stock_item_questions_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_questions_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_questions_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
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

# **get_stock_item_refund_policies_by_item_id**
> ItemRefundPolicyDtoListEnvelope get_stock_item_refund_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get refund policies for a stock item

Retrieves all refund policies associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_list_envelope import ItemRefundPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get refund policies for a stock item
        api_response = api_instance.get_stock_item_refund_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_refund_policies_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_refund_policies_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoListEnvelope**](ItemRefundPolicyDtoListEnvelope.md)

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

# **get_stock_item_refund_policy_by_id**
> ItemRefundPolicyDtoEnvelope get_stock_item_refund_policy_by_id(item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Get refund policy by ID for a stock item

Retrieves a specific refund policy by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_envelope import ItemRefundPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_refund_policy_id = 'item_refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get refund policy by ID for a stock item
        api_response = api_instance.get_stock_item_refund_policy_by_id(item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_refund_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_refund_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_refund_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoEnvelope**](ItemRefundPolicyDtoEnvelope.md)

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

# **get_stock_item_return_policies_by_item_id**
> ItemReturnPolicyDtoListEnvelope get_stock_item_return_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get return policies for a stock item

Retrieves all return policies associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_list_envelope import ItemReturnPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get return policies for a stock item
        api_response = api_instance.get_stock_item_return_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_return_policies_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_return_policies_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoListEnvelope**](ItemReturnPolicyDtoListEnvelope.md)

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

# **get_stock_item_return_policy_by_id**
> ItemReturnPolicyDtoEnvelope get_stock_item_return_policy_by_id(item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)

Get return policy by ID for a stock item

Retrieves a specific return policy by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_envelope import ItemReturnPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_return_policy_id = 'item_return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get return policy by ID for a stock item
        api_response = api_instance.get_stock_item_return_policy_by_id(item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_return_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_return_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_return_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoEnvelope**](ItemReturnPolicyDtoEnvelope.md)

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

# **get_stock_item_review_by_id**
> ItemReviewDtoEnvelope get_stock_item_review_by_id(item_id, item_review_id, api_version=api_version, x_api_version=x_api_version)

Get review by ID for a stock item

Retrieves a specific review by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_review_id = 'item_review_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get review by ID for a stock item
        api_response = api_instance.get_stock_item_review_by_id(item_id, item_review_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_review_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_review_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_review_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReviewDtoEnvelope**](ItemReviewDtoEnvelope.md)

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

# **get_stock_item_reviews_by_item_id**
> ItemReviewDtoListEnvelope get_stock_item_reviews_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get reviews for a stock item

Retrieves all reviews associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_list_envelope import ItemReviewDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get reviews for a stock item
        api_response = api_instance.get_stock_item_reviews_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_reviews_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_reviews_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReviewDtoListEnvelope**](ItemReviewDtoListEnvelope.md)

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

# **get_stock_item_shipping_policies_by_item_id**
> ItemShippingPolicyDtoListEnvelope get_stock_item_shipping_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get shipping policies for a stock item

Retrieves all shipping policies associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_list_envelope import ItemShippingPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping policies for a stock item
        api_response = api_instance.get_stock_item_shipping_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_shipping_policies_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_shipping_policies_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoListEnvelope**](ItemShippingPolicyDtoListEnvelope.md)

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

# **get_stock_item_shipping_policy_by_id**
> ItemShippingPolicyDtoEnvelope get_stock_item_shipping_policy_by_id(item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)

Get shipping policy by ID for a stock item

Retrieves a specific shipping policy by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_envelope import ItemShippingPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_shipping_policy_id = 'item_shipping_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get shipping policy by ID for a stock item
        api_response = api_instance.get_stock_item_shipping_policy_by_id(item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_shipping_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_shipping_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_shipping_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoEnvelope**](ItemShippingPolicyDtoEnvelope.md)

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

# **get_stock_item_tag_by_id**
> ItemTagDtoEnvelope get_stock_item_tag_by_id(item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)

Get tag by ID for a stock item

Retrieves a specific tag by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_envelope import ItemTagDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tag by ID for a stock item
        api_response = api_instance.get_stock_item_tag_by_id(item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_tag_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_tag_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoEnvelope**](ItemTagDtoEnvelope.md)

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

# **get_stock_item_tags_by_item_id**
> ItemTagDtoListEnvelope get_stock_item_tags_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get tags for a stock item

Retrieves all tags associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_list_envelope import ItemTagDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tags for a stock item
        api_response = api_instance.get_stock_item_tags_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_tags_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_tags_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoListEnvelope**](ItemTagDtoListEnvelope.md)

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

# **get_stock_item_tax_policies_by_item_id**
> ItemTaxPolicyDtoListEnvelope get_stock_item_tax_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get tax policies for a stock item

Retrieves all tax policies associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_list_envelope import ItemTaxPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax policies for a stock item
        api_response = api_instance.get_stock_item_tax_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_tax_policies_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_tax_policies_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoListEnvelope**](ItemTaxPolicyDtoListEnvelope.md)

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

# **get_stock_item_tax_policy_by_id**
> ItemTaxPolicyDtoEnvelope get_stock_item_tax_policy_by_id(item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Get tax policy by ID for a stock item

Retrieves a specific tax policy by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_envelope import ItemTaxPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_tax_policy_id = 'item_tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get tax policy by ID for a stock item
        api_response = api_instance.get_stock_item_tax_policy_by_id(item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_tax_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_tax_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoEnvelope**](ItemTaxPolicyDtoEnvelope.md)

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

# **get_stock_item_type_by_id**
> ItemTypeDtoEnvelope get_stock_item_type_by_id(item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)

Get type by ID for a stock item

Retrieves a specific type by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get type by ID for a stock item
        api_response = api_instance.get_stock_item_type_by_id(item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_type_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **get_stock_item_types_by_item_id**
> ItemTypeDtoListEnvelope get_stock_item_types_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get types for a stock item

Retrieves all types associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_list_envelope import ItemTypeDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get types for a stock item
        api_response = api_instance.get_stock_item_types_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_types_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_types_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoListEnvelope**](ItemTypeDtoListEnvelope.md)

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

# **get_stock_item_warranty_policies_by_item_id**
> ItemWarrantyPolicyDtoListEnvelope get_stock_item_warranty_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)

Get warranty policies for a stock item

Retrieves all warranty policies associated with a specific stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_list_envelope import ItemWarrantyPolicyDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warranty policies for a stock item
        api_response = api_instance.get_stock_item_warranty_policies_by_item_id(item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_warranty_policies_by_item_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_warranty_policies_by_item_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoListEnvelope**](ItemWarrantyPolicyDtoListEnvelope.md)

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

# **get_stock_item_warranty_policy_by_id**
> ItemWarrantyPolicyDtoEnvelope get_stock_item_warranty_policy_by_id(item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Get warranty policy by ID for a stock item

Retrieves a specific warranty policy by ID for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_envelope import ItemWarrantyPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_warranty_policy_id = 'item_warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warranty policy by ID for a stock item
        api_response = api_instance.get_stock_item_warranty_policy_by_id(item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_item_warranty_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_item_warranty_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_warranty_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoEnvelope**](ItemWarrantyPolicyDtoEnvelope.md)

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

# **get_stock_items_odata_max_price**
> MoneyEnvelope get_stock_items_odata_max_price(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get max price of stock items

Retrieves the maximum price among all stock items, optionally filtered by tenant and OData query options.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get max price of stock items
        api_response = api_instance.get_stock_items_odata_max_price(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_items_odata_max_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_items_odata_max_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **get_stock_items_odata_min_price**
> MoneyEnvelope get_stock_items_odata_min_price(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get min price of stock items

Retrieves the minimum price among all stock items, optionally filtered by tenant and OData query options.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get min price of stock items
        api_response = api_instance.get_stock_items_odata_min_price(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_items_odata_min_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_items_odata_min_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **get_stock_items_query**
> CatalogItemDtoListEnvelope get_stock_items_query(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all stock items

Retrieves all stock items, optionally filtered by tenant and OData query options.

### Example


```python
import openapi_client
from openapi_client.models.catalog_item_dto_list_envelope import CatalogItemDtoListEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all stock items
        api_response = api_instance.get_stock_items_query(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->get_stock_items_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_stock_items_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CatalogItemDtoListEnvelope**](CatalogItemDtoListEnvelope.md)

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

# **relate_attachment_to_stock_item**
> ItemAttachmentDtoEnvelope relate_attachment_to_stock_item(tenant_id, item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version, item_attachment_create_dto=item_attachment_create_dto)

Relate attachment to stock item

Associates an attachment with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_create_dto import ItemAttachmentCreateDto
from openapi_client.models.item_attachment_dto_envelope import ItemAttachmentDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_attachment_create_dto = openapi_client.ItemAttachmentCreateDto() # ItemAttachmentCreateDto |  (optional)

    try:
        # Relate attachment to stock item
        api_response = api_instance.relate_attachment_to_stock_item(tenant_id, item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version, item_attachment_create_dto=item_attachment_create_dto)
        print("The response of ItemsApi->relate_attachment_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_attachment_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_attachment_create_dto** | [**ItemAttachmentCreateDto**](ItemAttachmentCreateDto.md)|  | [optional] 

### Return type

[**ItemAttachmentDtoEnvelope**](ItemAttachmentDtoEnvelope.md)

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

# **relate_attribute_option_to_stock_item**
> ItemAttributeOptionDtoEnvelope relate_attribute_option_to_stock_item(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)

Relate attribute option to stock item

Associates an attribute option with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate attribute option to stock item
        api_response = api_instance.relate_attribute_option_to_stock_item(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_attribute_option_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_attribute_option_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_attribute_option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

# **relate_brand_to_stock_item**
> ItemBrandDtoEnvelope relate_brand_to_stock_item(tenant_id, item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)

Relate brand to stock item

Associates a brand with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate brand to stock item
        api_response = api_instance.relate_brand_to_stock_item(tenant_id, item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_brand_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_brand_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_brand_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

# **relate_category_to_stock_item**
> ItemCategoryDtoEnvelope relate_category_to_stock_item(tenant_id, item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)

Relate category to stock item

Associates a category with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_envelope import ItemCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate category to stock item
        api_response = api_instance.relate_category_to_stock_item(tenant_id, item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_category_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_category_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoEnvelope**](ItemCategoryDtoEnvelope.md)

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

# **relate_google_category_to_stock_item**
> ItemGoogleCategoryDtoEnvelope relate_google_category_to_stock_item(tenant_id, item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)

Relate Google category to stock item

Associates a Google category with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_envelope import ItemGoogleCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_google_category_id = 'item_google_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate Google category to stock item
        api_response = api_instance.relate_google_category_to_stock_item(tenant_id, item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_google_category_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_google_category_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_google_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoEnvelope**](ItemGoogleCategoryDtoEnvelope.md)

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

# **relate_image_to_stock_item**
> ItemImageDtoEnvelope relate_image_to_stock_item(tenant_id, item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)

Relate image to stock item

Associates an image with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_envelope import ItemImageDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate image to stock item
        api_response = api_instance.relate_image_to_stock_item(tenant_id, item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_image_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_image_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_image_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoEnvelope**](ItemImageDtoEnvelope.md)

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

# **relate_price_rule_to_stock_item**
> PricingRuleDtoEnvelope relate_price_rule_to_stock_item(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)

Relate price rule to stock item

Associates a pricing rule with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_price_rule_id = 'item_price_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate price rule to stock item
        api_response = api_instance.relate_price_rule_to_stock_item(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_price_rule_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_price_rule_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_price_rule_id** | **str**|  | 
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

# **relate_question_to_stock_item**
> ItemQuestionDtoEnvelope relate_question_to_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, item_question_record_create_dto=item_question_record_create_dto)

Create question for stock item

Creates a new question for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_question_dto_envelope import ItemQuestionDtoEnvelope
from openapi_client.models.item_question_record_create_dto import ItemQuestionRecordCreateDto
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_question_record_create_dto = openapi_client.ItemQuestionRecordCreateDto() # ItemQuestionRecordCreateDto |  (optional)

    try:
        # Create question for stock item
        api_response = api_instance.relate_question_to_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, item_question_record_create_dto=item_question_record_create_dto)
        print("The response of ItemsApi->relate_question_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_question_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_question_record_create_dto** | [**ItemQuestionRecordCreateDto**](ItemQuestionRecordCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relate_refund_policy_to_stock_item**
> ItemRefundPolicyDtoEnvelope relate_refund_policy_to_stock_item(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate refund policy to stock item

Associates a refund policy with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_envelope import ItemRefundPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_refund_policy_id = 'item_refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate refund policy to stock item
        api_response = api_instance.relate_refund_policy_to_stock_item(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_refund_policy_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_refund_policy_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_refund_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoEnvelope**](ItemRefundPolicyDtoEnvelope.md)

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

# **relate_return_policy_to_stock_item**
> ItemReturnPolicyDtoEnvelope relate_return_policy_to_stock_item(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate return policy to stock item

Associates a return policy with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_envelope import ItemReturnPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_return_policy_id = 'item_return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate return policy to stock item
        api_response = api_instance.relate_return_policy_to_stock_item(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_return_policy_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_return_policy_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_return_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoEnvelope**](ItemReturnPolicyDtoEnvelope.md)

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

# **relate_review_to_stock_item**
> ItemReviewDtoEnvelope relate_review_to_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, item_review_record_create_dto=item_review_record_create_dto)

Create review for stock item

Creates a new review for a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope
from openapi_client.models.item_review_record_create_dto import ItemReviewRecordCreateDto
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_review_record_create_dto = openapi_client.ItemReviewRecordCreateDto() # ItemReviewRecordCreateDto |  (optional)

    try:
        # Create review for stock item
        api_response = api_instance.relate_review_to_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, item_review_record_create_dto=item_review_record_create_dto)
        print("The response of ItemsApi->relate_review_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_review_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_review_record_create_dto** | [**ItemReviewRecordCreateDto**](ItemReviewRecordCreateDto.md)|  | [optional] 

### Return type

[**ItemReviewDtoEnvelope**](ItemReviewDtoEnvelope.md)

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

# **relate_shipping_policy_to_stock_item**
> ItemShippingPolicyDtoEnvelope relate_shipping_policy_to_stock_item(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate shipping policy to stock item

Associates a shipping policy with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_envelope import ItemShippingPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_shipping_policy_id = 'item_shipping_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate shipping policy to stock item
        api_response = api_instance.relate_shipping_policy_to_stock_item(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_shipping_policy_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_shipping_policy_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_shipping_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoEnvelope**](ItemShippingPolicyDtoEnvelope.md)

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

# **relate_tag_to_stock_item**
> ItemTagDtoEnvelope relate_tag_to_stock_item(tenant_id, item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)

Relate tag to stock item

Associates a tag with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_envelope import ItemTagDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate tag to stock item
        api_response = api_instance.relate_tag_to_stock_item(tenant_id, item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_tag_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_tag_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoEnvelope**](ItemTagDtoEnvelope.md)

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

# **relate_tax_policy_to_stock_item**
> ItemTaxPolicyDtoEnvelope relate_tax_policy_to_stock_item(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate tax policy to stock item

Associates a tax policy with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_envelope import ItemTaxPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_tax_policy_id = 'item_tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate tax policy to stock item
        api_response = api_instance.relate_tax_policy_to_stock_item(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_tax_policy_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_tax_policy_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoEnvelope**](ItemTaxPolicyDtoEnvelope.md)

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

# **relate_type_to_stock_item**
> ItemTypeDtoEnvelope relate_type_to_stock_item(tenant_id, item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)

Relate type to stock item

Associates a type with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate type to stock item
        api_response = api_instance.relate_type_to_stock_item(tenant_id, item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_type_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_type_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **relate_warranty_policy_to_stock_item**
> ItemWarrantyPolicyDtoEnvelope relate_warranty_policy_to_stock_item(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Relate warranty policy to stock item

Associates a warranty policy with a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_envelope import ItemWarrantyPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_warranty_policy_id = 'item_warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Relate warranty policy to stock item
        api_response = api_instance.relate_warranty_policy_to_stock_item(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->relate_warranty_policy_to_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->relate_warranty_policy_to_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_warranty_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoEnvelope**](ItemWarrantyPolicyDtoEnvelope.md)

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

# **remove_attachment_from_stock_item**
> ItemAttachmentDtoEnvelope remove_attachment_from_stock_item(tenant_id, item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)

Remove attachment from stock item

Removes an attachment from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attachment_dto_envelope import ItemAttachmentDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_attachment_id = 'item_attachment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove attachment from stock item
        api_response = api_instance.remove_attachment_from_stock_item(tenant_id, item_id, item_attachment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_attachment_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_attachment_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_attachment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttachmentDtoEnvelope**](ItemAttachmentDtoEnvelope.md)

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

# **remove_attribute_option_from_stock_item**
> ItemAttributeOptionDtoEnvelope remove_attribute_option_from_stock_item(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)

Remove attribute option from stock item

Removes an attribute option from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_attribute_option_dto_envelope import ItemAttributeOptionDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_attribute_option_id = 'item_attribute_option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove attribute option from stock item
        api_response = api_instance.remove_attribute_option_from_stock_item(item_id, item_attribute_option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_attribute_option_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_attribute_option_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_attribute_option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemAttributeOptionDtoEnvelope**](ItemAttributeOptionDtoEnvelope.md)

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

# **remove_brand_from_stock_item**
> ItemBrandDtoEnvelope remove_brand_from_stock_item(tenant_id, item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)

Remove brand from stock item

Removes a brand association from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_brand_dto_envelope import ItemBrandDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_brand_id = 'item_brand_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove brand from stock item
        api_response = api_instance.remove_brand_from_stock_item(tenant_id, item_id, item_brand_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_brand_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_brand_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_brand_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemBrandDtoEnvelope**](ItemBrandDtoEnvelope.md)

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

# **remove_category_from_stock_item**
> ItemCategoryDtoEnvelope remove_category_from_stock_item(tenant_id, item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)

Remove category from stock item

Removes a category association from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_category_dto_envelope import ItemCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_category_id = 'item_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove category from stock item
        api_response = api_instance.remove_category_from_stock_item(tenant_id, item_id, item_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_category_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_category_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCategoryDtoEnvelope**](ItemCategoryDtoEnvelope.md)

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

# **remove_google_category_from_stock_item**
> ItemGoogleCategoryDtoEnvelope remove_google_category_from_stock_item(tenant_id, item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)

Remove Google category from stock item

Removes a Google category from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_google_category_dto_envelope import ItemGoogleCategoryDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_google_category_id = 'item_google_category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove Google category from stock item
        api_response = api_instance.remove_google_category_from_stock_item(tenant_id, item_id, item_google_category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_google_category_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_google_category_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_google_category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemGoogleCategoryDtoEnvelope**](ItemGoogleCategoryDtoEnvelope.md)

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

# **remove_image_from_stock_item**
> ItemImageDtoEnvelope remove_image_from_stock_item(tenant_id, item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)

Remove image from stock item

Removes an image association from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_image_dto_envelope import ItemImageDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_image_id = 'item_image_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove image from stock item
        api_response = api_instance.remove_image_from_stock_item(tenant_id, item_id, item_image_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_image_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_image_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_image_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemImageDtoEnvelope**](ItemImageDtoEnvelope.md)

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

# **remove_price_rule_from_stock_item**
> PricingRuleDtoEnvelope remove_price_rule_from_stock_item(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)

Remove price rule from stock item

Removes a pricing rule from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    item_price_rule_id = 'item_price_rule_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove price rule from stock item
        api_response = api_instance.remove_price_rule_from_stock_item(item_id, item_price_rule_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_price_rule_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_price_rule_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_price_rule_id** | **str**|  | 
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

# **remove_question_from_stock_item**
> ItemQuestionDtoEnvelope remove_question_from_stock_item(tenant_id, item_id, item_question_id, api_version=api_version, x_api_version=x_api_version)

Remove question from stock item

Removes a question from a stock item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_question_id = 'item_question_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove question from stock item
        api_response = api_instance.remove_question_from_stock_item(tenant_id, item_id, item_question_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_question_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_question_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **remove_refund_policy_from_stock_item**
> ItemRefundPolicyDtoEnvelope remove_refund_policy_from_stock_item(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove refund policy from stock item

Removes a refund policy from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_refund_policy_dto_envelope import ItemRefundPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_refund_policy_id = 'item_refund_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove refund policy from stock item
        api_response = api_instance.remove_refund_policy_from_stock_item(tenant_id, item_id, item_refund_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_refund_policy_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_refund_policy_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_refund_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemRefundPolicyDtoEnvelope**](ItemRefundPolicyDtoEnvelope.md)

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

# **remove_return_policy_from_stock_item**
> ItemReturnPolicyDtoEnvelope remove_return_policy_from_stock_item(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove return policy from stock item

Removes a return policy from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_return_policy_dto_envelope import ItemReturnPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_return_policy_id = 'item_return_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove return policy from stock item
        api_response = api_instance.remove_return_policy_from_stock_item(tenant_id, item_id, item_return_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_return_policy_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_return_policy_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_return_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReturnPolicyDtoEnvelope**](ItemReturnPolicyDtoEnvelope.md)

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

# **remove_review_from_stock_item**
> ItemReviewDtoEnvelope remove_review_from_stock_item(tenant_id, item_id, item_review_id, api_version=api_version, x_api_version=x_api_version)

Remove review from stock item

Removes a review from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_review_id = 'item_review_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove review from stock item
        api_response = api_instance.remove_review_from_stock_item(tenant_id, item_id, item_review_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_review_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_review_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_review_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemReviewDtoEnvelope**](ItemReviewDtoEnvelope.md)

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

# **remove_shipping_policy_from_stock_item**
> ItemShippingPolicyDtoEnvelope remove_shipping_policy_from_stock_item(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove shipping policy from stock item

Removes a shipping policy from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_shipping_policy_dto_envelope import ItemShippingPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_shipping_policy_id = 'item_shipping_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove shipping policy from stock item
        api_response = api_instance.remove_shipping_policy_from_stock_item(tenant_id, item_id, item_shipping_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_shipping_policy_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_shipping_policy_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_shipping_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemShippingPolicyDtoEnvelope**](ItemShippingPolicyDtoEnvelope.md)

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

# **remove_tag_from_stock_item**
> ItemTagDtoEnvelope remove_tag_from_stock_item(tenant_id, item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)

Remove tag from stock item

Removes a tag association from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tag_dto_envelope import ItemTagDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_tag_id = 'item_tag_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove tag from stock item
        api_response = api_instance.remove_tag_from_stock_item(tenant_id, item_id, item_tag_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_tag_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_tag_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_tag_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTagDtoEnvelope**](ItemTagDtoEnvelope.md)

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

# **remove_tax_policy_from_stock_item**
> ItemTaxPolicyDtoEnvelope remove_tax_policy_from_stock_item(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove tax policy from stock item

Removes a tax policy from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_tax_policy_dto_envelope import ItemTaxPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_tax_policy_id = 'item_tax_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove tax policy from stock item
        api_response = api_instance.remove_tax_policy_from_stock_item(tenant_id, item_id, item_tax_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_tax_policy_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_tax_policy_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_tax_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTaxPolicyDtoEnvelope**](ItemTaxPolicyDtoEnvelope.md)

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

# **remove_type_from_stock_item**
> ItemTypeDtoEnvelope remove_type_from_stock_item(tenant_id, item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)

Remove type from stock item

Removes a type association from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_type_id = 'item_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove type from stock item
        api_response = api_instance.remove_type_from_stock_item(tenant_id, item_id, item_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_type_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_type_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemTypeDtoEnvelope**](ItemTypeDtoEnvelope.md)

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

# **remove_warranty_policy_from_stock_item**
> ItemWarrantyPolicyDtoEnvelope remove_warranty_policy_from_stock_item(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)

Remove warranty policy from stock item

Removes a warranty policy from a stock item.

### Example


```python
import openapi_client
from openapi_client.models.item_warranty_policy_dto_envelope import ItemWarrantyPolicyDtoEnvelope
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    item_warranty_policy_id = 'item_warranty_policy_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove warranty policy from stock item
        api_response = api_instance.remove_warranty_policy_from_stock_item(tenant_id, item_id, item_warranty_policy_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ItemsApi->remove_warranty_policy_from_stock_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_warranty_policy_from_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_warranty_policy_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemWarrantyPolicyDtoEnvelope**](ItemWarrantyPolicyDtoEnvelope.md)

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

# **update_product_primary_image_async**
> EmptyEnvelope update_product_primary_image_async(item_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, data=data)

Update item primary image

Updates the primary image for a specific catalog item.

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
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    data = None # bytearray |  (optional)

    try:
        # Update item primary image
        api_response = api_instance.update_product_primary_image_async(item_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version, data=data)
        print("The response of ItemsApi->update_product_primary_image_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_product_primary_image_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **data** | **bytearray**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

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

# **update_stock_item**
> update_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, catalog_item_update_dto=catalog_item_update_dto)

Update a stock item

Updates an existing stock item for the specified tenant and item ID.

### Example


```python
import openapi_client
from openapi_client.models.catalog_item_update_dto import CatalogItemUpdateDto
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
    api_instance = openapi_client.ItemsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    catalog_item_update_dto = openapi_client.CatalogItemUpdateDto() # CatalogItemUpdateDto |  (optional)

    try:
        # Update a stock item
        api_instance.update_stock_item(tenant_id, item_id, api_version=api_version, x_api_version=x_api_version, catalog_item_update_dto=catalog_item_update_dto)
    except Exception as e:
        print("Exception when calling ItemsApi->update_stock_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **catalog_item_update_dto** | [**CatalogItemUpdateDto**](CatalogItemUpdateDto.md)|  | [optional] 

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

