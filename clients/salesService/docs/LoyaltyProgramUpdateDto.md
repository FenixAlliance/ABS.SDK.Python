# LoyaltyProgramUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loyalty_program_update_dto import LoyaltyProgramUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyProgramUpdateDto from a JSON string
loyalty_program_update_dto_instance = LoyaltyProgramUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LoyaltyProgramUpdateDto.to_json())

# convert the object into a dict
loyalty_program_update_dto_dict = loyalty_program_update_dto_instance.to_dict()
# create an instance of LoyaltyProgramUpdateDto from a dict
loyalty_program_update_dto_from_dict = LoyaltyProgramUpdateDto.from_dict(loyalty_program_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


