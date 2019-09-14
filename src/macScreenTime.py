#
#  /**
#   * Created by ${AUTHOR}
#   * Date: 2019
#   * Time: 12:54 PM
#   */

#
#  /**
#   * Created by ${AUTHOR}
#   * Date: 2019
#   * Time: 12:54 PM
#   */

# Requiere ---> pip3 install PyObjC
# Not usable inside venv? weird
import time
import json
from datetime import datetime
from AppKit import NSWorkspace
from Foundation import NSAppleScript
import sys

from pprint import pprint

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

def url_to_name(url):
    """
    Convertimos el string de URL en solo la pagina principal, quitando lo especifico
    :param url:
    :return: string in a dictionary
    """
    string_list = url.split('/')
    if string_list[2].startswith('www.'):
        string_list[2] = string_list[2][4:]
    return string_list[2]


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


try:
    """
    Ubica el nombre de la app en uso en un archivo
    Si tenia una app anterior salvada, se compara y salva si cambia.
    """
    app_list = []
    start_time = ''
    previous_app_name = 'algo inventado'

    while True:

        current_time    = datetime.now()
        new_app_name    = get_active_app_name()

        if 'Safari' in new_app_name:
            # create applescript code object
            s = NSAppleScript.alloc().initWithSource_( # 'tell app "Safari" to {URL,name} of tabs of windows'
                "tell application \"Safari\" to return URL of front document as string"
            )
            # execute AS obj, get return value
            result,_ = s.executeAndReturnError_(None)

            time.sleep(1)

            # find number of tabs based on number of groups in the URL set
            # num_windows = result.descriptorAtIndex_(1).numberOfItems()

            # create a simple dictionary
            # tabs = dict(('window {0:}'.format(win_num), []) for win_num in range(1, num_windows + 1))

            # for page_idx, win_num in enumerate(tabs, start=1):
            #     urls = [result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).descriptorAtIndex_(tab_num).stringValue()
            #             for tab_num in range(1, result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).numberOfItems() + 1)]
            #
            #     titles = [result.descriptorAtIndex_(2).descriptorAtIndex_(page_idx).descriptorAtIndex_(tab_num).stringValue().encode('ascii', 'xmlcharrefreplace')
            #               for tab_num in range(1, result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).numberOfItems() + 1)]
            #
            #     tabs[win_num] = zip(urls, titles)

            url = result.stringValue()

            pprint(url_to_name(url))


        #     new_app_name = url_to_name()

        if previous_app_name != new_app_name:
            if start_time == '':
                start_time = datetime.now()

            '''
            Calculamos el tiempo que duro en la app que este de focus.
            '''
            time_on_app = current_time-start_time
            '''
            Hacemos el tiempo en formato datetime.timedelta manejable para nosotros con la funcion convert_timedelta.
            '''
            hours, minutes, seconds = convert_timedelta(time_on_app)

            print(previous_app_name)
            print('{} minutes, {} seconds'.format(minutes, seconds))
            # print(str(time_on_app))


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
