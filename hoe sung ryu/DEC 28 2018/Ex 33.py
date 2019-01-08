'''Ex 33 Magic 8 ball'''

#1.general
import random as r

question_list=['Will I be rich and famous']
anw_ran_num_list=['Yes','No','Maybe','Ask again later.']

q_ran_num=0
    # r.randint(0,len(question_list)-1))
anw_ran_num=r.randint(0,len(anw_ran_num_list)-1)

print("What's your question?",question_list[q_ran_num],anw_ran_num_list[anw_ran_num],sep='\n')



#list shuffle
r.shuffle(question_list,random=None)

