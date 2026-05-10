# KnowledgeArticleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
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

## Example

```python
from openapi_client.models.knowledge_article_create_dto import KnowledgeArticleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeArticleCreateDto from a JSON string
knowledge_article_create_dto_instance = KnowledgeArticleCreateDto.from_json(json)
# print the JSON string representation of the object
print(KnowledgeArticleCreateDto.to_json())

# convert the object into a dict
knowledge_article_create_dto_dict = knowledge_article_create_dto_instance.to_dict()
# create an instance of KnowledgeArticleCreateDto from a dict
knowledge_article_create_dto_from_dict = KnowledgeArticleCreateDto.from_dict(knowledge_article_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


