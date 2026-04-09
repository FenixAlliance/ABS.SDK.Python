# ShareClassDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**forex_rates** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_class_dto import ShareClassDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassDto from a JSON string
share_class_dto_instance = ShareClassDto.from_json(json)
# print the JSON string representation of the object
print(ShareClassDto.to_json())

# convert the object into a dict
share_class_dto_dict = share_class_dto_instance.to_dict()
# create an instance of ShareClassDto from a dict
share_class_dto_from_dict = ShareClassDto.from_dict(share_class_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


