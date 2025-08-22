import random

num_trials = 1000

def sim_probability(num_heads, num_flips):
    success = 0

    for x in range(num_trials):
        heads = 0
        for y in range(num_flips):
            if flip_coin_heads():
                heads += 1

        if heads == num_heads:
            success += 1

    proportion = success/num_trials

    print(f"Ran {num_trials} trials of {num_flips} coin flips each."
          f"Successfully obtained exactly {num_heads} heads {success} times, for a proportion of {proportion:.6f}")
    
    return proportion

        
#True if heads
def flip_coin_heads():
    r = random.random()
    return False if r < 0.5 else True

sum_prob = 0.0

for h in range(1, 101):
    sum_prob += sim_probability(h, 100)

print(f"Total probability of all possible outcomes: {sum_prob}")