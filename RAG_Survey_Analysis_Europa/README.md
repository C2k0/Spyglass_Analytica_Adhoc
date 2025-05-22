# RAG Survey Analysis Europa

A structured system for analyzing survey data using RAG (Retrieval-Augmented Generation) with AI/ChatGPT integration and SharePoint data access.

## 🏗️ Project Structure

```
RAG_Survey_Analysis_Europa/
├── config/                     # AI and system configuration
│   ├── ai_prompts/            # Structured prompts for AI analysis
│   ├── schemas/               # Data validation schemas
│   └── rag_config.json        # RAG system configuration
├── data/                      # Data storage and processing
│   ├── templates/             # Empty data templates
│   ├── processed/             # Cleaned/processed survey data
│   └── raw/                   # Original survey files
├── docs/                      # Documentation
│   ├── engineers/             # 👨‍💻 FOR ENGINEERS: Data prep guides
│   └── ai_reference/          # 🤖 FOR AI: Analysis instructions
├── surveys/                   # Individual survey projects
│   ├── survey_1/              # Template survey folder
│   ├── survey_2/              # Template survey folder
│   ├── survey_3/              # Template survey folder
│   ├── survey_4/              # Template survey folder
│   └── survey_5/              # Template survey folder
├── shared/                    # Common utilities and functions
│   ├── metrics/               # Common survey metric calculations
│   └── utils/                 # Data validation and processing tools
└── notebooks/                 # Jupyter notebooks for analysis
```

## 📚 Key Documents

### 👨‍💻 For Engineers (Data Producers)
- **[Data Ingestion Guide](docs/engineers/DATA_INGESTION_GUIDE.md)** - How to prepare and upload survey data
- **[Data Validator](shared/utils/data_validator.py)** - Script to validate CSV files before upload
- **[Common Schema](config/schemas/common_schema.json)** - Required and optional field definitions
- **[Survey Data Processor](notebooks/survey_data_processor.ipynb)** - Jupyter notebook for processing SQL queries

### 🤖 For AI Tools (Data Interpreters)
- **[AI Analysis Guide](docs/ai_reference/AI_ANALYSIS_GUIDE.md)** - Instructions for analyzing survey data
- **[Analysis Prompts](config/ai_prompts/survey_analysis_prompts.json)** - Standardized prompts for different analysis types
- **[RAG Configuration](config/rag_config.json)** - System settings and integration parameters
- **[ChatGPT Setup Instructions](CHATGPT_SETUP_INSTRUCTIONS.md)** - Complete setup guide for ChatGPT integration

## 🚀 Quick Start

### For Engineers Adding New Survey Data:

1. **For a New Survey (e.g., Survey 6)**:
   ```bash
   # Copy template directory
   cp -r surveys/survey_1/ surveys/survey_6/
   # Rename template file
   mv surveys/survey_6/survey_1_template.csv surveys/survey_6/survey_6_template.csv
   ```

2. **Prepare your CSV file** following the template structure
3. **Update metadata**: Edit `surveys/survey_6/survey_metadata.json` with survey details
4. **Validate your data**:
   ```bash
   python shared/utils/data_validator.py surveys/survey_6/your_survey_data.csv
   ```
5. **Test with a sample analysis**

### For AI Systems:

1. **Read the AI Analysis Guide** for field definitions and analysis standards
2. **Use the common metrics functions** from `shared/metrics/common_metrics.py`
3. **Apply standard prompts** from `config/ai_prompts/`
4. **Follow the analysis guidelines** for consistent reporting

## 📊 Supported Survey Metrics

### Column Types (ALL_COLUMNS Dictionary)
- **STANDARD**: Required identification fields (ResponseID, Timestamp)
- **LTR**: Likelihood to Recommend/NPS data (NPS_Score, NPS_Comment)
- **DRIVERS**: Driver/satisfaction scores (Satisfaction_Rating, Custom_Metric_1-5)
- **METADATA**: Demographics and comments (Demographics_Age, Free_Text_Feedback)

### Standard Metrics (Common Across Surveys)
- **LTR/NPS (Likelihood to Recommend)**: 0-10 scale with promoter/passive/detractor analysis
- **Satisfaction Rating**: 1-5 scale with satisfaction rate calculations
- **Demographics**: Age ranges and role-based segmentation
- **Text Analysis**: Sentiment analysis and theme extraction

### Custom Metrics
- Survey-specific questions and scales (Custom_Metric_1-5)
- Documented in each survey's metadata file
- Flexible field definitions for unique survey needs

## 🔧 Areas Requiring Updates

When setting up a new survey, update these files:

1. **Survey Metadata** (`surveys/survey_X/survey_metadata.json`):
   - Survey description and purpose
   - Custom field definitions
   - Analysis objectives

2. **Custom Field Documentation** (survey-specific):
   - What each Custom_Metric_X represents
   - Scale and interpretation guidelines

3. **RAG Configuration** (`config/rag_config.json`):
   - SharePoint folder paths
   - Analysis type preferences
   - Output format settings

## 🔗 Integration Points

- **SharePoint**: Automated data sync from SharePoint folders with file monitoring
- **ChatGPT/AI APIs**: Structured prompts and analysis workflows with custom GPT configuration
- **SQL Processing**: Automated processing of SQL query files into standardized CSV formats
- **Column Validation**: ALL_COLUMNS dictionary ensures data consistency across surveys
- **Validation Pipeline**: Automated data quality checks and error reporting

## 🛡️ Data Quality

- Automated validation of required fields
- Range checking for numeric scales
- Duplicate detection
- Missing value analysis
- Data consistency checks

## 📝 Notes

- Each survey folder contains a template CSV and metadata JSON
- All surveys use column type system (STANDARD, LTR, DRIVERS, METADATA)
- SQL query processing via Jupyter notebook with automated column validation
- AI analysis is standardized but customizable per survey type
- ChatGPT integration with SharePoint monitoring for automated workflows
- Data validation ensures quality before analysis

---

**Need Help?** 
- Engineers: See `docs/engineers/DATA_INGESTION_GUIDE.md`
- AI Integration: See `docs/ai_reference/AI_ANALYSIS_GUIDE.md`
- ChatGPT Setup: See `CHATGPT_SETUP_INSTRUCTIONS.md`
