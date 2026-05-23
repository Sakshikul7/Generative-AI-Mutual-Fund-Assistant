def get_market_summary():

    market_data = {
        "Nifty 50": "+0.85%",
        "Sensex": "+0.70%",
        "Top Sector": "Banking",
        "Market Mood": "Bullish"
    }

    summary = f"""
    Current Market Overview:
    Nifty 50 is up by {market_data['Nifty 50']}.
    Sensex gained {market_data['Sensex']}.
    Top Performing Sector: {market_data['Top Sector']}.
    Overall Market Mood is {market_data['Market Mood']}.
    """

    return summary
