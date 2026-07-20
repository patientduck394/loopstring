<p align="left">
  <a href="https://github.com">
    <img src="https://github.com/user-attachments/assets/6ae71d7c-646c-41a7-9483-5b2365df6eb3" width="225" alt="Loopstring Thumbnail">
  </a>
</p>

# Loopstring

A lightweight, powerful Python utility for terminal text formatting, custom box-drawing, and terminal UI layouts. 

## Features

- **Custom Box UI:** Wrap single or multi-line text blocks in `light`, `heavy`, `double`, `rounded`, or `dashed` geometric borders.
- **Clean Namespaces:** Organized using clean object structures (`FG`, `BG`, `FORMAT`, `BOXES`) to ensure autocomplete works perfectly in your IDE.
- **Styling Combinations:** Easily concatenate colors and text styles without syntax errors or formatting collisions.
- **Pre-built Symbols:** Enjoy stress-free symbol concatenation without having to copy-paste.

## Installation

Once published, you can install the package directly from PyPI using pip:

```bash
pip install loopstring
```

## Usage Examples

### 1. Drawing a Custom Box
```python
from loopstring import BOXES

# Draw a clean rounded box using the style parameter
print(BOXES.draw_box("System Online", style="rounded"))
```

### 2. Styling Terminal Text
```python
from loopstring import FG, BG, FORMAT

# Apply vibrant styles safely without tuples
print(f"{FG.GREEN}{FORMAT.BOLD}Success!{FORMAT.RESET} Everything loaded correctly.")
print(f"{BG.BLUE}{FG.WHITE} Notice {FORMAT.RESET} Check system updates.")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
