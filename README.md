# gemfyi

[![PyPI version](https://agentgif.com/badge/pypi/gemfyi/version.svg)](https://pypi.org/project/gemfyi/)
[![Python](https://img.shields.io/pypi/pyversions/gemfyi)](https://pypi.org/project/gemfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/gemfyi/)

Python API client and CLI for gemstones, mineralogy, and gemological grading. Access 442 gemstones across 5 categories — precious, semi-precious, organic, synthetic, and collector gems — with Mohs hardness, crystal systems, refractive indices, specific gravity, and geographic origins. Zero dependencies.

Extracted from [GemFYI](https://gemfyi.com/), a gemology reference platform with 43 glossary terms, 85 educational guides, 15 geographic origins, and comparison tools for gemologists, jewelers, and developers working with gemstone data.

> **Explore gemstones at [gemfyi.com](https://gemfyi.com/)** — browse the [gemstone database](https://gemfyi.com/gems/), compare [gem categories](https://gemfyi.com/categories/), explore [geographic origins](https://gemfyi.com/origins/), and read the [gemology glossary](https://gemfyi.com/glossary/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/gemfyi/main/demo.gif" alt="gemfyi demo — gemstone lookup, Mohs hardness comparison, and crystal system browsing in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Gemstone Categories](#gemstone-categories)
  - [Physical & Optical Properties](#physical--optical-properties)
  - [Crystal Systems & Mineralogy](#crystal-systems--mineralogy)
  - [Geographic Origins](#geographic-origins)
  - [Gemstone Comparisons](#gemstone-comparisons)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Gemstones](#learn-more-about-gemstones)
- [Also Available](#also-available)
- [Science FYI Family](#science-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install gemfyi                # Core (zero deps)
pip install "gemfyi[cli]"         # + Command-line interface (typer, rich)
pip install "gemfyi[mcp]"         # + MCP server for AI assistants
pip install "gemfyi[api]"         # + HTTP client for gemfyi.com API
pip install "gemfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from gemfyi gemfyi search diamond
```

## Quick Start

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # Browse 442 gemstones across 5 categories
    gems = api.list_gems(limit=10)
    print(gems["count"])  # 442 total gemstones

    # Look up a specific gemstone with full properties
    diamond = api.get_gem("diamond")
    print(diamond["mohs_hardness"])     # 10.0
    print(diamond["crystal_system"])    # Isometric
    print(diamond["refractive_index"])  # 2.417
    print(diamond["specific_gravity"])  # 3.5

    # Search across gems, origins, and guides
    results = api.search("sapphire")
    print(results["count"])
```

## What You Can Do

### Gemstone Categories

Gemstones are classified into **5 categories** based on rarity, durability, and value. The traditional "precious vs. semi-precious" distinction dates to 1854 French legislation, though modern gemology recognizes that some semi-precious gems (like alexandrite or paraiba tourmaline) exceed precious gems in market value.

| Category | Count | Examples |
|----------|-------|---------|
| **Precious Gems** | 7 | Diamond, Ruby, Sapphire, Emerald, Alexandrite |
| **Semi-Precious Gems** | 387 | Amethyst, Topaz, Garnet, Tourmaline, Aquamarine, Opal |
| **Organic Gems** | 12 | Pearl, Amber, Coral, Jet, Ammolite, Ivory |
| **Collector Gems** | 36 | Benitoite, Painite, Grandidierite, Jeremejevite |
| **Synthetic Gems** | — | Lab-grown diamond, Cubic zirconia, Moissanite |

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # List all 5 gem categories with gem counts
    categories = api.list_categories()
    for cat in categories["results"]:
        print(cat["slug"])  # precious-gems, semi-precious-gems, organic-gems, ...

    # Get category details with member gems
    precious = api.get_category("precious-gems")
    print(precious)
```

Learn more: [Gem Categories](https://gemfyi.com/categories/) · [Gemology Glossary](https://gemfyi.com/glossary/) · [Gem Guides](https://gemfyi.com/guides/)

### Physical & Optical Properties

Each gemstone in the database includes comprehensive physical and optical properties used in gemological identification and grading. These properties follow standards established by the Gemological Institute of America (GIA) and similar laboratories.

| Property | What It Measures | Example (Diamond) |
|----------|------------------|-------------------|
| **Mohs Hardness** | Scratch resistance on 1-10 scale | 10.0 |
| **Specific Gravity** | Density relative to water | 3.50-3.53 |
| **Refractive Index** | Light bending (brilliance) | 2.417-2.419 |
| **Birefringence** | Double refraction strength | None (singly refractive) |
| **Dispersion** | Spectral light splitting (fire) | 0.044 |
| **Crystal System** | Atomic arrangement geometry | Isometric (cubic) |
| **Cleavage** | Tendency to split along planes | Perfect octahedral |
| **Fracture** | Breaking pattern outside cleavage | Conchoidal |
| **Luster** | Surface light reflection quality | Adamantine |
| **Pleochroism** | Color change by viewing angle | None |
| **Fluorescence** | UV light response | Often blue (LW) |

The **4Cs of diamond grading** (Cut, Color, Clarity, Carat) apply specifically to diamonds, but Mohs hardness and refractive index are universal identification tools for all 442 gemstones.

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # Get complete gemstone properties
    ruby = api.get_gem("ruby")
    print(ruby.get("mohs_hardness"))      # 9.0 (corundum)
    print(ruby.get("crystal_system"))     # Trigonal
    print(ruby.get("refractive_index"))   # 1.762-1.770
    print(ruby.get("specific_gravity"))   # 3.97-4.05
    print(ruby.get("dispersion"))         # 0.018
```

Learn more: [Gemstone Database](https://gemfyi.com/gems/) · [Gemology Glossary](https://gemfyi.com/glossary/)

### Crystal Systems & Mineralogy

Gemstones form in **7 crystal systems** determined by the symmetry of their atomic lattice. Crystal system is a primary identification tool in gemology — for example, all garnets are isometric (cubic), while all beryls (emerald, aquamarine) are hexagonal.

| Crystal System | Axes | Examples |
|---------------|------|---------|
| **Isometric (Cubic)** | 3 equal, 90 degrees | Diamond, Garnet, Spinel, Fluorite |
| **Hexagonal** | 3 equal + 1 unique | Emerald, Aquamarine, Apatite |
| **Trigonal** | Like hexagonal, 3-fold symmetry | Ruby, Sapphire, Quartz, Tourmaline |
| **Tetragonal** | 2 equal + 1 unique, 90 degrees | Zircon, Rutile, Scapolite |
| **Orthorhombic** | 3 unequal, 90 degrees | Topaz, Peridot, Tanzanite, Chrysoberyl |
| **Monoclinic** | 3 unequal, 1 oblique angle | Jade (Jadeite), Moonstone, Spodumene |
| **Triclinic** | 3 unequal, no right angles | Labradorite, Turquoise, Kyanite |

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # Browse gems by crystal system
    emerald = api.get_gem("emerald")
    print(emerald.get("crystal_system"))  # Hexagonal (beryl group)

    diamond = api.get_gem("diamond")
    print(diamond.get("crystal_system"))  # Isometric (cubic carbon)
```

Learn more: [Gem Categories](https://gemfyi.com/categories/) · [Gem Guides](https://gemfyi.com/guides/)

### Geographic Origins

GemFYI catalogs **15 geographic origins** — the major gem-producing regions worldwide. Origin significantly affects value: a Kashmir sapphire commands premiums over identical stones from other localities, and Colombian emeralds are prized for their distinctive warm green.

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # Browse 15 geographic origins
    origins = api.list_origins()
    for origin in origins["results"]:
        print(origin["slug"])

    # Get origin detail with associated gems
    detail = api.get_origin("colombia")
```

Learn more: [Geographic Origins](https://gemfyi.com/origins/) · [Gem Guides](https://gemfyi.com/guides/)

### Gemstone Comparisons

Compare two gemstones side-by-side across all physical and optical properties. Pre-computed comparisons highlight the differences in hardness, refractive index, specific gravity, and crystal system for popular gem pairs.

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    # Browse gemstone comparisons
    comparisons = api.list_comparisons(limit=5)
    for comp in comparisons["results"]:
        print(comp["slug"])
```

Learn more: [Gem Comparisons](https://gemfyi.com/comparisons/) · [Gemology Glossary](https://gemfyi.com/glossary/)

## Command-Line Interface

```bash
pip install "gemfyi[cli]"

gemfyi search diamond                # Search gemstones by name
gemfyi search "blue sapphire"        # Search by color and name
gemfyi search moissanite             # Search synthetic and natural gems
```

## MCP Server (Claude, Cursor, Windsurf)

Add gemstone lookup tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "gemfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "gemfyi": {
            "command": "uvx",
            "args": ["--from", "gemfyi[mcp]", "python", "-m", "gemfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```bash
pip install "gemfyi[api]"
```

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    gems = api.list_gems()               # GET /api/v1/gems/
    diamond = api.get_gem("diamond")     # GET /api/v1/gems/diamond/
    categories = api.list_categories()   # GET /api/v1/categories/
    origins = api.list_origins()         # GET /api/v1/origins/
    results = api.search("ruby")        # GET /api/v1/search/?q=ruby
```

### Example

```bash
curl -s "https://gemfyi.com/api/v1/gems/diamond/"
```

```json
{
  "slug": "diamond",
  "category": "precious-gems",
  "mohs_hardness": 10.0,
  "specific_gravity": 3.5,
  "crystal_system": "Isometric",
  "refractive_index": 2.417,
  "dispersion": 0.044
}
```

Full API documentation at [gemfyi.com/developers/](https://gemfyi.com/developers/).

## API Reference

| Method | Description |
|--------|-------------|
| `list_gems(**params)` | List all 442 gemstones with pagination |
| `get_gem(slug)` | Get gemstone detail with full properties |
| `list_categories(**params)` | List all 5 gem categories |
| `get_category(slug)` | Get category detail with member gems |
| `list_origins(**params)` | List 15 geographic origins |
| `get_origin(slug)` | Get origin detail with associated gems |
| `list_comparisons(**params)` | List gemstone comparisons |
| `get_comparison(slug)` | Get side-by-side comparison |
| `list_glossary(**params)` | List 43 gemology glossary terms |
| `get_term(slug)` | Get glossary term definition |
| `list_guides(**params)` | List 85 educational guides |
| `get_guide(slug)` | Get guide content |
| `search(query)` | Search across all gemstone content |

## Learn More About Gemstones

- **Browse**: [Gemstone Database](https://gemfyi.com/gems/) · [Gem Categories](https://gemfyi.com/categories/) · [Geographic Origins](https://gemfyi.com/origins/)
- **Compare**: [Gem Comparisons](https://gemfyi.com/comparisons/)
- **Reference**: [Gemology Glossary](https://gemfyi.com/glossary/)
- **Guides**: [Educational Guides](https://gemfyi.com/guides/)
- **API**: [REST API Docs](https://gemfyi.com/developers/) · [OpenAPI Spec](https://gemfyi.com/api/v1/)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install gemfyi` | [npm](https://www.npmjs.com/package/gemfyi) |
| **MCP** | `uvx --from "gemfyi[mcp]" python -m gemfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Science FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — physical sciences, chemistry, geology, astronomy, and materials.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| chemfyi | [PyPI](https://pypi.org/project/chemfyi/) | [npm](https://www.npmjs.com/package/chemfyi) | Periodic table, 500 compounds, 371 reactions — [chemfyi.com](https://chemfyi.com/) |
| alloyfyi | [PyPI](https://pypi.org/project/alloyfyi/) | [npm](https://www.npmjs.com/package/alloyfyi) | 765 metal alloys, 12 families, compositions — [alloyfyi.com](https://alloyfyi.com/) |
| **gemfyi** | [PyPI](https://pypi.org/project/gemfyi/) | [npm](https://www.npmjs.com/package/gemfyi) | **442 gemstones, Mohs scale, grading — [gemfyi.com](https://gemfyi.com/)** |
| starfyi | [PyPI](https://pypi.org/project/starfyi/) | [npm](https://www.npmjs.com/package/starfyi) | 119,602 stars, 6,128 exoplanets, 13,305 deep-sky objects — [starfyi.com](https://starfyi.com/) |
| mineralfyi | [PyPI](https://pypi.org/project/mineralfyi/) | [npm](https://www.npmjs.com/package/mineralfyi) | 6,215 minerals, 7 crystal systems — [mineralfyi.com](https://mineralfyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times — [distancefyi.com](https://distancefyi.com/) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours — [timefyi.com](https://timefyi.com/) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements — [namefyi.com](https://namefyi.com/) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units — [unitfyi.com](https://unitfyi.com/) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation — [holidayfyi.com](https://holidayfyi.com/) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | — | Cocktail ABV, calories, flavor — [cocktailfyi.com](https://cocktailfyi.com/) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | — | Unified CLI: `fyi gem info diamond` — [fyipedia.com](https://fyipedia.com/) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | — | Unified MCP hub for AI assistants — [fyipedia.com](https://fyipedia.com/) |

## Embed Widget

Embed [GemFYI](https://gemfyi.com) widgets on any website with [gemfyi-embed](https://widget.gemfyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/gemfyi-embed@1/dist/embed.min.js"></script>
<div data-gemfyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.gemfyi.com)

## License

MIT
