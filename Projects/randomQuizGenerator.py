import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
    quizfile=open(f'capitalsquiz{quiznum+1}.txt','w')
    answerfile=open(f'capitalsquizanswers{quiznum+1}.txt','w')
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n') 
    quizfile.write((' ' * 20) + f'State Capitals Quiz (Form{quiznum + 1})')
    quizfile.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for i in range(50):
        correctanswer=capitals[states[i]]
        wronganswer=list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer=random.sample(wronganswer,3)
        answeroptions=wronganswer+[correctanswer]
        random.shuffle(answeroptions)
        quizfile.write(f'{i+1}.Capital of {states[i]}:\n')
        for num in range(4):
            quizfile.write(f'{'ABCD'[num]} {answeroptions[num]}\n')
        quizfile.write('\n')
        answerfile.write(f'{i+1} {'ABCD'[answeroptions.index(correctanswer)]}\n')
    quizfile.close()
    answerfile.close()
