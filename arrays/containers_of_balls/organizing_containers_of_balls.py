#!/bin/python3

import sys

def organizingContainers(container):
    container_capacity = {key: 0 for key in range(len(container))}
    balls_counts = [0] * len(container[0])
    for cont_type, cont_values in enumerate(container):        
        for ball_type, ball_count in enumerate(cont_values):            
            balls_counts[ball_type] += ball_count
        container_capacity[sum(cont_values)] = True
    
    for ball_type, ball_count in enumerate(balls_counts):
        if not container_capacity.get(ball_count, False):
            return 'Impossible'
        return 'Possible'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        print(result)


