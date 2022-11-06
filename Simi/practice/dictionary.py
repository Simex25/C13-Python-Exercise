if __name__ == "__main__":
    # captains = {"Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko"}
    # captains["name"] = "Simex"
    # print(captains)
    # # print(captains.items())
    # #
    # # if captains["Enterprise"] in captains:
    # #     print(captains["Enterprise"])
    # # if "Discovery" not in captains:
    # #     print('unknown')
    # # if "Discovery" not in captains:
    # #     print("Unknown")
    # # if "Enterprise" not in captains:
    # #     print("Unknown")
    # # else:
    # #     print()
    # # for items in captains:
    # #     print(f"{items} is captained by {captains[items]}")
    # # a = dict(captains)
    # # del captains["Defiant"]
    # # print(captains)
    # # print(a)
    #
    import random

    capitals_dict = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
    }
    state, capital = random.choice(list(capitals_dict.items()))
    # help(random)
    guess = input(f"The capital of {state} is ?").lower()
    while guess != "exit":
        if guess == capital:
            print("Correct")
            break
        elif guess != capital:
            guess = input(f"The capital of {state} is ?")

        if guess == "exit":
            print(f"The capital of {state} is {capital}")
            print("Goodbye")
            break
    #
    # for keys in captains.items():
    #     print(keys)
