#!/bin/bash

# Set the target directory
target_dir="/etc"

# Find and count files excluding directories and symbolic links
file_count=$(find "$target_dir" -type f ! -type l | wc -l)

# Output the result
echo "The number of regular files in $target_dir is: $file_count"

