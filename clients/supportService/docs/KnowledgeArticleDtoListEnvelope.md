# KnowledgeArticleDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[KnowledgeArticleDto]**](KnowledgeArticleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.knowledge_article_dto_list_envelope import KnowledgeArticleDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeArticleDtoListEnvelope from a JSON string
knowledge_article_dto_list_envelope_instance = KnowledgeArticleDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(KnowledgeArticleDtoListEnvelope.to_json())

# convert the object into a dict
knowledge_article_dto_list_envelope_dict = knowledge_article_dto_list_envelope_instance.to_dict()
# create an instance of KnowledgeArticleDtoListEnvelope from a dict
knowledge_article_dto_list_envelope_from_dict = KnowledgeArticleDtoListEnvelope.from_dict(knowledge_article_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


