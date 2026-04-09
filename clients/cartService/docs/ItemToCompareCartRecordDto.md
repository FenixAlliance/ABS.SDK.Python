# ItemToCompareCartRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**item_short_description** | **str** |  | [optional] 
**item_primary_image_url** | **str** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**brand_name** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**google_category_id** | **str** |  | [optional] 
**google_category_name** | **str** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_price_in_usd** | **float** |  | [optional] 
**shipping_country_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_to_compare_cart_record_dto import ItemToCompareCartRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemToCompareCartRecordDto from a JSON string
item_to_compare_cart_record_dto_instance = ItemToCompareCartRecordDto.from_json(json)
# print the JSON string representation of the object
print(ItemToCompareCartRecordDto.to_json())

# convert the object into a dict
item_to_compare_cart_record_dto_dict = item_to_compare_cart_record_dto_instance.to_dict()
# create an instance of ItemToCompareCartRecordDto from a dict
item_to_compare_cart_record_dto_from_dict = ItemToCompareCartRecordDto.from_dict(item_to_compare_cart_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


