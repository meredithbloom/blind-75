# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Constraints
'''
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

intervals2 = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.

intervals3 = [[1,4],[4,5],[2,3],[6,10],[9,12]]

intervals4 = [[1,3]]

intervals5 = [[1,4],[5,6]]

# compare ending interval of one pair with the starting interval of another
# if we've seen an ending interval greater than starting interval ALREADY


def merge(intervals):
	# sort intervals based on starting point
	intervals.sort(key = lambda x: x[0])
	#print(intervals)
	index = 0
	output = []
	if len(intervals) == 1:
		return intervals
	for i in range(1, len(intervals)):
		if intervals[index][1] >= intervals[i][0]:
			intervals[index][1] = max(intervals[index][1], intervals[i][1])
		else:
			index = index + 1
			intervals[index] = intervals[i]
	for i in range(index+1):
		output.append(intervals[i])
	print(output)
	return output


		
			
			
		

#merge(intervals1)
#merge(intervals2)
merge(intervals3)
#merge(intervals4)
#merge(intervals5)
