# CostCentreCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**cost_centre_type** | **str** |  | [optional] 
**cost_centres_group_id** | **str** |  | [optional] 
**parent_cost_centre_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_create_dto import CostCentreCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreCreateDto from a JSON string
cost_centre_create_dto_instance = CostCentreCreateDto.from_json(json)
# print the JSON string representation of the object
print(CostCentreCreateDto.to_json())

# convert the object into a dict
cost_centre_create_dto_dict = cost_centre_create_dto_instance.to_dict()
# create an instance of CostCentreCreateDto from a dict
cost_centre_create_dto_from_dict = CostCentreCreateDto.from_dict(cost_centre_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


