# WebPageTagDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**web_portal_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_page_tag_dto import WebPageTagDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageTagDto from a JSON string
web_page_tag_dto_instance = WebPageTagDto.from_json(json)
# print the JSON string representation of the object
print(WebPageTagDto.to_json())

# convert the object into a dict
web_page_tag_dto_dict = web_page_tag_dto_instance.to_dict()
# create an instance of WebPageTagDto from a dict
web_page_tag_dto_from_dict = WebPageTagDto.from_dict(web_page_tag_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


