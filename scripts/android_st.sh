#!/bin/bash

# Check if argument is passed
if [ "$#" -ne 1 ]; then
    echo "Error: No directory path provided. Please provide a directory path."
    exit 1
fi

# Check if directory exists
if [ ! -d "$1" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi

# Check if subdirectory 'printer-support' exists
if [ -d "$1/print-support" ]; then
    rm -r "$1/print-support"
    echo "Subdirectory 'print-support' has been deleted."
else
    echo "Subdirectory 'print-support' does not exist."
fi

# Delete subdirectories in the hpx directory that start with raw
for dir in "$1"/hpx/*; do
    # Check if it is a directory and starts with 'raw'
    if [ -d "$dir" ] && [[ $(basename "$dir") == raw* ]]; then
        rm -r "$dir"
        echo "Deleted directory $dir"
    fi
done

# Rename the hpx directory to res
mv "$1/hpx" "$1/res"
destination_dir="$1/res"
echo "The destination directory is: $destination_dir"

# Remove strings.xml files from each subdirectory in the cloud-services-ows directory
for dir in "$1"/cloud-services-ows/*; do
    if [ -d "$dir" ]; then
        rm "$dir/strings.xml"
        echo "Deleted strings.xml in directory $dir"
    fi
done

# Remove values-ar and values-iw directories from each directory
for dir in "$1"/*; do
    if [ -d "$dir" ]; then
        for subdir in "$dir"/*; do
            if [ -d "$subdir" ] && { [ "$(basename "$subdir")" == "values-ar" ] || [ "$(basename "$subdir")" == "values-iw" ]; }; then
                rm -r "$subdir"
                echo "Deleted values directory $subdir"
            fi
        done
    fi
done

# Rename subfiles to avoid duplicates and move them to the destination directory
for dir in "$1"/*; do
    if [ -d "$dir" ]; then
        if [[ $(basename "$dir") == "res" ]]; then
            continue
        fi
        # Get the directory name
        dir_name=$(basename "$dir")
        for subdir in "$dir"/*; do
            if [ -d "$subdir" ]; then
                # Loop over files in the subdirectory
                for file in "$subdir"/*; do
                    # Check if it is a file
                    if [ -f "$file" ]; then
                        # Get the file name and extension
                        file_name=$(basename "$file")
                        base_name="${file_name%.*}"
                        ext="${file_name##*.}"
                        destination_sub_dir=$(basename "$subdir")
                        # Rename the file
                        new_file_name="${base_name}_${dir_name}.${ext}"
                        mv "$file" "$subdir/$new_file_name"
                        mv "$subdir/$new_file_name" "$destination_dir/$destination_sub_dir/"
                    fi
                done
            fi
        done
    fi
done

# Remove strings_chinese_only.xml strings_mediaclip.xml strings_unused.xml string_unused_dynamic-studio.xml
declare -a files_to_remove=("strings_chinese_only.xml" "strings_mediaclip.xml" "strings_unused.xml" "strings_unused_dynamic-studio.xml")

for subdir in "$destination_dir"/*; do
    for file in "${files_to_remove[@]}"; do
        if [ -f "$subdir/$file" ]; then
            rm "$subdir/$file"
            echo "Removed $subdir/$file"
        fi
    done
done
echo "Path for string localisation testing:"
echo "$1/res"
