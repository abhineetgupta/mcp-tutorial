# calculator.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def degrees_to_radians(degrees: float) -> float:
    """Convert degrees to radians"""
    return degrees * math.pi / 180

@mcp.tool()
def radians_to_degrees(radians: float) -> float:
    """Convert radians to degrees"""
    return radians * 180 / math.pi

@mcp.tool()
def sine(radians: float) -> float:
    """Calculate sine of angle in radians"""
    return math.sin(radians)

@mcp.tool()
def cosine(radians: float) -> float:
    """Calculate cosine of angle in radians"""
    return math.cos(radians)

@mcp.tool()
def tangent(radians: float) -> float:
    """Calculate tangent of angle in radians"""
    return math.tan(radians)


# execute and return the stdio output
if __name__ == "__main__":
    mcp.run(transport="stdio")
