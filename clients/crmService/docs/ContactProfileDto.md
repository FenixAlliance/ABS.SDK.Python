# ContactProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**submitted** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
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
from openapi_client.models.contact_profile_dto import ContactProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContactProfileDto from a JSON string
contact_profile_dto_instance = ContactProfileDto.from_json(json)
# print the JSON string representation of the object
print(ContactProfileDto.to_json())

# convert the object into a dict
contact_profile_dto_dict = contact_profile_dto_instance.to_dict()
# create an instance of ContactProfileDto from a dict
contact_profile_dto_from_dict = ContactProfileDto.from_dict(contact_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


