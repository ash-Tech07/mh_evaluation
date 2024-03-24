from chatbot_diagnostics import HAMD, PHQ9, json_loader

questionnaire_loader = lambda name: json_loader("questionnaires/", name)
index = questionnaire_loader("index.json")

print ("\nHello, I am a chatbot.")
# PHQ9(filename = "phq-9.json")
HAMD()
print ("\nThank you for your responses.")

# general support services to recommend after survey is complete
try:
    print("\nIf you are in need of immediate support, please consider services like the following:\n")
    with open("data/services.txt", "r") as file:
        for line in file.read().split("\n"):
            print(line.strip())
except Exception as e:
    print("File Not Found!")



    
