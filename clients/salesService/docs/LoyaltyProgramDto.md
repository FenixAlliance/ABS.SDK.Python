# LoyaltyProgramDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loyalty_program_dto import LoyaltyProgramDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyProgramDto from a JSON string
loyalty_program_dto_instance = LoyaltyProgramDto.from_json(json)
# print the JSON string representation of the object
print(LoyaltyProgramDto.to_json())

# convert the object into a dict
loyalty_program_dto_dict = loyalty_program_dto_instance.to_dict()
# create an instance of LoyaltyProgramDto from a dict
loyalty_program_dto_from_dict = LoyaltyProgramDto.from_dict(loyalty_program_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


