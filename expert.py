from experta import *
import os

def input_validation(question):
        while True:
            data = input(question)
            if not data:
                print("Sorry, you must enter an answer.")
                continue
            else:
                if data.lower() not in ('no', 'low', 'high'):
                    print("Not an appropriate choice.")
                else:
                    break
        return data

class MedConsult(KnowledgeEngine):
    def __init__(self, symptom_MAP, if_unmatched, get_disease_TREAT, get_disease_DESC):
        self.symptom_map = symptom_MAP
        self.if_unmatched = if_unmatched
        self.get_disease_DESC = get_disease_DESC
        self.get_disease_TREAT = get_disease_TREAT
        KnowledgeEngine.__init__(self)

    #code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        os.system('cls')
        print("###################################################################")
        print("#################### Medical Diagnosis Bot ########################")
        print("###################################################################")
        print("\nDo you feel any of the following symptoms? (Enter 'high', 'low' or 'no')")
        yield Fact(action = "find_disease")

    #defines the facts, the input data from user
    @Rule(Fact(action = "find_disease"), NOT(Fact(headache = W())), salience = 4)
    def SYMP_0(self):
        self.declare(Fact(headache = input_validation("Headache: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(back_pain = W())), salience = 1)
    def SYMP_1(self):
        self.declare(Fact(back_pain = input_validation("Back pain: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(chest_pain = W())), salience = 1)
    def SYMP_2(self):
        self.declare(Fact(chest_pain = input_validation("Chest pain: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(cough = W())), salience = 3)
    def SYMP_3(self):
        self.declare(Fact(cough = input_validation("Cough: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(fainting = W())), salience = 1)
    def SYMP_4(self):
        self.declare(Fact(fainting = input_validation("Fainting: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(fatigue = W())), salience = 1)
    def SYMP_5(self):
        self.declare(Fact(fatigue = input_validation("Fatigue: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(sunken_eyes = W())), salience = 1)
    def SYMP_6(self):
        self.declare(Fact(sunken_eyes = input_validation("Sunken eyes: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(low_body_temp = W())), salience = 1)
    def SYMP_7(self):
        self.declare(Fact(low_body_temp = input_validation("Low body temperature: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(restlessness = W())), salience = 1)
    def SYMP_8(self):
        self.declare(Fact(restlessness = input_validation("Restlessness: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(sore_throat=W())), salience = 1)
    def SYMP_9(self):
        self.declare(Fact(sore_throat = input_validation("Sore throat: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(fever=W())), salience = 1)
    def SYMP_10(self):
        self.declare(Fact(fever = input_validation("Fever: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(nausea=W())), salience=1)
    def SYMP_11(self):
        self.declare(Fact(nausea=input_validation("Nausea: ")))

    @Rule(Fact(action = "find_disease"), NOT(Fact(blurred_vision = W())), salience = 1)
    def SYMP_12(self):
        self.declare(Fact(blurred_vision = input_validation("Blurred_vision: ")))

    #defines the rules, restrictions applied to the facts for checking for each disease match
    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "high"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "low"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "high"),
        Fact(blurred_vision = "no"),
    )
    def DIS_0(self):
        self.declare(Fact(disease = "Jaundice"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "high"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_1(self):
        self.declare(Fact(disease = "Alzheimers"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "high"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "low"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_2(self):
        self.declare(Fact(disease = "Arthritis"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "high"),
        Fact(cough = "low"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "high"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_3(self):
        self.declare(Fact(disease = "Tuberculosis"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "high"),
        Fact(cough = "high"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "low"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_4(self):
        self.declare(Fact(disease = "Asthma"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "low"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "high"),
        Fact(fainting = "no"),
        Fact(sore_throat = "high"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "low"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_5(self):
        self.declare(Fact(disease = "Sinusitis"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "low"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_6(self):
        self.declare(Fact(disease = "Epilepsy"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "high"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "high"),
        Fact(blurred_vision = "no"),
    )
    def DIS_7(self):
        self.declare(Fact(disease = "Heart_Disease"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "high"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "low"),
        Fact(blurred_vision = "low"),
    )
    def DIS_8(self):
        self.declare(Fact(disease = "Diabetes"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "low"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "high"),
        Fact(blurred_vision = "low"),
    )
    def DIS_9(self):
        self.declare(Fact(disease = "Glaucoma"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "high"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "low"),
        Fact(blurred_vision = "no"),
    )
    def DIS_10(self):
        self.declare(Fact(disease = "Hyperthyroidism"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "high"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "no"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "high"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "high"),
        Fact(blurred_vision = "no"),
    )
    def DIS_11(self):
        self.declare(Fact(disease = "Heat_Stroke"))

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "no"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "no"),
        Fact(cough = "no"),
        Fact(fainting = "yes"),
        Fact(sore_throat = "no"),
        Fact(fatigue = "no"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "high"),
        Fact(fever = "no"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_12(self):
        self.declare(Fact(disease = "Hypothermia"))
    
    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = "high"),
        Fact(back_pain = "no"),
        Fact(chest_pain = "high"),
        Fact(cough = "high"),
        Fact(fainting = "no"),
        Fact(sore_throat = "high"),
        Fact(fatigue = "high"),
        Fact(restlessness = "no"),
        Fact(low_body_temp = "no"),
        Fact(fever = "high"),
        Fact(sunken_eyes = "no"),
        Fact(nausea = "no"),
        Fact(blurred_vision = "no"),
    )
    def DIS_13(self):
        self.declare(Fact(disease = "Coronavirus"))

    #check if user's input matches any disease in the knowledge base
    @Rule(Fact(action = "find_disease"), Fact(disease = MATCH.disease), salience =- 998)
    def disease(self, disease):
        disease_DESC = self.get_disease_DESC(disease)
        disease_TREAT = self.get_disease_TREAT(disease)
        os.system('cls')
        print(f"Your symptoms match with: {disease}\n")
        print(f"Description: {disease_DESC}\n")
        print(f"Treatment: {disease_TREAT}\n")
        print("-----------------------------------------------")

    @Rule(
        Fact(action = "find_disease"),
        Fact(headache = MATCH.headache),
        Fact(back_pain = MATCH.back_pain),
        Fact(chest_pain = MATCH.chest_pain),
        Fact(cough = MATCH.cough),
        Fact(fainting = MATCH.fainting),
        Fact(sore_throat = MATCH.sore_throat),
        Fact(fatigue = MATCH.fatigue),
        Fact(low_body_temp = MATCH.low_body_temp),
        Fact(restlessness = MATCH.restlessness),
        Fact(fever = MATCH.fever),
        Fact(sunken_eyes = MATCH.sunken_eyes),
        Fact(nausea = MATCH.nausea),
        Fact(blurred_vision = MATCH.blurred_vision),
        NOT(Fact(disease = MATCH.disease)),
        salience =- 999
    )

    def not_matched(self, headache,back_pain, chest_pain,cough,fainting,sore_throat,
        fatigue, restlessness, low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
        os.system('cls')
        print("\nThe bot did not find any diseases that match your exact symptoms.")
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat,
        fatigue, restlessness, low_body_temp, fever, sunken_eyes, nausea, blurred_vision]
        max_count, max_disease = 0, ""
        for key, val in self.symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "high" or lis[j] == "low" or lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease != "":
            self.if_unmatched(max_disease)