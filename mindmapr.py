import json
import random

FILE = "mindmapr.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_topic(data):
    topic = input("Enter topic name: ").strip()
    if not topic:
        print("Topic cannot be empty.")
        return
    points = []
    while True:
        point = input("Add key point (or 'done' to finish): ").strip()
        if point.lower() == "done":
            break
        if point:
            points.append(point)
    data.setdefault(topic, []).extend(points)
    save_data(data)
    print(f"✅ Saved {len(points)} points for '{topic}'")

def view_all(data):
    if not data:
        print("No topics added yet.")
        return
    for t, p in data.items():
        print(f"\n📘 {t}")
        for i, point in enumerate(p, 1):
            print(f"   {i}. {point}")

def search_topic(data):
    topic = input("Enter topic name to search: ").strip()
    if topic in data:
        print(f"\n📗 {topic}")
        for i, point in enumerate(data[topic], 1):
            print(f"   {i}. {point}")
    else:
        print("Topic not found!")

def quiz_mode(data):
    if not data:
        print("No data available for quiz.")
        return
    topic = random.choice(list(data.keys()))
    point = random.choice(data[topic])
    print(f"\n🧩 Topic: {topic}")
    input("Press Enter to see hint...")
    print(f"💡 Hint: {point}")

def main():
    data = load_data()
    while True:
        print("\n--- MindMapr – Smart Revision Assistant ---")
        print("1. Add Topic")
        print("2. View All Topics")
        print("3. Search Topic")
        print("4. Quiz Mode")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_topic(data)
        elif choice == "2":
            view_all(data)
        elif choice == "3":
            search_topic(data)
        elif choice == "4":
            quiz_mode(data)
        elif choice == "5":
            print("Goodbye 👋 Keep Revising!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
  
