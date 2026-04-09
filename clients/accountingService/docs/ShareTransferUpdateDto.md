# ShareTransferUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**new_share_holder_id** | **str** |  | [optional] 
**former_share_holder_id** | **str** |  | [optional] 
**share_transfer_reason_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_update_dto import ShareTransferUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferUpdateDto from a JSON string
share_transfer_update_dto_instance = ShareTransferUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShareTransferUpdateDto.to_json())

# convert the object into a dict
share_transfer_update_dto_dict = share_transfer_update_dto_instance.to_dict()
# create an instance of ShareTransferUpdateDto from a dict
share_transfer_update_dto_from_dict = ShareTransferUpdateDto.from_dict(share_transfer_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


