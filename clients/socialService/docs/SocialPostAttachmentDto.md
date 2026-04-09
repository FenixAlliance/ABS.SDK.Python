# SocialPostAttachmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**hash** | **str** |  | [optional] 
**file_url** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**key_words** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**parent_file_id** | **str** |  | [optional] 
**valid_response** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**folder_path** | **str** |  | [optional] 
**social_post_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_attachment_dto import SocialPostAttachmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostAttachmentDto from a JSON string
social_post_attachment_dto_instance = SocialPostAttachmentDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostAttachmentDto.to_json())

# convert the object into a dict
social_post_attachment_dto_dict = social_post_attachment_dto_instance.to_dict()
# create an instance of SocialPostAttachmentDto from a dict
social_post_attachment_dto_from_dict = SocialPostAttachmentDto.from_dict(social_post_attachment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


