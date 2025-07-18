# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T11:58:26+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query

from models import (
    ApiCheckoutPubOrderFormsSimulationPostRequest,
    ApiCheckoutPubOrderFormsSimulationPostResponse,
    Approveorder,
    Deliverybyfranchiseseller,
    Deliverybyseller,
    EnqueueNewOrderRequest,
    FieldFulfillmentEndpointPvtOrderFormsSimulationPostRequest,
    FieldFulfillmentEndpointPvtOrderFormsSimulationPostResponse,
    FieldFulfillmentEndpointPvtOrdersOrderIdCancelPostRequest,
    FieldFulfillmentEndpointPvtOrdersSellerOrderIdFulfillPostRequest,
    FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdCancelPostRequest,
    FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoiceInvoiceNumberPostRequest,
    FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoiceInvoiceNumberTrackingPostRequest,
    FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoicePostRequest,
    OrderPlacement,
    SendCategoryMappingToVtexMapper,
    UpdateOrderStatusRequest,
    VtexMapperRegistration,
)
from models.field_accountName_.field_environment_.com import (
    BrApiFulfillmentPvtOrdersOrderIdFulfillPostRequest,
    BrApiFulfillmentPvtOrdersPostRequest,
)

app = MCPProxy(
    contact={},
    description='\r\nThe _Marketplace Protocol_ is a set of API requests and definitions to help you integrate external sellers into a VTEX marketplace as well as external marketplaces into VTEX sellers.\r\n\r\n## External Seller\r\n\r\nHere you will find the endpoints involved in the integration between a VTEX marketplace and an external seller. Note that some of these requests are typically sent by the seller while others are received.\r\n\r\n| **Request** | **From** | **To** |\r\n|-|-|-|\r\n| [Fulfillment simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) | Marketplace | Seller |\r\n| [Order placement](https://developers.vtex.com/vtex-rest-api/reference/order-placement) | Marketplace | Seller |\r\n| [Authorize fulfillment](https://developers.vtex.com/vtex-rest-api/reference/authorize-fulfillment) | Marketplace | Seller |\r\n| [Marketplace order cancellation](https://developers.vtex.com/vtex-rest-api/reference/marketplace-order-cancellation) | Marketplace | Seller |\r\n| [Send invoice](https://developers.vtex.com/vtex-rest-api/reference/send-invoice) | Seller | Marketplace |\r\n| [Send tracking information](https://developers.vtex.com/vtex-rest-api/reference/send-tracking-information) | Seller      | Marketplace |\r\n| [Update tracking status](https://developers.vtex.com/vtex-rest-api/reference/update-tracking-status) | Seller | Marketplace |\r\n| [Cancel order in marketplace](https://developers.vtex.com/vtex-rest-api/reference/cancel-order-in-marketplace) | Seller | Marketplace |\r\n\r\nFor a detailed explanation of the steps required to develop a custom connector to sell products from an external seller in your storefront, check out our complete [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide).\r\n\r\n\r\n## External Marketplace\r\n\r\nIn this section, you will find the endpoints involved in the VTEX integration between an external marketplace and a VTEX seller.\r\n\r\n\r\n| **Request** | **From** | **To** |\r\n|-|-|-|\r\n| [VTEX Mapper Registration](https://developers.vtex.com/vtex-rest-api/reference/vtex-mapper-registration) | External marketplace | VTEX system |\r\n| [Send Category Mapping to VTEX Mapper](https://developers.vtex.com/vtex-rest-api/reference/send-category-mapping-to-vtex-mapper) |  External marketplace | VTEX system |\r\n| [Authorize fulfillment](https://developers.vtex.com/vtex-rest-api/reference/authorize-fulfillment) | Marketplace | Seller |\r\n| [Place fulfillment order](https://developers.vtex.com/vtex-rest-api/reference/place-fulfillment-order)   | External marketplace | VTEX Seller |\r\n| [Authorize dispatch for fulfillment order](https://developers.vtex.com/vtex-rest-api/reference/authorize-dispatch-for-fulfillment-order) | External marketplace | VTEX Seller |\r\n\r\n\r\nFor a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide).',
    title='Marketplace Protocol',
    version='1.0',
    servers=[{'url': 'https://vtex.local'}, {'description': '', 'url': '/'}],
)


@app.post(
    '/api/checkout/pub/orderForms/simulation',
    description=""" This endpoint can be triggered by marketplaces to simulate the fulfillment of an item in the cart.

The fulfillment information is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data. """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def fulfillment_simulation_external_marketplace(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    affiliate_id: Optional[str] = Query('MNF', alias='affiliateId'),
    sc: Optional[int] = None,
    body: ApiCheckoutPubOrderFormsSimulationPostRequest = None,
):
    """
    Fulfillment simulation - External Marketplace
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/portal.vtexcommercestable.com.br/api/mkp-category-mapper/categories/marketplace/{id}',
    description=""" Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree. 

To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace. 

This endpoint allows connectors to send the marketplace's category tree mapped in the integration. 

Connectors should send the payload compacted in .gzip format. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['category_mapping', 'vtex_interaction_operations'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def send_category_mapping_vtex_mapper(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    id: str = '123456789',
    body: SendCategoryMappingToVtexMapper = ...,
):
    """
    Send Category Mapping to VTEX Mapper
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/portal.vtexcommercestable.com.br/api/mkp-category-mapper/connector/register',
    description=""" Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree. 

To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace. 

This endpoint allows connectors to register the external marketplace integration in VTEX Mapper. 

In case VTEX Mapper detects an error and the call fails, the connector should check if mandatory information was sent correctly. Ex. are URLs correctly registered in the properties categoryTreeEndPoint and mappingEndPoint? 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['category_mapping', 'vtex_interaction_operations'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def vtex_mapper_registration(
    an: str,
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    body: VtexMapperRegistration = ...,
):
    """
    VTEX Mapper Registration
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{accountName}.vtexcommercestable.com.br/api/order-integration/orders',
    description=""" API to integrate an external channel's order into the VTEX plataform.

This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectorEndpoint** field in [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. If the account is not informed in the URL host, it should also be defined as a query string parameter in the route: `an={account}`. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def enqueue_new_order(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    an: Optional[str] = None,
    account_name: str = Path(..., alias='accountName'),
    affiliate_id: str = Query(..., alias='affiliateId'),
    body: EnqueueNewOrderRequest = ...,
):
    """
    New Order Integration
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/{accountName}.vtexcommercestable.com.br/api/order-integration/orders/status',
    description=""" API request used to update an order status in VTEX.

This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectiorEndpoint** field or the **connectiorEndpoint** [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def update_order_status(
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    an: Optional[str] = None,
    account_name: str = Path(..., alias='accountName'),
    body: UpdateOrderStatusRequest = ...,
):
    """
    Update Order Status
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{accountName}.{environment}.com.br/api/fulfillment/pvt/orders',
    description=""" Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.


> If you plan to integrate external orders with possible [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#) be mindful of the `isCreatedAsync` request body field. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def place_fulfillment_order(
    account_name: str = Path(..., alias='accountName'),
    environment: str = 'vtexcommercestable',
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    sc: Optional[str] = None,
    affiliate_id: str = Query(..., alias='affiliateId'),
    body: BrApiFulfillmentPvtOrdersPostRequest = None,
):
    """
    Place fulfillment order
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{accountName}.{environment}.com.br/api/fulfillment/pvt/orders/{orderId}/fulfill',
    description=""" Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side. 

For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide). """,
    tags=['fulfillment_process_management', 'order_handling'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def authorize_dispatch_for_fulfillment_order(
    account_name: str = Path(..., alias='accountName'),
    environment: str = 'vtexcommercestable',
    order_id: str = Path(..., alias='orderId'),
    content__type: str = Header(..., alias='Content-Type'),
    accept: str = Header(..., alias='Accept'),
    sc: Optional[str] = None,
    affiliate_id: str = Query(..., alias='affiliateId'),
    body: BrApiFulfillmentPvtOrdersOrderIdFulfillPostRequest = None,
):
    """
    Authorize dispatch for fulfillment order
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{fulfillmentEndpoint}/pvt/orderForms/simulation',
    description=""" This endpoint may be called upon by VTEX for fulfillment simulation in the external seller different contexts. See examples below.

When a [price](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) or [inventory](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory) notification request returns a response with status `200 OK`, it means that the SKU already exists in the marketplace. Whenever this happens, the marketplace will call the seller to get two updated information about the SKU: Price and Inventory.

The seller needs to have an endpoint implemented in order to receive this call and send a response containing the requested information to the marketplace. We call it the Fulfillment Simulation endpoint.

If the seller wishes to include other parameters in this call (like account name, or [sales channel](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) ID), this should be done within their {fulfillmentEndpoint}. This path is then inserted in the marketplace's VTEX admin when [configuring a seller](https://help.vtex.com/en/tutorial/configurando-seller--tutorials_392). 

The marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference. 

This call is also applied in the Storefront simulation scenario, in which case the request from VTEX does not send the paramenters `country` and `postalCode`. 
The call's payload can be adapted into two scenarios: 

- **Displaying items in the storefront**: the address information can be nulled in the request, since they are not mandatory data for this context.   
- **Making a shopping cart simulation during checkout**: address information must be sent, since this data is needed to calculate freight values. If the address information (including `postalCode` and `country`) is not sent through the call, VTEX interprets the stock balance as zero. Without a valid stock balance, the seller will not be shown as an option during checkout. 
  
## Request body example - Indexing simulation

```
{
    "items": [
      {
        "id": "7908010136043",
        "quantity": 1,
        "seller": "1",
      }
    ],
    "isCheckedIn": false,
  }
``` 
## Request body example - Checkout simulation

```
{
    "items": [
      {
        "id": "7908010136043",
        "quantity": 1,
        "seller": "1",
      }
    ],
    "postalCode": "22270-030",
    "country": "BRA",
  }
``` """,
    tags=['fulfillment_process_management', 'order_handling'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def fulfillment_simulation(
    fulfillment_endpoint: str = Path(..., alias='fulfillmentEndpoint'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    body: FieldFulfillmentEndpointPvtOrderFormsSimulationPostRequest = ...,
):
    """
    Fulfillment simulation - External Seller
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{fulfillmentEndpoint}/pvt/orders',
    description=""" This request is sent by VTEX to the external seller once the customer finishes their checkout, to let the seller know there is a newly placed order. It does that by calling the **Order Placement** endpoint, which needs to be implemented by the seller.

The marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With all that, the seller will be able to create the order in their own store. """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def order_placement(
    fulfillment_endpoint: str = Path(..., alias='fulfillmentEndpoint'),
    content_length: str = Header(..., alias='content-length'),
    authorization: str = ...,
    x_vtex_api_appkey: str = Header(..., alias='x-vtex-api-appkey'),
    x_vtex_api_apptoken: str = Header(..., alias='x-vtex-api-apptoken'),
    accept: str = ...,
    accept_enconding: str = Header(..., alias='accept-enconding'),
    x_vtex_operation_id: str = Header(..., alias='x-vtex-operation-id'),
    x_forwarded_proto: str = Header(..., alias='x-forwarded-proto'),
    x_forwarded_for: str = Header(..., alias='x-forwarded-for'),
    x_vtex_cache_client_bypass: str = Header(..., alias='x-vtex-cache-client-bypass'),
    content_type: str = Header(..., alias='content-type'),
    traceparent: str = ...,
    body: OrderPlacement = ...,
):
    """
    Order placement
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{fulfillmentEndpoint}/pvt/orders/{orderId}/cancel',
    description=""" This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed. 

For the seller to: 

- **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not. 

- **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`). 

- **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/vtex-rest-api/reference/external-seller#send-invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#order-invoicing) step, and the ones that follow it. 

This call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*. """,
    tags=['order_handling', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def mkp_order_cancellation(
    fulfillment_endpoint: str = Path(..., alias='fulfillmentEndpoint'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    order_id: str = Path(..., alias='orderId'),
    body: FieldFulfillmentEndpointPvtOrdersOrderIdCancelPostRequest = ...,
):
    """
    Marketplace order cancellation
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{fulfillmentEndpoint}/pvt/orders/{sellerOrderId}/fulfill',
    description=""" This request is sent from VTEX to the seller after the payment is approved, to notify them that the fulfillment process can start. """,
    tags=['fulfillment_process_management', 'order_handling'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def authorize_fulfillment(
    fulfillment_endpoint: str = Path(..., alias='fulfillmentEndpoint'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    seller_order_id: str = Path(..., alias='sellerOrderId'),
    body: FieldFulfillmentEndpointPvtOrdersSellerOrderIdFulfillPostRequest = ...,
):
    """
    Authorize fulfillment
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{marketplaceServicesEndpoint}/pvt/orders/{marketplaceOrderId}/cancel',
    description=""" This request is sent by the external seller to the VTEX marketplace to cancel an order. """,
    tags=['order_handling'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def cancel_order_in_marketplace(
    marketplace_services_endpoint: str = Path(..., alias='marketplaceServicesEndpoint'),
    marketplace_order_id: str = Path(..., alias='marketplaceOrderId'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    body: FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdCancelPostRequest = ...,
):
    """
    Cancel order in marketplace
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{marketplaceServicesEndpoint}/pvt/orders/{marketplaceOrderId}/invoice',
    description=""" This request is sent by the external seller to the VTEX marketplace to send invoice information.

This can be necessary in a regular order or in the case of a return. The `type` field is used to indicate which of these is the case. """,
    tags=['invoice_and_tracking', 'order_handling'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def send_invoice(
    marketplace_services_endpoint: str = Path(..., alias='marketplaceServicesEndpoint'),
    marketplace_order_id: str = Path(..., alias='marketplaceOrderId'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    body: FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoicePostRequest = ...,
):
    """
    Send invoice
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{marketplaceServicesEndpoint}/pvt/orders/{marketplaceOrderId}/invoice/{invoiceNumber}',
    description=""" This request is sent by the external seller to the VTEX marketplace to add tracking information to a given order's invoice, in case it is necessary to do so after the invoice has been sent. """,
    tags=['invoice_and_tracking', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def send_tracking_information(
    marketplace_services_endpoint: str = Path(..., alias='marketplaceServicesEndpoint'),
    marketplace_order_id: str = Path(..., alias='marketplaceOrderId'),
    invoice_number: str = Path(..., alias='invoiceNumber'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    body: FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoiceInvoiceNumberPostRequest = ...,
):
    """
    Send tracking information
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/{marketplaceServicesEndpoint}/pvt/orders/{marketplaceOrderId}/invoice/{invoiceNumber}/tracking',
    description=""" This request is sent by the external seller to the VTEX marketplace to update a given order's tracking status. """,
    tags=['invoice_and_tracking', 'fulfillment_process_management'],
    security=[
        APIKeyHeader(name="X-VTEX-API-AppKey"),
        APIKeyHeader(name="X-VTEX-API-AppToken"),
    ],
)
def update_tracking_status(
    marketplace_services_endpoint: str = Path(..., alias='marketplaceServicesEndpoint'),
    marketplace_order_id: str = Path(..., alias='marketplaceOrderId'),
    invoice_number: str = Path(..., alias='invoiceNumber'),
    accept: str = Header(..., alias='Accept'),
    content__type: str = Header(..., alias='Content-Type'),
    body: FieldMarketplaceServicesEndpointPvtOrdersMarketplaceOrderIdInvoiceInvoiceNumberTrackingPostRequest = ...,
):
    """
    Update tracking status
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
