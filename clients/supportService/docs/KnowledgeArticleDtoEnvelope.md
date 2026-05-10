# KnowledgeArticleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**KnowledgeArticleDto**](KnowledgeArticleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.knowledge_article_dto_envelope import KnowledgeArticleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeArticleDtoEnvelope from a JSON string
knowledge_article_dto_envelope_instance = KnowledgeArticleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(KnowledgeArticleDtoEnvelope.to_json())

# convert the object into a dict
knowledge_article_dto_envelope_dict = knowledge_article_dto_envelope_instance.to_dict()
# create an instance of KnowledgeArticleDtoEnvelope from a dict
knowledge_article_dto_envelope_from_dict = KnowledgeArticleDtoEnvelope.from_dict(knowledge_article_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


