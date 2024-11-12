# WGDI Inspired Tool

This tool is inspired by the WGDI (Whole Genome Duplication Identification) project. It provides a simple way to visualize synteny between two genomes.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Input File Format](#input-file-format)
4. [Output](#output)
5. [Example](#example)
6. [Troubleshooting](#troubleshooting)
7. [Credits](#credits)

## Installation

1. Ensure you have Python 3.7+ installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
   ```
   git clone https://github.com/ezrafchev/wgdi-inspired.git
   cd wgdi-inspired
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the tool, use the following command:

```
python wgdi_inspired.py <input_file> <output_file>
```

- `<input_file>`: Path to your input CSV file containing synteny data.
- `<output_file>`: Path where the output synteny plot will be saved.

## Input File Format

The input file should be a CSV file with two columns:
- `genome1_position`: Position in the first genome
- `genome2_position`: Corresponding position in the second genome

Example:
```
genome1_position,genome2_position
100,120
200,220
300,310
...
```

## Output

The tool generates a scatter plot showing the syntenic regions between two genomes. The x-axis represents positions in Genome 1, and the y-axis represents positions in Genome 2.

## Example

1. Use the provided sample data:
   ```
   python wgdi_inspired.py sample_synteny_data.csv synteny_plot.png
   ```

2. Check the generated `synteny_plot.png` file.

## Troubleshooting

- If you encounter a "command not found" error, make sure you've activated the virtual environment.
- For any import errors, ensure you've installed all required packages using `pip install -r requirements.txt`.

## Credits

Developed by Mariana Silva de Oliveira

Inspired by: https://github.com/SunPengChuan/wgdi

