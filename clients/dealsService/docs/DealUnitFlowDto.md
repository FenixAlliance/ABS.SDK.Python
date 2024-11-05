# DealUnitFlowDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_business_process_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tenant_enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_flow_dto import DealUnitFlowDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitFlowDto from a JSON string
deal_unit_flow_dto_instance = DealUnitFlowDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitFlowDto.to_json())

# convert the object into a dict
deal_unit_flow_dto_dict = deal_unit_flow_dto_instance.to_dict()
# create an instance of DealUnitFlowDto from a dict
deal_unit_flow_dto_from_dict = DealUnitFlowDto.from_dict(deal_unit_flow_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


