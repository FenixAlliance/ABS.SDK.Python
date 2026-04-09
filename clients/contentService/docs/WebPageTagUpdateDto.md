# WebPageTagUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**seo_title** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**cornerstone_content** | **bool** |  | [optional] 
**allow_serach_engines** | **bool** |  | [optional] 
**seo_key_phrases** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**image** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_page_tag_update_dto import WebPageTagUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageTagUpdateDto from a JSON string
web_page_tag_update_dto_instance = WebPageTagUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WebPageTagUpdateDto.to_json())

# convert the object into a dict
web_page_tag_update_dto_dict = web_page_tag_update_dto_instance.to_dict()
# create an instance of WebPageTagUpdateDto from a dict
web_page_tag_update_dto_from_dict = WebPageTagUpdateDto.from_dict(web_page_tag_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


