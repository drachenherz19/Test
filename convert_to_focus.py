import subprocess

# Define the input and output file paths
input_file_path = r'C:\Users\rianl\OneDrive\Desktop\Internship FOCUS 1.0 docs\New folder\summary_view_export_234229113444_833804721509.csv'
output_file_path = r'C:\Users\rianl\OneDrive\Desktop\Internship FOCUS 1.0 docs\New folder\Output1.csv'

subprocess.run([
    'python', '-m', 'focus_converter.main',
    '--input-file', input_file_path,
    '--output-file', output_file_path,
    '--format', 'csv'
])

print(f"File saved to {output_file_path}")
