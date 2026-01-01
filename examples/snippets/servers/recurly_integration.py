"""Recurly integration example server.

This example demonstrates how to use the Recurly Python SDK to manage
subscriptions and customer billing information.

To run this server:
    cd examples/snippets
    uv run server recurly_integration stdio
"""

from typing import Any

from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP(name="Recurly Integration Example")


@mcp.tool()
def get_customer_info(customer_id: str) -> dict[str, Any]:
    """Fetch customer information from Recurly.

    Args:
        customer_id: The unique identifier for the customer in Recurly

    Returns:
        A dictionary containing customer information
    """
    # Note: In a real application, you would:
    # 1. Configure the Recurly client with your API key
    # 2. Use the client to fetch actual customer data
    # 3. Handle errors appropriately
    #
    # Example initialization:
    # import recurly
    # recurly.SUBDOMAIN = "your-subdomain"
    # recurly.API_KEY = "your-api-key"
    # client = recurly.Client()
    # account = client.get_account(customer_id)

    return {
        "customer_id": customer_id,
        "name": "Example Customer",
        "email": "customer@example.com",
        "status": "active",
    }


@mcp.tool()
def list_subscriptions(customer_id: str, limit: int = 10) -> dict[str, Any]:
    """List all subscriptions for a customer.

    Args:
        customer_id: The unique identifier for the customer
        limit: Maximum number of subscriptions to return

    Returns:
        A dictionary containing subscription list and metadata
    """
    # Real implementation would use:
    # import recurly
    # client = recurly.Client()
    # subscriptions = client.list_account_subscriptions(
    #     customer_id,
    #     params={"limit": limit}
    # )

    return {
        "customer_id": customer_id,
        "subscriptions": [
            {
                "subscription_id": "sub_12345",
                "plan_code": "premium",
                "state": "active",
                "current_period_ends_at": "2025-02-01",
            },
        ],
        "total_count": 1,
        "has_more": False,
    }


@mcp.tool()
def create_subscription(
    customer_id: str, plan_code: str, currency: str = "USD"
) -> dict[str, Any]:
    """Create a new subscription for a customer.

    Args:
        customer_id: The unique identifier for the customer
        plan_code: The code of the plan to subscribe to
        currency: Currency code (default: USD)

    Returns:
        A dictionary containing the created subscription details
    """
    # Real implementation would use:
    # import recurly
    # client = recurly.Client()
    # subscription = client.create_subscription(
    #     {
    #         "account": {"code": customer_id},
    #         "plan_code": plan_code,
    #         "currency": currency,
    #     }
    # )

    return {
        "subscription_id": "sub_new_12345",
        "customer_id": customer_id,
        "plan_code": plan_code,
        "currency": currency,
        "state": "active",
        "created_at": "2025-01-01T00:00:00Z",
    }


@mcp.tool()
def cancel_subscription(subscription_id: str) -> dict[str, Any]:
    """Cancel an existing subscription.

    Args:
        subscription_id: The unique identifier for the subscription

    Returns:
        A dictionary confirming the cancellation
    """
    # Real implementation would use:
    # import recurly
    # client = recurly.Client()
    # client.cancel_subscription(subscription_id)

    return {
        "subscription_id": subscription_id,
        "status": "canceled",
        "canceled_at": "2025-01-01T00:00:00Z",
        "remaining_billing_cycles": 0,
    }


@mcp.tool()
def get_plan_details(plan_code: str) -> dict[str, Any]:
    """Get details about a specific plan.

    Args:
        plan_code: The code of the plan to retrieve

    Returns:
        A dictionary containing plan information
    """
    # Real implementation would use:
    # import recurly
    # client = recurly.Client()
    # plan = client.get_plan(plan_code)

    return {
        "plan_code": plan_code,
        "plan_name": "Premium Plan",
        "description": "Premium subscription plan with unlimited features",
        "price": 99.99,
        "currency": "USD",
        "billing_cycle_type": "monthly",
        "trial_duration": 0,
    }
