# ItemQuestionRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**needs_revision** | **bool** |  | 
**question** | **str** |  | 
**social_profile_id** | **str** |  | [optional] 
**business_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_question_record_create_dto import ItemQuestionRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemQuestionRecordCreateDto from a JSON string
item_question_record_create_dto_instance = ItemQuestionRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemQuestionRecordCreateDto.to_json())

# convert the object into a dict
item_question_record_create_dto_dict = item_question_record_create_dto_instance.to_dict()
# create an instance of ItemQuestionRecordCreateDto from a dict
item_question_record_create_dto_from_dict = ItemQuestionRecordCreateDto.from_dict(item_question_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


