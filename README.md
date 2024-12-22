# ColorPrint Utility

## Overview
`ColorPrint` is a Python utility class designed to make terminal text output more dynamic and visually appealing by leveraging ANSI escape codes for colored text, text styles, and background highlights.

## Features
- Print colored text to the terminal.
- Add text styles such as bold and underline.
- Use background highlights for emphasis.
- Create and display solid color bars for separators or visual breaks.

## How to Use

### 1. Colorizing Text
You can use the `colorize` method to return a formatted string with specified color, style, and highlight:

```python
from color_print import ColorPrint

text = ColorPrint.colorize("Hello, World!", color="blue", style="bold", highlight="yellow")
print(text)
```

### 2. Printing with Styles
The `print` method simplifies printing directly to the terminal with the desired styles:

```python
ColorPrint.print("Important Message", color="red", style="bold", highlight="white")
```

### 3. Creating a Color Bar
Use `color_bar` to create a visual separator:

```python
ColorPrint.color_bar(width=50, char="*", color="cyan", highlight="magenta")
```

## Customization Options

### Colors
Supported text colors:
- `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `reset`

### Styles
Supported text styles:
- `bold`, `underline`, `reset`

### Highlights
Supported background colors:
- `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `reset`

## Example Use Case
```python
ColorPrint.print("Welcome to ColorPrint!", color="green", style="bold")
ColorPrint.color_bar(width=40, char="=", color="yellow")
ColorPrint.print("Error: Something went wrong!", color="red", highlight="white")
```

## Requirements
No external libraries are required. Works with Python 3.6+.
