# Requiere ---> pip3 install PyObjC
import time
import json
from datetime import datetime
from AppKit import NSWorkspace

"""
Variables iniciales
"""


def serialize():
    return {
        'app_name': previous_app_name,
        'date': str(time_on_app)
    }


def get_active_app_name():
    """
    Asigna a active_app la app en uso y
    :return: el nombre de la app en uso
    """
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    return active_app['NSApplicationName']
    # # app_name    = app['NSApplicationName']
    # appName     = active_app.localizedName()
    # appIcon     = active_app.icon()
    # appURL      = active_app.bundleURL()
    # # icon      = app['NSWorkspaceApplicationKey'].icon()             Uso esto para salvar el icono. Posibles usos
    # print(appName)
    # print(appURL)


# print(get_active_app_name())

try:
    """
    Ubica el nombre de la app en uso en un archivo
    Si tenia una app anterior salvada, se compara y salva si cambia.
    """
    app_list = []
    start_time = ''
    previous_app_name = 'algo inventado'

    while True:

        current_time = datetime.now()
        new_app_name = get_active_app_name()
        # if 'Google Chrome' in new_app_name:
        #     new_app_name = url_to_name()

        if previous_app_name != new_app_name:
            if start_time == '':
                start_time = datetime.now()

            '''
            Calculamos el tiempo que duro en la app que este de focus.
            '''
            time_on_app = current_time-start_time
            print(previous_app_name)
            print(str(time_on_app))

            app_list.append(serialize())

            start_time = current_time
            previous_app_name = new_app_name
            # activity_name = active_app_name

            # if not first_time:

            # with open('apps.json', 'w') as json_file:
            #     json.dump()

            """
            Escribo en un archivo la lectura constante de la app en focus
            """
            with open('apps.json', 'w') as json_file:
                json.dump(app_list, json_file, indent=4)
                # json_file.append(new_app_name) no funciono como estimabamos para el file, lo tenemos que meter en
                # una lista
        time.sleep(1)

except KeyboardInterrupt:
    raise
