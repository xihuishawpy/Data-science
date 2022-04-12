import simpy 

def waiter(env):
    take_order_duration = 5
    give_order_duration = 2
    while True: # Simulate until the time limit
        print(f"Start taking orders from customers at {env.now}")
        yield env.timeout(take_order_duration) # models duration

        print(f'Start giving the orders to the cooks at {env.now}')
        yield env.timeout(give_order_duration)

        print(f'Start serving customers food at {env.now}\n')
        yield env.timeout(5)

env = simpy.Environment() # the environment where the waiter lives
env.process(waiter(env)) # pass the waiter to the environment
env.run(until=30) # Run simulation until 30s