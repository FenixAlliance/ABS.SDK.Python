# SupplierProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**submitted** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**contact** | [**ContactDto**](ContactDto.md) |  | [optional] 
**qualified_name** | **str** |  | [optional] [readonly] 
**verification_timestamp** | **datetime** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**data2_label** | **str** |  | [optional] 
**data3** | **str** |  | [optional] 
**data3_label** | **str** |  | [optional] 
**data4** | **str** |  | [optional] 
**data4_label** | **str** |  | [optional] 
**data5** | **str** |  | [optional] 
**data5_label** | **str** |  | [optional] 
**data6** | **str** |  | [optional] 
**data6_label** | **str** |  | [optional] 
**data7** | **str** |  | [optional] 
**data7_label** | **str** |  | [optional] 
**data8** | **str** |  | [optional] 
**data8_label** | **str** |  | [optional] 
**data9** | **str** |  | [optional] 
**data9_label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.supplier_profile_dto import SupplierProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierProfileDto from a JSON string
supplier_profile_dto_instance = SupplierProfileDto.from_json(json)
# print the JSON string representation of the object
print(SupplierProfileDto.to_json())

# convert the object into a dict
supplier_profile_dto_dict = supplier_profile_dto_instance.to_dict()
# create an instance of SupplierProfileDto from a dict
supplier_profile_dto_from_dict = SupplierProfileDto.from_dict(supplier_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


