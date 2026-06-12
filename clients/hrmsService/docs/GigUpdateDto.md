# GigUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expected_delivery_date** | **datetime** |  | [optional] 
**employer_profile_id** | **str** |  | [optional] 
**min_budget** | **float** |  | [optional] 
**max_budget** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**data2_label** | **str** |  | [optional] 
**data3** | **str** |  | [optional] 
**data3_label** | **str** |  | [optional] 
**data4** | **str** |  | [optional] 
**data4_label** | **str** |  | [optional] 
**data5** | **str** |  | [optional] 
**data5_label** | **str** |  | [optional] 
**data6** | **str** |  | [optional] 
**data6_label** | **str** |  | [optional] 
**data7** | **str** |  | [optional] 
**data7_label** | **str** |  | [optional] 
**data8** | **str** |  | [optional] 
**data8_label** | **str** |  | [optional] 
**data9** | **str** |  | [optional] 
**data9_label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gig_update_dto import GigUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of GigUpdateDto from a JSON string
gig_update_dto_instance = GigUpdateDto.from_json(json)
# print the JSON string representation of the object
print(GigUpdateDto.to_json())

# convert the object into a dict
gig_update_dto_dict = gig_update_dto_instance.to_dict()
# create an instance of GigUpdateDto from a dict
gig_update_dto_from_dict = GigUpdateDto.from_dict(gig_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


