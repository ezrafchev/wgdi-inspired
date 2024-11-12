import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_synteny_data(file_path):
    """Read synteny data from a CSV file."""
    return pd.read_csv(file_path)

def plot_synteny(data, output_file):
    """Create a synteny plot based on the input data."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(data['genome1_position'], data['genome2_position'], alpha=0.5)
    ax.set_xlabel('Genome 1 Position')
    ax.set_ylabel('Genome 2 Position')
    ax.set_title('Synteny Plot')
    plt.savefig(output_file)
    plt.close()
    print(f"Synteny plot saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="WGDI Inspired Tool for Synteny Analysis")
    parser.add_argument("input_file", help="Path to the input CSV file containing synteny data")
    parser.add_argument("output_file", help="Path to save the output synteny plot")
    args = parser.parse_args()
    
    data = read_synteny_data(args.input_file)
    plot_synteny(data, args.output_file)

if __name__ == "__main__":
    main()
