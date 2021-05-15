#Reto 3 - Conversor de millas a kilómetros
#Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. Para no estar repitiendo este cálculo escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.


#Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.

MI_IN_KM = 1.609344
KM_IN_MI = 0.621371

CONVERSIONS = (
    {
        "id": 0,
        "name": "Miles to Kilometers",
        "converter": MI_IN_KM,
        "main_units": "miles",
        "result_units": "kilometers"
    }
    ,{
        "id": 1,
        "name": "Kilometers to Miles",
        "converter": KM_IN_MI,
        "main_units": "kilometers",
        "result_units": "miles"
    }
)

def option_selector ():
    option = ''
    is_first_time = True

    while option not in list(map(lambda option: option["id"], CONVERSIONS)):
        message = f"Hi\nPlease, select" if is_first_time == True else "It must be"
        options = "".join(map(lambda option: str(option["id"]) + ". " + option["name"] + ".\n", CONVERSIONS))
        option = int(
            input(
                f"{message} one of these options:\n{options}\n>>> "
            )
        )
        is_first_time = False

    return CONVERSIONS[option]

def run():
    conversion = option_selector()
    units = float(input(f'Please, add the number of {conversion["main_units"]}: '))

    result = units * conversion["converter"]
    print(str(units) + " " + conversion["main_units"] + " are " + str(result) + " " + conversion["result_units"])

if __name__ == "__main__":
    run()
