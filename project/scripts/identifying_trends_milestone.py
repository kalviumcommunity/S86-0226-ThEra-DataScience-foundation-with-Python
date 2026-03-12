"""
Identifying Trends Over Time Using Line Plots - Milestone

This script demonstrates how to create and interpret line plots for time-series data.
Line plots are essential for visualizing how data changes over time, revealing:
- Long-term trends (upward, downward, stable)
- Short-term fluctuations and volatility
- Seasonal patterns
- Anomalies and sudden changes
- Cyclical behavior

Key Learning Objectives:
1. Understand time-based data structure
2. Create clear line plots for temporal analysis
3. Identify and interpret trends over time
4. Spot anomalies and unusual patterns
5. Make data-driven decisions based on temporal insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)


def create_sample_time_series_data():
    """
    Create sample time-series datasets with various patterns for demonstration.
    Includes trends, seasonality, noise, and anomalies.
    """
    np.random.seed(42)
    
    # Generate daily dates for 2 years
    start_date = datetime(2024, 1, 1)
    dates = pd.date_range(start=start_date, periods=730, freq='D')
    
    # 1. Sales data with upward trend and seasonality
    trend = np.linspace(1000, 2500, 730)  # Upward trend
    seasonality = 300 * np.sin(np.linspace(0, 4 * np.pi, 730))  # Seasonal pattern
    noise = np.random.normal(0, 100, 730)  # Random noise
    sales = trend + seasonality + noise
    
    # Add some anomalies (promotional spikes and drops)
    sales[180] += 800  # Big promotion
    sales[365] += 600  # Holiday spike
    sales[450] -= 400  # Supply chain issue
    sales[600] += 700  # End of year sale
    
    # 2. Website traffic with strong growth
    base_traffic = np.linspace(5000, 25000, 730)
    weekly_pattern = 2000 * np.sin(np.linspace(0, 104 * np.pi, 730))  # Weekly cycle
    traffic_noise = np.random.normal(0, 500, 730)
    traffic = base_traffic + weekly_pattern + traffic_noise
    traffic = np.maximum(traffic, 0)  # Ensure no negative values
    
    # 3. Temperature data with seasonal cycle
    yearly_cycle = 20 * np.sin(np.linspace(0, 4 * np.pi, 730) - np.pi/2) + 20
    daily_variation = np.random.normal(0, 3, 730)
    temperature = yearly_cycle + daily_variation
    
    # 4. Stock price with volatility
    returns = np.random.normal(0.001, 0.02, 730)  # Daily returns
    stock_price = 100 * np.exp(np.cumsum(returns))  # Compound returns
    
    # 5. Customer signups with declining trend (churn)
    declining_trend = np.linspace(500, 200, 730)
    signup_noise = np.random.normal(0, 30, 730)
    signups = declining_trend + signup_noise
    signups = np.maximum(signups, 0)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Sales': sales,
        'Website_Traffic': traffic,
        'Temperature_C': temperature,
        'Stock_Price': stock_price,
        'Customer_Signups': signups
    })
    
    return df


def explain_time_series_concepts():
    """
    Explanation of time-series data concepts.
    """
    print("=" * 80)
    print("UNDERSTANDING TIME-BASED DATA")
    print("=" * 80)
    print("""
    Time-series data has a temporal ordering that must be preserved:
    
    KEY CHARACTERISTICS:
    
    1. TEMPORAL ORDERING:
       - Data points are ordered by time
       - Order matters! Cannot be shuffled
       - Past influences future (temporal dependency)
    
    2. TIME INTERVALS:
       - Regular: Daily, weekly, monthly (evenly spaced)
       - Irregular: Events, transactions (unevenly spaced)
       - Important for analysis method selection
    
    3. COMMON PATTERNS:
       - Trend: Long-term increase or decrease
       - Seasonality: Regular, predictable patterns
       - Cycles: Irregular, longer-term fluctuations
       - Noise: Random, unpredictable variation
    
    4. WHY LINE PLOTS?
       - Show continuity between points
       - Emphasize temporal flow
       - Make trends visually obvious
       - Highlight changes and patterns
    
    TIME-SERIES vs. OTHER DATA:
    - Static data: Single snapshot in time
    - Cross-sectional: Multiple subjects at one time
    - Time-series: One subject tracked over time
    - Panel data: Multiple subjects over time
    
    CRITICAL: Always ensure data is sorted by time before plotting!
    """)
    print("=" * 80)


def create_basic_line_plot(df, column, title=None):
    """
    Create a basic line plot for a single time series.
    
    Args:
        df: DataFrame with 'Date' column and numeric data
        column: Name of the column to plot
        title: Optional custom title
    """
    print(f"\n{'=' * 80}")
    print(f"BASIC LINE PLOT: {column}")
    print("=" * 80)
    
    # Ensure data is sorted by date
    df_sorted = df.sort_values('Date')
    
    # Basic statistics
    print(f"\nTime Period: {df_sorted['Date'].min().date()} to {df_sorted['Date'].max().date()}")
    print(f"Number of data points: {len(df_sorted)}")
    print(f"\nStatistics for {column}:")
    print(f"  Mean:     {df_sorted[column].mean():.2f}")
    print(f"  Median:   {df_sorted[column].median():.2f}")
    print(f"  Std Dev:  {df_sorted[column].std():.2f}")
    print(f"  Min:      {df_sorted[column].min():.2f}")
    print(f"  Max:      {df_sorted[column].max():.2f}")
    
    # Create the plot
    plt.figure(figsize=(14, 6))
    
    plt.plot(df_sorted['Date'], df_sorted[column], 
             linewidth=2, color='steelblue', alpha=0.8)
    
    # Add trend line
    x_numeric = np.arange(len(df_sorted))
    z = np.polyfit(x_numeric, df_sorted[column], 1)
    p = np.poly1d(z)
    plt.plot(df_sorted['Date'], p(x_numeric), 
             '--', color='red', linewidth=2, alpha=0.7, label='Trend Line')
    
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel(column.replace('_', ' '), fontsize=12, fontweight='bold')
    plt.title(title or f'{column.replace("_", " ")} Over Time', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save plot
    filename = f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_{column.lower()}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\n✓ Line plot saved to outputs/lineplot_{column.lower()}.png")
    plt.show()
    
    # Calculate trend direction
    if z[0] > 0:
        trend_direction = "UPWARD (increasing over time)"
    elif z[0] < 0:
        trend_direction = "DOWNWARD (decreasing over time)"
    else:
        trend_direction = "FLAT (stable over time)"
    
    print(f"\nTrend Analysis:")
    print(f"  Overall trend: {trend_direction}")
    print(f"  Slope: {z[0]:.4f}")


def identify_trend_patterns(df, column):
    """
    Detailed trend pattern analysis.
    
    Args:
        df: DataFrame with 'Date' column
        column: Column to analyze
    """
    print(f"\n{'=' * 80}")
    print(f"TREND PATTERN ANALYSIS: {column}")
    print("=" * 80)
    
    df_sorted = df.sort_values('Date').copy()
    
    # Moving averages to smooth out noise
    df_sorted['MA_7'] = df_sorted[column].rolling(window=7, min_periods=1).mean()
    df_sorted['MA_30'] = df_sorted[column].rolling(window=30, min_periods=1).mean()
    df_sorted['MA_90'] = df_sorted[column].rolling(window=90, min_periods=1).mean()
    
    # Calculate percentage change
    df_sorted['Pct_Change'] = df_sorted[column].pct_change() * 100
    
    # Statistics
    avg_daily_change = df_sorted['Pct_Change'].mean()
    volatility = df_sorted['Pct_Change'].std()
    
    print(f"\nTrend Metrics:")
    print(f"  Average daily change: {avg_daily_change:.2f}%")
    print(f"  Volatility (std dev): {volatility:.2f}%")
    print(f"  Largest increase: {df_sorted['Pct_Change'].max():.2f}%")
    print(f"  Largest decrease: {df_sorted['Pct_Change'].min():.2f}%")
    
    # Plot with multiple moving averages
    plt.figure(figsize=(14, 7))
    
    plt.plot(df_sorted['Date'], df_sorted[column], 
             linewidth=1, color='gray', alpha=0.5, label='Original Data')
    plt.plot(df_sorted['Date'], df_sorted['MA_7'], 
             linewidth=2, color='blue', alpha=0.7, label='7-Day Moving Average')
    plt.plot(df_sorted['Date'], df_sorted['MA_30'], 
             linewidth=2, color='green', alpha=0.7, label='30-Day Moving Average')
    plt.plot(df_sorted['Date'], df_sorted['MA_90'], 
             linewidth=2.5, color='red', alpha=0.8, label='90-Day Moving Average (Trend)')
    
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel(column.replace('_', ' '), fontsize=12, fontweight='bold')
    plt.title(f'{column.replace("_", " ")} - Trend Analysis with Moving Averages', 
              fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    filename = f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_trend_{column.lower()}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\n✓ Trend analysis plot saved")
    plt.show()
    
    print(f"\n{'=' * 80}")
    print("INTERPRETING MOVING AVERAGES")
    print("=" * 80)
    print("""
    Moving averages smooth out short-term fluctuations:
    
    - 7-Day MA:  Captures weekly patterns, still shows noise
    - 30-Day MA: Monthly trend, reduces daily volatility
    - 90-Day MA: Quarterly trend, reveals long-term direction
    
    WHY USE MOVING AVERAGES?
    ✓ Remove noise to see the underlying trend
    ✓ Identify when trends change direction
    ✓ Compare short-term vs long-term behavior
    ✓ Make better decisions based on sustained patterns
    """)


def detect_anomalies(df, column, threshold=3):
    """
    Detect and visualize anomalies in time series data.
    
    Args:
        df: DataFrame with time-series data
        column: Column to analyze
        threshold: Number of standard deviations for anomaly detection
    """
    print(f"\n{'=' * 80}")
    print(f"ANOMALY DETECTION: {column}")
    print("=" * 80)
    
    df_sorted = df.sort_values('Date').copy()
    
    # Calculate rolling statistics
    df_sorted['Rolling_Mean'] = df_sorted[column].rolling(window=30, min_periods=1).mean()
    df_sorted['Rolling_Std'] = df_sorted[column].rolling(window=30, min_periods=1).std()
    
    # Identify anomalies (points beyond threshold standard deviations)
    df_sorted['Z_Score'] = (df_sorted[column] - df_sorted['Rolling_Mean']) / df_sorted['Rolling_Std']
    df_sorted['Is_Anomaly'] = (np.abs(df_sorted['Z_Score']) > threshold)
    
    anomalies = df_sorted[df_sorted['Is_Anomaly']]
    
    print(f"\nAnomaly Detection Results:")
    print(f"  Total data points: {len(df_sorted)}")
    print(f"  Anomalies found: {len(anomalies)}")
    print(f"  Percentage: {(len(anomalies) / len(df_sorted) * 100):.2f}%")
    print(f"  Threshold: {threshold} standard deviations")
    
    if len(anomalies) > 0:
        print(f"\nAnomaly Details:")
        for idx, row in anomalies.iterrows():
            print(f"  Date: {row['Date'].date()}, Value: {row[column]:.2f}, Z-Score: {row['Z_Score']:.2f}")
    
    # Visualize anomalies
    plt.figure(figsize=(14, 7))
    
    # Plot normal data
    normal_data = df_sorted[~df_sorted['Is_Anomaly']]
    plt.plot(normal_data['Date'], normal_data[column], 
             linewidth=2, color='steelblue', alpha=0.8, label='Normal Data')
    
    # Plot rolling mean
    plt.plot(df_sorted['Date'], df_sorted['Rolling_Mean'], 
             '--', linewidth=2, color='green', alpha=0.7, label='30-Day Moving Average')
    
    # Highlight anomalies
    if len(anomalies) > 0:
        plt.scatter(anomalies['Date'], anomalies[column], 
                   color='red', s=100, zorder=5, label='Anomalies', marker='o')
        
        # Annotate some anomalies
        for idx, row in anomalies.head(5).iterrows():
            plt.annotate(f"{row[column]:.0f}", 
                        xy=(row['Date'], row[column]),
                        xytext=(10, 10), textcoords='offset points',
                        fontsize=9, color='red',
                        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel(column.replace('_', ' '), fontsize=12, fontweight='bold')
    plt.title(f'{column.replace("_", " ")} - Anomaly Detection', 
              fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    filename = f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_anomalies_{column.lower()}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\n✓ Anomaly detection plot saved")
    plt.show()
    
    print(f"\n{'=' * 80}")
    print("UNDERSTANDING ANOMALIES")
    print("=" * 80)
    print("""
    Anomalies can indicate:
    
    1. SPECIAL EVENTS:
       - Promotions, sales, marketing campaigns
       - Holidays or seasonal events
       - Product launches
    
    2. OPERATIONAL ISSUES:
       - System outages or failures
       - Supply chain disruptions
       - Data collection errors
    
    3. EXTERNAL FACTORS:
       - Economic events
       - Weather extremes
       - Competitor actions
    
    4. NATURAL VOLATILITY:
       - Random variation (not all anomalies are meaningful)
       - Expected fluctuation in volatile systems
    
    ALWAYS INVESTIGATE:
    ✓ What happened on that date?
    ✓ Is there a reasonable explanation?
    ✓ Is this a one-time event or pattern?
    ✓ Should action be taken?
    """)


def compare_multiple_time_series(df, columns):
    """
    Compare multiple time series on the same plot.
    
    Args:
        df: DataFrame with time-series data
        columns: List of columns to compare
    """
    print(f"\n{'=' * 80}")
    print(f"COMPARING MULTIPLE TIME SERIES")
    print("=" * 80)
    
    df_sorted = df.sort_values('Date')
    
    # Plot 1: Absolute values (different scales)
    fig, axes = plt.subplots(len(columns), 1, figsize=(14, 4 * len(columns)))
    if len(columns) == 1:
        axes = [axes]
    
    for idx, column in enumerate(columns):
        axes[idx].plot(df_sorted['Date'], df_sorted[column], 
                      linewidth=2, color=f'C{idx}')
        axes[idx].set_ylabel(column.replace('_', ' '), fontsize=11, fontweight='bold')
        axes[idx].grid(True, alpha=0.3)
        axes[idx].tick_params(axis='x', rotation=45)
        
        if idx == 0:
            axes[idx].set_title('Multiple Time Series - Separate Scales', 
                              fontsize=14, fontweight='bold')
    
    axes[-1].set_xlabel('Date', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('d:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_comparison_separate.png', 
                dpi=300, bbox_inches='tight')
    print("\n✓ Separate scales comparison saved")
    plt.show()
    
    # Plot 2: Normalized comparison (0-100 scale)
    plt.figure(figsize=(14, 7))
    
    for column in columns:
        # Normalize to 0-100 scale
        normalized = 100 * (df_sorted[column] - df_sorted[column].min()) / \
                     (df_sorted[column].max() - df_sorted[column].min())
        plt.plot(df_sorted['Date'], normalized, 
                linewidth=2, label=column.replace('_', ' '), alpha=0.8)
    
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Normalized Value (0-100)', fontsize=12, fontweight='bold')
    plt.title('Multiple Time Series - Normalized Comparison', 
              fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('d:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_comparison_normalized.png', 
                dpi=300, bbox_inches='tight')
    print("✓ Normalized comparison saved")
    plt.show()
    
    print(f"\n{'=' * 80}")
    print("COMPARISON INSIGHTS")
    print("=" * 80)
    print("""
    When comparing multiple time series:
    
    SEPARATE PLOTS:
    ✓ Use when scales are very different
    ✓ Preserves actual values
    ✓ Easier to see individual patterns
    
    NORMALIZED PLOTS:
    ✓ Use to compare relative trends
    ✓ Shows which changes most/least
    ✓ Reveals correlation patterns
    
    KEY QUESTIONS:
    - Do series move together or opposite?
    - Which is more volatile?
    - Are trends consistent across series?
    - Are there leading/lagging relationships?
    """)


def analyze_seasonality(df, column):
    """
    Analyze and visualize seasonal patterns in time series.
    
    Args:
        df: DataFrame with time-series data
        column: Column to analyze
    """
    print(f"\n{'=' * 80}")
    print(f"SEASONALITY ANALYSIS: {column}")
    print("=" * 80)
    
    df_sorted = df.sort_values('Date').copy()
    
    # Extract time components
    df_sorted['Year'] = df_sorted['Date'].dt.year
    df_sorted['Month'] = df_sorted['Date'].dt.month
    df_sorted['Month_Name'] = df_sorted['Date'].dt.strftime('%b')
    df_sorted['DayOfWeek'] = df_sorted['Date'].dt.dayofweek
    df_sorted['DayOfWeek_Name'] = df_sorted['Date'].dt.strftime('%a')
    
    # Monthly average pattern
    monthly_avg = df_sorted.groupby('Month_Name')[column].mean().reindex(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    )
    
    # Day of week pattern
    day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    daily_avg = df_sorted.groupby('DayOfWeek_Name')[column].mean().reindex(day_order)
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # 1. Original time series
    axes[0, 0].plot(df_sorted['Date'], df_sorted[column], linewidth=1.5, color='steelblue')
    axes[0, 0].set_title('Original Time Series', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Date', fontsize=10)
    axes[0, 0].set_ylabel(column.replace('_', ' '), fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Monthly seasonality
    axes[0, 1].plot(monthly_avg.index, monthly_avg.values, 
                    marker='o', linewidth=2, color='green', markersize=8)
    axes[0, 1].set_title('Monthly Seasonal Pattern', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Month', fontsize=10)
    axes[0, 1].set_ylabel(f'Average {column.replace("_", " ")}', fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Day of week pattern
    axes[1, 0].bar(daily_avg.index, daily_avg.values, color='coral', alpha=0.7)
    axes[1, 0].set_title('Day of Week Pattern', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Day of Week', fontsize=10)
    axes[1, 0].set_ylabel(f'Average {column.replace("_", " ")}', fontsize=10)
    axes[1, 0].grid(True, alpha=0.3, axis='y')
    
    # 4. Year-over-year comparison
    for year in df_sorted['Year'].unique():
        year_data = df_sorted[df_sorted['Year'] == year]
        axes[1, 1].plot(year_data['Date'].dt.dayofyear, year_data[column], 
                       label=str(year), linewidth=1.5, alpha=0.7)
    axes[1, 1].set_title('Year-over-Year Comparison', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Day of Year', fontsize=10)
    axes[1, 1].set_ylabel(column.replace('_', ' '), fontsize=10)
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.suptitle(f'Seasonality Analysis: {column.replace("_", " ")}', 
                fontsize=14, fontweight='bold', y=1.00)
    plt.tight_layout()
    
    filename = f'd:/Kalvium/Python-DS(SW)/S86-0226-ThEra-DataScience-foundation-with-Python/project/outputs/lineplot_seasonality_{column.lower()}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\n✓ Seasonality analysis saved")
    plt.show()
    
    print("\n" + "=" * 80)
    print("SEASONALITY INSIGHTS")
    print("=" * 80)
    print(f"\nMonthly Pattern:")
    print(f"  Highest month: {monthly_avg.idxmax()} ({monthly_avg.max():.2f})")
    print(f"  Lowest month: {monthly_avg.idxmin()} ({monthly_avg.min():.2f})")
    print(f"  Seasonal variation: {monthly_avg.max() - monthly_avg.min():.2f}")
    
    print(f"\nWeekly Pattern:")
    print(f"  Highest day: {daily_avg.idxmax()} ({daily_avg.max():.2f})")
    print(f"  Lowest day: {daily_avg.idxmin()} ({daily_avg.min():.2f})")
    print(f"  Weekly variation: {daily_avg.max() - daily_avg.min():.2f}")


def main():
    """
    Main function to run all time-series line plot demonstrations.
    """
    print("\n" + "=" * 80)
    print(" " * 15 + "IDENTIFYING TRENDS OVER TIME MILESTONE")
    print(" " * 12 + "Time-Series Analysis Using Line Plots")
    print("=" * 80)
    
    # 1. Explain time-series concepts
    explain_time_series_concepts()
    input("\nPress Enter to create sample time-series data...")
    
    # 2. Create sample data
    print("\nCreating sample time-series datasets...")
    df = create_sample_time_series_data()
    print(f"✓ Dataset created with {len(df)} time points over {(df['Date'].max() - df['Date'].min()).days} days")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst few rows:")
    print(df.head())
    input("\nPress Enter to continue to basic line plot...")
    
    # 3. Basic line plot
    create_basic_line_plot(df, 'Sales', 'Daily Sales Revenue Over Time')
    input("\nPress Enter to continue to trend pattern analysis...")
    
    # 4. Trend pattern analysis
    identify_trend_patterns(df, 'Website_Traffic')
    input("\nPress Enter to continue to anomaly detection...")
    
    # 5. Anomaly detection
    detect_anomalies(df, 'Sales', threshold=2.5)
    input("\nPress Enter to continue to multiple time-series comparison...")
    
    # 6. Compare multiple series
    compare_multiple_time_series(df, ['Sales', 'Website_Traffic', 'Customer_Signups'])
    input("\nPress Enter to continue to seasonality analysis...")
    
    # 7. Seasonality analysis
    analyze_seasonality(df, 'Temperature_C')
    
    # Final summary
    print("\n" + "=" * 80)
    print("MILESTONE COMPLETE!")
    print("=" * 80)
    print("""
    You have successfully learned:
    ✓ What time-based data represents and why ordering matters
    ✓ How to create clear line plots for temporal analysis
    ✓ How to identify trends (upward, downward, stable)
    ✓ How to detect and interpret anomalies
    ✓ How to compare multiple time series
    ✓ How to analyze seasonal patterns
    
    KEY TAKEAWAYS:
    1. Always sort time-series data by date before analysis
    2. Line plots show continuity and flow over time
    3. Moving averages help identify underlying trends
    4. Anomalies require investigation, not automatic removal
    5. Normalize data when comparing series with different scales
    6. Look for patterns: trends, seasonality, cycles, anomalies
    7. Context matters - numbers alone don't tell the story
    
    BEST PRACTICES:
    • Label axes clearly with units and time periods
    • Use appropriate time granularity (daily, weekly, monthly)
    • Add trend lines to emphasize direction
    • Annotate significant events or anomalies
    • Consider multiple time scales (short-term vs long-term)
    • Combine visualization with domain knowledge
    
    NEXT STEPS:
    - Apply line plots to your own time-series data
    - Practice identifying trends and patterns
    - Investigate anomalies with business context
    - Combine with statistical analysis for deeper insights
    - Consider forecasting and predictive modeling (advanced)
    """)
    print("=" * 80)


if __name__ == "__main__":
    main()
