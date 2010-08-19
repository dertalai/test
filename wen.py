#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Script para configurar automáticamente al ratón Wen cuando éste se pone a
cargar y se producen fallos al enviar pulsaciones falsas
"""

import os
import re

pipe = os.popen("xinput list")
listaIds = []
for line in pipe.readlines():
    if "Bluetooth" in line:
        print "Detectado: " + line
        obj = re.search("id=(\d+)", line)
        if obj != None:
            listaIds.append(obj.group(1))
pipe.close()


for id in listaIds:
    """
    print "Probando dispositivo " + id + "..."
    pipe = os.popen("xinput test " + id)
    contador = 10
    for line in pipe.readlines():
        print line
        obj = re.search("button.*?(\d+)", line)
        if obj != None:
            print "se pulsó " + obj.group(1)
            contador -= 1
            if contador == 0:
                break
    pipe.close()
    """
    #Eliminamos la pulsación 7
    os.popen("xinput set-button-map " + id + " 1 2 3 4 5 6 0")
