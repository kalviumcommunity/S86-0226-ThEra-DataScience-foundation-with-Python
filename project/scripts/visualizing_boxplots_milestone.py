"""
Visualizing Data Distributions Using Boxplots - Milestone

This script demonstrates how to create and interpret boxplots for exploratory data analysis.
Boxplots provide a compact summary of data distribution, highlighting:
- Median (central line)
- Quartiles (Q1, Q3 - box edges)
- Interquartile Range (IQR - box height)
- Whiskers (1.5 * IQR from quartiles)
- Outliers (points beyond whiskers)

Key Learning Objectives:
1. Understand what each component of a boxplot represents
2. Create boxplots for single and multiple columns
3. Identify outliers visually
4. Compare distributions across columns
5. Make informed EDA decisions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def create_sample_data():
    """
    Create sample dataset with multiple numeric columns for demonstration.
    Includes some outliers intentionally for learning purposes.
    """
    np.random.seed(42)
    
    # Generate data with different distributions
    data = {
        'Age': np.concatenate([
            np.random.normal(35, 10, 95),  # Normal distribution
            [75, 80, 15]  # Some outliers
        ]),
        'Income': np.concatenate([
            np.random.normal(50000, 15000, 90),
            [150000, 180000, 200000, 220000, 10000]  # High earners and one low outlier
        ]),
        'Experience_Years': np.concatenate([
            np.random.normal(8, 4, 92),
            [25, 28, 1]  # Long experience and novice outliers
        ]),
        'Satisfaction_Score': np.concatenate([
            np.random.normal(7.5, 1.2, 93),
            [3.0, 3.5, 10.0, 2.0]  # Low and high satisfaction outliers
        ]),
        'Hours_Worked_Weekly': np.concatenate([
            np.random.normal(40, 5, 94),
            [70, 75, 15, 18]  # Overworkers and part-timers
        ])
    }
    
    df = pd.DataFrame(data)
    return df


def explain_boxplot_components():
    """
    Explanation of boxplot components.
    """
    print("=" * 80)
    print("UNDERSTANDING BOXPLOT COMPONENTS")
    print("=" * 80)
    print("""
    A boxplot consists of:
    
    1. BOX (Interquartile Range - IQR):
       - Bottom edge: Q1 (25th percentile)
       - Top edge: Q3 (75th percentile)
       - Box height: IQR = Q3 - Q1 (middle 50% of data)
    
    2. MEDIAN LINE:
       - Line inside the box
       - Shows the middle value (50th percentile)
       - Different from mean (average)
    
    3. WHISKERS:
       - Extend from box to 1.5 * IQR
       - Lower whisker: Q1 - 1.5 * IQR (but not below minimum data point)
       - Upper whisker: Q3 + 1.5 * IQR (but not above maximum data point)
    
    4. OUTLIERS:
       - Individual points beyond whiskers
       - Potential anomalies or extreme values
       - NOT always errors - need context!
    
    WHY BOXPLOTS MATTER:
    - Quick comparison across multiple groups/columns
    - Clear visualization of spread and central tendency
    - Easy outlier detection
    - Compact representation of distribution
    """)
    print("=" * 80)


def create_single_column_boxplot(df, column):
    """
    Create a boxplot for a single numeric column.
    
    Args:
        df: DataFrame containing the data
        column: Name of the column to visualize
    """
    print(f"\n{'=' * 80}")
    print(f"BOXPLOT FOR SINGLE COLUMN: {column}")
    print("=" * 80)
    
    # Calculate statistics
    q1 = df[column].quantile(0.25)
    median = df[column].median()
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_whisker = q1 - 1.5 * iqr
    upper_whisker = q3 + 1.5 * iqr
    
    print(f"\nStatistics for {column}:")
    print(f"  Median (Q2):        {median:.2f}")
    print(f"  Q1 (25th %ile):     {q1:.2f}")
    print(f"  Q3 (75th %ile):     {q3:.2f}")
    print(f"  IQR (Q3 - Q1):      {iqr:.2f}")
    print(f"  Lower Whisker:      {lower_whisker:.2f}")
    print(f"  Upper Whisker:      {upper_whisker:.2f}")
    
    # Identify outliers
    outliers = df[(df[column] < lower_whisker) | (df[column] > upper_whisker)][column]
    print(f"\n  Number of outliers: {len(outliers)}")
    if len(outliers) > 0:
        print(f"  Outlier values:     {sorted(outliers.values)}")
    
    # Create the boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[column].dropna(), vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=8, alpha=0.5))
    
    plt.ylabel(column, fontsize=12)
    plt.title(f'Boxplot of {column}', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add annotation
    plt.text(1.15, median, f'Median: {median:.2f}', 
             verticalalignment='center', fontsize=10, color='red')
    
    plt.tight_layout()
    plt.savefig(f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/boxplot_{column.lower().replace(" ", "_")}.png', 
                dpi=300, bbox_inches='tight')
    print(f"\n✓ Boxplot saved to outputs/boxplot_{column.lower().replace(' ', '_')}.png")
    plt.show()


def create_multiple_column_boxplots(df, columns):
    """
    Create side-by-side boxplots for multiple columns to compare distributions.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print(f"\n{'=' * 80}")
    print(f"COMPARING DISTRIBUTIONS ACROSS COLUMNS")
    print("=" * 80)
    
    # Print comparison statistics
    print("\nComparative Statistics:")
    print("-" * 80)
    comparison_stats = pd.DataFrame({
        'Median': df[columns].median(),
        'Q1': df[columns].quantile(0.25),
        'Q3': df[columns].quantile(0.75),
        'IQR': df[columns].quantile(0.75) - df[columns].quantile(0.25),
        'Range': df[columns].max() - df[columns].min()
    })
    print(comparison_stats.to_string())
    
    # Create boxplots using matplotlib
    plt.figure(figsize=(14, 6))
    
    positions = range(1, len(columns) + 1)
    bp_data = [df[col].dropna() for col in columns]
    
    bp = plt.boxplot(bp_data, positions=positions, patch_artist=True,
                     labels=columns,
                     boxprops=dict(facecolor='lightgreen', edgecolor='black'),
                     medianprops=dict(color='darkred', linewidth=2),
                     whiskerprops=dict(color='black', linewidth=1.5),
                     capprops=dict(color='black', linewidth=1.5),
                     flierprops=dict(marker='D', markerfacecolor='red', 
                                   markersize=6, alpha=0.6))
    
    plt.xlabel('Variables', fontsize=12, fontweight='bold')
    plt.ylabel('Values', fontsize=12, fontweight='bold')
    plt.title('Comparing Distributions Across Multiple Columns', 
              fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('d:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/boxplot_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("\n✓ Comparison boxplot saved to outputs/boxplot_comparison.png")
    plt.show()
    
    # Insights
    print("\n" + "=" * 80)
    print("KEY INSIGHTS FROM COMPARISON:")
    print("=" * 80)
    
    # Find column with largest IQR (most spread)
    largest_iqr_col = comparison_stats['IQR'].idxmax()
    print(f"  • Most variable column: {largest_iqr_col} (IQR: {comparison_stats.loc[largest_iqr_col, 'IQR']:.2f})")
    
    # Find column with smallest IQR (least spread)
    smallest_iqr_col = comparison_stats['IQR'].idxmin()
    print(f"  • Least variable column: {smallest_iqr_col} (IQR: {comparison_stats.loc[smallest_iqr_col, 'IQR']:.2f})")
    
    # Count outliers for each column
    print("\n  Outlier counts:")
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outlier_count = len(df[(df[col] < lower) | (df[col] > upper)])
        print(f"    - {col}: {outlier_count} outliers")


def create_standardized_boxplots(df, columns):
    """
    Create boxplots using standardized (z-score) data for better comparison
    when columns have different scales.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to standardize and compare
    """
    print(f"\n{'=' * 80}")
    print(f"STANDARDIZED BOXPLOTS (Z-SCORES)")
    print("=" * 80)
    print("""
    When columns have different scales (e.g., Age vs Income), 
    standardizing helps compare distributions more fairly.
    
    Z-score = (value - mean) / standard_deviation
    """)
    
    # Standardize the data
    df_standardized = df[columns].apply(lambda x: (x - x.mean()) / x.std())
    
    plt.figure(figsize=(14, 6))
    
    positions = range(1, len(columns) + 1)
    bp_data = [df_standardized[col].dropna() for col in columns]
    
    bp = plt.boxplot(bp_data, positions=positions, patch_artist=True,
                     labels=columns,
                     boxprops=dict(facecolor='lightcoral', edgecolor='black'),
                     medianprops=dict(color='darkblue', linewidth=2),
                     whiskerprops=dict(color='black', linewidth=1.5),
                     capprops=dict(color='black', linewidth=1.5),
                     flierprops=dict(marker='s', markerfacecolor='blue', 
                                   markersize=6, alpha=0.6))
    
    plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7, linewidth=1)
    plt.xlabel('Variables', fontsize=12, fontweight='bold')
    plt.ylabel('Z-Score (Standard Deviations from Mean)', fontsize=12, fontweight='bold')
    plt.title('Standardized Boxplots for Fair Comparison', 
              fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('d:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/boxplot_standardized.png', 
                dpi=300, bbox_inches='tight')
    print("✓ Standardized boxplot saved to outputs/boxplot_standardized.png")
    plt.show()


def create_horizontal_boxplot(df, column):
    """
    Create a horizontal boxplot (useful for long labels or preference).
    
    Args:
        df: DataFrame containing the data
        column: Name of the column to visualize
    """
    print(f"\n{'=' * 80}")
    print(f"HORIZONTAL BOXPLOT: {column}")
    print("=" * 80)
    
    plt.figure(figsize=(10, 4))
    plt.boxplot(df[column].dropna(), vert=False, patch_artist=True,
                boxprops=dict(facecolor='lightyellow', edgecolor='black'),
                medianprops=dict(color='darkgreen', linewidth=2),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                flierprops=dict(marker='o', markerfacecolor='orange', 
                              markersize=8, alpha=0.5))
    
    plt.xlabel(column, fontsize=12)
    plt.title(f'Horizontal Boxplot of {column}', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/boxplot_horizontal_{column.lower().replace(" ", "_")}.png', 
                dpi=300, bbox_inches='tight')
    print(f"✓ Horizontal boxplot saved")
    plt.show()


def interpret_outliers(df, column):
    """
    Detailed outlier analysis and interpretation.
    
    Args:
        df: DataFrame containing the data
        column: Name of the column to analyze
    """
    print(f"\n{'=' * 80}")
    print(f"OUTLIER INTERPRETATION: {column}")
    print("=" * 80)
    
    # Calculate outlier boundaries
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    print(f"\nOutlier Detection Results:")
    print(f"  Total data points:     {len(df)}")
    print(f"  Number of outliers:    {len(outliers)}")
    print(f"  Percentage outliers:   {(len(outliers) / len(df) * 100):.2f}%")
    print(f"\n  Lower bound:           {lower_bound:.2f}")
    print(f"  Upper bound:           {upper_bound:.2f}")
    
    if len(outliers) > 0:
        print(f"\n  Outlier values:")
        for idx, value in enumerate(sorted(outliers[column].values), 1):
            print(f"    {idx}. {value:.2f}")
        
        print(f"\n{'=' * 80}")
        print("IMPORTANT: HOW TO INTERPRET OUTLIERS")
        print("=" * 80)
        print("""
  Outliers are NOT always errors! Consider:
  
  1. DATA ENTRY ERRORS:
     - Typos (e.g., age = 150 instead of 15)
     - Wrong units (e.g., meters vs. centimeters)
     → Solution: Verify and correct if confirmed as errors
  
  2. GENUINE EXTREME VALUES:
     - High earners in income data
     - Athletes in physical performance data
     → Solution: Keep them! They represent real phenomena
  
  3. DIFFERENT POPULATIONS:
     - Part-time vs. full-time workers
     - Different age groups mixed together
     → Solution: Consider separate analysis or grouping
  
  4. MEASUREMENT ERRORS:
     - Instrument malfunction
     - Recording mistakes
     → Solution: Investigate root cause
  
  BEFORE REMOVING OUTLIERS:
  ✓ Understand the domain context
  ✓ Investigate the cause
  ✓ Document your decision
  ✓ Consider separate analysis with/without outliers
        """)


def boxplot_vs_histogram(df, column):
    """
    Compare boxplot and histogram for the same data to show complementary insights.
    
    Args:
        df: DataFrame containing the data
        column: Name of the column to visualize
    """
    print(f"\n{'=' * 80}")
    print(f"BOXPLOT VS HISTOGRAM: {column}")
    print("=" * 80)
    print("""
    Boxplots and histograms provide complementary information:
    
    BOXPLOT STRENGTHS:
    - Quick outlier identification
    - Easy comparison across groups
    - Clear quartile visualization
    - Compact representation
    
    HISTOGRAM STRENGTHS:
    - Shows distribution shape (normal, skewed, bimodal)
    - Frequency information
    - Detailed view of data density
    - Reveals modality (number of peaks)
    """)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Boxplot
    axes[0].boxplot(df[column].dropna(), vert=True, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', edgecolor='black'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(marker='o', markerfacecolor='red', markersize=8, alpha=0.5))
    axes[0].set_ylabel(column, fontsize=11)
    axes[0].set_title('Boxplot', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Histogram
    axes[1].hist(df[column].dropna(), bins=20, color='lightgreen', 
                 edgecolor='black', alpha=0.7)
    axes[1].axvline(df[column].median(), color='red', linestyle='--', 
                    linewidth=2, label='Median')
    axes[1].axvline(df[column].mean(), color='blue', linestyle='--', 
                    linewidth=2, label='Mean')
    axes[1].set_xlabel(column, fontsize=11)
    axes[1].set_ylabel('Frequency', fontsize=11)
    axes[1].set_title('Histogram', fontsize=12, fontweight='bold')
    axes[1].legend()
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.suptitle(f'Boxplot vs Histogram: {column}', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/boxplot_vs_histogram_{column.lower().replace(" ", "_")}.png', 
                dpi=300, bbox_inches='tight')
    print("\n✓ Comparison visualization saved")
    plt.show()


def main():
    """
    Main function to run all boxplot demonstrations.
    """
    print("\n" + "=" * 80)
    print(" " * 20 + "VISUALIZING BOXPLOTS MILESTONE")
    print(" " * 15 + "Data Distribution Analysis Using Boxplots")
    print("=" * 80)
    
    # 1. Explain boxplot components
    explain_boxplot_components()
    input("\nPress Enter to continue to single-column boxplot demo...")
    
    # 2. Create sample data
    print("\nCreating sample dataset with intentional outliers for demonstration...")
    df = create_sample_data()
    print(f"✓ Dataset created with {len(df)} rows and {len(df.columns)} columns")
    print(f"\nColumns: {list(df.columns)}")
    
    # 3. Single column boxplot
    create_single_column_boxplot(df, 'Age')
    input("\nPress Enter to continue to multiple-column comparison...")
    
    # 4. Multiple column comparison
    columns_to_compare = ['Satisfaction_Score', 'Experience_Years', 'Hours_Worked_Weekly']
    create_multiple_column_boxplots(df, columns_to_compare)
    input("\nPress Enter to continue to standardized boxplots...")
    
    # 5. Standardized boxplots (for different scales)
    create_standardized_boxplots(df, ['Age', 'Income'])
    input("\nPress Enter to continue to horizontal boxplot...")
    
    # 6. Horizontal boxplot
    create_horizontal_boxplot(df, 'Income')
    input("\nPress Enter to continue to outlier interpretation...")
    
    # 7. Outlier interpretation
    interpret_outliers(df, 'Income')
    input("\nPress Enter to continue to boxplot vs histogram comparison...")
    
    # 8. Boxplot vs Histogram
    boxplot_vs_histogram(df, 'Hours_Worked_Weekly')
    
    # Final summary
    print("\n" + "=" * 80)
    print("MILESTONE COMPLETE!")
    print("=" * 80)
    print("""
    You have successfully learned:
    ✓ What each component of a boxplot represents
    ✓ How to create boxplots for single and multiple columns
    ✓ How to identify and interpret outliers
    ✓ How to compare distributions across columns
    ✓ When to use boxplots vs. histograms
    
    KEY TAKEAWAYS:
    1. Boxplots summarize distribution using 5 numbers (min, Q1, median, Q3, max)
    2. Outliers are visible as individual points beyond whiskers
    3. IQR (box height) shows the spread of middle 50% of data
    4. Median line shows central tendency (resistant to outliers)
    5. Boxplots excel at comparing distributions side-by-side
    6. Always investigate outliers - don't remove blindly!
    
    NEXT STEPS:
    - Apply boxplots to your own datasets
    - Combine with summary statistics for complete analysis
    - Use boxplots as part of comprehensive EDA
    - Consider creating boxplots by groups/categories
    """)
    print("=" * 80)


if __name__ == "__main__":
    main()
