# ItemCartRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.item_cart_record_create_dto import ItemCartRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCartRecordCreateDto from a JSON string
item_cart_record_create_dto_instance = ItemCartRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemCartRecordCreateDto.to_json())

# convert the object into a dict
item_cart_record_create_dto_dict = item_cart_record_create_dto_instance.to_dict()
# create an instance of ItemCartRecordCreateDto from a dict
item_cart_record_create_dto_from_dict = ItemCartRecordCreateDto.from_dict(item_cart_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


