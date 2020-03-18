#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import errno
import random
import sys
from datetime import date


def create_directory(name):
    try:
        os.mkdir(name)

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def getJson():
    data = {'Error': {'description': 'Error parametros invalidos', 'date': str(date.today)}}

    if SonArgumentosValidos():
        if sys.argv.__contains__("--noMutations"):
            data = resultAnalyze
        else:
            data = resultDesign

    return data

def getName(DATA_RESULT):
    if json.dumps(DATA_RESULT).__contains__('Error'):
        return "error"

    return "results"

def create_file(path):
    DATA_RESULT = getJson()
    if path.__contains__(DIR_ROOT_INPUT):
        file = open(path + "/input.json", "w")
        file.write(MOCK_INPUT_DATA)
    if path.__contains__(DIR_ROOT_OUTPUT):
        filename = getName(DATA_RESULT)
        file = open(path + "/" + filename + ".json", "w")
        file.write(str(DATA_RESULT))
    file.close()
    return DATA_RESULT

def SonArgumentosValidos():
    composition = "average"
    userComposition = {"A": -999, "R": -999, "N": -999, "D": -999, "C": -999, "E": -999, "Q": -999, "G": -999,
                       "H": -999,
                       "I": -999, "L": -999, "K": -999, "M": -999, "F": -999, "P": -999, "S": -999, "T": -999,
                       "W": -999,
                       "Y": -999, "V": -999}

    valido = True
    index = 0
    #   print ("cantidad de argumentos", len(sys.argv))
    while valido == True and index < len(sys.argv) - 2:
        index = index + 1
        arg = sys.argv[index]
        if (arg == '--length') and (index < len(sys.argv)):
            length = int(sys.argv[index + 1])
        elif (arg == '--beta') and (index < len(sys.argv)):
            beta = float(sys.argv[index + 1])
        elif (arg == '--seq') and (index < len(sys.argv)):
            sequence = sys.argv[index + 1]
            length = len(sequence)
            rand = False
            index = index + 1
        elif arg == '--noMutations':
            global_evaluation = True
        elif (arg == '--db') and (index < len(sys.argv)):
            database = sys.argv[index + 1]
        elif arg == '--blastweb':
            blastWeb = True
        elif arg == '--uvsilent':
            uvsilent = True
        elif (arg == '--netcharge') and (index < len(sys.argv)):
            targetNetCharge = int(sys.argv[index + 1])
            evaluateNetCharge = True


        ##   SELECT WHICH TOOLS WONT ME EVALUATED
        elif (arg == '--noblast'):
            runBlast = False
        elif (arg == '--notango'):
            runTango = False
        elif (arg == '--noelm'):
            runElm = False
        elif (arg == '--noiupred'):
            runIupred = False
        elif (arg == '--noanchor'):
            runAnchor = False
        elif (arg == '--noprosite'):
            runProsite = False
        elif (arg == '--nolimbo'):
            runLimbo = False
        elif (arg == '--notmhmm'):
            runTmhmm = False
        elif (arg == '--nopasta'):
            runPasta = False
        elif (arg == '--nowaltz'):
            runWaltz = False
        elif (arg == '--noamyloidpattern'):
            runAmyloidPattern = False

        elif (arg == '--maxiterations') and (index < len(sys.argv)):
            maxIterations = int(sys.argv[index + 1])

            # CHECK IF THE USER DEFINED ANY OF THE AAs FREQUENCIES

        # elif (arg== '--composition') and (index < len(sys.argv)):
        # composition = sys.argv[index+1]
        # if (composition=="user_specified"):  #frequencies specified by parameter
        # for j in range(index+2,len(sys.argv),2):
        elif (arg == '-a'):
            userComposition['A'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-r'):
            userComposition['R'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-n'):
            userComposition['N'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-d'):
            userComposition['D'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-c'):
            userComposition['C'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-q'):
            userComposition['Q'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-e'):
            userComposition['E'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-g'):
            userComposition['G'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-h'):
            userComposition['H'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-i'):
            userComposition['I'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-l'):
            userComposition['L'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-k'):
            userComposition['K'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-m'):
            userComposition['M'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-f'):
            userComposition['F'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-p'):
            userComposition['P'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-s'):
            userComposition['S'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-t'):
            userComposition['T'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-w'):
            userComposition['W'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-y'):
            userComposition['Y'] = int(sys.argv[index + 1])
            composition == "user_specified"
        elif (arg == '-v'):
            userComposition['V'] = int(sys.argv[index + 1])
            composition == "user_specified"



        ###   OUTPUT DETAILS
        elif (arg == '--verbose'):
            verbose = True
        elif (arg == '--detailed') and (index < len(sys.argv)):  # print detailed output for each (to output file)
            detailed_output = True
            detailedOutFile = open(sys.argv[index + 1], 'w')
            index = index + 1
        elif (arg == '--minoutput') and (index < len(sys.argv)):
            minimalOutput = True
            logsPath = sys.argv[index + 1]
            index = index + 1
        elif (arg == '--testoutput') and (index < len(sys.argv)):
            testing = True
            testOutputPath = sys.argv[index + 1]
            index = index + 1
        elif (arg == '--gettime'):
            testTimes = True
        elif (arg == '--jobid') and (index < len(sys.argv)):
            exeId = sys.argv[index + 1]
            index = index + 1
        else:
            valido = False

    return valido


DIR_ROOT_INPUT = 'Input'
DIR_ROOT_OUTPUT = 'Output'
MOCK_INPUT_DATA = 'MOCKQVCLTAELGLIL'

resultAnalyze = {
    "analysis": {
        "blast": {
            "prop1": "value1",
            "prop2": "value2"
        },
        "otro": {
            "prop3": "value3"
        }
    }
}
resultDesign = {
    "design": {
        "initialSequence": "ABC",
        "finalSequence": "DEF",
        "steps": [
            {
                "changed": "(A) -> D ", "score": "1"
            }
        ]
    }
}

cantDeArgumentos = len(sys.argv)
action = ""
parameter_action = ""

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

if sys.argv.__contains__('--verbose'):
    print (result_log)

print ("FIN DEL PROCESO")
