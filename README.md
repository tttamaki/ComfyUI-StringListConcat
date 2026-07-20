# ComfyUI String List Concat

A ComfyUI custom node that concatenates multiple string inputs into one string.

## Features

- **Multiple Text Inputs**: Concatenate 2 to 32 string inputs
- **Delimiter Support**: Insert a delimiter between each input string
- **Dynamic Input Growth**: UI automatically expands input slots as needed

## Installation

1. Clone or download this repository into your ComfyUI custom_nodes directory:

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/tttamaki/ComfyUI-StringListConcat.git
   ```

2. Restart ComfyUI

## Usage

1. Add the **String List Concat** node to your workflow
2. Connect 2 or more string inputs
3. Optionally set **delimiter** (default is empty string)
4. Read the concatenated string from output

## Inputs

- **inputs** (Autogrow String): 2-32 string inputs
- **delimiter** (String): separator inserted between input strings

## Outputs

- **output** (String): concatenated text

## License

MIT License

## Author

tttamaki and GitHub Copilot
