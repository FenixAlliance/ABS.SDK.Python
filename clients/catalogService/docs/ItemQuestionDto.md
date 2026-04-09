# ItemQuestionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**needs_revision** | **bool** |  | [optional] 
**question** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_question_dto import ItemQuestionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemQuestionDto from a JSON string
item_question_dto_instance = ItemQuestionDto.from_json(json)
# print the JSON string representation of the object
print(ItemQuestionDto.to_json())

# convert the object into a dict
item_question_dto_dict = item_question_dto_instance.to_dict()
# create an instance of ItemQuestionDto from a dict
item_question_dto_from_dict = ItemQuestionDto.from_dict(item_question_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


