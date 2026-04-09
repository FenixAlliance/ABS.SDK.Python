# SuiteLicenseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**license_string** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**available_seats** | **int** |  | [optional] 
**total_seats** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.suite_license_dto import SuiteLicenseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SuiteLicenseDto from a JSON string
suite_license_dto_instance = SuiteLicenseDto.from_json(json)
# print the JSON string representation of the object
print(SuiteLicenseDto.to_json())

# convert the object into a dict
suite_license_dto_dict = suite_license_dto_instance.to_dict()
# create an instance of SuiteLicenseDto from a dict
suite_license_dto_from_dict = SuiteLicenseDto.from_dict(suite_license_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


