#!/usr/bin/env python3
"""
Data validation utilities for survey CSV files.
Use this to validate survey data before ingestion.
"""

import pandas as pd
import json
from typing import List, Dict, Tuple
from pathlib import Path

def validate_survey_csv(csv_path: str, schema_path: str = None) -> Dict[str, any]:
    """
    Validate a survey CSV file against the common schema.
    
    Args:
        csv_path: Path to the CSV file
        schema_path: Path to schema JSON (optional)
    
    Returns:
        Dictionary with validation results
    """
    results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'summary': {}
    }
    
    try:
        # Load CSV
        df = pd.read_csv(csv_path)
        results['summary']['total_rows'] = len(df)
        results['summary']['total_columns'] = len(df.columns)
        
        # Required fields check
        required_fields = ['ResponseID', 'Timestamp']
        missing_required = [field for field in required_fields if field not in df.columns]
        
        if missing_required:
            results['valid'] = False
            results['errors'].append(f"Missing required fields: {missing_required}")
        
        # Check for duplicate ResponseIDs
        if 'ResponseID' in df.columns:
            duplicates = df['ResponseID'].duplicated().sum()
            if duplicates > 0:
                results['valid'] = False
                results['errors'].append(f"Found {duplicates} duplicate ResponseIDs")
        
        # Validate NPS scores if present
        if 'NPS_Score' in df.columns:
            invalid_nps = df[(df['NPS_Score'] < 0) | (df['NPS_Score'] > 10)]['NPS_Score'].dropna()
            if len(invalid_nps) > 0:
                results['warnings'].append(f"Found {len(invalid_nps)} NPS scores outside 0-10 range")
        
        # Validate satisfaction ratings if present
        if 'Satisfaction_Rating' in df.columns:
            invalid_sat = df[(df['Satisfaction_Rating'] < 1) | (df['Satisfaction_Rating'] > 5)]['Satisfaction_Rating'].dropna()
            if len(invalid_sat) > 0:
                results['warnings'].append(f"Found {len(invalid_sat)} satisfaction ratings outside 1-5 range")
        
        # Check for empty critical fields
        critical_fields = ['ResponseID', 'Timestamp']
        for field in critical_fields:
            if field in df.columns:
                empty_count = df[field].isna().sum()
                if empty_count > 0:
                    results['valid'] = False
                    results['errors'].append(f"Field '{field}' has {empty_count} empty values")
        
        # Data quality summary
        results['summary']['response_id_unique'] = df['ResponseID'].nunique() if 'ResponseID' in df.columns else 0
        results['summary']['nps_responses'] = df['NPS_Score'].count() if 'NPS_Score' in df.columns else 0
        results['summary']['satisfaction_responses'] = df['Satisfaction_Rating'].count() if 'Satisfaction_Rating' in df.columns else 0
        results['summary']['text_responses'] = df['Free_Text_Feedback'].count() if 'Free_Text_Feedback' in df.columns else 0
        
    except Exception as e:
        results['valid'] = False
        results['errors'].append(f"Error reading CSV: {str(e)}")
    
    return results

def generate_validation_report(csv_path: str) -> str:
    """
    Generate a human-readable validation report.
    
    Args:
        csv_path: Path to the CSV file
    
    Returns:
        Formatted validation report string
    """
    results = validate_survey_csv(csv_path)
    
    report = f"\n=== SURVEY DATA VALIDATION REPORT ===\n"
    report += f"File: {csv_path}\n"
    report += f"Status: {'VALID' if results['valid'] else 'INVALID'}\n\n"
    
    # Summary
    summary = results['summary']
    report += "SUMMARY:\n"
    report += f"  Total Rows: {summary.get('total_rows', 0)}\n"
    report += f"  Total Columns: {summary.get('total_columns', 0)}\n"
    report += f"  Unique ResponseIDs: {summary.get('response_id_unique', 0)}\n"
    report += f"  NPS Responses: {summary.get('nps_responses', 0)}\n"
    report += f"  Satisfaction Responses: {summary.get('satisfaction_responses', 0)}\n"
    report += f"  Text Responses: {summary.get('text_responses', 0)}\n\n"
    
    # Errors
    if results['errors']:
        report += "ERRORS:\n"
        for error in results['errors']:
            report += f"  ❌ {error}\n"
        report += "\n"
    
    # Warnings
    if results['warnings']:
        report += "WARNINGS:\n"
        for warning in results['warnings']:
            report += f"  ⚠️  {warning}\n"
        report += "\n"
    
    if results['valid'] and not results['warnings']:
        report += "✅ All validations passed!\n"
    
    return report

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python data_validator.py <csv_file_path>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    print(generate_validation_report(csv_file))
