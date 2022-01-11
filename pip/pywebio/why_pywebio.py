


from random import shuffle

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

from random import randint
def rand_questions(cnt):
    ret = []
    for i in range(cnt):
        a = randint(1, 100)
        b = randint(1, 100)
        r = a + b

        options  = [randint(1, 200),randint(1, 200),r]
        shuffle(options)
        ret.append({'question':"%s+%s=?"%(a,b), 'options':options, 'answer':r})
    return ret

questions = [
    {'question':"1+1=?", 'options':[1,2,3], 'answer':2}
]

questions = rand_questions(5)

def main():
    idxs = list(range(len(questions)))
    shuffle(idxs)
    for cnt, idx in enumerate(idxs):
        q = questions[idx]
        answer = radio('Question-%s: %s' % (cnt+1, q['question']), options=q['options'])
        if answer != q['answer']:
            put_error(f'Game Over. You has passed {cnt} questions.')
            break
    else:
        put_success(f'Congratulations! You have passed all the {len(questions)} quetions.')


if __name__ == '__main__':
#    start_server(main, port=8080)
    main()

