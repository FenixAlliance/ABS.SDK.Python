# SocialPostAttachmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**file_name** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**key_words** | **str** |  | [optional] 
**valid_response** | **bool** |  | [optional] 
**parent_file_upload_id** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**social_post_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_attachment_create_dto import SocialPostAttachmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostAttachmentCreateDto from a JSON string
social_post_attachment_create_dto_instance = SocialPostAttachmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostAttachmentCreateDto.to_json())

# convert the object into a dict
social_post_attachment_create_dto_dict = social_post_attachment_create_dto_instance.to_dict()
# create an instance of SocialPostAttachmentCreateDto from a dict
social_post_attachment_create_dto_from_dict = SocialPostAttachmentCreateDto.from_dict(social_post_attachment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


