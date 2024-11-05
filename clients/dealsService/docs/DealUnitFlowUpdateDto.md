# DealUnitFlowUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_business_process_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tenant_enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_flow_update_dto import DealUnitFlowUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitFlowUpdateDto from a JSON string
deal_unit_flow_update_dto_instance = DealUnitFlowUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitFlowUpdateDto.to_json())

# convert the object into a dict
deal_unit_flow_update_dto_dict = deal_unit_flow_update_dto_instance.to_dict()
# create an instance of DealUnitFlowUpdateDto from a dict
deal_unit_flow_update_dto_from_dict = DealUnitFlowUpdateDto.from_dict(deal_unit_flow_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


