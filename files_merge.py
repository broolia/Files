import os

def merge_files(directory="text", output_file="merged_file.txt"):
    
    files_data = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                files_data.append((filename, len(lines), lines))

    files_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename, line_count, lines in files_data:
            outfile.write(f"{filename}\n")
            outfile.write(f"{line_count}\n")
            outfile.writelines(lines)
            outfile.write("\n")
            
merge_files("text", "merged_files.txt")