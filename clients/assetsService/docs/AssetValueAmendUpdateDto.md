# AssetValueAmendUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_value** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**amendment_date** | **datetime** |  | [optional] 
**approved_by** | **str** |  | [optional] 
**approval_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.asset_value_amend_update_dto import AssetValueAmendUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetValueAmendUpdateDto from a JSON string
asset_value_amend_update_dto_instance = AssetValueAmendUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetValueAmendUpdateDto.to_json())

# convert the object into a dict
asset_value_amend_update_dto_dict = asset_value_amend_update_dto_instance.to_dict()
# create an instance of AssetValueAmendUpdateDto from a dict
asset_value_amend_update_dto_from_dict = AssetValueAmendUpdateDto.from_dict(asset_value_amend_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


