# LoyaltyProgramCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loyalty_program_create_dto import LoyaltyProgramCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyProgramCreateDto from a JSON string
loyalty_program_create_dto_instance = LoyaltyProgramCreateDto.from_json(json)
# print the JSON string representation of the object
print(LoyaltyProgramCreateDto.to_json())

# convert the object into a dict
loyalty_program_create_dto_dict = loyalty_program_create_dto_instance.to_dict()
# create an instance of LoyaltyProgramCreateDto from a dict
loyalty_program_create_dto_from_dict = LoyaltyProgramCreateDto.from_dict(loyalty_program_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


