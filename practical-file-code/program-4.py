import simpy.rt
from time import perf_counter

FACTOR = 1
start_time = 0

class RedLight(object):
    def __init__(self, env, red_time, green_time, yellow_time):
        self.env = env
        self.red_time = red_time
        self.green_time = green_time
        self.yellow_time = yellow_time
        self.action = self.env.process(self.run())
    def run(self):
        while True:
            global start_time
            print("time:", self.env.now, "red light", ", wall clock time: ", perf_counter() - start_time)
            yield self.env.timeout(self.red_time)
            print("time:", self.env.now, "green light", ", wall clock time: ", perf_counter() - start_time)
            yield self.env.timeout(self.green_time)
            print("time:", self.env.now, "yellow light", ", wall clock time: ", perf_counter() - start_time)
            yield self.env.timeout(self.yellow_time)


def main() :
    env = simpy.rt.RealtimeEnvironment(factor = FACTOR, strict = False) #1 second real-time is 
                                                                        #actually 15 seconds in simulation
    red_t = input("Enter the time for which the light is red: ")
    green_t = input("Enter the time for which the light is green: ")
    yellow_t = input("Enter the time for which the light is yellow: ")
    if(not all([red_t.isdigit(), green_t.isdigit(), yellow_t.isdigit()])):
        print("the parameters are in the incorrect format")
        print("default values will be used")
        red_t = 4
        green_t = 3
        yellow_t = 1
    else:
        red_t = int(red_t)
        green_t = int(green_t)
        yellow_t = int(yellow_t)
    rl = RedLight(env, red_t, green_t, yellow_t)
    global start_time
    start_time = perf_counter()
    print("starting wallclock time: ", perf_counter())
    env.run(until = 60) 


if __name__ == "__main__":
    main()



