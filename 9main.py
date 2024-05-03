def load_symptoms(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def load_diseases(filename):
    disease_data = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            disease = parts[0].strip()
            symptoms = [symptom.strip() for symptom in parts[1].split(',')]
            disease_data[disease] = symptoms
    return disease_data

def medical_expert_system():
    print("Hello! This is a medical expert system. ")
    print("Do you feel any of the following symptoms? Reply yes or no /n")

    symptoms = load_symptoms('symptoms.txt')
    diseases = load_diseases('diseases.txt')

    user_symptoms = {}
    for symptom in symptoms:
        response = input(symptom + ": ").lower()
        if response == "yes":
            user_symptoms[symptom] = True

    possible_diseases = []
    for disease, disease_symptoms in diseases.items():
        if all(symptom in user_symptoms for symptom in disease_symptoms):
            possible_diseases.append(disease)

    if possible_diseases:
        print("The disease that you have is : ", ", ".join(possible_diseases))
    else:
        print("No specific disease could be determined based on the symptoms provided.")

    response = input("Would you like to diagnose some other symptoms? Reply yes or no: ").lower()
    if response == "yes":
        medical_expert_system()
    else:
        print("Thank you for using the medical expert system.")

medical_expert_system()
