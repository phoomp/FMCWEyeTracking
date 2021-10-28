import pandas as pd
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt

combined_bin_dir = Path('D:/FMCW/processed_data/adc_data.bin')

with open(combined_bin_dir, 'rb') as file:
    data = np.fromfile(combined_bin_dir)
    data = data.reshape([-1, 64, 256, 8])
    print(data.shape)

    radar_data = data[0, :, :, 0]

    range_fft = np.fft.fft(radar_data)
    doppler_fft = np.fft.fftshift(np.fft.fft(range_fft, axis=0), axes=0)
    plt.figure()
    plt.imshow(np.abs(range_fft[:, :128]))
    plt.figure()
    plt.imshow(np.abs(doppler_fft[:, :128]))
    plt.show()