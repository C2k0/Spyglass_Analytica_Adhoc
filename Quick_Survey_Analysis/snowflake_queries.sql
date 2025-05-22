-- Snowflake SQL Queries for Survey Analysis
-- These queries create temporary tables for analysis in the notebook

-- Create temporary table for survey responses
CREATE OR REPLACE TEMPORARY TABLE SURVEY_RESPONSES AS
SELECT 
    response_id,
    respondent_id,
    question_id,
    response_text,
    response_value,
    response_timestamp,
    survey_id
FROM 
    RAW_SURVEY_DATA.RESPONSES
WHERE 
    survey_id = '{survey_id}'
    AND response_timestamp BETWEEN '{start_date}' AND '{end_date}';

-- Create temporary table for respondent demographics
CREATE OR REPLACE TEMPORARY TABLE RESPONDENT_DEMOGRAPHICS AS
SELECT 
    r.respondent_id,
    r.age_group,
    r.gender,
    r.education,
    r.income_bracket,
    r.location,
    r.customer_since
FROM 
    RAW_SURVEY_DATA.RESPONDENTS r
JOIN 
    SURVEY_RESPONSES sr ON r.respondent_id = sr.respondent_id
GROUP BY 
    1, 2, 3, 4, 5, 6, 7;

-- Create temporary table for question metadata
CREATE OR REPLACE TEMPORARY TABLE QUESTION_METADATA AS
SELECT 
    q.question_id,
    q.question_text,
    q.question_type,
    q.question_category,
    q.response_type
FROM 
    RAW_SURVEY_DATA.QUESTIONS q
JOIN 
    SURVEY_RESPONSES sr ON q.question_id = sr.question_id
GROUP BY 
    1, 2, 3, 4, 5;

-- Create aggregated responses by demographic segments
CREATE OR REPLACE TEMPORARY TABLE SEGMENT_ANALYSIS AS
SELECT 
    rd.age_group,
    rd.gender,
    rd.education,
    rd.income_bracket,
    rd.location,
    qm.question_category,
    AVG(sr.response_value) as avg_response,
    STDDEV(sr.response_value) as stddev_response,
    COUNT(DISTINCT sr.respondent_id) as respondent_count
FROM 
    SURVEY_RESPONSES sr
JOIN 
    RESPONDENT_DEMOGRAPHICS rd ON sr.respondent_id = rd.respondent_id
JOIN 
    QUESTION_METADATA qm ON sr.question_id = qm.question_id
WHERE 
    sr.response_value IS NOT NULL
GROUP BY 
    1, 2, 3, 4, 5, 6;