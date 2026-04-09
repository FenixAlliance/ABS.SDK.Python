# AssetRepairDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **object** |  | [optional] 
**business_profile_record_id** | **object** |  | [optional] 
**asset_id** | **object** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**repair_status** | **str** |  | [optional] 
**scheduled_date** | **datetime** |  | [optional] 
**completion_date** | **datetime** |  | [optional] 
**reported_date** | **datetime** |  | [optional] 
**estimated_cost** | **float** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**problem_description** | **str** |  | [optional] 
**repair_description** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**asset_maintenance_team_id** | **str** |  | [optional] 
**asset_maintenance_team_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_repair_dto import AssetRepairDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRepairDto from a JSON string
asset_repair_dto_instance = AssetRepairDto.from_json(json)
# print the JSON string representation of the object
print(AssetRepairDto.to_json())

# convert the object into a dict
asset_repair_dto_dict = asset_repair_dto_instance.to_dict()
# create an instance of AssetRepairDto from a dict
asset_repair_dto_from_dict = AssetRepairDto.from_dict(asset_repair_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


