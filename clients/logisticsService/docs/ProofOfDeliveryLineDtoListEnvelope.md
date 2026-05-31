# ProofOfDeliveryLineDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ProofOfDeliveryLineDto]**](ProofOfDeliveryLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.proof_of_delivery_line_dto_list_envelope import ProofOfDeliveryLineDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProofOfDeliveryLineDtoListEnvelope from a JSON string
proof_of_delivery_line_dto_list_envelope_instance = ProofOfDeliveryLineDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProofOfDeliveryLineDtoListEnvelope.to_json())

# convert the object into a dict
proof_of_delivery_line_dto_list_envelope_dict = proof_of_delivery_line_dto_list_envelope_instance.to_dict()
# create an instance of ProofOfDeliveryLineDtoListEnvelope from a dict
proof_of_delivery_line_dto_list_envelope_from_dict = ProofOfDeliveryLineDtoListEnvelope.from_dict(proof_of_delivery_line_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


