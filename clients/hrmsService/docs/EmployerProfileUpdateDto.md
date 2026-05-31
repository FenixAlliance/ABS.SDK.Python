# EmployerProfileUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
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
from openapi_client.models.employer_profile_update_dto import EmployerProfileUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployerProfileUpdateDto from a JSON string
employer_profile_update_dto_instance = EmployerProfileUpdateDto.from_json(json)
# print the JSON string representation of the object
print(EmployerProfileUpdateDto.to_json())

# convert the object into a dict
employer_profile_update_dto_dict = employer_profile_update_dto_instance.to_dict()
# create an instance of EmployerProfileUpdateDto from a dict
employer_profile_update_dto_from_dict = EmployerProfileUpdateDto.from_dict(employer_profile_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


