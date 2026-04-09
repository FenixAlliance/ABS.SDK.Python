# ShareTransferDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShareTransferDto**](ShareTransferDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_dto_envelope import ShareTransferDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferDtoEnvelope from a JSON string
share_transfer_dto_envelope_instance = ShareTransferDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShareTransferDtoEnvelope.to_json())

# convert the object into a dict
share_transfer_dto_envelope_dict = share_transfer_dto_envelope_instance.to_dict()
# create an instance of ShareTransferDtoEnvelope from a dict
share_transfer_dto_envelope_from_dict = ShareTransferDtoEnvelope.from_dict(share_transfer_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


