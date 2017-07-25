'''
Helps to do statistics calculation
like mean, median & mode
'''
import statistics

ex_list = [1,2,3,4,5,6,7,8,9,10]
res = statistics.mean(ex_list)
print("Mean of first 10 natural numbers:",res)
res = statistics.median(ex_list)
print("Median of first 10 natural numbers:",res)
res = statistics.variance(ex_list)
print("Variance of first 10 natural numbers:",res)
res = statistics.stdev(ex_list)#Standard Deviation
print("Standard Deviation of first 10 natural numbers:",res)
