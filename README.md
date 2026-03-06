# gemfyi

Gemstone and mineralogy reference API client — [gemfyi.com](https://gemfyi.com)

## Install

```bash
pip install gemfyi
```

## Quick Start

```python
from gemfyi.api import GemFYI

with GemFYI() as api:
    results = api.search("diamond")
    print(results)
```

## License

MIT
