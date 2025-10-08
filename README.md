# Merging MediaPipe with ELAN Annotations

Merge MediaPipe keypoint time series with ELAN annotation data for multimodal gesture analysis.

## 🔬 Research Context

This module enables temporal alignment of gesture motion data with linguistic annotations, supporting multimodal communication research that examines the relationship between speech and gesture.

## 🎯 What This Project Does

1. **Load multimodal data**: Read MediaPipe keypoint CSVs and ELAN annotation files
2. **Temporal alignment**: Map ELAN annotations to corresponding time points in motion data
3. **Data merging**: Combine motion trajectories with linguistic annotations
4. **Export merged datasets**: Save aligned multimodal data for downstream analysis

## 📊 Merging Process

1. **Load Data Sources**: Import MediaPipe keypoints and ELAN annotation files
2. **Inspect Formats**: Examine data structures and time ranges
3. **Temporal Mapping**: Align annotation time windows with motion data timestamps
4. **Merge Datasets**: Combine motion and annotation data by time
5. **Export Results**: Save merged multimodal datasets

## 🔧 Methods

- **Time-based alignment**: Map ELAN begin/end times to MediaPipe timestamps
- **Annotation propagation**: Assign annotation labels to corresponding motion frames
- **Multi-file processing**: Handle multiple participants/sessions
- **Data validation**: Ensure temporal consistency across modalities

## 📁 Project Structure

```
Merging_Motion_ELAN/
├── README.md
├── environment.yml
├── notebooks/
│   └── Multimodal_Merging.ipynb
├── data/
│   ├── processed/                     # Processed motion data
│   └── raw/                          # Raw input files
├── src/
│   ├── __init__.py
│   ├── main.py                       # Main processing script
│   └── utils.py                      # Utility functions
└── tests/
    ├── __init__.py
    └── test_processing.py
```

## 🚀 Quick Start

### Prerequisites

```bash
conda env create -f environment.yml
conda activate merging
```

### Run the Interactive Notebook

```bash
jupyter lab
# Open notebooks/Multimodal_Merging.ipynb
```

### Basic Usage

1. Place MediaPipe keypoint CSVs in `data/processed/`
2. Place ELAN annotation files in `data/raw/`
3. Run the merging notebook to align and combine datasets
4. Export merged data for multimodal analysis

## 📈 Data Format

### Input
- **MediaPipe CSVs**: Time series with keypoint coordinates (X, Y, Z) and timestamps
- **ELAN annotations**: Tab-separated files with begin/end times and annotation labels

### Output
- **Merged CSVs**: Combined datasets with motion data and corresponding annotations
- **Aligned time series**: Motion trajectories with linguistic labels at each time point

## 🔗 Related Projects

- `../MediaPipe_keypoints_extraction/`
- `../Smoothing/`
- `../Normalization/`
- `../Speed_Acceleration_Jerk/`

## 📖 References

- ELAN documentation: [https://archive.mpi.nl/tla/elan](https://archive.mpi.nl/tla/elan)
- Multimodal gesture analysis literature

## 🤝 Contributing

This project is part of the MPI Multimodal Interaction Research framework. For questions or contributions, please refer to the main project documentation.

## 📄 License

This project is part of the MPI research framework. Please refer to the main project license for usage terms.