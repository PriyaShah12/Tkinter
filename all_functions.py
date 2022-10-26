import requests
import json
import tkinter.messagebox as tmsg

class Jsondata_Class_Page:
    @classmethod
    def get(cls, url):
        retries = 3
        for n in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.ConnectionError as err:
                # eg, no internet
                raise SystemExit(err)
            except requests.exceptions.HTTPError as err:
                # eg, url, server and other errors
                raise SystemExit(err)
            # print("######", response.text)
            return response.text
    @classmethod
    def convert_json_string_to_python_dictionary(cls, json_string):  # has to be response.text
        python_dictionary = json.loads(json_string)
        return (python_dictionary)

    @classmethod
    def get_fact_text(cls):
        resp_text = Jsondata_Class_Page.get("https://uselessfacts.jsph.pl/random.json?language=en")
        python_dict = Jsondata_Class_Page.convert_json_string_to_python_dictionary(resp_text)
        print("******", python_dict["text"])
        # message = python_dict["text"]
        # tmsg.showinfo("New Fact", message)
        return python_dict["text"]


# j = Jsondata_Class_Page()
# Jsondata_Class_Page.get_fact_text()



