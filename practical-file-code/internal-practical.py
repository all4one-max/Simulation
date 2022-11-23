#Import important library
from random import randint
import simpy
import random
import statistics

"""
    The idea is:
    Exam center seat allotment:
    1. Students reach center
    2. Wait in the queue
    3. staff scans the aadhar card, check admit card
    4. student travels to room
    5. exam start
"""


### Inital Variable 
wait_times = []


### A class "Exam center" contain event for simulation 
class ExamCenter(object):
    def __init__(self, env, num_staff):
        self.env = env
        self.staff =simpy.Resource(env, num_staff)

    def scan_admit_card(self, student):
        yield self.env.timeout(random.randint(1, 3))

    def scan_aadhar_card(self, student):
        yield self.env.timeout(3 / 60)

    def frisk_student(self, student):
        yield self.env.timeout(random.randint(1, 5))

def enter_exam_center(env, student, exam_center):
    # Movie goer arrives at the theater
    arrival_time = env.now

    with exam_center.staff.request() as request:
        yield request
        yield env.process(exam_center.scan_aadhar_card(student))

    with exam_center.staff.request() as request:
        yield request
        yield env.process(exam_center.scan_admit_card(student))

    with exam_center.staff.request() as request:
        yield request
        yield env.process(exam_center.frisk_student(student))

    # student enter hall
    wait_times.append(env.now - arrival_time)


def run_exam_center(env, num_staff):
    exam_center = ExamCenter(env, num_staff)

    for student in range(3):
        env.process(enter_exam_center(env, student, exam_center))

    while True:
        yield env.timeout(0.20)  # Wait a bit before next student comes

        student += 1
        env.process(enter_exam_center(env, student, exam_center))

def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)

def get_user_input():
    num_staff = input("Input number of staff working : ")
    params = [num_staff]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]  
    return params

def main():
    # Setup
    random.seed(42)
    num_staff = get_user_input()[0]

    # Run the simulation
    env = simpy.Environment()
    env.process(run_exam_center(env, num_staff))
    env.run(until=90.0)

    # View the results
    mins, secs = get_average_wait_time(wait_times)
    print("Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.")

## Run simulation 
if __name__ == "__main__":
    main()