from mysql.connector import Error
from greetings import Greetings
import mysql.connector
import pandas as pd
import os
import warnings

#FOR FINAL USE ONLY, IMPORTANT CODE WARNINGS MAY BE IGNORED WHILE DEBUGGING!
warnings.filterwarnings("ignore")

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

#creates connection to MySQL local DB
def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = database,
        buffered = True
        )
        #print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

connection = create_server_connection("localhost", "root", "hejefica", "medicaldiagnosis")

#gets a disease list from DB 
def get_DB_diseases(cursor):
    cursor.execute('SELECT disease FROM medicaldiagnosis.diseases')
    Diseases = []
    for row in cursor:
        for field in row:
            Diseases.append(field)
    return Diseases

#loads the knowledge from MySQL DB into variables
def preprocess():
    cursor = connection.cursor()
    diseases_list = get_DB_diseases(cursor)

    for disease in diseases_list:
        cursor.execute(f"SELECT {disease} FROM medicaldiagnosis.symptoms")
        Symptoms = []
        for row in cursor:
            for field in row:
                Symptoms.append(field)
        diseases_symptoms.append(Symptoms)
        symptom_map[str(Symptoms)] = disease

        cursor.execute(f"SELECT description FROM medicaldiagnosis.diseases WHERE disease = '{disease}'")
        description =  pd.read_sql(f"SELECT description FROM medicaldiagnosis.diseases WHERE disease = '{disease}'", connection)
        d_desc_map[disease] = description.iloc[0,0]

        cursor.execute(f"SELECT treatment FROM medicaldiagnosis.diseases WHERE disease = '{disease}'")
        treatment =  pd.read_sql(f"SELECT treatment FROM medicaldiagnosis.diseases WHERE disease = '{disease}'", connection)
        d_treatment_map[disease] = treatment.iloc[0,0]

def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)

    return symptom_map[str(symptom_list)]

def get_details(disease): return d_desc_map[disease]

def get_treatments(disease): return d_treatment_map[disease]

def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    os.system('cls')
    print(f"Your symptoms mostly match with: {id_disease}\n")
    print(f"Description: {disease_details}\n")
    print(f"Treatment: {treatments}\n")
    print("-----------------------------------------------")

#program entry point
if __name__ == "__main__":
    preprocess()

    #creating class object
    engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details)

    #loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("\nWould you like to diagnose some other symptoms? (Reply yes or no)")
        if input() == "no":
            exit()
