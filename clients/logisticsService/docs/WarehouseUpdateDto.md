# WarehouseUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**is_group** | **bool** |  | [optional] 
**shipwire_warehouse_id** | **str** |  | [optional] 
**parent_warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_update_dto import WarehouseUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseUpdateDto from a JSON string
warehouse_update_dto_instance = WarehouseUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WarehouseUpdateDto.to_json())

# convert the object into a dict
warehouse_update_dto_dict = warehouse_update_dto_instance.to_dict()
# create an instance of WarehouseUpdateDto from a dict
warehouse_update_dto_from_dict = WarehouseUpdateDto.from_dict(warehouse_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


