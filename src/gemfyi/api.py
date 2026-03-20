"""HTTP API client for gemfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install gemfyi[api]``

Usage::

    from gemfyi.api import GemFYI

    with GemFYI() as api:
        items = api.list_categories()
        detail = api.get_category("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class GemFYI:
    """API client for the gemfyi.com REST API.

    Provides typed access to all gemfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://gemfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://gemfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_categories(self, **params: Any) -> dict[str, Any]:
        """List all categories."""
        return self._get("/api/v1/categories/", **params)

    def get_category(self, slug: str) -> dict[str, Any]:
        """Get category by slug."""
        return self._get(f"/api/v1/categories/" + slug + "/")

    def list_comparisons(self, **params: Any) -> dict[str, Any]:
        """List all comparisons."""
        return self._get("/api/v1/comparisons/", **params)

    def get_comparison(self, slug: str) -> dict[str, Any]:
        """Get comparison by slug."""
        return self._get(f"/api/v1/comparisons/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_gems(self, **params: Any) -> dict[str, Any]:
        """List all gems."""
        return self._get("/api/v1/gems/", **params)

    def get_gem(self, slug: str) -> dict[str, Any]:
        """Get gem by slug."""
        return self._get(f"/api/v1/gems/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_origins(self, **params: Any) -> dict[str, Any]:
        """List all origins."""
        return self._get("/api/v1/origins/", **params)

    def get_origin(self, slug: str) -> dict[str, Any]:
        """Get origin by slug."""
        return self._get(f"/api/v1/origins/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> GemFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
