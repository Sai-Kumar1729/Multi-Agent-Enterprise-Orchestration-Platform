def validate(df):
    return {
        "row_count": len(df),
        "missing_values": df.isnull().sum().to_dict()
    }
