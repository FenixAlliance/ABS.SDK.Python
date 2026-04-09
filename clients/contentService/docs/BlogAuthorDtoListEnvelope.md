# BlogAuthorDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BlogAuthorDto]**](BlogAuthorDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.blog_author_dto_list_envelope import BlogAuthorDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BlogAuthorDtoListEnvelope from a JSON string
blog_author_dto_list_envelope_instance = BlogAuthorDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BlogAuthorDtoListEnvelope.to_json())

# convert the object into a dict
blog_author_dto_list_envelope_dict = blog_author_dto_list_envelope_instance.to_dict()
# create an instance of BlogAuthorDtoListEnvelope from a dict
blog_author_dto_list_envelope_from_dict = BlogAuthorDtoListEnvelope.from_dict(blog_author_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


