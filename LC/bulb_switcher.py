"""
There are n bulbs that are initially off. You first turn on all the bulbs.
 Then, you turn off every second bulb. On the third round, you toggle every third bulb
  (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb.
   For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off, off].
After first round, the bulbs are [on, on, on, on].
After second round, the bulbs are [on, off, on, off].
After third round, the bulbs are [on, off, off, off].
After fourth round, the bulbs are [on, off, off, on].

So you should return 1, because there is only one bulb is on.

"""


class Solution:

    def bulbSwitch(self, n):
    	bulbs = {index : 0 for index in range(n)}
    	counter = 1
    	if n > 0:
    		bulbs =  {index : 1 for index in range(n)}
    	for index in range(1, n+1):
	    	intermediate = {}
    		if index == 1:
    			continue
    		else:
    			bulb_keys = set(bulbs.keys()[counter::index])
	    		# print("--" * 20)
    			# print("bulb_keys", bulb_keys)
    			intermediate = {each: 1 if bulbs[each] == 0 else 0 for each in bulb_keys}
	    		# print("intermediate", intermediate)
	    		# print("--" * 20)
	    		# print("bulbs", bulbs)
	    		# print("--" * 20)
	    		bulbs.update(intermediate)
	    		counter += 1
    		# print("--" * 20)
    		# print("bulbs after update", bulbs)

    	return len([i for i in bulbs if bulbs[i] == 1])



print(Solution().bulbSwitch(4))
















