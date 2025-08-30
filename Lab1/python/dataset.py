import pandas as pd

def load_data():
    data = {
        "Employee Name": ["Rupesh", "Jake", "Amira", "Tony", "Neha",
                          "Sam", "Aisha", "Carlos", "Priya", "Zane"],
        "Review": [
            "The BOXING session was Lit! 🥊🔥 Coach really pushed us hard. Loved it!",
            "Cricket nets need maintenance. The turf is uneven and risky 😕",
            "Great energy during the boxing drills. But pls remove the broken gloves :(",
            "Can we get new cricket bats? The current ones are cracked. #TeamSpirit",
            "<div>Best fitness day ever! Started with boxing, ended with a fun cricket match.</div>",
            "idk if the equipment is ready yet... pls update ASAP! 😟",
            "U should check the cricket pitch. It's full of holes!!!",
            "Amazing effort by the players!!! But the coach's feedback was a bit harsh :-/",
            "Check out https://cricketsite.com for latest updates on the tournament.",
            "The gym's AC isn't working, it's sooo hot! 🔥🔥🔥"
        ]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df)
