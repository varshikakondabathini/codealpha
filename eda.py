for col in numeric_cols:
    mean = df[col].mean()
    median = df[col].median()

    print(f"\nColumn: {col}")
    print(f"Mean   : {mean}")
    print(f"Median : {median}")

    if abs(mean - median) > 10:
        print("Possible skewness detected")
    else:
        print("Data appears approximately symmetric")

# ============================================
# 9. DETECT DATA ISSUES
# ============================================

print("\n----- DATA ISSUES DETECTED -----")

# Missing Values
missing = df.isnull().sum().sum()
if missing > 0:
    print(f"Missing values found: {missing}")
else:
    print("No missing values")

# Duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"Duplicate rows found: {duplicates}")
else:
    print("No duplicate rows")

# Data Types
print("\nCheck whether data types are correct for analysis.")

# ============================================
# 10. FINAL OBSERVATIONS
# ============================================

print("\n----- EDA COMPLETED SUCCESSFULLY -----")
print("Dataset structure explored")
print("Trends and patterns identified")
print("Correlations analyzed")
print("Outliers detected")
print("Potential data issues identified")
