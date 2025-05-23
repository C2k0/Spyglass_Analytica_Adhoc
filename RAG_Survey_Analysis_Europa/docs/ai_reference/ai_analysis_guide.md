# AI Analysis Reference Guide

## Overview
This document provides context and instructions for AI systems analyzing survey data in this repository.

## Data Access
Processed survey data is available in `rag_outputs/current/`:
- **combined_ltr_drivers.csv** - NPS scores and driver metrics across all surveys
- **combined_all_surveys.csv** - Complete dataset with all survey responses
- **processing_summary.csv** - Metadata about data freshness and processing status

Always check the processing_summary.csv first to understand data recency and any processing issues.

## Data Structure

### Common Fields Across All Surveys
- **ResponseID**: Unique identifier - use for response counting and deduplication
- **Timestamp**: Response date/time - use for trend analysis over time
- **NPS_Score**: Net Promoter Score (0-10) - calculate NPS using standard formula
- **NPS_Comment**: Text feedback for NPS - analyze sentiment and themes
- **Satisfaction_Rating**: 1-5 scale - calculate satisfaction metrics
- **Satisfaction_Comment**: Text feedback - identify satisfaction drivers
- **Demographics_Age**: Age ranges - use for segmentation analysis
- **Demographics_Role**: Job roles - use for role-based insights
- **Free_Text_Feedback**: General feedback - perform comprehensive text analysis

### Custom Fields
- **Custom_Metric_1/2**: Survey-specific metrics - refer to survey metadata for interpretation
- Check each survey's metadata file for custom field definitions

## Analysis Guidelines

### 1. NPS Analysis
- **Promoters**: Scores 9-10
- **Passives**: Scores 7-8  
- **Detractors**: Scores 0-6
- **NPS Formula**: ((Promoters - Detractors) / Total Responses) × 100

### 2. Satisfaction Analysis
- **Satisfied**: Ratings 4-5 (on 1-5 scale)
- **Neutral**: Rating 3
- **Dissatisfied**: Ratings 1-2
- Calculate mean, median, and satisfaction rate

### 3. Text Analysis Priorities
1. **Sentiment Classification**: Positive, Negative, Neutral
2. **Theme Extraction**: Identify key topics and concerns
3. **Actionable Insights**: Focus on specific, implementable recommendations
4. **Correlation Analysis**: Link text sentiment to quantitative scores

### 4. Demographic Segmentation
- Always segment key metrics by available demographics
- Look for significant differences between groups
- Identify underrepresented segments

## Standard Analysis Types

### Executive Summary
- Response count and completion rate
- Key metric scores (NPS, satisfaction)
- Top 3 positive themes
- Top 3 areas for improvement
- 2-3 specific recommendations

### Detailed Analysis
- Full statistical breakdown
- Demographic segmentation
- Trend analysis (if historical data available)
- Comprehensive text analysis
- Correlation analysis between metrics

### Comparative Analysis
- Compare against benchmarks when available
- Identify significant changes from previous periods
- Highlight best and worst performing segments

## Response Guidelines

### For Business Users
- Lead with key numbers and percentages
- Use clear, non-technical language
- Focus on actionable insights
- Provide specific examples from feedback

### For Technical Users
- Include statistical significance testing
- Show confidence intervals where appropriate
- Provide data quality notes
- Include methodology notes

## Data Quality Considerations
- Note any data quality issues (missing values, outliers)
- Highlight small sample sizes that may affect reliability
- Flag potential bias in responses
- Consider response rate implications

## Available Utilities
- Use functions from `shared/metrics/common_metrics.py` for standard calculations
- Refer to `config/schemas/common_schema.json` for field definitions
- Use prompts from `config/ai_prompts/survey_analysis_prompts.json` for consistency
