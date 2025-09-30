# Contents of /Merging_Motion_ELAN/Merging_Motion_ELAN/src/main.py

import os
import sys
from utils import process_data, merge_data

def main():
    # Define paths
    raw_elan_path = os.path.join('data', 'raw', 'ELAN')
    raw_mediapipe_path = os.path.join('data', 'raw', 'mediapipe')
    processed_data_path = os.path.join('data', 'processed', 'merged_data.csv')

    # Process raw data
    elan_data = process_data(raw_elan_path)
    mediapipe_data = process_data(raw_mediapipe_path)

    # Merge data
    merged_data = merge_data(elan_data, mediapipe_data)

    # Save merged data
    with open(processed_data_path, 'w') as f:
        f.write(merged_data)

if __name__ == "__main__":
    main()