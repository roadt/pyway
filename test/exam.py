#!/usr/bin/env python


import random

class Exam:
    def __init__(self, cnt):
        self.cnt = cnt
        self.current_no = 0;

        self.score_per_question = 100/ self.cnt
        self.current_score = 0

        self.low_limit = 0
        self.high_limit  = 100

        self.operators = [ '+', '-' ]
      
        self.max_tries = 3
        self.assistant = True
#
# @ret   (a, op,  b, answer)
#
    def get_question(self):
        a = random.randint(self.low_limit, self.high_limit)
        b = random.randint(self.low_limit, self.high_limit)
        if a < b:
            a , b = b, a
        op = '+'
        if len(self.operators) == 1:
            op = self.operators[0]
        else:
            opIdx = random.randint(0, len(self.operators) -1)
            op = self.operators[opIdx]
        answer = self.get_answer(a,b,op)
        return (a,op, b, answer)
#
#
#

    def get_answer(self, a, b, op):
        if op == '+':
            return a+b
        if op == '-':
            return a-b
        if op == '*':
            return a*b
        if op == '/':
            return a/b

    def get_input(self):
        input_value = 0
        while True:
            input_text = raw_input()
            if input_text.isdigit():
                input_value = int(input_text)
                break;
        return input_value

    def start(self):
        print "] Exam start "
        print "] You have %s questions to answer" % self.cnt
        print "] Possible operators are %s" % self.operators.__str__()
        
        
        while self.current_no < self.cnt:
            print "> the %s question" % (self.current_no+1)
            question  = self.get_question()
            correct_answer =  question[3]
            tries = 0
            while tries < self.max_tries:
                if tries == 0:
                    print "New question:"
                else:
                    print "Wrong, retry ..."
                print " %s %s %s  =?" % question[0:3]
                
                input_value = self.get_input()
                if input_value == correct_answer:
                    print "Right! Good answer!"
                    self.current_score = self.current_score + self.score_per_question
                    self.current_no = self.current_no + 1
                    break;
                else:
                    tries = tries + 1
            if tries >= self.max_tries:   # no right
                print "answer is %s" % correct_answer 
                
                        
            

            



        
if __name__ == '__main__':
    e = Exam(100)
    e.start()



