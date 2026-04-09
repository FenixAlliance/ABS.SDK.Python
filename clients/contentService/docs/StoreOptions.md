# StoreOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**footer_logo** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**decimal_separator** | **str** |  | [optional] 
**sell_to_all_countries** | **bool** |  | [optional] 
**cart_options** | [**CartOptions**](CartOptions.md) |  | [optional] 
**email_options** | [**EmailOptions**](EmailOptions.md) |  | [optional] 
**coupons_options** | [**CouponsOptions**](CouponsOptions.md) |  | [optional] 
**payment_options** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 
**product_options** | **object** |  | [optional] 
**reviews_options** | [**ReviewsOptions**](ReviewsOptions.md) |  | [optional] 
**advanced_options** | [**AdvancedOptions**](AdvancedOptions.md) |  | [optional] 
**services_options** | [**ServicesOptions**](ServicesOptions.md) |  | [optional] 
**inventory_options** | [**InventoryOptions**](InventoryOptions.md) |  | [optional] 
**integration_options** | [**IntegrationOptions**](IntegrationOptions.md) |  | [optional] 
**measurement_options** | [**MeasurementOptions**](MeasurementOptions.md) |  | [optional] 
**downloadables_options** | [**DownloadablesOptions**](DownloadablesOptions.md) |  | [optional] 
**subscriptions_options** | [**SubscriptionsOptions**](SubscriptionsOptions.md) |  | [optional] 
**tax_calculation_options** | [**TaxCalculationOptions**](TaxCalculationOptions.md) |  | [optional] 
**recommendation_options** | [**RecommendationOptions**](RecommendationOptions.md) |  | [optional] 
**price_calculation_options** | [**PriceCalculationOptions**](PriceCalculationOptions.md) |  | [optional] 
**identity_and_privacy_options** | [**IdentityAndPrivacyOptions**](IdentityAndPrivacyOptions.md) |  | [optional] 
**included_selling_locations** | **List[str]** |  | [optional] 
**excluded_selling_locations** | **List[str]** |  | [optional] 
**included_shipping_locations** | **List[str]** |  | [optional] 
**excluded_shipping_locations** | **List[str]** |  | [optional] 
**currency_position** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.store_options import StoreOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StoreOptions from a JSON string
store_options_instance = StoreOptions.from_json(json)
# print the JSON string representation of the object
print(StoreOptions.to_json())

# convert the object into a dict
store_options_dict = store_options_instance.to_dict()
# create an instance of StoreOptions from a dict
store_options_from_dict = StoreOptions.from_dict(store_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


