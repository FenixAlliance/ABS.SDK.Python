# DealUnitFlowStageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**deal_unit_flow_id** | **str** |  | [optional] 
**parent_business_process_stage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_flow_stage_update_dto import DealUnitFlowStageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitFlowStageUpdateDto from a JSON string
deal_unit_flow_stage_update_dto_instance = DealUnitFlowStageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitFlowStageUpdateDto.to_json())

# convert the object into a dict
deal_unit_flow_stage_update_dto_dict = deal_unit_flow_stage_update_dto_instance.to_dict()
# create an instance of DealUnitFlowStageUpdateDto from a dict
deal_unit_flow_stage_update_dto_from_dict = DealUnitFlowStageUpdateDto.from_dict(deal_unit_flow_stage_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


