from greetings import Greetings
import mysql.connector
from mysql.connector import Error
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = database
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

connection = create_server_connection("localhost", "root", "hejefica", "medicaldiagnosis")

def get_DB_diseases(cursor):
    cursor.execute('SELECT disease FROM medicaldiagnosis.diseases')
    Diseases = []
    for row in cursor:
        for field in row:
            Diseases.append(field)
    return Diseases

#loads the knowledge from .txt files into variables to allow the code to use it
def preprocess():
    cursor = connection.cursor()
    diseases_list = get_DB_diseases(cursor)
    #print(diseases_list)

    for disease in diseases_list:
        #disease_s_file = cursor.execute(f'SELECT description FROM medicaldiagnosis.diseases WHERE disease = {disease}')
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()

        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

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
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments + "\n")

#driver function
if __name__ == "__main__":
    preprocess()
    #creating class object
    engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details)
    #loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("Would you like to diagnose some other symptoms?\n Reply yes or no")
        if input() == "no":
            exit()
