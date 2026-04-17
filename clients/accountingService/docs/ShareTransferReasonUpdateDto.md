# ShareTransferReasonUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_reason_update_dto import ShareTransferReasonUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferReasonUpdateDto from a JSON string
share_transfer_reason_update_dto_instance = ShareTransferReasonUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShareTransferReasonUpdateDto.to_json())

# convert the object into a dict
share_transfer_reason_update_dto_dict = share_transfer_reason_update_dto_instance.to_dict()
# create an instance of ShareTransferReasonUpdateDto from a dict
share_transfer_reason_update_dto_from_dict = ShareTransferReasonUpdateDto.from_dict(share_transfer_reason_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


