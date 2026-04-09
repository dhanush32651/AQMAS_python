import csv
from services.aq_service import add_record
from storage.file_handler import load
from analysis.analysis import show_analysis
from visual.charts import plot_graph

FILE_NAME = "air_quality.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "PM2.5", "PM10", "AQI", "Category"])
    except:
        pass

def view_records():
    df = load()
    if df is not None:
        print(df)
    else:
        print("No records found")

def main():
    init_file()

    while True:
        print("\n--- AQMAS SYSTEM ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Analyze Data")
        print("4. Show Graph")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            show_analysis()
        elif choice == '4':
            plot_graph()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()