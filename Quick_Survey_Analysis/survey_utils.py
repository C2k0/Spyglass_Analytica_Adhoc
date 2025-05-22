"""
Utility functions and data structures for survey analysis.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Union, Optional, Callable, Any, Tuple


# Response mapping dictionaries
SATISFACTION_MAP = {
    "very dissatisfied": 1,
    "dissatisfied": 2,
    "neutral": 3,
    "satisfied": 4,
    "very satisfied": 5
}

AGREEMENT_MAP = {
    "strongly disagree": 1,
    "disagree": 2,
    "neither agree nor disagree": 3,
    "agree": 4,
    "strongly agree": 5
}

FREQUENCY_MAP = {
    "never": 1,
    "rarely": 2,
    "sometimes": 3,
    "often": 4,
    "always": 5
}

LIKELIHOOD_MAP = {
    "very unlikely": 1,
    "unlikely": 2,
    "neutral": 3,
    "likely": 4,
    "very likely": 5
}

# Template functions for survey analysis

def map_responses(df: pd.DataFrame, column: str, mapping: Dict[str, int]) -> pd.Series:
    """
    Map text responses to numerical values based on provided dictionary.
    
    Args:
        df: DataFrame containing survey data
        column: Column name with text responses
        mapping: Dictionary mapping text responses to numerical values
        
    Returns:
        Series with mapped numerical values
    """
    return df[column].str.lower().map(mapping)


def calculate_response_stats(df: pd.DataFrame, column: str) -> Dict[str, float]:
    """
    Calculate basic statistics for a response column.
    
    Args:
        df: DataFrame containing survey data
        column: Column name to analyze
        
    Returns:
        Dictionary with statistics (mean, median, std, etc.)
    """
    stats = {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "std": df[column].std(),
        "min": df[column].min(),
        "max": df[column].max()
    }
    return stats


def plot_response_distribution(df: pd.DataFrame, column: str, title: Optional[str] = None) -> None:
    """
    Create a histogram or bar chart of response distribution.
    
    Args:
        df: DataFrame containing survey data
        column: Column name to visualize
        title: Optional plot title
    """
    plt.figure(figsize=(10, 6))
    
    if df[column].dtype in ['int64', 'float64']:
        # For numerical data
        sns.histplot(df[column], kde=True)
    else:
        # For categorical data
        value_counts = df[column].value_counts().sort_index()
        sns.barplot(x=value_counts.index, y=value_counts.values)
        plt.xticks(rotation=45)
    
    plt.title(title or f'Distribution of {column}')
    plt.tight_layout()
    plt.show()


def correlation_matrix(df: pd.DataFrame, columns: List[str], method: str = 'pearson') -> pd.DataFrame:
    """
    Calculate correlation matrix for selected survey questions.
    
    Args:
        df: DataFrame containing survey data
        columns: List of columns to include in correlation analysis
        method: Correlation method ('pearson', 'spearman', or 'kendall')
        
    Returns:
        Correlation matrix as DataFrame
    """
    return df[columns].corr(method=method)


def plot_correlation_heatmap(corr_matrix: pd.DataFrame, title: Optional[str] = None) -> None:
    """
    Plot a heatmap of the correlation matrix.
    
    Args:
        corr_matrix: Correlation matrix DataFrame
        title: Optional plot title
    """
    plt.figure(figsize=(10, 8))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    sns.heatmap(
        corr_matrix, 
        mask=mask,
        cmap="coolwarm",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        vmin=-1, 
        vmax=1
    )
    
    plt.title(title or 'Correlation Matrix')
    plt.tight_layout()
    plt.show()


def segment_analysis(df: pd.DataFrame, 
                    segment_col: str, 
                    analysis_col: str,
                    stat_func: Callable = np.mean) -> pd.Series:
    """
    Analyze responses by demographic or other segments.
    
    Args:
        df: DataFrame containing survey data
        segment_col: Column to segment by (e.g., 'age_group', 'gender')
        analysis_col: Column to analyze
        stat_func: Statistical function to apply (default: mean)
        
    Returns:
        Series with results per segment
    """
    return df.groupby(segment_col)[analysis_col].apply(stat_func).sort_values(ascending=False)


def response_cross_tabulation(df: pd.DataFrame, 
                             row_col: str, 
                             col_col: str, 
                             normalize: Optional[str] = None) -> pd.DataFrame:
    """
    Create a cross-tabulation of two survey questions.
    
    Args:
        df: DataFrame containing survey data
        row_col: Column for row dimension
        col_col: Column for column dimension
        normalize: Optional normalization ('index', 'columns', or 'all')
        
    Returns:
        Cross-tabulation DataFrame
    """
    return pd.crosstab(df[row_col], df[col_col], normalize=normalize)


def prepare_likert_data(df: pd.DataFrame, 
                       questions: List[str], 
                       mapping: Dict[str, int],
                       question_text_map: Optional[Dict[str, str]] = None) -> pd.DataFrame:
    """
    Prepare data for Likert scale analysis.
    
    Args:
        df: DataFrame containing survey data
        questions: List of column names with Likert responses
        mapping: Dictionary mapping text responses to numerical values
        question_text_map: Optional mapping of column names to readable question text
        
    Returns:
        DataFrame with numeric responses
    """
    result_df = pd.DataFrame()
    
    for q in questions:
        result_df[q] = map_responses(df, q, mapping)
    
    if question_text_map:
        result_df = result_df.rename(columns=question_text_map)
        
    return result_df


def free_text_word_count(df: pd.DataFrame, text_column: str, min_count: int = 1) -> pd.Series:
    """
    Analyze word frequency in free text responses.
    
    Args:
        df: DataFrame containing survey data
        text_column: Column with free text responses
        min_count: Minimum count to include in results
        
    Returns:
        Series with word counts
    """
    # Combine all text, lowercase, and split words
    all_words = ' '.join(df[text_column].dropna()).lower().split()
    
    # Count words
    word_counts = pd.Series(all_words).value_counts()
    
    # Filter by minimum count
    return word_counts[word_counts >= min_count]


def apply_mapping_if_exists(df: pd.DataFrame, column: str, mapping: Dict[str, int]) -> Optional[pd.Series]:
    """
    Apply a mapping to a column if it exists in the dataframe.
    
    Args:
        df: DataFrame containing survey data
        column: Column name with text responses
        mapping: Dictionary mapping text responses to numerical values
        
    Returns:
        Series with mapped numerical values or None if column doesn't exist
    """
    if column in df.columns:
        return map_responses(df, column, mapping)
    return None


def setup_snowflake_data(snowflake_config: Dict[str, Any], 
                         sql_file_path: str, 
                         sql_params: Dict[str, Any] = None) -> Any:
    """
    Connect to Snowflake and set up temp tables defined in the SQL file.
    
    Args:
        snowflake_config: Snowflake connection configuration dictionary
        sql_file_path: Path to SQL file with table creation statements
        sql_params: Optional parameters for SQL query substitution
        
    Returns:
        Snowflake connection object or None if connection fails
    """
    try:
        # Import here to avoid circular imports
        from snowflake_config import connect_to_snowflake, execute_sql_file
        
        # Connect to Snowflake
        conn = connect_to_snowflake(snowflake_config)
        if not conn:
            print("Failed to connect to Snowflake.")
            return None
        
        # Execute the SQL statements to create temp tables
        success = execute_sql_file(conn, sql_file_path, sql_params)
        
        if not success:
            print("WARNING: Failed to create one or more temporary tables in Snowflake.")
        
        return conn
    
    except Exception as e:
        print(f"Error setting up Snowflake data: {e}")
        return None


def execute_query(conn: Any, query: str, params: Dict[str, Any] = None) -> Optional[pd.DataFrame]:
    """
    Execute a custom SQL query with optional parameter substitution.
    
    Args:
        conn: Snowflake connection object
        query: SQL query string
        params: Optional parameters for SQL query substitution
        
    Returns:
        DataFrame with query results or None if query fails
    """
    if not conn:
        print("No connection available.")
        return None
    
    try:
        cursor = conn.cursor()
        
        # Format query with parameters if provided
        if params:
            formatted_query = query.format(**params)
        else:
            formatted_query = query
        
        # Execute the query
        cursor.execute(formatted_query)
        
        # Convert to DataFrame
        result_df = pd.DataFrame.from_records(
            cursor.fetchall(),
            columns=[desc[0] for desc in cursor.description]
        )
        
        return result_df
    
    except Exception as e:
        print(f"Error executing query: {e}")
        return None


def generate_data_summary(df: pd.DataFrame, max_unique_values: int = 5) -> pd.DataFrame:
    """
    Generate a comprehensive summary of a dataframe.
    
    Args:
        df: DataFrame to analyze
        max_unique_values: Maximum number of unique values to display
        
    Returns:
        DataFrame with summary information for each column
    """
    if df is None or df.empty:
        print("No data available for summary.")
        return pd.DataFrame()
    
    # Initialize summary dataframe
    summary_data = []
    
    # Analyze each column
    for col in df.columns:
        # Get basic info
        dtype = str(df[col].dtype)
        non_null_count = df[col].count()
        total_count = len(df)
        fill_rate = non_null_count / total_count * 100 if total_count > 0 else 0
        
        # Get unique values
        if df[col].dtype == 'object' or df[col].dtype == 'string':
            # For string/object columns
            unique_values = df[col].dropna().unique()
            unique_count = len(unique_values)
            
            # Format unique values as string
            if unique_count > max_unique_values:
                unique_values = unique_values[:max_unique_values]
                values_str = ', '.join([str(val) for val in unique_values]) + ', etc.'
            else:
                values_str = ', '.join([str(val) for val in unique_values])
        else:
            # For numeric columns
            unique_count = df[col].nunique()
            
            # Get min, max, and sample values
            if pd.api.types.is_numeric_dtype(df[col]):
                min_val = df[col].min() if not df[col].empty else None
                max_val = df[col].max() if not df[col].empty else None
                values_str = f"Min: {min_val}, Max: {max_val}"
                
                # Add some sample values if there are not too many
                if unique_count <= max_unique_values:
                    sample_values = sorted(df[col].dropna().unique())
                    values_str = ', '.join([str(val) for val in sample_values])
                elif unique_count > max_unique_values:
                    sample_values = sorted(df[col].dropna().unique())[:max_unique_values]
                    values_str = ', '.join([str(val) for val in sample_values]) + ', etc.'
            else:
                # For other types (dates, etc.)
                values_str = "Non-string, non-numeric data type"
        
        # Add row to summary data
        summary_data.append({
            'Column': col,
            'Data Type': dtype,
            'Fill Rate (%)': round(fill_rate, 2),
            'Non-Null Count': non_null_count,
            'Total Count': total_count,
            'Unique Count': unique_count,
            'Sample Values': values_str
        })
    
    # Create summary dataframe
    summary_df = pd.DataFrame(summary_data)
    
    # Sort by column name
    summary_df = summary_df.sort_values('Column').reset_index(drop=True)
    
    return summary_df


def export_data_summary(df: pd.DataFrame, output_path: str, format: str = 'csv') -> None:
    """
    Export data summary to a file.
    
    Args:
        df: DataFrame with summary information
        output_path: Path to save the output file
        format: Export format ('csv', 'excel', or 'html')
    """
    if df is None or df.empty:
        print("No summary data to export.")
        return
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Export based on format
        if format.lower() == 'csv':
            df.to_csv(output_path, index=False)
            print(f"Summary exported to CSV: {output_path}")
        
        elif format.lower() == 'excel':
            df.to_excel(output_path, index=False)
            print(f"Summary exported to Excel: {output_path}")
        
        elif format.lower() == 'html':
            df.to_html(output_path, index=False)
            print(f"Summary exported to HTML: {output_path}")
        
        else:
            print(f"Unsupported export format: {format}")
            
    except Exception as e:
        print(f"Error exporting data summary: {e}")