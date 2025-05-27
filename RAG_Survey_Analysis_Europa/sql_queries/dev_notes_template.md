# [Survey Name] - Developer Notes

## Overview
[Brief description of survey purpose and goals]

## Data Source
- **Database**: [database name]
- **Main Table**: [primary table name]
- **Join Tables**: [list any joined tables]

## Required Fields

All queries must include these mandatory fields:

| SQL Column | Description | Format | Transformation |
|------------|-------------|--------|----------------|
| YRMO | Survey period date | YYMM (e.g., 2401) | None |
| LTR | Satisfaction score | Numerical | None |
| ResponseID | Unique response identifier | String/Integer | None |
| Timestamp | Response submission time | Datetime | None |

## Additional Column Mappings

| SQL Column | Description | Transformation |
|------------|-------------|----------------|
| [Column_Name] | [Description] | [dictionary_name or None] |

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