"""Command-line interface for gemfyi."""

from __future__ import annotations

import json

import typer

from gemfyi.api import GemFYI

app = typer.Typer(help="GemFYI — Gemstone and mineralogy reference API client.")


@app.command()
def search(query: str) -> None:
    """Search gemfyi.com."""
    with GemFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
