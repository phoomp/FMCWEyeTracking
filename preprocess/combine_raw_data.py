# Combines adc_data_*.bin files into a single file

from pathlib import Path
import glob

bin_data_dir = glob.glob("D:/FMCW/raw_data/*.bin")
combined_file_dir = Path("D:/FMCW/processed_data/adc_data.bin")

print(f'Found a total of {len(bin_data_dir)} files.')
print(f'F')
print(', '.join(bin_data_dir) + '\n')

combined_file = open(combined_file_dir, 'wb')

for bin_file in bin_data_dir:
    with open(bin_file, 'rb') as file:
        combined_file.write(file.read())

combined_file.close()

