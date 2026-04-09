# ShareTransferCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**new_share_holder_id** | **str** |  | [optional] 
**former_share_holder_id** | **str** |  | [optional] 
**share_transfer_reason_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_transfer_create_dto import ShareTransferCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareTransferCreateDto from a JSON string
share_transfer_create_dto_instance = ShareTransferCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShareTransferCreateDto.to_json())

# convert the object into a dict
share_transfer_create_dto_dict = share_transfer_create_dto_instance.to_dict()
# create an instance of ShareTransferCreateDto from a dict
share_transfer_create_dto_from_dict = ShareTransferCreateDto.from_dict(share_transfer_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


