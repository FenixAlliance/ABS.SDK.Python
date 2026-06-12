# KnowledgeArticleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**excerpt** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**highlight_image** | **str** |  | [optional] 
**seo_title** | **str** |  | [optional] 
**seo_key_words** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**last_modification** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.knowledge_article_dto import KnowledgeArticleDto

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeArticleDto from a JSON string
knowledge_article_dto_instance = KnowledgeArticleDto.from_json(json)
# print the JSON string representation of the object
print(KnowledgeArticleDto.to_json())

# convert the object into a dict
knowledge_article_dto_dict = knowledge_article_dto_instance.to_dict()
# create an instance of KnowledgeArticleDto from a dict
knowledge_article_dto_from_dict = KnowledgeArticleDto.from_dict(knowledge_article_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


