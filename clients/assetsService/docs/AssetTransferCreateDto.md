# AssetTransferCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**is_root_transfer** | **bool** |  | [optional] 
**serial_list** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**previous_asset_transfer_id** | **str** |  | [optional] 
**source_location_id** | **str** |  | [optional] 
**destination_location_id** | **str** |  | [optional] 
**source_contact_id** | **str** |  | [optional] 
**destination_contact_id** | **str** |  | [optional] 
**source_department_id** | **str** |  | [optional] 
**destination_department_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_transfer_create_dto import AssetTransferCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTransferCreateDto from a JSON string
asset_transfer_create_dto_instance = AssetTransferCreateDto.from_json(json)
# print the JSON string representation of the object
print(AssetTransferCreateDto.to_json())

# convert the object into a dict
asset_transfer_create_dto_dict = asset_transfer_create_dto_instance.to_dict()
# create an instance of AssetTransferCreateDto from a dict
asset_transfer_create_dto_from_dict = AssetTransferCreateDto.from_dict(asset_transfer_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


