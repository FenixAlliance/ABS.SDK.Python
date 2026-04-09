# LogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**log_type** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.log_dto import LogDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogDto from a JSON string
log_dto_instance = LogDto.from_json(json)
# print the JSON string representation of the object
print(LogDto.to_json())

# convert the object into a dict
log_dto_dict = log_dto_instance.to_dict()
# create an instance of LogDto from a dict
log_dto_from_dict = LogDto.from_dict(log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


