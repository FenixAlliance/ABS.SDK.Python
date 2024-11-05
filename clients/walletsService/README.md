# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.1.4089
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://fenixalliance.com.co/Support](https://fenixalliance.com.co/Support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    location_create_dto = openapi_client.LocationCreateDto() # LocationCreateDto |  (optional)

    try:
        # Create Wallet Location
        api_response = api_instance.create_wallet_location_async(wallet_id, api_version=api_version, x_api_version=x_api_version, location_create_dto=location_create_dto)
        print("The response of WalletsApi->create_wallet_location_async:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletsApi->create_wallet_location_async: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WalletsApi* | [**create_wallet_location_async**](docs/WalletsApi.md#create_wallet_location_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Locations | Create Wallet Location
*WalletsApi* | [**delete_wallet_location_async**](docs/WalletsApi.md#delete_wallet_location_async) | **DELETE** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Delete Wallet Location
*WalletsApi* | [**get_incoming_payments_async**](docs/WalletsApi.md#get_incoming_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming | Get Incoming Payments
*WalletsApi* | [**get_incoming_payments_count_async**](docs/WalletsApi.md#get_incoming_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming/Count | Get Incoming Payments Count
*WalletsApi* | [**get_incoming_wallet_invoices_async**](docs/WalletsApi.md#get_incoming_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming | Get Incoming Wallet Invoices
*WalletsApi* | [**get_incoming_wallet_invoices_count_async**](docs/WalletsApi.md#get_incoming_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming/Count | Get Incoming Wallet Invoices Count
*WalletsApi* | [**get_outgoing_payments_async**](docs/WalletsApi.md#get_outgoing_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing | Get Outgoing Payments
*WalletsApi* | [**get_outgoing_payments_count_async**](docs/WalletsApi.md#get_outgoing_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing/Count | Get Outgoing Payments Count
*WalletsApi* | [**get_outgoing_wallet_invoices_async**](docs/WalletsApi.md#get_outgoing_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing | Get Outgoing Wallet Invoices
*WalletsApi* | [**get_outgoing_wallet_invoices_count_async**](docs/WalletsApi.md#get_outgoing_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing/Count | Get Outgoing Wallet Invoices Count
*WalletsApi* | [**get_wallet_details_async**](docs/WalletsApi.md#get_wallet_details_async) | **GET** /api/v2/WalletsService/Wallets/{walletId} | Get Wallet Details
*WalletsApi* | [**get_wallet_extended_orders_async**](docs/WalletsApi.md#get_wallet_extended_orders_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders/Extended | Get Wallet Extended Orders
*WalletsApi* | [**get_wallet_invoices_async**](docs/WalletsApi.md#get_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices | Get Wallet Invoices
*WalletsApi* | [**get_wallet_invoices_count_async**](docs/WalletsApi.md#get_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Count | Get Wallet Invoices Count
*WalletsApi* | [**get_wallet_location_async**](docs/WalletsApi.md#get_wallet_location_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Get Wallet Location
*WalletsApi* | [**get_wallet_locations_async**](docs/WalletsApi.md#get_wallet_locations_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations | Get Wallet Locations
*WalletsApi* | [**get_wallet_locations_count_async**](docs/WalletsApi.md#get_wallet_locations_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations/Count | Get Wallet Locations Count
*WalletsApi* | [**get_wallet_orders_async**](docs/WalletsApi.md#get_wallet_orders_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders | Get Wallet Orders
*WalletsApi* | [**get_wallet_orders_count_async**](docs/WalletsApi.md#get_wallet_orders_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders/Count | Get Wallet Orders Count
*WalletsApi* | [**get_wallet_payments_async**](docs/WalletsApi.md#get_wallet_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments | Get Wallet Payments
*WalletsApi* | [**get_wallet_payments_count_async**](docs/WalletsApi.md#get_wallet_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Count | Get Wallet Payments Count
*WalletsApi* | [**update_wallet_location_async**](docs/WalletsApi.md#update_wallet_location_async) | **PUT** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Update Wallet Location


## Documentation For Models

 - [ContactDto](docs/ContactDto.md)
 - [Currency](docs/Currency.md)
 - [EmptyEnvelope](docs/EmptyEnvelope.md)
 - [ErrorEnvelope](docs/ErrorEnvelope.md)
 - [ExtendedOrderDto](docs/ExtendedOrderDto.md)
 - [ExtendedOrderDtoListEnvelope](docs/ExtendedOrderDtoListEnvelope.md)
 - [Int32Envelope](docs/Int32Envelope.md)
 - [InvoiceDto](docs/InvoiceDto.md)
 - [InvoiceDtoListEnvelope](docs/InvoiceDtoListEnvelope.md)
 - [LocationCreateDto](docs/LocationCreateDto.md)
 - [LocationDto](docs/LocationDto.md)
 - [LocationDtoEnvelope](docs/LocationDtoEnvelope.md)
 - [LocationDtoListEnvelope](docs/LocationDtoListEnvelope.md)
 - [LocationUpdateDto](docs/LocationUpdateDto.md)
 - [Money](docs/Money.md)
 - [OrderDto](docs/OrderDto.md)
 - [OrderDtoListEnvelope](docs/OrderDtoListEnvelope.md)
 - [PaymentDto](docs/PaymentDto.md)
 - [PaymentDtoListEnvelope](docs/PaymentDtoListEnvelope.md)
 - [TenantDto](docs/TenantDto.md)
 - [TenantEnrolmentDto](docs/TenantEnrolmentDto.md)
 - [UserDto](docs/UserDto.md)
 - [WalletDto](docs/WalletDto.md)
 - [WalletDtoEnvelope](docs/WalletDtoEnvelope.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@fenix-alliance.com

