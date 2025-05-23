"""
Simple Dictionary Mapper for Survey Transformations

This module provides a straightforward way to apply dictionary mappings
to survey columns based on configuration files.
"""

import pandas as pd
import json
import os
from typing import Dict, List, Union, Optional


class SimpleSurveyMapper:
    """Simple mapper that applies dictionary transformations to survey data."""
    
    def __init__(self, 
                 mappings_file: str = None, 
                 column_config_file: str = None):
        """
        Initialize the mapper with configuration files.
        
        Args:
            mappings_file: Path to mapping dictionaries JSON file
            column_config_file: Path to survey column mappings JSON file
        """
        # Set default paths if not provided
        if mappings_file is None:
            mappings_file = os.path.join(
                os.path.dirname(__file__), 
                '../../config/mapping_dictionaries.json'
            )
        if column_config_file is None:
            column_config_file = os.path.join(
                os.path.dirname(__file__), 
                '../../config/survey_column_mappings.json'
            )
        
        self.mapping_dictionaries = self._load_mapping_dictionaries(mappings_file)
        self.survey_configs = self._load_survey_configs(column_config_file)
        self.default_mappings = self.survey_configs.get('default_mappings', {})
    
    def _load_mapping_dictionaries(self, filepath: str) -> Dict[str, Dict]:
        """Load the mapping dictionaries from JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['dictionaries']
    
    def _load_survey_configs(self, filepath: str) -> Dict:
        """Load the survey column configurations from JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_available_mappings(self) -> List[str]:
        """Get list of available mapping dictionary names."""
        return list(self.mapping_dictionaries.keys())
    
    def get_survey_mappings(self, survey_name: str) -> Dict[str, str]:
        """
        Get column mappings for a specific survey.
        
        Args:
            survey_name: Name of the survey
            
        Returns:
            Dictionary mapping column names to dictionary names
        """
        survey_data = self.survey_configs.get('surveys', {}).get(survey_name, {})
        return survey_data.get('columns', {})
    
    def apply_mapping(self, 
                     series: pd.Series, 
                     mapping_name: str,
                     case_sensitive: bool = False) -> pd.Series:
        """
        Apply a specific mapping dictionary to a pandas Series.
        
        Args:
            series: The data to transform
            mapping_name: Name of the mapping dictionary to use
            case_sensitive: Whether to match case exactly
            
        Returns:
            Transformed series with mapped values
        """
        if mapping_name not in self.mapping_dictionaries:
            print(f"Warning: Mapping '{mapping_name}' not found. Returning original series.")
            return series
        
        mapping_dict = self.mapping_dictionaries[mapping_name]
        
        if not case_sensitive:
            # Create case-insensitive mapping
            mapping_dict = {k.lower(): v for k, v in mapping_dict.items()}
            
            def map_value(val):
                if pd.isna(val):
                    return val
                return mapping_dict.get(str(val).strip().lower(), val)
            
            return series.apply(map_value)
        else:
            # Use case-sensitive mapping
            return series.map(lambda x: mapping_dict.get(str(x).strip(), x) if pd.notna(x) else x)
    
    def transform_survey(self, 
                        df: pd.DataFrame, 
                        survey_name: str,
                        include_defaults: bool = True,
                        verbose: bool = True) -> pd.DataFrame:
        """
        Transform all configured columns in a survey DataFrame.
        
        Args:
            df: Survey data DataFrame
            survey_name: Name of the survey
            include_defaults: Whether to apply default mappings
            verbose: Whether to print progress
            
        Returns:
            DataFrame with transformed columns
        """
        # Create a copy to avoid modifying original
        result_df = df.copy()
        
        # Get survey-specific mappings
        column_mappings = self.get_survey_mappings(survey_name)
        
        # Add default mappings if requested
        if include_defaults:
            for col, mapping in self.default_mappings.items():
                if col in result_df.columns and col not in column_mappings:
                    column_mappings[col] = mapping
        
        if verbose:
            print(f"\nTransforming survey: {survey_name}")
            print(f"Columns to transform: {len(column_mappings)}")
        
        # Apply transformations
        transformed_count = 0
        for column_name, mapping_name in column_mappings.items():
            if column_name in result_df.columns:
                if verbose:
                    print(f"  Applying '{mapping_name}' to column '{column_name}'")
                
                result_df[column_name] = self.apply_mapping(
                    result_df[column_name], 
                    mapping_name
                )
                transformed_count += 1
            else:
                if verbose:
                    print(f"  Warning: Column '{column_name}' not found in data")
        
        if verbose:
            print(f"Transformed {transformed_count} columns successfully")
        
        return result_df
    
    def get_mapping_summary(self, survey_name: str) -> Dict[str, List[str]]:
        """
        Get a summary of mappings for a survey showing the actual mappings.
        
        Args:
            survey_name: Name of the survey
            
        Returns:
            Dictionary with column names and their mapping examples
        """
        column_mappings = self.get_survey_mappings(survey_name)
        summary = {}
        
        for column, mapping_name in column_mappings.items():
            if mapping_name in self.mapping_dictionaries:
                mapping_dict = self.mapping_dictionaries[mapping_name]
                # Show first 3 mappings as examples
                examples = list(mapping_dict.items())[:3]
                summary[column] = {
                    'mapping_type': mapping_name,
                    'examples': examples,
                    'total_mappings': len(mapping_dict)
                }
        
        return summary
    
    def validate_survey_config(self, survey_name: str, df: pd.DataFrame) -> Dict[str, List[str]]:
        """
        Validate that configured columns exist in the DataFrame.
        
        Args:
            survey_name: Name of the survey
            df: DataFrame to validate against
            
        Returns:
            Dictionary with 'missing' and 'extra' column lists
        """
        configured_columns = set(self.get_survey_mappings(survey_name).keys())
        actual_columns = set(df.columns)
        
        # Exclude system columns
        system_columns = {'Survey_Name', 'Processed_Date', 'ResponseID', 'Timestamp'}
        actual_columns = actual_columns - system_columns
        
        return {
            'missing': list(configured_columns - actual_columns),
            'extra': list(actual_columns - configured_columns),
            'configured': list(configured_columns),
            'actual': list(actual_columns)
        }


def quick_transform(df: pd.DataFrame, 
                   survey_name: str, 
                   mappings_file: str = None,
                   column_config_file: str = None) -> pd.DataFrame:
    """
    Quick function to transform a survey DataFrame.
    
    Args:
        df: Survey data
        survey_name: Name of the survey
        mappings_file: Optional path to mappings file
        column_config_file: Optional path to column config file
        
    Returns:
        Transformed DataFrame
    """
    mapper = SimpleSurveyMapper(mappings_file, column_config_file)
    return mapper.transform_survey(df, survey_name)