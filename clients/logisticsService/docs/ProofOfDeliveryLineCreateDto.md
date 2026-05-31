# ProofOfDeliveryLineCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity_expected** | **int** |  | [optional] 
**quantity_received** | **int** |  | [optional] 
**quantity_rejected** | **int** |  | [optional] 
**condition** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**hs_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.proof_of_delivery_line_create_dto import ProofOfDeliveryLineCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProofOfDeliveryLineCreateDto from a JSON string
proof_of_delivery_line_create_dto_instance = ProofOfDeliveryLineCreateDto.from_json(json)
# print the JSON string representation of the object
print(ProofOfDeliveryLineCreateDto.to_json())

# convert the object into a dict
proof_of_delivery_line_create_dto_dict = proof_of_delivery_line_create_dto_instance.to_dict()
# create an instance of ProofOfDeliveryLineCreateDto from a dict
proof_of_delivery_line_create_dto_from_dict = ProofOfDeliveryLineCreateDto.from_dict(proof_of_delivery_line_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


