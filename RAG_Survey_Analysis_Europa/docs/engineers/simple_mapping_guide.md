# Simple Dictionary Mapping Guide

## Overview

The RAG Survey Analysis system uses a simple dictionary-based approach to transform text survey responses into numeric values. This is managed through two JSON configuration files:

1. **Mapping Dictionaries** (`config/mapping_dictionaries.json`) - Contains 15 pre-defined dictionaries
2. **Survey Column Mappings** (`config/survey_column_mappings.json`) - Specifies which columns use which dictionaries

## How It Works

### Step 1: Define Dictionaries
The system includes 15 standard mapping dictionaries for common survey response types:

```json
"satisfaction_5_scale": {
  "very dissatisfied": 1,
  "dissatisfied": 2,
  "neutral": 3,
  "satisfied": 4,
  "very satisfied": 5
}
```

### Step 2: Configure Survey Mappings
For each survey, specify which columns need which dictionary:

```json
"Customer_Satisfaction_Q1": {
  "columns": {
    "Satisfaction_Level": "satisfaction_5_scale",
    "Product_Quality": "quality_5_scale",
    "Will_Purchase_Again": "likelihood_5_scale"
  }
}
```

### Step 3: Process Automatically
The notebook automatically applies the configured mappings when processing each survey.

## Available Dictionaries

| Dictionary Name | Description | Example Mapping |
|----------------|-------------|-----------------|
| `satisfaction_5_scale` | Satisfaction levels | "very satisfied" → 5 |
| `agreement_5_scale` | Agreement levels | "strongly agree" → 5 |
| `frequency_5_scale` | Frequency of occurrence | "always" → 5 |
| `quality_5_scale` | Quality ratings | "excellent" → 5 |
| `yes_no_binary` | Yes/No responses | "yes" → 1, "no" → 0 |
| `true_false_binary` | True/False responses | "true" → 1, "false" → 0 |
| `importance_5_scale` | Importance levels | "extremely important" → 5 |
| `likelihood_5_scale` | Likelihood ratings | "very likely" → 5 |
| `difficulty_5_scale` | Difficulty levels | "very easy" → 5 |
| `performance_5_scale` | Performance ratings | "far above expectations" → 5 |
| `recommendation_10_scale` | NPS scores | "10" → 10 |
| `priority_3_scale` | Priority levels | "high" → 3 |
| `size_5_scale` | Size perception | "just right" → 3 |
| `change_5_scale` | Change perception | "much better" → 5 |
| `awareness_4_scale` | Awareness levels | "extremely aware" → 4 |

## Quick Start

### 1. Check Current Configuration
View configured mappings for a survey:
```python
mapper = SimpleSurveyMapper()
mappings = mapper.get_survey_mappings("Your_Survey_Name")
print(mappings)

# Get list of all available mapping dictionaries
available = mapper.get_available_mappings()
print(f"Available dictionaries: {available}")

# Get detailed mapping summary with examples
summary = mapper.get_mapping_summary("Your_Survey_Name")
for column, info in summary.items():
    print(f"{column}: {info['mapping_type']} - {info['examples']}")
```

### 2. Add New Survey
Edit `config/survey_column_mappings.json`:
```json
"Your_New_Survey": {
  "columns": {
    "Q1_Satisfaction": "satisfaction_5_scale",
    "Q2_Recommend": "yes_no_binary",
    "Q3_Quality": "quality_5_scale"
  }
}
```

### 3. Add Custom Dictionary
Edit `config/mapping_dictionaries.json`:
```json
"custom_scale": {
  "option_1": 1,
  "option_2": 2,
  "option_3": 3
}
```

### 4. Process Survey
```python
# Using the notebook pipeline
df = execute_query_and_load_data("Your_Survey_Name")
df = mapper.transform_survey(df, "Your_Survey_Name")

# Or use quick transform
transformed_df = quick_transform(df, "Your_Survey_Name")

# Advanced options
df = mapper.transform_survey(
    df, 
    "Your_Survey_Name",
    include_defaults=True,  # Apply default mappings (default: True)
    verbose=False          # Suppress progress messages (default: True)
)

# Use custom configuration files
custom_mapper = SimpleSurveyMapper(
    mappings_file="path/to/custom_mappings.json",
    column_config_file="path/to/custom_config.json"
)
```

## Default Mappings

The system supports default mappings that are automatically applied to common column names across all surveys. These are defined in the `default_mappings` section of `survey_column_mappings.json`:

```json
"default_mappings": {
  "NPS_Score": "recommendation_10_scale",
  "Satisfaction_Rating": "satisfaction_5_scale",
  "Yes_No_Question": "yes_no_binary"
}
```

Default mappings are applied when:
- The column exists in the survey data
- The column is not already configured in the survey-specific mappings
- `include_defaults=True` (default behavior)

## Best Practices

1. **Case Insensitive**: The mapper is case-insensitive by default
2. **Handles Variations**: Include common variations (e.g., "yes", "y")
3. **Preserve Original**: Original values are kept if no mapping found
4. **Missing Values**: NaN/null values are preserved
5. **Whitespace Handling**: Leading/trailing spaces are automatically trimmed

## Validation

The system provides validation to ensure mappings work correctly:

```python
# Check which columns are missing/extra
validation = mapper.validate_survey_config("Survey_Name", df)
print(f"Missing columns: {validation['missing']}")
print(f"Extra columns: {validation['extra']}")
```

## Examples

### Example 1: Simple Survey
```json
"survey_6": {
  "columns": {
    "Overall_Satisfaction": "satisfaction_5_scale",
    "Would_Recommend": "yes_no_binary",
    "Service_Quality": "quality_5_scale"
  }
}
```

### Example 2: Mixed Types
```json
"survey_7": {
  "columns": {
    "Rating_Score": "recommendation_10_scale",
    "Ease_of_Use": "difficulty_5_scale",
    "Purchase_Intent": "likelihood_5_scale",
    "Issue_Priority": "priority_3_scale"
  }
}
```

## Troubleshooting

**Issue**: Column not transformed
- Check column name matches exactly in config
- Verify dictionary name is spelled correctly
- Look for typos in the mapping configuration

**Issue**: Wrong values after transformation
- Check the dictionary definition
- Verify text values match (case-insensitive)
- Look for extra spaces in responses

**Issue**: Survey not configured
- Add survey to `survey_column_mappings.json`
- Ensure survey name matches exactly