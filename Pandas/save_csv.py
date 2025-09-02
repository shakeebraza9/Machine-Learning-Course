import pandas as pd
data = {
    "Symbol": [f"S{i}" for i in range(1, 27)],
    "Security": [f"Company_{i}" for i in range(1, 27)],
    "Total_valoume": [i * 1000 for i in range(1, 27)],
    "AVG_volume": [round((i * 1000) / 10, 2) for i in range(1, 27)],
    "Chnage": [round((i % 5 - 2) * 0.5, 2) for i in range(1, 27)]  
}

df = pd.DataFrame(data)
df.to_csv("test_pandas.csv", index=False)

print("CSV file generated successfully with 26 rows!")
