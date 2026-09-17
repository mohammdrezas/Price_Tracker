
def send_alerts(drops):
    if not drops:
        print("هیچ افتی یافت نشد")
        return
    for drop in drops:
        print(f"قیمت {drop['name']} افت کرد! الان {drop['latest']} تومان. اخیر {drop['average']} تومان")

if __name__ == "__main__":
    sample = [
        {"name": "Test Game 1", "latest": 500000, "average": 700000},
        {"name": "Test Game 2", "latest": 1200000, "average": 1500000},
    ]
    send_alerts(sample)