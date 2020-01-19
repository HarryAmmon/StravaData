# SETUP
import requests

print("Strava API")
clientID = #REPLACE WITH CLIENT ID
clientSecret = # REPLACE WITH CLIENT SECRET

# STEP 2
step2Response = requests.get(
    'https://www.strava.com/oauth/authorize?',
    params={'client_id': clientID,
            'response_type': 'code',
            'redirect_uri': 'http://localhost/exchange_token',
            'approval_prompt': 'force',
            'scope': 'read_all'})
# This wil redirect the user to the strava log in page
# they will need to click 'authorize'
# Strava server will then send us a authorization_code

# we should use this authoriization_code to populate a the code parameter in the POST request

# STEP 3
# THESE PROBS DONT WORK ANYMORE
# The authorization_code from step2
codeRead = "3a0911d82f6e66fd143dcc3402989247045def31"  # Scope: read

# Scope: profile:read_all
codeProfileReadAll = "d46882ca6e1c565c293b6866ea31bcf8d63c1ca5"

# Scope activity:read_all
codeActivityReadAll = "b56ef17e960a08d70165ec749d5ee9de01c15abb"


step3Response = requests.post(
    'https://www.strava.com/oauth/token',
    params={'client_id': clientID,
            'client_secret': clientSecret,
            'code': codeActivityReadAll,
            'grant_type': 'authorization_code'
            }
)

responseContent = step3Response.json()
accessToken = responseContent['access_token']

# STEP4
AthleteResponse = requests.get(
    'https://www.strava.com/api/v3/athlete',
    headers={'Authorization': 'Bearer '+accessToken},

)

ActivityResponse = requests.get(
    'https://www.strava.com/api/v3/activities/2967250829',
    headers={'Authorization': 'Bearer '+accessToken}
)

# GearResponse = requests.get(
#    'https://www.strava.com/api/v3/gears',
#    headers={'Authorization': 'Bearer '+accessToken},
# )

Athletejson_response = AthleteResponse.json()
athleteID = print(Athletejson_response)

#GearJsonResponse = GearResponse.json()

# print(json_response['id'])
# print(foo)
print()
