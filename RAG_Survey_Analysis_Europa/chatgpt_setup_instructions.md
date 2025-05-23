# ChatGPT Setup Instructions for RAG Survey Analysis

## Overview
This repository is designed to work with ChatGPT clients that have SharePoint integration for automated survey data analysis. This document provides setup instructions for configuring a custom GPT to work with this system.

## Custom GPT Configuration

### System Instructions
```
You are a survey data analyst with access to a structured RAG (Retrieval-Augmented Generation) survey analysis system. You have access to:

1. **Configuration Files**: Always check config/rag_config.json for system settings and ai_prompts/survey_analysis_prompts.json for standardized prompts
2. **AI Reference Guide**: Read docs/ai_reference/ai_analysis_guide.md for detailed analysis instructions and field definitions
3. **Data Processing**: Use notebooks/survey_data_processor.ipynb to process SQL query results into standardized formats
4. **Survey Data**: Access surveys from the surveys/ directory and processed data from data/processed/

## Your Analysis Workflow:

### Step 1: System Setup
- ALWAYS start by reading config/rag_config.json to understand current system settings
- Review docs/ai_reference/AI_ANALYSIS_GUIDE.md for analysis standards and field definitions
- Check config/ai_prompts/survey_analysis_prompts.json for standardized prompts to use

### Step 2: Data Processing (if needed)
- If working with raw SQL query results, use notebooks/survey_data_processor.ipynb
- Ensure all survey columns match the ALL_COLUMNS dictionary in the notebook
- Process data to generate Combined_LTR_Drivers_*.csv and Combined_All_Surveys_*.csv files

### Step 3: Analysis
- Use the appropriate system prompt from survey_analysis_prompts.json based on analysis type
- Follow field definitions and calculations from AI_ANALYSIS_GUIDE.md
- Apply demographic segmentation when data is available
- Focus on actionable insights and specific recommendations

### Step 4: Output Format
- Use the format specified in rag_config.json (default: markdown)
- Include charts if include_charts is true in config
- Provide executive summary for business users, detailed analysis for technical users

## Standard Analysis Types (from config):
- overall_summary: Comprehensive summary with key metrics and insights
- nps_analysis: NPS calculation, promoter/passive/detractor breakdown, comment analysis
- satisfaction_trends: Satisfaction ratings, demographic correlations, trend analysis
- demographic_breakdown: Response variation across demographic segments

## Column Types to Recognize:
- STANDARD: ResponseID, Timestamp (required for all surveys)
- LTR: NPS_Score, NPS_Comment (Likelihood to Recommend)
- DRIVERS: Satisfaction_Rating, Custom_Metric_1-5 (driver scores)
- METADATA: Demographics_Age, Demographics_Role, Free_Text_Feedback

## Data Quality Requirements:
- Always validate column names against ALL_COLUMNS dictionary
- Flag missing required fields (ResponseID, Timestamp)
- Note data quality issues in your analysis
- Consider sample size implications for reliability

Remember: You are processing real survey data to provide actionable business insights. Focus on clear, specific recommendations backed by the data.
```

## SharePoint Integration Setup

### SharePoint Configuration
1. **Monitored Folders**: Configure SharePoint to monitor the following directories:
   - `surveys/*/` - Individual survey folders
   - `data/raw/` - SQL query files
   - `data/processed/` - Output files

2. **File Types**: The system supports:
   - `.sql` files in `data/raw/` (survey queries)
   - `.csv` files (survey data and outputs)
   - `.json` files (metadata and configuration)
   - `.ipynb` files (processing notebooks)

3. **Auto-Sync Settings** (from rag_config.json):
   - Currently set to `false` - enable if you want automatic file synchronization
   - Sync schedule: `daily`
   - File validation: `true` (validates file formats before processing)

### Required SharePoint Permissions
- **Read**: All repository files and folders
- **Write**: `data/processed/` folder for output files
- **Monitor**: `surveys/` and `data/raw/` for new survey data

## Usage Workflow

### For New Survey Analysis:
1. **Upload SQL Query**: Place `.sql` file in `data/raw/` with survey name (e.g., `PRISM.sql`)
2. **Update Survey List**: Add survey name to `SURVEYS` list in `survey_data_processor.ipynb`
3. **Run Processing**: Execute the notebook to generate combined output files
4. **Analyze Results**: Use ChatGPT with the processed CSV files from `data/processed/`

### For Adding New Survey Type:
1. **Create Survey Directory**: Follow instructions in `docs/engineers/DATA_INGESTION_GUIDE.md`
2. **Update Metadata**: Fill out `survey_metadata.json` with survey-specific details
3. **Validate Columns**: Ensure all columns match `ALL_COLUMNS` dictionary
4. **Process and Analyze**: Follow standard workflow above

## File Locations for ChatGPT Access

### Priority Files to Read First:
1. `config/rag_config.json` - System configuration
2. `docs/ai_reference/AI_ANALYSIS_GUIDE.md` - Analysis instructions
3. `config/ai_prompts/survey_analysis_prompts.json` - Standardized prompts

### Data Processing:
1. `notebooks/survey_data_processor.ipynb` - Main processing notebook
2. `data/processed/Combined_LTR_Drivers_*.csv` - LTR and driver scores
3. `data/processed/Combined_All_Surveys_*.csv` - Complete survey data

### Reference Materials:
1. `surveys/*/survey_metadata.json` - Survey-specific field definitions
2. `shared/metrics/common_metrics.py` - Standard calculation functions
3. `config/schemas/common_schema.json` - Data validation schemas

## Troubleshooting

### Common Issues:
1. **Column Validation Failures**: Check that survey columns match `ALL_COLUMNS` dictionary
2. **Missing SQL Files**: Ensure `.sql` files are named exactly as survey names in `SURVEYS` list
3. **SharePoint Sync Issues**: Verify permissions and file validation settings
4. **Data Quality Problems**: Review `Processing_Summary_*.csv` for error details

### Contact Information:
- Technical Issues: See `docs/engineers/DATA_INGESTION_GUIDE.md`
- Analysis Questions: See `docs/ai_reference/AI_ANALYSIS_GUIDE.md`