# RoundingPolicyUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_free** | **bool** |  | [optional] 
**reduce** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**allow_international** | **bool** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**weeks** | **int** |  | [optional] 
**months** | **int** |  | [optional] 
**years** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.rounding_policy_update_dto import RoundingPolicyUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingPolicyUpdateDto from a JSON string
rounding_policy_update_dto_instance = RoundingPolicyUpdateDto.from_json(json)
# print the JSON string representation of the object
print(RoundingPolicyUpdateDto.to_json())

# convert the object into a dict
rounding_policy_update_dto_dict = rounding_policy_update_dto_instance.to_dict()
# create an instance of RoundingPolicyUpdateDto from a dict
rounding_policy_update_dto_from_dict = RoundingPolicyUpdateDto.from_dict(rounding_policy_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


