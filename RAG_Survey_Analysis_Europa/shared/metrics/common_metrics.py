#!/usr/bin/env python3
"""
Common metrics and calculations for survey analysis.
This module provides standardized functions for calculating common survey metrics.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional

def calculate_nps(scores: List[int]) -> Dict[str, float]:
    """
    Calculate Net Promoter Score from a list of scores (0-10).
    
    Args:
        scores: List of NPS scores (0-10)
    
    Returns:
        Dictionary with NPS score and breakdown
    """
    scores = [s for s in scores if pd.notna(s) and 0 <= s <= 10]
    
    if not scores:
        return {'nps_score': 0, 'promoters': 0, 'passives': 0, 'detractors': 0}
    
    promoters = len([s for s in scores if s >= 9])
    passives = len([s for s in scores if 7 <= s <= 8])
    detractors = len([s for s in scores if s <= 6])
    total = len(scores)
    
    nps_score = ((promoters - detractors) / total) * 100
    
    return {
        'nps_score': round(nps_score, 2),
        'promoters': round((promoters / total) * 100, 2),
        'passives': round((passives / total) * 100, 2),
        'detractors': round((detractors / total) * 100, 2),
        'total_responses': total
    }

def calculate_satisfaction_metrics(ratings: List[int], scale_max: int = 5) -> Dict[str, float]:
    """
    Calculate satisfaction metrics from rating data.
    
    Args:
        ratings: List of satisfaction ratings
        scale_max: Maximum value of the rating scale (default 5)
    
    Returns:
        Dictionary with satisfaction metrics
    """
    ratings = [r for r in ratings if pd.notna(r) and 1 <= r <= scale_max]
    
    if not ratings:
        return {'mean_rating': 0, 'median_rating': 0, 'satisfaction_rate': 0}
    
    mean_rating = np.mean(ratings)
    median_rating = np.median(ratings)
    
    # Consider ratings of 4+ (on 5-point scale) as satisfied
    satisfied_threshold = scale_max - 1
    satisfied_count = len([r for r in ratings if r >= satisfied_threshold])
    satisfaction_rate = (satisfied_count / len(ratings)) * 100
    
    return {
        'mean_rating': round(mean_rating, 2),
        'median_rating': median_rating,
        'satisfaction_rate': round(satisfaction_rate, 2),
        'total_responses': len(ratings)
    }

def analyze_text_sentiment(text_responses: List[str]) -> Dict[str, any]:
    """
    Basic sentiment analysis for text responses.
    Note: This is a placeholder - implement with actual sentiment analysis library.
    
    Args:
        text_responses: List of text responses
    
    Returns:
        Dictionary with sentiment analysis results
    """
    # Placeholder implementation
    valid_responses = [t for t in text_responses if pd.notna(t) and t.strip()]
    
    return {
        'total_text_responses': len(valid_responses),
        'avg_response_length': np.mean([len(t) for t in valid_responses]) if valid_responses else 0,
        'sentiment_analysis': 'Requires implementation with sentiment analysis library'
    }

def demographic_breakdown(df: pd.DataFrame, metric_column: str, demographic_column: str) -> pd.DataFrame:
    """
    Break down a metric by demographic segments.
    
    Args:
        df: DataFrame containing the data
        metric_column: Column name for the metric to analyze
        demographic_column: Column name for demographic segmentation
    
    Returns:
        DataFrame with metric breakdown by demographic
    """
    return df.groupby(demographic_column)[metric_column].agg([
        'count', 'mean', 'median', 'std'
    ]).round(2)
