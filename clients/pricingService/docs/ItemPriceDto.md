# ItemPriceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**discount_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**rounding_policy_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**percent** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.item_price_dto import ItemPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPriceDto from a JSON string
item_price_dto_instance = ItemPriceDto.from_json(json)
# print the JSON string representation of the object
print(ItemPriceDto.to_json())

# convert the object into a dict
item_price_dto_dict = item_price_dto_instance.to_dict()
# create an instance of ItemPriceDto from a dict
item_price_dto_from_dict = ItemPriceDto.from_dict(item_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


