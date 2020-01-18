# ADD MAC OS ShEBANG Line
# RandomQuizGenerator.py
# Creates a series of quizes with questions and answers in a random order + there are answer keys

import random

#the quiz data, states = Keys     Capitals = Values

capitals = {'Alabama': 'Montgomery','Alaska': 'Juneau','Arizona': 'Phoenix','Arkansas':
            'Little Rock','California': 'Sacramento','Colorado': 'Denver','Connecticut': 'Hartford',
            'Delaware': 'Dover','Florida': 'Tallahassee','Georgia': 'Atlanta','Hawaii': 'Honolulu',
            'Idaho': 'Boise','Illinois': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Moines',
            'Kansas': 'Topeka','Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge','Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts': 'Boston',
            'Michigan': 'Lansing','Minnesota': 'St. Paul','Mississippi': 'Jackson',
            'Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln','Nevada': 'Carson City',
            'New Hampshire': 'Concord','New Jersey': 'Trenton','New Mexico': 'Santa Fe','New York': 'Albany',
            'North Carolina': 'Raleigh','North Dakota': 'Bismark',
            'Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem','Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence','South Carolina': 'Columbia','South Dakota': 'Pierre','Tennessee': 'Nashville',
            'Texas': 'Austin','Utah': 'Salt Lake City','Vermont': 'Montpelier','Virginia': 'Richmond',
            'West Virginia': 'Charleston','Wisconsin': 'Madison','Wyoming': 'Cheyenne', }

# Generate 35 Quiz files
for quizNum in range(35):
    #Create the Quiz and Answer Key files  #WTF does the % do below
    quizFile = open("capitalsquiz%.txt" % (quizNum + 1), "w") #need to make a full file path when actually executing this program save to folder and desktop so its easily deletabe
    answerKeyFile = open("capitalsquiz_answers%.txt" % (quizNum + 1), 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\nDate:\nPeriod:\n\n')
    quizFile.write(' ' * 20 + "State Capitals Quiz (Form %s)" %(quizNum +1))
    quizFile.write('\n\n')

    #Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):

        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]] #QuestionNum is possibly used to reference a separate state for each question
        wrongAnswers = list(capitals.values()) # creates a list of all capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #index finds the correct answer and deletes it
        wrongAnswers = random.sample(wrongAnswers,3) # takes three random samples and uses them as wrong answers
        answerOptions = wrongAnswers + [correctAnswer] # creates an list obj w all right and wrong answers
        random.shuffle(answerOptions) # puts the 4 possible answers in a random order

    # writes the question and the answer options to the quiz file
        quizFile.write('%s What is the capital of %s?\n' % questionNum + 1, # again wtf is the % doing
                       states[questionNum]) # clean this up
        for i in range(4):
            quizFile.write("   %s. %s\n" %('ABCD'[i], answerOptions[i])) # puts the answer options next to ABCD, not suure how it does this though
            quizFile.write('\n')

        #write answer Key to the file
        answerKeyFile.write('%s. %\n'%questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)])
    quizFile.close() # clean up the highlighted above
    answerKeyFile.close()
    