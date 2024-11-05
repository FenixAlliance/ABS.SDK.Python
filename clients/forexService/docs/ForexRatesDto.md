# ForexRatesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**var_date** | **str** |  | [optional] 
**base** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**request_timestamp** | **datetime** |  | [optional] 
**rates** | **Dict[str, float]** |  | [optional] 

## Example

```python
from openapi_client.models.forex_rates_dto import ForexRatesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForexRatesDto from a JSON string
forex_rates_dto_instance = ForexRatesDto.from_json(json)
# print the JSON string representation of the object
print(ForexRatesDto.to_json())

# convert the object into a dict
forex_rates_dto_dict = forex_rates_dto_instance.to_dict()
# create an instance of ForexRatesDto from a dict
forex_rates_dto_from_dict = ForexRatesDto.from_dict(forex_rates_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


