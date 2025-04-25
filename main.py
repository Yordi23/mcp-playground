from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def get_current_date() -> str:
    """Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")


@mcp.tool()
def get_current_doctor() -> str:
    """Get the currently logged in doctor name"""
    return "Dr. Smith"


@mcp.tool()
def get_future_appointments() -> int:
    """Get future patient appointments for all doctors"""
    return [
        {
            "id": 1,
            "date": "2025-05-01",
            "time": "10:00",
            "patient": "John Doe",
            "doctor": "Dr. Smith",
        },
        {
            "id": 2,
            "date": "2025-05-02",
            "time": "11:00",
            "patient": "Jane Smith",
            "doctor": "Dr. Johnson",
        },
        {
            "id": 2,
            "date": "2025-05-02",
            "time": "11:00",
            "patient": "Jane Smith",
            "doctor": "Dr. Johnson",
        },
        {
            "id": 3,
            "date": "2025-04-24",
            "time": "11:00",
            "patient": "Molly Harrys",
            "doctor": "Dr. Johnson",
        },
        {
            "id": 4,
            "date": "2025-04-24",
            "time": "11:00",
            "patient": "John Harrys",
            "doctor": "Dr. Smith",
        },
        {
            "id": 5,
            "date": "2025-04-24",
            "time": "12:00",
            "patient": "Dina Wards",
            "doctor": "Dr. Smith",
        },
    ]


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
