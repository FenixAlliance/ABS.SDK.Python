# ItemPriceUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**item_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**percent** | **float** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**rounding_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_price_update_dto import ItemPriceUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPriceUpdateDto from a JSON string
item_price_update_dto_instance = ItemPriceUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPriceUpdateDto.to_json())

# convert the object into a dict
item_price_update_dto_dict = item_price_update_dto_instance.to_dict()
# create an instance of ItemPriceUpdateDto from a dict
item_price_update_dto_from_dict = ItemPriceUpdateDto.from_dict(item_price_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


