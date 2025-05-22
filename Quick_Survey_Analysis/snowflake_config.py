"""
Snowflake configuration for survey data analysis.
This file contains configurations and utilities for connecting to Snowflake.
"""

import os
import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Default private key path is blank - set this to the actual path when using
DEFAULT_PRIVATE_KEY_PATH = ""

# Snowflake connection configuration template
snowflake_cfg = {
    "account": "your_account_identifier",
    "user": "your_username",
    "role": "ANALYST",
    "warehouse": "ANALYTICS_WH",
    "database": "SURVEY_DATA",
    "schema": "PUBLIC",
    "private_key_path": DEFAULT_PRIVATE_KEY_PATH,
    "session_parameters": {
        "QUERY_TAG": "survey_analysis"
    }
}

def load_private_key(private_key_path=None):
    """
    Load the RSA private key from the specified path.
    
    Args:
        private_key_path (str, optional): Path to the private key file. 
                                         Defaults to the value in snowflake_cfg.
    
    Returns:
        bytes: The private key or None if the path is empty
    """
    key_path = private_key_path or snowflake_cfg["private_key_path"]
    
    if not key_path:
        print("No private key path provided. Authentication will use the method configured in the connector.")
        return None
    
    try:
        with open(key_path, "rb") as key_file:
            p_key = load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return p_key
    except Exception as e:
        print(f"Error loading private key: {e}")
        return None

def connect_to_snowflake(config=None):
    """
    Connect to Snowflake using the specified configuration.
    
    Args:
        config (dict, optional): Snowflake connection parameters.
                               Defaults to snowflake_cfg.
    
    Returns:
        snowflake.connector.connection: Snowflake connection object
    """
    cfg = config or snowflake_cfg
    
    try:
        # Load private key
        p_key = load_private_key(cfg.get("private_key_path"))
        
        # Build connection parameters
        conn_params = {
            "account": cfg["account"],
            "user": cfg["user"],
            "role": cfg["role"],
            "warehouse": cfg["warehouse"],
            "database": cfg["database"],
            "schema": cfg["schema"],
            "session_parameters": cfg.get("session_parameters", {})
        }
        
        # Add private key if available
        if p_key:
            conn_params["private_key"] = p_key
        
        # Connect to Snowflake
        print(f"Connecting to Snowflake account: {cfg['account']}")
        conn = snowflake.connector.connect(**conn_params)
        print(f"Successfully connected to Snowflake as user: {cfg['user']}")
        
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        return None

def execute_sql_file(conn, sql_file_path, params=None):
    """
    Execute SQL from a file with optional parameter substitution.
    Creates the temp tables defined in the SQL file.
    
    Args:
        conn (snowflake.connector.connection): Snowflake connection
        sql_file_path (str): Path to the SQL file
        params (dict, optional): Parameters for SQL substitution
    
    Returns:
        bool: True if successful, False otherwise
    """
    import time
    import re
    
    # Read SQL file
    with open(sql_file_path, 'r') as f:
        sql_content = f.read()
    
    # Split into individual statements (separated by semicolons)
    sql_statements = [s.strip() for s in sql_content.split(';') if s.strip()]
    
    print(f"Starting execution of {len(sql_statements)} SQL statements from {sql_file_path}")
    print("-" * 60)
    
    cursor = conn.cursor()
    temp_tables_created = []
    start_time = time.time()
    
    try:
        for i, statement in enumerate(sql_statements, 1):
            # Format statement with parameters if provided
            if params:
                formatted_statement = statement.format(**params)
            else:
                formatted_statement = statement
            
            # Execute the statement
            if formatted_statement:
                stmt_start_time = time.time()
                
                # Extract temp table name using regex
                table_match = re.search(r'CREATE\s+OR\s+REPLACE\s+TEMPORARY\s+TABLE\s+(\w+)', 
                                       formatted_statement, re.IGNORECASE)
                table_name = table_match.group(1) if table_match else f"Statement {i}"
                
                print(f"Executing {table_name}... ", end="", flush=True)
                cursor.execute(formatted_statement)
                
                stmt_time = time.time() - stmt_start_time
                print(f"Done! ({stmt_time:.2f} seconds)")
                
                if table_match:
                    temp_tables_created.append(table_name)
        
        total_time = time.time() - start_time
        print("-" * 60)
        print(f"Successfully created {len(temp_tables_created)} temporary tables:")
        for table in temp_tables_created:
            print(f"  - {table}")
        print(f"Total execution time: {total_time:.2f} seconds")
        
        return True
    except Exception as e:
        total_time = time.time() - start_time
        print(f"Error executing SQL at {table_name}: {e}")
        print(f"Execution failed after {total_time:.2f} seconds")
        cursor.close()
        return False