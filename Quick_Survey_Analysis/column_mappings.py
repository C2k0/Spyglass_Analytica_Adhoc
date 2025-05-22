"""
Column mapping dictionaries for survey data analysis.
This file contains dictionaries used to transform and standardize survey data.
"""

# Likert scale mapping (text to numerical)
likert_scale_mapping = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5,
    "N/A": None,
    "": None
}

# Yes/No mapping
yes_no_mapping = {
    "Yes": 1,
    "No": 0,
    "Maybe": 0.5,
    "N/A": None,
    "": None
}

# Satisfaction scale mapping
satisfaction_mapping = {
    "Very Dissatisfied": 1,
    "Dissatisfied": 2,
    "Neutral": 3, 
    "Satisfied": 4,
    "Very Satisfied": 5,
    "N/A": None,
    "": None
}

# Frequency scale mapping
frequency_mapping = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Often": 4,
    "Always": 5,
    "N/A": None,
    "": None
}

# Demographic mappings
age_group_mapping = {
    "Under 18": 1,
    "18-24": 2,
    "25-34": 3,
    "35-44": 4,
    "45-54": 5,
    "55-64": 6,
    "65+": 7,
    "Prefer not to say": None,
    "": None
}

education_mapping = {
    "Less than high school": 1,
    "High school": 2,
    "Some college": 3,
    "Associate's degree": 4,
    "Bachelor's degree": 5,
    "Master's degree": 6,
    "Doctoral or professional degree": 7,
    "Prefer not to say": None,
    "": None
}

# Column groupings (for analysis purposes)
demographic_columns = [
    "age_group",
    "gender",
    "education",
    "income_bracket",
    "location"
]

satisfaction_columns = [
    "overall_satisfaction",
    "product_satisfaction",
    "service_satisfaction",
    "support_satisfaction"
]

engagement_columns = [
    "usage_frequency",
    "recommendation_likelihood",
    "feature_usage",
    "participation"
]