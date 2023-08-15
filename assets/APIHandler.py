import requests
import os

TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
PUBLIC_URL = "https://www.warcraftlogs.com/api/v2/client"

QUERY_TABLE="""
        query($code:String, $fightIDs:[Int], $startTime:Float, $endTime:Float) {
            reportData{
                report(code:$code){
                    table(fightIDs:$fightIDs, dataType: DamageDone, startTime: $startTime, endTime: $endTime)
                }
            }
        }
        """


QUERY_VALID_CODE="""
        query($code:String) {
            reportData{
                report(code:$code){
                    code
                }
            }
        }
        """


QUERY_POINTS="""
query{
	rateLimitData{
        limitPerHour
        pointsSpentThisHour
        pointsResetIn
    }
}
"""


def retrieve_headers():
    data = {"grant_type":"client_credentials"}
    auth = (os.environ.get("AUG_CLIENT_ID"), os.environ.get("AUG_CLIENT_SECRET"))
    with requests.Session() as session:
        response = session.post(TOKEN_URL, data = data, auth = auth).json()

    return {"Authorization": f"Bearer {response.get('access_token')}"}


def get_fight_times(query, **kwargs):
    data = {"query":query, "variables":kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(PUBLIC_URL, json = data)
        return response.json()
    
def get_table(query, **kwargs):
    data = {"query":query, "variables":kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(PUBLIC_URL, json = data)
        return response.json()
    
def check_code_valid(query, **kwargs):
    data = {"query":query, "variables":kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(PUBLIC_URL, json = data)
        return response.json()
    
def get_point_data(query, **kwargs):
    data = {"query":query, "variables":kwargs}
    with requests.Session() as session:
        session.headers = retrieve_headers()
        response = session.get(PUBLIC_URL, json = data)
        return response.json()