# example in p.219
from survey import AnonymousSurvey

#define question, make instance (survey)
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

#show question, store responses to question
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#show survey results
print("\nThank you for participating!")
language_survey.show_results()