#quiz App

#question sınıfı
#    ınstance Attributes
#       -text,choices,answer
#    ınstance methods
#       -checkAnswer('python')=>True ya da False

#q1=Question("en iyi programlama dili hangisidir?"["python","c#","java","dart"],"python")
#q2=Question("en popüler programlama dili hangisidie?",["python","java","C#","dart"],"python")
#q3=Question("en çok kazandıran programlama dili hangisidir",["python","java","dart","C#"],"python")

#sorular=[q1,q2,q3]

#Quiz sınıfı
#  instance Attributes
#       -questions,questionIndex,score
#  instance methods
#       -getQuestion()      => questionIndex'e göre question nesnesi getirir.
#       -displayQuestion()  => getQuestion() ile alınan nesneyi gösterir.
#       -loadQuestion()     => Testi başlatır.
#       -displayScore()     => Score bilgisini gösterir
#       -displayProgress()  => Testdeki ilerlemeyi gösterir.(5 sorunun 2.sorusundasınız)


#Her bir soruyu temsil edecek question nesnesi oluşturunuz

#Question sınıfı
#  -text  =>soru
#  -choices =>cevap şıkları
#  -answer =>soru

#checkAnswer() metodu ile cevap kontrolü yapınız

#q1.checkAnswer("cevap")=>True
#q1.checkAnswer("cevap")=>False
import random

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer== answer
class Quiz:
    def __init__(self,questions):
        self.questions= random.sample(questions,len(questions))
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[quiz.quesiton.Index]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f"soru {self.questionIndex+1}: {question.text}")

        for q in question.choices:
            print("-"+q)
        answer=input('cevap:')
        print(question.checkAnswer(answer))
q1=Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2=Question("en popüler programlama dili hangisidie?",["python","java","C#","dart"],"python")
q3=Question("en çok kazandıran programlama dili hangisidir",["python","java","dart","C#"],"python")
sorular=[q1,q2,q3]

quiz=Quiz(sorular)
print(quiz.questions[quiz.questionIndex].text)