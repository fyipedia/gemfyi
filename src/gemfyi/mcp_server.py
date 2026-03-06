"""MCP server for gemfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from gemfyi.api import GemFYI

mcp = FastMCP("gemfyi")


@mcp.tool()
def search_gemfyi(query: str) -> dict[str, Any]:
    """Search gemfyi.com for content matching the query."""
    with GemFYI() as api:
        return api.search(query)
