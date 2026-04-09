# CostCentreGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**parent_cost_centres_group_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_group_dto import CostCentreGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreGroupDto from a JSON string
cost_centre_group_dto_instance = CostCentreGroupDto.from_json(json)
# print the JSON string representation of the object
print(CostCentreGroupDto.to_json())

# convert the object into a dict
cost_centre_group_dto_dict = cost_centre_group_dto_instance.to_dict()
# create an instance of CostCentreGroupDto from a dict
cost_centre_group_dto_from_dict = CostCentreGroupDto.from_dict(cost_centre_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


