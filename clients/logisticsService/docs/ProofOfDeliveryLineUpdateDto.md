# ProofOfDeliveryLineUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**quantity_expected** | **int** |  | [optional] 
**quantity_received** | **int** |  | [optional] 
**quantity_rejected** | **int** |  | [optional] 
**condition** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**hs_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.proof_of_delivery_line_update_dto import ProofOfDeliveryLineUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProofOfDeliveryLineUpdateDto from a JSON string
proof_of_delivery_line_update_dto_instance = ProofOfDeliveryLineUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProofOfDeliveryLineUpdateDto.to_json())

# convert the object into a dict
proof_of_delivery_line_update_dto_dict = proof_of_delivery_line_update_dto_instance.to_dict()
# create an instance of ProofOfDeliveryLineUpdateDto from a dict
proof_of_delivery_line_update_dto_from_dict = ProofOfDeliveryLineUpdateDto.from_dict(proof_of_delivery_line_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


