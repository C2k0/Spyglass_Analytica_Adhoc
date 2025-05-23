# Survey 1 - Developer Notes

## Overview
[Brief description of survey purpose and goals]

## Data Source
- **Database**: [database name]
- **Main Table**: [primary table name]
- **Join Tables**: [list any joined tables]

## Column Mappings

| SQL Column | Description | Transformation |
|------------|-------------|----------------|
| ResponseID | Unique response identifier | None |
| Timestamp | Response submission time | None |
| Custom_Metric_1 | [Description] | `satisfaction_5_scale` |
| Custom_Metric_2 | [Description] | `agreement_5_scale` |
| Custom_Metric_3 | [Description] | `quality_5_scale` |
| Custom_Metric_4 | [Description] | `yes_no_binary` |
| Custom_Metric_5 | [Description] | `frequency_5_scale` |

## SQL Logic
- **Date Range**: [Specify date filters]
- **Filters**: [List any WHERE conditions]
- **Exclusions**: [Note any excluded records]
- **Special Logic**: [Describe any complex joins or calculations]

## Data Quality Notes
- [Expected record count]
- [Known data issues]
- [Validation rules]

## Change History
- [Date] - [Developer] - Initial query creation
- [Date] - [Developer] - [Changes made]