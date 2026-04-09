# CostCentreGroupDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CostCentreGroupDto]**](CostCentreGroupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_group_dto_list_envelope import CostCentreGroupDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreGroupDtoListEnvelope from a JSON string
cost_centre_group_dto_list_envelope_instance = CostCentreGroupDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CostCentreGroupDtoListEnvelope.to_json())

# convert the object into a dict
cost_centre_group_dto_list_envelope_dict = cost_centre_group_dto_list_envelope_instance.to_dict()
# create an instance of CostCentreGroupDtoListEnvelope from a dict
cost_centre_group_dto_list_envelope_from_dict = CostCentreGroupDtoListEnvelope.from_dict(cost_centre_group_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


