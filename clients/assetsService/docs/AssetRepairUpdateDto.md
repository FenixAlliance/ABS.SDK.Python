# AssetRepairUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repair_status** | **str** |  | [optional] 
**scheduled_date** | **datetime** |  | [optional] 
**completion_date** | **datetime** |  | [optional] 
**estimated_cost** | **float** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**problem_description** | **str** |  | [optional] 
**repair_description** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**asset_maintenance_team_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_repair_update_dto import AssetRepairUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRepairUpdateDto from a JSON string
asset_repair_update_dto_instance = AssetRepairUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetRepairUpdateDto.to_json())

# convert the object into a dict
asset_repair_update_dto_dict = asset_repair_update_dto_instance.to_dict()
# create an instance of AssetRepairUpdateDto from a dict
asset_repair_update_dto_from_dict = AssetRepairUpdateDto.from_dict(asset_repair_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


