from storage.file_handler import load

def show_analysis():
    df = load()
    if df is None:
        print("No data")
        return

    print("\n--- Analysis ---")
    print("Average PM2.5:", df["PM2.5"].mean())
    print("Max AQI:", df["AQI"].max())