# AssetTransferUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_list** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**destination_location_id** | **str** |  | [optional] 
**destination_contact_id** | **str** |  | [optional] 
**destination_department_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_transfer_update_dto import AssetTransferUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTransferUpdateDto from a JSON string
asset_transfer_update_dto_instance = AssetTransferUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetTransferUpdateDto.to_json())

# convert the object into a dict
asset_transfer_update_dto_dict = asset_transfer_update_dto_instance.to_dict()
# create an instance of AssetTransferUpdateDto from a dict
asset_transfer_update_dto_from_dict = AssetTransferUpdateDto.from_dict(asset_transfer_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


