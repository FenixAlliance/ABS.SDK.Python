# SignProofOfDeliveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_by** | **str** |  | [optional] 
**signer_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sign_proof_of_delivery_request import SignProofOfDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignProofOfDeliveryRequest from a JSON string
sign_proof_of_delivery_request_instance = SignProofOfDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(SignProofOfDeliveryRequest.to_json())

# convert the object into a dict
sign_proof_of_delivery_request_dict = sign_proof_of_delivery_request_instance.to_dict()
# create an instance of SignProofOfDeliveryRequest from a dict
sign_proof_of_delivery_request_from_dict = SignProofOfDeliveryRequest.from_dict(sign_proof_of_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


