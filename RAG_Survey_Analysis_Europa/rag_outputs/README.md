# RAG Output Directory

This directory contains processed survey data for RAG (Retrieval-Augmented Generation) access.

## Structure

```
rag_outputs/
├── current/                    # Latest processed data (RAG reads from here)
│   ├── combined_ltr_drivers.csv      # LTR and driver scores across all surveys
│   ├── combined_all_surveys.csv      # All survey data combined
│   └── processing_summary.csv        # Summary of last processing run
└── archive/                    # Historical runs (timestamped files)
    ├── Combined_LTR_Drivers_YYYYMMDD_HHMMSS.csv
    ├── Combined_All_Surveys_YYYYMMDD_HHMMSS.csv
    └── Processing_Summary_YYYYMMDD_HHMMSS.csv
```

## File Descriptions

### current/combined_ltr_drivers.csv
- Contains NPS scores and driver metrics from all surveys
- Columns: ResponseID, Survey_Name, NPS_Score, driver columns, timestamps
- Used for: NPS analysis, driver correlation studies

### current/combined_all_surveys.csv
- Complete dataset with all columns from all surveys
- Includes transformed numeric values from text responses
- Used for: Comprehensive analysis, segment analysis, custom queries

### current/processing_summary.csv
- Metadata about the last processing run
- Shows which surveys were processed, record counts, success/failure status
- Used for: Data quality checks, monitoring

## Usage

The RAG system should:
1. Always read from the `current/` directory
2. Check `processing_summary.csv` for data freshness
3. Use `combined_ltr_drivers.csv` for NPS-specific analysis
4. Use `combined_all_surveys.csv` for detailed analysis

## Updates

Files in `current/` are overwritten with each processing run. Historical versions are preserved in `archive/` with timestamps.