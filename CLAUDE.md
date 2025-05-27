# CLAUDE.md

**Version: 0.8.0**

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository (Spyglass_Analytica_Adhoc) contains a collection of small ad hoc data analytics projects. Each project typically consists of Jupyter notebooks (.ipynb) for analysis and visualization, Python modules (.py) containing supporting functions and data structures, and when applicable, related data files.

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

## Common Development Workflows

### Working with Jupyter Notebooks

1. **Running notebooks**: Use a Jupyter notebook environment to open and run the `.ipynb` files
2. **Importing custom modules**: Each project's supporting modules should be imported directly in the notebook (e.g., `from survey_utils import *`)

### Python Utility Modules

- Project-specific utility functions are stored in `.py` files within each project directory
- These modules typically contain:
  - Helper functions for data processing and analysis
  - Data mappings (e.g., dictionaries mapping text responses to numerical values)
  - Visualization functions

### Data Import Standards

All projects must adhere to the following data import requirements:

1. **YRMO Field**: Required date field in YYMM format (e.g., "2401" for January 2024)
   - Must be present in all datasets
   - Format: Two-digit year followed by two-digit month
   - Field name: "YRMO"

2. **LTR Field**: Required satisfaction score field
   - Must be present in all datasets  
   - Field name: "LTR"
   - Should contain numerical satisfaction scores

### Extending Projects

When adding new functionality:
1. Add new functions to the project's utility module
2. Update the notebook to demonstrate the new functionality
3. Document any new dependencies or data format requirements
4. Ensure data imports comply with YRMO and LTR field standards


## Git Commit Message Guidelines

When creating git commits, use this exact format:

1. **First line**: Version number (e.g., "Version 0.5.0")
2. **Blank line**
3. **Features added** (bulleted list starting with "- Add")
4. **Blank line** 
5. **Removals** (bulleted list starting with "- Remove")

**DO NOT INCLUDE**: Authoring, reviewing info, emojis, or any other text.