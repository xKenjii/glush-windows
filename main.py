import os.path, requests, sched, time, json, requests, uuid

    ##############
    # Init Start #
    ##############

s = sched.scheduler(time.time, time.sleep)

if not os.path.isfile('./config.json'):
    print("Configuration file not found...")
    f = open('error-logs.txt', 'a')
    f.write("config.json was not found...\n")
    f.close()
    exit()

with open('config.json', 'r') as jsonfile:
    config = json.load(jsonfile)

if config['apikey'] == "":
    f = open('error-logs.txt', 'a')
    f.write("The Api Key in config.json is unspecified.\n")
    f.close()
    exit()

if config['devicename'] == "":
    f = open('error-logs.txt', 'a')
    f.write("The Device Name in config.json is unspecified.\n")
    f.close()
    exit()

    ############
    # Init End #
    ############

def pingServer(sc):
    s.enter(180, 1, pingServer, (sc,))

    URL = 'http://ddns.defi-mining.nl/api/sync.php?uniqueid=' + str(uuid.getnode())
    
    for values in config.items():
        URL += f"&{values[0]}={values[1]}"

    print(URL)

    r = requests.get(URL).json()
    
    if r['response'] != 'SUCCESS':
        f = open('error-logs.txt', 'a')
        f.write(f"An error occurred trying to synchronise this device with the Glush server: {r['error']}\n")
        f.close()

pingServer(s)
s.run()