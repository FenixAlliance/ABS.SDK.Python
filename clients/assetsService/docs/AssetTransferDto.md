# AssetTransferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**is_root_transfer** | **bool** |  | [optional] 
**serial_list** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**previous_asset_transfer_id** | **str** |  | [optional] 
**source_location_id** | **str** |  | [optional] 
**source_location_name** | **str** |  | [optional] 
**destination_location_id** | **str** |  | [optional] 
**destination_location_name** | **str** |  | [optional] 
**source_contact_id** | **str** |  | [optional] 
**source_contact_name** | **str** |  | [optional] 
**destination_contact_id** | **str** |  | [optional] 
**destination_contact_name** | **str** |  | [optional] 
**source_department_id** | **str** |  | [optional] 
**source_department_name** | **str** |  | [optional] 
**destination_department_id** | **str** |  | [optional] 
**destination_department_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_transfer_dto import AssetTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTransferDto from a JSON string
asset_transfer_dto_instance = AssetTransferDto.from_json(json)
# print the JSON string representation of the object
print(AssetTransferDto.to_json())

# convert the object into a dict
asset_transfer_dto_dict = asset_transfer_dto_instance.to_dict()
# create an instance of AssetTransferDto from a dict
asset_transfer_dto_from_dict = AssetTransferDto.from_dict(asset_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


