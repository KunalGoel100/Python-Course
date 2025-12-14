class quizBrain:

    def __init__(self,list):
        self.questionNumber = 0
        self.questionList = list
        self.score = 0

    def checkAnswer(self, userAnswer):
        if userAnswer == self.questionList[self.questionNumber].answer:
            self.score += 1
            print('Correct')
        else:
            print('Incorrect')
        print(f'Total Score: {self.score}/{self.questionNumber+1}\n')

    def nextQuestion(self):
        userAnswer = input(f'Q.{self.questionNumber+1}: {self.questionList[self.questionNumber].text} (True/False)\t')
        self.checkAnswer(userAnswer)
        self.questionNumber += 1
        return userAnswer

    def stillQuestion(self):
        if self.questionNumber <= len(self.questionList)-1:
            return 1
        else:
            return 0

