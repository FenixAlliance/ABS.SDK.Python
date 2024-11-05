# DealUnitFlowCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_business_process_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tenant_enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_flow_create_dto import DealUnitFlowCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitFlowCreateDto from a JSON string
deal_unit_flow_create_dto_instance = DealUnitFlowCreateDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitFlowCreateDto.to_json())

# convert the object into a dict
deal_unit_flow_create_dto_dict = deal_unit_flow_create_dto_instance.to_dict()
# create an instance of DealUnitFlowCreateDto from a dict
deal_unit_flow_create_dto_from_dict = DealUnitFlowCreateDto.from_dict(deal_unit_flow_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


