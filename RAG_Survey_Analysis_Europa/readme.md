# RAG Survey Analysis Europa

A structured system for analyzing survey data using RAG (Retrieval-Augmented Generation) with AI/ChatGPT integration and SharePoint data access.

## 🏗️ Project Structure

```
RAG_Survey_Analysis_Europa/
├── config/                     # AI and system configuration
│   ├── ai_prompts/            # Structured prompts for AI analysis
│   ├── schemas/               # Data validation schemas
│   ├── mapping_dictionaries.json  # 15 text-to-numeric mapping dictionaries
│   ├── survey_column_mappings.json # Survey-specific column transformations
│   └── rag_config.json        # RAG system configuration
├── sql_queries/               # SQL queries and documentation for each survey
│   ├── survey_1/              # Survey 1 folder
│   │   ├── get_data.sql       # SQL query to extract data
│   │   └── dev_notes.md       # Developer documentation
│   ├── survey_2/
│   │   ├── get_data.sql
│   │   └── dev_notes.md
│   └── [survey_3, survey_4, survey_5...]
├── rag_outputs/               # Processed data for RAG access
│   ├── current/               # Latest processed files (RAG reads here)
│   │   ├── combined_ltr_drivers.csv
│   │   ├── combined_all_surveys.csv
│   │   └── processing_summary.csv
│   └── archive/               # Historical runs with timestamps
├── data/                      # Data storage and processing
│   ├── processed/             # Legacy output location
│   └── raw/                   # Original survey files
├── docs/                      # Documentation
│   ├── engineers/             # 👨‍💻 FOR ENGINEERS: Data prep guides
│   └── ai_reference/          # 🤖 FOR AI: Analysis instructions
├── shared/                    # Common utilities and functions
│   ├── metrics/               # Common survey metric calculations
│   ├── transformations/       # Dictionary-based text-to-numeric mapper
│   └── utils/                 # Data validation and processing tools
└── notebooks/                 # Jupyter notebooks for analysis
```

## 📚 Key Documents

### 👨‍💻 For Engineers (Data Producers)
- **[Data Ingestion Guide](docs/engineers/data_ingestion_guide.md)** - How to prepare and upload survey data
- **[Simple Mapping Guide](docs/engineers/simple_mapping_guide.md)** - How to configure text-to-numeric transformations
- **[Data Validator](shared/utils/data_validator.py)** - Script to validate CSV files before upload
- **[Common Schema](config/schemas/common_schema.json)** - Required and optional field definitions
- **[Survey Data Processor](notebooks/survey_data_processor.ipynb)** - Jupyter notebook for processing SQL queries

### 🤖 For AI Tools (Data Interpreters)
- **[AI Analysis Guide](docs/ai_reference/ai_analysis_guide.md)** - Instructions for analyzing survey data
- **[Analysis Prompts](config/ai_prompts/survey_analysis_prompts.json)** - Standardized prompts for different analysis types
- **[RAG Configuration](config/rag_config.json)** - System settings and integration parameters
- **[ChatGPT Setup Instructions](chatgpt_setup_instructions.md)** - Complete setup guide for ChatGPT integration

## 🚀 Quick Start

### For Engineers Adding New Survey Data:

1. **Create Survey SQL Folder**:
   ```bash
   # Create a new survey folder in sql_queries/
   mkdir -p sql_queries/survey_6
   touch sql_queries/survey_6/get_data.sql
   touch sql_queries/survey_6/dev_notes.md
   ```
   Add your SQL query to `get_data.sql` and document it in `dev_notes.md`.

2. **Configure Text-to-Numeric Mappings**:
   - Edit `config/survey_column_mappings.json` to add your survey
   - Map columns to one of the 15 available dictionaries
   - Example:
     ```json
     "survey_6": {
       "columns": {
         "Q1_Satisfaction": "satisfaction_5_scale",
         "Q2_Recommend": "yes_no_binary"
       }
     }
     ```

3. **Run the Processing Notebook**:
   - Open `notebooks/survey_data_processor.ipynb`
   - Add your survey name to the SURVEYS list
   - Execute the notebook to process data

4. **Validate Output**:
   - Check `rag_outputs/current/` for the latest processed files
   - Review `processing_summary.csv` for success/failure status
   - Verify transformations were applied correctly
   - Historical runs are preserved in `rag_outputs/archive/`

### For AI Systems:

1. **Access processed data** from `rag_outputs/current/`:
   - `combined_ltr_drivers.csv` - NPS and driver metrics
   - `combined_all_surveys.csv` - Complete survey data
   - `processing_summary.csv` - Data freshness and quality info
2. **Read the AI Analysis Guide** for field definitions and analysis standards
3. **Use the common metrics functions** from `shared/metrics/common_metrics.py`
4. **Apply standard prompts** from `config/ai_prompts/`
5. **Follow the analysis guidelines** for consistent reporting

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

1. **Column Mappings** (`config/survey_column_mappings.json`):
   - Add your survey name
   - Map text columns to appropriate dictionaries
   - Uses one of 15 pre-defined mappings (satisfaction, yes/no, etc.)

2. **SQL Query Files** (`sql_queries/survey_X/get_data.sql`):
   - Write SQL to extract survey data
   - Ensure column names match expected format
   - Apply any necessary filters or joins

3. **Developer Notes** (`sql_queries/survey_X/dev_notes.md`):
   - Document SQL logic and table sources
   - Explain what each column represents
   - Note any special considerations
   - Include column-to-transformation mappings

4. **RAG Configuration** (`config/rag_config.json`):
   - SharePoint folder paths
   - Analysis type preferences
   - Output format settings

## 🔗 Integration Points

- **SharePoint**: Automated data sync from SharePoint folders with file monitoring
- **ChatGPT/AI APIs**: Structured prompts and analysis workflows with custom GPT configuration
- **SQL Processing**: Automated processing of SQL query files into standardized CSV formats
- **RAG Data Access**: Processed files in `rag_outputs/current/` for AI analysis
- **Text-to-Numeric Transformation**: 15 pre-configured mapping dictionaries for consistent data conversion
- **Column Validation**: ALL_COLUMNS dictionary ensures data consistency across surveys
- **Validation Pipeline**: Automated data quality checks and error reporting

## 🛡️ Data Quality

- Automated validation of required fields
- Range checking for numeric scales
- Duplicate detection
- Missing value analysis
- Data consistency checks

## 📝 Notes

- Each survey has a folder in `sql_queries/` containing SQL query and documentation
- SQL files (`get_data.sql`) define how to extract each survey's data
- Developer notes (`dev_notes.md`) document the SQL logic and column meanings
- All surveys use column type system (STANDARD, LTR, DRIVERS, METADATA)
- Text responses are automatically converted to numeric using configured mappings
- SQL query processing via Jupyter notebook with automated transformations
- AI analysis is standardized but customizable per survey type
- ChatGPT integration with SharePoint monitoring for automated workflows

---

**Need Help?** 
- Engineers: See `docs/engineers/DATA_INGESTION_GUIDE.md`
- AI Integration: See `docs/ai_reference/AI_ANALYSIS_GUIDE.md`
- ChatGPT Setup: See `CHATGPT_SETUP_INSTRUCTIONS.md`
