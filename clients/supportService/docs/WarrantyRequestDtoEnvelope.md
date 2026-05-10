# WarrantyRequestDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WarrantyRequestDto**](WarrantyRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.warranty_request_dto_envelope import WarrantyRequestDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WarrantyRequestDtoEnvelope from a JSON string
warranty_request_dto_envelope_instance = WarrantyRequestDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WarrantyRequestDtoEnvelope.to_json())

# convert the object into a dict
warranty_request_dto_envelope_dict = warranty_request_dto_envelope_instance.to_dict()
# create an instance of WarrantyRequestDtoEnvelope from a dict
warranty_request_dto_envelope_from_dict = WarrantyRequestDtoEnvelope.from_dict(warranty_request_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


