from mysql.connector import Error
from expert import MedConsult
import mysql.connector
import pandas as pd
import os
import warnings

#FOR FINAL USE ONLY, IMPORTANT CODE WARNINGS MAY BE IGNORED WHILE DEBUGGING!
warnings.filterwarnings("ignore")

diseases_LIST, diseases_SYMP_LIST = [], []
diseases_SYMP_MAP, diseases_DESC_MAP, diseases_TREAT_MAP = {}, {}, {}

#creates connection to MySQL local DB
def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = database,
        buffered = True)
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
def process_DB_knowledge():
    cursor = connection.cursor()
    diseases_list = get_DB_diseases(cursor)

    for disease in diseases_list:
        cursor.execute(f"SELECT {disease} FROM medicaldiagnosis.symptoms")
        Symptoms = []
        for row in cursor:
            for field in row:
                Symptoms.append(field)
        diseases_SYMP_LIST.append(Symptoms)
        diseases_SYMP_MAP[str(Symptoms)] = disease

        cursor.execute(f"SELECT description FROM medicaldiagnosis.diseases WHERE disease = '{disease}'")
        description =  pd.read_sql(f"SELECT description FROM medicaldiagnosis.diseases WHERE disease = '{disease}'", connection)
        diseases_DESC_MAP[disease] = description.iloc[0,0]

        cursor.execute(f"SELECT treatment FROM medicaldiagnosis.diseases WHERE disease = '{disease}'")
        treatment =  pd.read_sql(f"SELECT treatment FROM medicaldiagnosis.diseases WHERE disease = '{disease}'", connection)
        diseases_TREAT_MAP[disease] = treatment.iloc[0,0]

def get_disease_DESC(disease): return diseases_DESC_MAP[disease]

def get_disease_TREAT(disease): return diseases_TREAT_MAP[disease]

def if_unmatched(disease):
    disease_DESC = get_disease_DESC(disease)
    disease_TREAT = get_disease_TREAT(disease)
    os.system('cls')
    print(f"Your symptoms mostly match with: {disease}\n")
    print(f"Description: {disease_DESC}\n")
    print(f"Treatment: {disease_TREAT}\n")
    print(f"-----------------------------------------------")

#program entry point for greeting class creation and loop while user exits the program
if __name__ == "__main__":
    process_DB_knowledge()
    engine = MedConsult(diseases_SYMP_MAP, if_unmatched, get_disease_TREAT, get_disease_DESC)

    while 1:
        engine.reset()
        engine.run()
        print("\nEnter any key to diagnose some other symptoms or enter 'EXIT' to quit...")
        if input().lower() == "EXIT":
            exit()