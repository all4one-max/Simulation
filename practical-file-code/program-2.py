import simpy as sp

## A simply traffic light function
def traffic_light(environment):
    while True:
        print("light turn green at " + str(environment.now))
    
        yield environment.timeout(50)
    
        print("light turn yellow at " + str(environment.now))
    
        yield environment.timeout(5)
    
        print("light turn red at " + str(environment.now))
    
        yield environment.timeout(60)

# Run Simulation
environment = sp.Environment()
environment.process(traffic_light(environment))
environment.run(until = 300)