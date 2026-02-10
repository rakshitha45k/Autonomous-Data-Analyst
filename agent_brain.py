import pandas as pd

def analyze_data(df):
    # This block MUST be INDENTED
    summary = {
        "Total Sales": df["sales"].sum(),
        "Total Profit": df["profit"].sum(),
        "Average Sales": df["sales"].mean(),
        "Average Profit": df["profit"].mean(),
        "Max Sales": df["sales"].max(),
        "Max Profit": df["profit"].max(),
    }
    return summary # Correctly placed inside the function

def generate_insights(df):
    # This block MUST be INDENTED
    insights = []
    
    # Example logic for insights (assuming the index represents time)
    if df["sales"].iloc[-1] > df["sales"].iloc[0]:
        insights.append("✅ Sales are increasing over time.")
    else:
        insights.append("❌ Sales trend is flat or decreasing.")
        
    insights.append(f"Average Profit Margin: {df['profit'].sum() / df['sales'].sum() * 100:.2f}%")
        
    return insights # Correctly placed inside the function
