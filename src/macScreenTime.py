# Requiere ---> pip3 install PyObjC
import time
import json
from AppKit import NSWorkspace


"""
Variables iniciales
"""


def serialize():
    return {
        'app_name': get_active_app_name()
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
    previous_app_name = 'app inventada'
    while True:

        new_app_name = serialize()
        # if 'Google Chrome' in new_app_name:
        #     new_app_name = url_to_name()
        if previous_app_name != new_app_name:
            print(new_app_name)
            app_list.append(new_app_name)
            # activity_name = active_app_name

            # if not first_time:

            # with open('apps.json', 'w') as json_file:
            #     json.dump()

            previous_app_name = new_app_name
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

