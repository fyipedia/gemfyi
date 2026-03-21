"""MCP server for gemfyi — AI assistant tools for gemfyi.com.

Run: uvx --from "gemfyi[mcp]" python -m gemfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GemFYI")


@mcp.tool()
def list_gems(limit: int = 20, offset: int = 0) -> str:
    """List gems from gemfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from gemfyi.api import GemFYI

    with GemFYI() as api:
        data = api.list_gems(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No gems found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_gem(slug: str) -> str:
    """Get detailed information about a specific gem.

    Args:
        slug: URL slug identifier for the gem.
    """
    from gemfyi.api import GemFYI

    with GemFYI() as api:
        data = api.get_gem(slug)
        return str(data)


@mcp.tool()
def list_origins(limit: int = 20, offset: int = 0) -> str:
    """List origins from gemfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from gemfyi.api import GemFYI

    with GemFYI() as api:
        data = api.list_origins(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No origins found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_gem(query: str) -> str:
    """Search gemfyi.com for gemstones, mineralogy, and origins.

    Args:
        query: Search query string.
    """
    from gemfyi.api import GemFYI

    with GemFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
