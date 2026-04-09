# ShareTransferDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShareTransferDto]**](ShareTransferDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_dto_list_envelope import ShareTransferDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferDtoListEnvelope from a JSON string
share_transfer_dto_list_envelope_instance = ShareTransferDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShareTransferDtoListEnvelope.to_json())

# convert the object into a dict
share_transfer_dto_list_envelope_dict = share_transfer_dto_list_envelope_instance.to_dict()
# create an instance of ShareTransferDtoListEnvelope from a dict
share_transfer_dto_list_envelope_from_dict = ShareTransferDtoListEnvelope.from_dict(share_transfer_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


