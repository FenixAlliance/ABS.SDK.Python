# AssetCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**asset_class** | **str** |  | [optional] 
**asset_owner** | **str** |  | [optional] 
**is_existing_asset** | **bool** |  | [optional] 
**calculate_depreciation** | **bool** |  | [optional] 
**allow_monthly_depreciation** | **bool** |  | [optional] 
**opening_depreciation** | **float** |  | [optional] 
**purchase_date** | **datetime** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**asset_category_id** | **str** |  | [optional] 
**purchase_invoice_id** | **str** |  | [optional] 
**purchase_receipt_id** | **str** |  | [optional] 
**asset_location_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**organization_department_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_create_dto import AssetCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCreateDto from a JSON string
asset_create_dto_instance = AssetCreateDto.from_json(json)
# print the JSON string representation of the object
print(AssetCreateDto.to_json())

# convert the object into a dict
asset_create_dto_dict = asset_create_dto_instance.to_dict()
# create an instance of AssetCreateDto from a dict
asset_create_dto_from_dict = AssetCreateDto.from_dict(asset_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


