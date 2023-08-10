import assets.APIHandler as APIHandler
import heapq
import assets.AugFightID as AugFightID
import assets.AugEncID as AugEncID
import assets.AugPhase as AugPhase
import assets.AugPhasePlusEncID as AugPhasePlusEncID
import assets.AugDebug as AugDebug


VALID_FIGHT_SELECTION_OPTIONS = {"1", "2", "3", "4"}


def compile_top_two(fight_dict):
    top_two_dict = {}
    intervals_reached = {}
    for fight_id in fight_dict:
        fight = fight_dict[fight_id]
        for interval in fight:
            interval_top_two = top_two_dict.setdefault(interval, {})
            times_reached = intervals_reached.setdefault(interval, 0)
            times_reached += 1
            intervals_reached[interval] = times_reached
            player_list = fight[interval]
            if player_list[0].name in interval_top_two.keys():
                interval_top_two[player_list[0].name] += 1
            else:
                interval_top_two[player_list[0].name] = 1
            if player_list[1].name in interval_top_two.keys():
                interval_top_two[player_list[1].name] += 1
            else:
                interval_top_two[player_list[1].name] = 1
            top_two_dict[interval] = interval_top_two
    return top_two_dict, intervals_reached


def compile_best_buff_list(top_two_dict):
    best_buffs = {}
    for interval in top_two_dict:
        player_list = top_two_dict[interval]
        best_players = heapq.nlargest(3, player_list.items(), key=lambda item: item[1])
        names = [item[0] for item in best_players]
        best_buffs[interval] = names
    return best_buffs


def print_results(best_buffs, startTime, code, fightID, single_fight, intervals_reached):
    print("----------------------------------------")
    for interval in best_buffs:
        if single_fight:
            time_segments = interval.split('-')
            start_time_secs = get_seconds_from_segments(time_segments[0])
            end_time_secs = get_seconds_from_segments(time_segments[1])
            start_time = startTime + (start_time_secs*1_000)
            end_time = startTime + (end_time_secs*1_000)
            print(f"{interval} ({generate_url(code, fightID, start_time, end_time)}): ")
        else:
            print(f"{interval} Reached {intervals_reached[interval]} times:")
        for i in range(len(best_buffs[interval])):
            if i == 0:
                print("Best Buff Targets:")
            if i == 2:
                print("Fallback Target:")
            print(f"{i+1}. {best_buffs[interval][i]}")
        print("----------------------------------------")


def generate_url(code, fightID, start_time, end_time):
    return f"https://warcraftlogs.com/reports/{code}#fight={fightID}&type=damage-done&start={start_time}&end={end_time}"

def get_seconds_from_segments(segment):
    minutes, seconds = map(int, segment.split(':'))
    return minutes * 60 + seconds


def main():
    while True:
        while True:
            code = input("Please enter the code for the report, found in the URL (or exit to close the program): ")
            if code == 'exit':
                exit()
            real_code_resp = APIHandler.check_code_valid(APIHandler.QUERY_VALID_CODE, code=code)
            try:
                real_code = real_code_resp['data']['reportData']['report']['code']
            except TypeError:
                print("Invalid code, try again.")
                continue
            break
        while True:
            fight_selection_option = input("Choose how pulls will be selected, 1 for fight ID, 2 for encounter ID, 3 for phase, or 4 for both phase and encounter ID: ")
            if fight_selection_option in VALID_FIGHT_SELECTION_OPTIONS:
                break
        if fight_selection_option == "1":
            while True:
                fightID_inp = input("Please enter the fight IDs found in the URL of the report, separated by a space: ")
                fightIDs_str = fightID_inp.split()
                fightIDs = {int(num) for num in fightIDs_str}
                fight_resp = APIHandler.get_fight_times(AugFightID.QUERY_TIMES, code=code)
                fight_list = fight_resp['data']['reportData']['report']['fights']
                valid_id_set = {fight['id'] for fight in fight_list}
                if all(item in valid_id_set for item in fightIDs):
                    break
                else:
                    print("One or more fight IDs are invalid.")
                    continue
            fight_dict, fight_list = AugFightID.create_fight_dict(fight_list, fightIDs, code)
        elif fight_selection_option == "2":
            while True:
                print("Possible encounter IDs: \n\
        Kazzara - 2688\n\
        Amalgamation Chamber - 2687\n\
        Forgotten Experiments - 2693\n\
        Assault of the Zaqali - 2682\n\
        Rashok - 2680\n\
        Zskarn - 2689\n\
        Magmorax - 2683\n\
        Neltharion - 2684\n\
        Sarkareth - 2685")
                encID_inp = input("Please enter the encounter ID(s) for a pull to be considered, separated by a space: ")
                encID_set_str = set(encID_inp.split())
                encID_set = {int(ID) for ID in encID_set_str}
                fight_resp = APIHandler.get_fight_times(AugEncID.QUERY_TIMES, code=code)
                fight_list = fight_resp['data']['reportData']['report']['fights']
                valid_enc_id_set = {fight['encounterID'] for fight in fight_list}
                if all(item in valid_enc_id_set for item in encID_set):
                    break
                else:
                    print("One or more encounter IDs are invalid.")
                    continue
            fight_dict, fight_list = AugEncID.create_fight_dict(fight_list, encID_set, code)
        elif fight_selection_option == "3":
            while True:
                phase_inp = input("Please enter the phase to be reached for a wipe to be considered. If there are multiple, separate them by a space: ")
                phase_set_str = set(phase_inp.split())
                phase_set = {int(phase) for phase in phase_set_str}
                fight_resp = APIHandler.get_fight_times(AugPhase.QUERY_TIMES, code=code)
                fight_list = fight_resp['data']['reportData']['report']['fights']
                valid_phase_set = {fight['lastPhase'] for fight in fight_list}
                if all(item in valid_phase_set for item in phase_set):
                    break
                else:
                    print("One or more phases are invalid.")
                    continue
            fight_dict, fight_list = AugPhase.create_fight_dict(fight_list, phase_set, code)
        elif fight_selection_option == "4":
            while True:
                print("Possible encounter IDs: \n\
        Kazzara - 2688\n\
        Amalgamation Chamber - 2687\n\
        Forgotten Experiments - 2693\n\
        Assault of the Zaqali - 2682\n\
        Rashok - 2680\n\
        Zskarn - 2689\n\
        Magmorax - 2683\n\
        Neltharion - 2684\n\
        Sarkareth - 2685")
                encID_inp = input("Please enter the encounter ID(s) for a pull to be considered, separated by a space: ")
                encID_set_str = set(encID_inp.split())
                encID_set = {int(ID) for ID in encID_set_str}
                phase_inp = input("Please enter the phase to be reached for a wipe to be considered. If there are multiple, separate them by a space: ")
                phase_set_str = set(phase_inp.split())
                phase_set = {int(phase) for phase in phase_set_str}
                fight_resp = APIHandler.get_fight_times(AugPhasePlusEncID.QUERY_TIMES, code=code)
                fight_list = fight_resp['data']['reportData']['report']['fights']
                valid_enc_id_set = {fight['encounterID'] for fight in fight_list}
                valid_phase_set = {fight['lastPhase'] for fight in fight_list}
                if all(item in valid_enc_id_set for item in encID_set) and all(item in valid_phase_set for item in phase_set):
                    break
                else:
                    print("One or more selections are invalid.")
                    continue
            fight_dict, fight_list = AugPhasePlusEncID.create_fight_dict(fight_list, phase_set, encID_set, code)
        top_two_dict, intervals_reached = compile_top_two(fight_dict)
        best_buffs = compile_best_buff_list(top_two_dict)
        single_fight = True if len(fight_dict) == 1 else False
        print_results(best_buffs, fight_list[0]['startTime'], code, fight_list[0]['id'], single_fight, intervals_reached)
if __name__ == "__main__": main()