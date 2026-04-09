# ItemQuestionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**needs_revision** | **bool** |  | 
**question** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_question_update_dto import ItemQuestionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemQuestionUpdateDto from a JSON string
item_question_update_dto_instance = ItemQuestionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemQuestionUpdateDto.to_json())

# convert the object into a dict
item_question_update_dto_dict = item_question_update_dto_instance.to_dict()
# create an instance of ItemQuestionUpdateDto from a dict
item_question_update_dto_from_dict = ItemQuestionUpdateDto.from_dict(item_question_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


