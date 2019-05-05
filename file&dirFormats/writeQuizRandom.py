import random

capitals={'France':'Paris','Germany':'Berlin','Czech':'Pragha','Italy':'Roma',
          'Spain':'Madrid','Poland':'Warsaw','uk':'london','sweden':'stockholm','denmark':'kopenhaga','norwey':'oslo'}

for quizNum in range(3):
    quizFile=open('capitalquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile=open('capitalquiz_answer%s.txt' % (quizNum +1), 'w')

    quizFile.write('Name:\n\nDate:\n')
    quizFile.write((' '*15)+ 'State Capitals Quiz (Form %s)' %(quizNum+1))
    quizFile.write('\n\n')

    states=list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(10):
        correctAnswer=capitals[states[questionNum]]
        wrongAnswer=list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        ansOption=wrongAnswer+[correctAnswer]
        random.shuffle(ansOption)

        quizFile.write('%s.What is the capital of %s?\n' % (questionNum+1,states[questionNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i],ansOption[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum +1, 'ABCD'[ansOption.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()