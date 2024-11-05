# DealUnitFlowStageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**order** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**deal_unit_flow_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**parent_business_process_stage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_flow_stage_dto import DealUnitFlowStageDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitFlowStageDto from a JSON string
deal_unit_flow_stage_dto_instance = DealUnitFlowStageDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitFlowStageDto.to_json())

# convert the object into a dict
deal_unit_flow_stage_dto_dict = deal_unit_flow_stage_dto_instance.to_dict()
# create an instance of DealUnitFlowStageDto from a dict
deal_unit_flow_stage_dto_from_dict = DealUnitFlowStageDto.from_dict(deal_unit_flow_stage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


