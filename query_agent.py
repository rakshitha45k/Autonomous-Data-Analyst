def answer_query(df, query):
    query = query.lower()

    if "highest sales" in query:
        row = df.loc[df["sales"].idxmax()]
        return f"📈 Highest sales was {row['sales']} on {row['date']}"

    elif "lowest sales" in query:
        row = df.loc[df["sales"].idxmin()]
        return f"📉 Lowest sales was {row['sales']} on {row['date']}"

    elif "average sales" in query:
        avg = df["sales"].mean()
        return f"💰 Average sales: {avg:.2f}"

    elif "average profit" in query:
        avg = df["profit"].mean()
        return f"💰 Average profit: {avg:.2f}"

    elif "compare sales profit" in query:
        total_sales = df["sales"].sum()
        total_profit = df["profit"].sum()
        return f"Sales: {total_sales}, Profit: {total_profit}"

    else:
        return "❓ Sorry, I cannot answer that question."
