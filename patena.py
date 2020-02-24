#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import errno
import random
import sys


def create_directory(name):
    try:
        os.mkdir(name)

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def create_file(path):
    DATA_RESULT = "MOCKQVCLTAELGLIL"
    file = open(path + "/sequenceFASTA", "w")
    file.write(">gi" + os.linesep)
    if path.__contains__(DIR_ROOT_INPUT):
        file.write(MOCK_INPUT_DATA)
    if path.__contains__(DIR_ROOT_OUTPUT):
        DATA_RESULT = MOCK_OUTPUT_DATA
        file.write(DATA_RESULT)
    else:
        file.write(DATA_RESULT)
    file.close()
    return DATA_RESULT


DIR_ROOT_INPUT = 'Input'
DIR_ROOT_OUTPUT = 'Output'
MOCK_INPUT_DATA = 'MOCKQVCLTAELGLIL'
MOCK_OUTPUT_DATA = 'MOCKFINALRESULTTAELGLIL'

cantDeArgumentos = len(sys.argv)
action = ""
parameter_action = ""
# print(cantDeArgumentos)
# print sys.argv
if cantDeArgumentos == 3:
    action = sys.argv[1]
    parameter_action = sys.argv[2]

    if action.__contains__('--seq'):
        print "Iniciando secuencia...", parameter_action

    if action.__contains__('--length'):
        print "Iniciando secuencia con longitud...", parameter_action

if cantDeArgumentos == 2:
    action = sys.argv[1]
    if action == "--verbose":
        print("El resultado final se mostrara en consola tambien")

create_directory(DIR_ROOT_INPUT)
create_directory(DIR_ROOT_OUTPUT)

Id = random.randrange(1000, 9999)

print(" Procesando su cadena...")
print("Su Id de proceso: " + str(Id))

PATH_INPUT = DIR_ROOT_INPUT + '/' + str(Id)
PATH_OUTPUT = DIR_ROOT_OUTPUT + '/' + str(Id)

create_directory(PATH_INPUT)
create_directory(PATH_OUTPUT)

create_file(PATH_INPUT)
result_log = create_file(PATH_OUTPUT)

print ("Generando archivos de input y output")

if action.__contains__('--verbose'):
    print (result_log)

print ("FIN DEL PROCESO")
