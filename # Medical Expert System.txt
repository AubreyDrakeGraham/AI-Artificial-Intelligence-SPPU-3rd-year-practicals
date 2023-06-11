# Medical Expert System

def ask_question(question):
    """Ask a yes/no question and return the user's response."""
    while True:
        response = input(question + " (yes/no): ").lower()
        if response == "yes" or response == "no":
            return response
        print("Please answer with 'yes' or 'no'.")

def diagnose():
    """Diagnose the medical condition based on user's symptoms."""
    print("Welcome to the Medical Expert System!")
    print("Please answer the following questions.")

    # Ask questions to determine the condition
    fever = ask_question("Do you have a fever?")
    cough = ask_question("Do you have a cough?")
    headache = ask_question("Do you have a headache?")
    sore_throat = ask_question("Do you have a sore throat?")
    fatigue = ask_question("Do you feel fatigued?")

    # Make a diagnosis based on the symptoms
    if fever == "yes" and cough == "yes" and headache == "yes":
        print("You may have the flu.")
    elif sore_throat == "yes" and fatigue == "yes":
        print("You may have a viral infection.")
    else:
        print("I'm sorry, I couldn't determine the condition based on your symptoms.")

diagnose()
