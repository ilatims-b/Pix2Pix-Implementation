#!/bin/bash

# combine_data_files.sh
# This script combines data files that were previously split into smaller chunks
# back into their original format.
#
# The script combines:
# 1. train_data_sketch_part_* into train_data_sketch.txt
# 2. train_data_full_part_* into train_data_full.txt

echo "Starting the file combination process..."

# Create the output directory if it doesn't exist
mkdir -p combined_data

# Combine the sketch data files
echo "Combining sketch data files..."
cat data_chunks/train_data_sketch_part_* > combined_data/train_data_sketch.txt

# Check if the combination was successful
if [ $? -eq 0 ]; then
    echo "Sketch data files combined successfully."
    echo "Output: combined_data/train_data_sketch.txt"
else
    echo "Error: Failed to combine sketch data files."
    exit 1
fi

# Combine the full data files
echo "Combining full data files..."
cat data_chunks/train_data_full_part_* > combined_data/train_data_full.txt

# Check if the combination was successful
if [ $? -eq 0 ]; then
    echo "Full data files combined successfully."
    echo "Output: combined_data/train_data_full.txt"
else
    echo "Error: Failed to combine full data files."
    exit 1
fi

# Display file sizes to verify successful combination
echo -e "\nFile sizes after combination:"
ls -lh combined_data/

echo -e "\nCombination process completed successfully!"
echo "Original files are now available in the 'combined_data' directory."

