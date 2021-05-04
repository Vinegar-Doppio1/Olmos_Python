import csv
import json
import os


#yapf: disable
def create_json(str_name, dic_list):
    """Crea el Json con el nombre del str que se le pasó a la función
    y guarda la infomarción de diccionario de listas dentro

    Args:
        str_name (string): [nombre del archivo Json]
        dic_list ([Diccionario de lista]): [información que se guarda en el Json]
    """
    with open(os.path.join(os.getcwd(), f"Data_files{os.sep}{str_name}.json"),
              "w") as output:
        json.dump(dic_list, output, indent=4)


def start1():
    """Abre el csv, guarda la información en una lista de diccionarios,
    la filta para que sólo queden los paises,
    el sorted nos da los 10 que más gastaron en el 2018 y
    mete los nombres y le gasto a la función create_json
    """
    with open(os.path.join(os.getcwd(),
                           f"Data_files{os.sep}Military Expenditure.csv"),
              "r",encoding="utf-8") as me_data:
        me_list = list(csv.DictReader(me_data))
    me_list = filter(lambda x: x["Type"] == "Country", me_list)
    me_top10 = sorted(me_list,
                      key=lambda x: 0 if x["2018"] == "" else float(x["2018"]),
                      reverse=True)[:10]

    create_json(
        "militar_expenditure",
        list(map(lambda x: {
            "Name": x["Name"],
            "2018": x["2018"]
        }, me_top10)))


def start2():
    """Abre el csv, guarda la información en una lista de diccionarios,
    el map nos da los 10 más fatales de la historia y
    mete las localizaciones y las fatalidades a la función create_json
    """
    with open(os.path.join(
            os.getcwd(),
            f"Data_files{os.sep}Airplane_Crashes_and_Fatalities_Since_1908.csv"
    ),
              "r",encoding="utf-8") as airplanes_data:
        airplanes_list = list(csv.DictReader(airplanes_data))
    airplane_top10 = sorted(airplanes_list,
                            key=lambda x: 0
                            if x["Fatalities"] == "" else int(x["Fatalities"]),
                            reverse=True)[:10]
    create_json(
        "airplane_accidents",
        list(
            map(
                lambda x: {
                    "Location": x["Location"],
                    "Fatalities": x["Fatalities"]
                }, airplane_top10)))
