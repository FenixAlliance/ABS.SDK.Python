# EmailGroupCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_group_create_dto import EmailGroupCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGroupCreateDto from a JSON string
email_group_create_dto_instance = EmailGroupCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmailGroupCreateDto.to_json())

# convert the object into a dict
email_group_create_dto_dict = email_group_create_dto_instance.to_dict()
# create an instance of EmailGroupCreateDto from a dict
email_group_create_dto_from_dict = EmailGroupCreateDto.from_dict(email_group_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


