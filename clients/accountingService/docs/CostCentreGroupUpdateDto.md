# CostCentreGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**parent_cost_centres_group_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_group_update_dto import CostCentreGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreGroupUpdateDto from a JSON string
cost_centre_group_update_dto_instance = CostCentreGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CostCentreGroupUpdateDto.to_json())

# convert the object into a dict
cost_centre_group_update_dto_dict = cost_centre_group_update_dto_instance.to_dict()
# create an instance of CostCentreGroupUpdateDto from a dict
cost_centre_group_update_dto_from_dict = CostCentreGroupUpdateDto.from_dict(cost_centre_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


