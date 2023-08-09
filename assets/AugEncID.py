import assets.APIHandler as APIHandler
from assets.AugPlayer import Player, VALID_SPECS


QUERY_TIMES="""
        query($code:String) {
            reportData{
                report(code:$code){
                    fights{
                        id
                        name
                        startTime
                        endTime
                        encounterID
                    }
                }
            }
        }
        """


def create_fight_dict(fight_list, encID_set, code):
    fight_dict = {}
    fight_list_reduced = []
    for fight in fight_list:
        if fight['encounterID'] in encID_set:
            fight_list_reduced.append(fight)
            print(f"Fetching data from fight: {fight['id']}")
            table_dict = {}
            start_difference = 0
            end_difference = 30_000
            end_time = 0
            while fight['endTime'] - end_time > 30_000:
                start_time = fight['startTime'] + start_difference
                end_time = fight['startTime'] + end_difference
                response = APIHandler.get_table(APIHandler.QUERY_TABLE, code=code, fightIDs=fight['id'], startTime=start_time, endTime=end_time)
                table_entry = response['data']['reportData']['report']['table']['data']['entries']
                player_list = []
                for entry in table_entry:
                    if entry['icon'] in VALID_SPECS:
                        player_list.append(Player(entry['name'], entry['id'], entry['icon'], entry['total'], round((entry['total']/30), 2)))
                start_time_str_secs = int(start_difference/1000)
                end_time_str_secs = int(end_difference/1000)
                time_str = f"{start_time_str_secs//60}:{start_time_str_secs%60:02d}-{end_time_str_secs//60}:{end_time_str_secs%60:02d}"
                player_list.sort(key=Player.get_dps, reverse=True)
                table_dict[time_str] = player_list
                start_difference += 30_000
                end_difference += 30_000
            
            fight_dict[fight['id']] = table_dict
    return fight_dict, fight_list_reduced