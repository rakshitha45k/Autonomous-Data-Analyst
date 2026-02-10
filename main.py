from agent_brain import analyze_data, generate_insights
import pandas as pd

print("Data Analyst Agent Started")

# Make sure 'data/sample.csv' exists
df = pd.read_csv("data/sample.csv")

summary = analyze_data(df)
insights = generate_insights(df)

print("\n SUMMARY REPORT")
for key, value in summary.items():
    # INDENTATION FIXED BELOW
    print(f"{key}: {value}")

print("\n AI INSIGHTS")
for i in insights:
    # INDENTATION FIXED BELOW
    print(i)
