# BulkProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**supplier** | **str** |  | [optional] 
**tax_policies** | **str** |  | [optional] 
**supplier_code** | **str** |  | [optional] 
**google_category** | **str** |  | [optional] 
**shipping_country** | **str** |  | [optional] 
**regular_price** | **float** |  | [optional] 
**discount_percentage** | **float** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**current_stock** | **float** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**in_stock** | **bool** |  | [optional] 
**on_discount** | **bool** |  | [optional] 
**by_request** | **bool** |  | [optional] 
**is_fixed_discount** | **bool** |  | [optional] 
**manage_inventory** | **bool** |  | [optional] 
**is_deadline_discount** | **bool** |  | [optional] 
**deadline_discount_from_date** | **datetime** |  | [optional] 
**deadline_discount_due_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.bulk_product import BulkProduct

# TODO update the JSON string below
json = "{}"
# create an instance of BulkProduct from a JSON string
bulk_product_instance = BulkProduct.from_json(json)
# print the JSON string representation of the object
print(BulkProduct.to_json())

# convert the object into a dict
bulk_product_dict = bulk_product_instance.to_dict()
# create an instance of BulkProduct from a dict
bulk_product_from_dict = BulkProduct.from_dict(bulk_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


