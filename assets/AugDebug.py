def print_fight_dict(fight_dict):
    for fight in fight_dict:
        table_dict = fight_dict[fight]
        print(f"Fight ID: {fight}\n")
        for interval in table_dict:
            print(f"{interval}:")
            for player in table_dict[interval]:
                print(player)
            print("\n")
        print("----------------------------------------")


def print_top_two_dict(top_two_dict):
    for interval in top_two_dict:
        print(f"{interval}:")
        interval_dict = top_two_dict[interval]
        for player in interval_dict:
            print(f"{player}: {interval_dict[player]}")
        print("----------------------------------------")