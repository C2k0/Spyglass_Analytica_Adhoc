# Spyglass Analytica Ad Hoc Projects

This repository contains a collection of small ad hoc data analytics projects. Each project typically consists of:

- Jupyter notebooks (`.ipynb`) for analysis and visualization
- Python modules (`.py`) containing supporting functions and data structures
- Related data files (when applicable)

## Project Structure

Projects are organized in their own directories:

```
Spyglass_Analytica_Adhoc/
├── Project_Name_1/
│   ├── project_name_1.ipynb
│   ├── project_name_1_utils.py
│   └── data/
├── Project_Name_2/
│   ├── project_name_2.ipynb
│   └── project_name_2_utils.py
└── ...
```

## Current Projects

- **Quick_Survey_Analysis**: Tools for analyzing and interpreting survey data with response mapping functionality. Contains utilities for converting text responses to numerical values, statistical analysis, data visualization, segment analysis, and free text analysis.

- **RAG_Survey_Analysis_Europa**: A structured RAG (Retrieval-Augmented Generation) system for analyzing survey data using AI/ChatGPT integration with SharePoint data access. Features automated SQL query processing, column validation, LTR/driver analysis, and standardized AI prompts for consistent survey analysis across multiple data sources.

## Data Import Standards

All projects must adhere to the following data import requirements:

- **YRMO Field**: Required date field in YYMM format (e.g., "2401" for January 2024)
- **LTR Field**: Required satisfaction score field with numerical values

## Usage

Each project is self-contained and can be run independently. Navigate to the project directory and open the Jupyter notebook to explore the analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.