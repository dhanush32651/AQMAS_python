import matplotlib.pyplot as plt
from storage.file_handler import load

def plot_graph():
    df = load()
    if df is None:
        print("No data")
        return

    plt.plot(df["PM2.5"])
    plt.title("PM2.5 Trend")
    plt.xlabel("Records")
    plt.ylabel("PM2.5")
    plt.show()