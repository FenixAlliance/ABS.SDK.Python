# ShareTransferReasonCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_reason_create_dto import ShareTransferReasonCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferReasonCreateDto from a JSON string
share_transfer_reason_create_dto_instance = ShareTransferReasonCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShareTransferReasonCreateDto.to_json())

# convert the object into a dict
share_transfer_reason_create_dto_dict = share_transfer_reason_create_dto_instance.to_dict()
# create an instance of ShareTransferReasonCreateDto from a dict
share_transfer_reason_create_dto_from_dict = ShareTransferReasonCreateDto.from_dict(share_transfer_reason_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


