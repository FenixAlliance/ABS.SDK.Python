# AssetValueAmendDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **object** |  | [optional] 
**business_profile_record_id** | **object** |  | [optional] 
**asset_id** | **object** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**previous_value** | **float** |  | [optional] 
**new_value** | **float** |  | [optional] 
**amendment_amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**amendment_date** | **datetime** |  | [optional] 
**approved_by** | **str** |  | [optional] 
**approval_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.asset_value_amend_dto import AssetValueAmendDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetValueAmendDto from a JSON string
asset_value_amend_dto_instance = AssetValueAmendDto.from_json(json)
# print the JSON string representation of the object
print(AssetValueAmendDto.to_json())

# convert the object into a dict
asset_value_amend_dto_dict = asset_value_amend_dto_instance.to_dict()
# create an instance of AssetValueAmendDto from a dict
asset_value_amend_dto_from_dict = AssetValueAmendDto.from_dict(asset_value_amend_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


