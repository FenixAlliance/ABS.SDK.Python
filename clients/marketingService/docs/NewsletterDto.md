# NewsletterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.newsletter_dto import NewsletterDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewsletterDto from a JSON string
newsletter_dto_instance = NewsletterDto.from_json(json)
# print the JSON string representation of the object
print(NewsletterDto.to_json())

# convert the object into a dict
newsletter_dto_dict = newsletter_dto_instance.to_dict()
# create an instance of NewsletterDto from a dict
newsletter_dto_from_dict = NewsletterDto.from_dict(newsletter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


