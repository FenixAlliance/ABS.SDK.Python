# EmailSignatureDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**order** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**excerpt** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**highlight_image** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**seo_title** | **str** |  | [optional] 
**seo_key_words** | **str** |  | [optional] 
**seo_key_phrases** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**twitter_image** | **str** |  | [optional] 
**twitter_title** | **str** |  | [optional] 
**twitter_description** | **str** |  | [optional] 
**facebook_image** | **str** |  | [optional] 
**facebook_title** | **str** |  | [optional] 
**facebook_description** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**generated_code** | **str** |  | [optional] 
**compilation_path** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**c_sharp_content** | **str** |  | [optional] 
**razor_content** | **str** |  | [optional] 
**css_content** | **str** |  | [optional] 
**js_content** | **str** |  | [optional] 
**css_files** | **str** |  | [optional] 
**js_files** | **str** |  | [optional] 
**razor_generated_code** | **str** |  | [optional] 
**c_sharp_generated_code** | **str** |  | [optional] 
**template** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**enable_comments** | **bool** |  | [optional] 
**display_social_box** | **bool** |  | [optional] 
**published** | **bool** |  | [optional] 
**in_trash_can** | **bool** |  | [optional] 
**system_locked** | **bool** |  | [optional] 
**allow_ping_backs** | **bool** |  | [optional] 
**allow_trackbacks** | **bool** |  | [optional] 
**cornerstone_content** | **bool** |  | [optional] 
**is_essential_content** | **bool** |  | [optional] 
**allow_search_engine_indexing** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**web_portal_id** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**parent_web_content_id** | **str** |  | [optional] 
**parent_web_content_version_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_signature_dto import EmailSignatureDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSignatureDto from a JSON string
email_signature_dto_instance = EmailSignatureDto.from_json(json)
# print the JSON string representation of the object
print(EmailSignatureDto.to_json())

# convert the object into a dict
email_signature_dto_dict = email_signature_dto_instance.to_dict()
# create an instance of EmailSignatureDto from a dict
email_signature_dto_from_dict = EmailSignatureDto.from_dict(email_signature_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


