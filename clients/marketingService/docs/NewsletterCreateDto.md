# NewsletterCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.newsletter_create_dto import NewsletterCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewsletterCreateDto from a JSON string
newsletter_create_dto_instance = NewsletterCreateDto.from_json(json)
# print the JSON string representation of the object
print(NewsletterCreateDto.to_json())

# convert the object into a dict
newsletter_create_dto_dict = newsletter_create_dto_instance.to_dict()
# create an instance of NewsletterCreateDto from a dict
newsletter_create_dto_from_dict = NewsletterCreateDto.from_dict(newsletter_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


