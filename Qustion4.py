'''Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.'''

'''
P = int(input("Enter the time tsken in min"))
N = int(input("Enter the number of problems"))
Time=240
count=0
Left=Time-P
for i in range(1,N+1):
    if Left!=0:
        a=i*5
        if a<Left:
            Left-=a
            count+=1
        else:
            break

print(count)'''
inp1=int(input())
inp2=int(input())
problem_solved=0
reminning_time=240-inp2
for i in range(1,inp1+1):
    if(reminning_time>0 and reminning_time>i*5):
        reminning_time=reminning_time-i*5
        problem_solved+=1
print(problem_solved)