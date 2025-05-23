"""
Survey Transformations Module

Simple dictionary-based transformation system for survey data.
"""

from .simple_mapper import SimpleSurveyMapper, quick_transform

__all__ = [
    'SimpleSurveyMapper',
    'quick_transform'
]