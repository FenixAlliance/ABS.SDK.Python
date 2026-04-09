# AssetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
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
**currency_code** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_name** | **str** |  | [optional] 
**asset_category_id** | **str** |  | [optional] 
**asset_category_name** | **str** |  | [optional] 
**purchase_invoice_id** | **str** |  | [optional] 
**purchase_invoice_number** | **str** |  | [optional] 
**asset_location_id** | **str** |  | [optional] 
**asset_location_name** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**organization_department_id** | **str** |  | [optional] 
**organization_department_name** | **str** |  | [optional] 
**purchase_receipt_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_dto import AssetDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDto from a JSON string
asset_dto_instance = AssetDto.from_json(json)
# print the JSON string representation of the object
print(AssetDto.to_json())

# convert the object into a dict
asset_dto_dict = asset_dto_instance.to_dict()
# create an instance of AssetDto from a dict
asset_dto_from_dict = AssetDto.from_dict(asset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


