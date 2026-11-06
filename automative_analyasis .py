# ==========================================
# Automotive Data Management - Week 1 Task
# Data Preprocessing & Pipeline Simulation
# ==========================================

import pandas as pd
import numpy as np

def initialize_automotive_pipeline():
    print("Initializing Automotive Data Management Pipeline...")
    
    # Sample automotive telemetry dataset simulation
    data = {
        'Vehicle_ID': ['V001', 'V002', 'V003', 'V004', 'V005'],
        'Engine_RPM': [2400, 3100, np.nan, 2900, 3500],
        'Oil_Temperature_C': [95.5, 102.0, 98.4, np.nan, 110.2],
        'Tire_Pressure_PSI': [32.0, 30.5, 31.0, 29.5, np.nan],
        'Vehicle_Speed_KMH': [60, 85, 45, 90, 120]
    }
    
    df = pd.DataFrame(data)
    print("\n--- Raw Automotive Dataset ---")
    print(df)
    
    # 1. Handling Missing Values (Data Cleaning)
    df['Engine_RPM'] = df['Engine_RPM'].fillna(df['Engine_RPM'].mean())
    df['Oil_Temperature_C'] = df['Oil_Temperature_C'].fillna(df['Oil_Temperature_C'].mean())
    df['Tire_Pressure_PSI'] = df['Tire_Pressure_PSI'].fillna(df['Tire_Pressure_PSI'].median())
    
    print("\n--- Cleaned Dataset (Missing Values Imputed) ---")
    print(df)
    
    # 2. Feature Engineering: High RPM Flag & Component Wear Index
    df['High_RPM_Alert'] = df['Engine_RPM'] > 3000
    df['Wear_Index'] = (df['Oil_Temperature_C'] / 100) * (df['Vehicle_Speed_KMH'] / 50)
    
    print("\n--- Processed Dataset with Feature Engineering ---")
    print(df)
    
    # Exporting cleaned data to CSV
    df.to_csv('cleaned_automotive_data.csv', index=False)
    print("\nPipeline executed successfully! Cleaned data exported to 'cleaned_automotive_data.csv'.")

if _name_ == "_main_":
    initialize_automotive_pipeline()
	