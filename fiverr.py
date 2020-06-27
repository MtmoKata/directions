for i in json1_dictionary['legs']:
        print("Ankunft:", i['arrival_time']['text'], "\n",
              "Start:", i['departure_time']['text'], "\n",
              "Strecke:", i['distance']['text'], "\n",
              "Dauer:", i['duration']['text'], "\n", "\n")


'''try:
        for i in json1_dictionary['legs'][0]['steps']:
                print(i['distance']['text'], i['duration']['text'], "\n", i["html_instructions"], "\n", i["steps"][0]["distance"]["text"], i["steps"][0]["duration"]["text"], i["steps"][0]["html_instructions"], "\n")
except KeyError:
        for i in json1_dictionary['legs'][0]['steps']:
                print("1")'''


for i in json1_dictionary['legs'][0]['steps']:
                print(i['distance']['text'], i['duration']['text'], "\n", i["html_instructions"], "\n", i["steps"][0]["distance"]["text"], i["steps"][0]["duration"]["text"])
