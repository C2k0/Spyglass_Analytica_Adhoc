# Data Ingestion Guide for Engineers

## Overview
This guide is for engineers responsible for preparing and uploading survey data to the RAG system.

## Data Preparation Requirements

### 1. File Format
- All survey data must be provided as **CSV files**
- Use UTF-8 encoding
- Include header row with column names
- One file per survey

### 2. Required Fields
Every survey CSV must include these columns:
- `ResponseID`: Unique identifier for each response
- `Timestamp`: Date/time when survey was completed (ISO format preferred)

### 3. Standard Fields (Include if Available)
- `NPS_Score`: Net Promoter Score (0-10 scale)
- `NPS_Comment`: Open text feedback for NPS
- `Satisfaction_Rating`: Overall satisfaction (1-5 scale)
- `Satisfaction_Comment`: Open text feedback for satisfaction
- `Demographics_Age`: Age range (18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- `Demographics_Role`: Job role/position
- `Free_Text_Feedback`: General open-ended feedback

### 4. Custom Fields
- Use `Custom_Metric_1`, `Custom_Metric_2`, etc. for survey-specific questions
- Document what each custom field represents in the survey metadata

## File Naming Convention
```
{survey_name}_{date}.csv
Example: employee_satisfaction_2024_Q1.csv
```

## Adding a New Survey (e.g., Survey 6)

### Step-by-Step Process:

1. **Create Survey Directory**:
   ```bash
   cp -r surveys/survey_1/ surveys/survey_6/
   ```

2. **Update Template Files**:
   - Rename `survey_1_template.csv` to `survey_6_template.csv`
   - Keep the same column structure unless survey-specific columns are needed

3. **Update Metadata File**:
   - Edit `surveys/survey_6/survey_metadata.json`
   - Replace all "UPDATE_REQUIRED" fields with actual survey information
   - Define any custom metrics specific to this survey

4. **Add Survey Data**:
   - Place your actual survey CSV file in `surveys/survey_6/`
   - Ensure column names match the template
   - Follow the naming convention: `{survey_name}_{date}.csv`

5. **Validate and Test**:
   ```bash
   python shared/utils/data_validator.py surveys/survey_6/your_survey_file.csv
   ```

### Files That Need Updates for New Survey:
- `surveys/survey_X/survey_metadata.json` (survey-specific details)
- `config/rag_config.json` (only if special configuration needed)
- Template CSV file (renamed for consistency)

## Standard Upload Process
1. **Validate Data**: Run validation script (see shared/utils/)
2. **Place File**: Copy to appropriate survey folder (surveys/survey_X/)
3. **Update Metadata**: Fill out survey_metadata.json
4. **Test**: Run sample analysis to verify data quality

## Data Quality Checklist
- [ ] No duplicate ResponseIDs
- [ ] Timestamps in valid format
- [ ] NPS scores between 0-10
- [ ] Satisfaction ratings between 1-5
- [ ] No sensitive PII in text fields
- [ ] Consistent demographic categories

## Common Issues to Avoid
- **Mixed scales**: Don't mix 1-5 and 1-10 rating scales in the same survey
- **Inconsistent categories**: Use consistent demographic options across surveys
- **Missing metadata**: Always provide survey context and custom field definitions
- **Large files**: Split very large surveys (>10MB) into chunks if needed

## Support
Contact the data team if you encounter issues or need help with data formatting.
