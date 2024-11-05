# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.1.4089
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://fenixalliance.com.co/Support](https://fenixalliance.com.co/Support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_count_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_count_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_count_get**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_count_get) | **GET** /api/v2/PricingService/DiscountLists/Count | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_delete**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_delete) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId} | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/Count | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_discounts_get**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_discounts_post**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_post) | **POST** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_get**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId} | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_discount_list_id_put**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_put) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId} | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_get**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_get) | **GET** /api/v2/PricingService/DiscountLists | 
*DiscountListsApi* | [**api_v2_pricing_service_discount_lists_post**](docs/DiscountListsApi.md#api_v2_pricing_service_discount_lists_post) | **POST** /api/v2/PricingService/DiscountLists | 
*DiscountListsApi* | [**get_discount_list_entry**](docs/DiscountListsApi.md#get_discount_list_entry) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_count_get**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_count_get) | **GET** /api/v2/PricingService/PriceLists/Count | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_get**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_get) | **GET** /api/v2/PricingService/PriceLists | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_post**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_post) | **POST** /api/v2/PricingService/PriceLists | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_price_list_id_delete**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_delete) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId} | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_price_list_id_prices_post**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_post) | **POST** /api/v2/PricingService/PriceLists/{priceListId}/Prices | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_price_id_delete) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_prices_price_id_put) | **PUT** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
*PriceListsApi* | [**api_v2_pricing_service_price_lists_price_list_id_put**](docs/PriceListsApi.md#api_v2_pricing_service_price_lists_price_list_id_put) | **PUT** /api/v2/PricingService/PriceLists/{priceListId} | 
*PriceListsApi* | [**get_price_list_async**](docs/PriceListsApi.md#get_price_list_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId} | 
*PriceListsApi* | [**get_price_list_price_async**](docs/PriceListsApi.md#get_price_list_price_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | 
*PriceListsApi* | [**get_price_list_prices_async**](docs/PriceListsApi.md#get_price_list_prices_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices | 
*PricesApi* | [**api_v2_pricing_service_prices_item_id_final_price_get**](docs/PricesApi.md#api_v2_pricing_service_prices_item_id_final_price_get) | **GET** /api/v2/PricingService/Prices/{itemId}/FinalPrice | 
*PricesApi* | [**api_v2_pricing_service_prices_item_id_price_get**](docs/PricesApi.md#api_v2_pricing_service_prices_item_id_price_get) | **GET** /api/v2/PricingService/Prices/{itemId}/Price | 
*PricesApi* | [**api_v2_pricing_service_prices_item_id_total_savings_get**](docs/PricesApi.md#api_v2_pricing_service_prices_item_id_total_savings_get) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalSavings | 
*PricesApi* | [**api_v2_pricing_service_prices_item_id_total_taxes_get**](docs/PricesApi.md#api_v2_pricing_service_prices_item_id_total_taxes_get) | **GET** /api/v2/PricingService/Prices/{itemId}/TotalTaxes | 


## Documentation For Models

 - [Currency](docs/Currency.md)
 - [DiscountCreateDto](docs/DiscountCreateDto.md)
 - [DiscountDto](docs/DiscountDto.md)
 - [DiscountDtoEnvelope](docs/DiscountDtoEnvelope.md)
 - [DiscountDtoListEnvelope](docs/DiscountDtoListEnvelope.md)
 - [DiscountListCreateDto](docs/DiscountListCreateDto.md)
 - [DiscountListDto](docs/DiscountListDto.md)
 - [DiscountListDtoEnvelope](docs/DiscountListDtoEnvelope.md)
 - [DiscountListDtoListEnvelope](docs/DiscountListDtoListEnvelope.md)
 - [DiscountListUpdateDto](docs/DiscountListUpdateDto.md)
 - [DiscountUpdateDto](docs/DiscountUpdateDto.md)
 - [EmptyEnvelope](docs/EmptyEnvelope.md)
 - [ErrorEnvelope](docs/ErrorEnvelope.md)
 - [Int32Envelope](docs/Int32Envelope.md)
 - [ItemPriceCreateDto](docs/ItemPriceCreateDto.md)
 - [ItemPriceDto](docs/ItemPriceDto.md)
 - [ItemPriceDtoEnvelope](docs/ItemPriceDtoEnvelope.md)
 - [ItemPriceDtoListEnvelope](docs/ItemPriceDtoListEnvelope.md)
 - [ItemPriceUpdateDto](docs/ItemPriceUpdateDto.md)
 - [Money](docs/Money.md)
 - [MoneyEnvelope](docs/MoneyEnvelope.md)
 - [PriceCalculationDto](docs/PriceCalculationDto.md)
 - [PriceCalculationDtoEnvelope](docs/PriceCalculationDtoEnvelope.md)
 - [PriceListCreateDto](docs/PriceListCreateDto.md)
 - [PriceListDto](docs/PriceListDto.md)
 - [PriceListDtoEnvelope](docs/PriceListDtoEnvelope.md)
 - [PriceListDtoListEnvelope](docs/PriceListDtoListEnvelope.md)
 - [PriceListUpdateDto](docs/PriceListUpdateDto.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@fenix-alliance.com

