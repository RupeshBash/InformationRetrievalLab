import pandas as pd

def load_data():
    data = {
        "Employee Name": ["Ravi", "Jake", "Amira", "Tony", "Neha"],
        "Review": [
            "The boxing session was lit! 🥊🔥 Coach really pushed us hard. Loved it!",
            "Cricket nets need maintenance. The turf is uneven and risky 😕",
            "Great energy during the boxing drills. But pls remove the broken gloves :(",
            "Can we get new cricket bats? The current ones are cracked. #TeamSpirit",
            "<div>Best fitness day ever! Started with boxing, ended with a fun cricket match.</div>"
        ]
    }
    df = pd.DataFrame(data)
    return df

# Test run only when this file is executed directly
if __name__ == "__main__":
    df = load_data()
    print(df)
