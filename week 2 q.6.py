def remove_empty(input_tuples):
    input_tuples = [t for t in input_tuples if t]
    return input_tuples
   
input_tuples = [(), ('', ''), ('python', 'coding'), () , ('alpha', 'beta'), ('physics', 'maths'), ('', ''), ()]


print(remove_empty(input_tuples))