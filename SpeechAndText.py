
from text import texttospeech
from datetime import datetime
from covid import covidstats
from speech import speechtotext

def start():
    ##texttospeech("Hello Veera ! I am Jimmy ! Your Work Assistant !")
    while True:
        query=speechtotext(2).lower()
        print(f"{query}")
        if "time now" in query:
            texttospeech("Time now is "+datetime.today().strftime("%I:%M:%S %p"))
        elif "covid" in query:
            covidobj=covidstats()
            covid_dict=covidobj.covidstatscall("India")
            texttospeech("Active cases in India is"+str(covid_dict["active"]))
            texttospeech("Critical cases in India is"+str(covid_dict["critical"]))
        elif "exit" in query:
            texttospeech("Bye ! I am exit now")
            break

if __name__=="__main__":
    start()

