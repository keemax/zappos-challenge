from bucket import Bucket
from node import Node
import sys
import math
import heapq

# ordered list of bucket capacities
capacities = []
# ordered list of desired bucket volumes
endState = []

def main():
	# parse input
	userInput = input().split(' ')
	bucketCapacitiesInput = userInput[0].split(',')
	endVolumesInput = userInput[1].split(',')
	# check for mismatched input
	if len(bucketCapacitiesInput) != len(endVolumesInput):
		print("capacities and end volumes mismatch")
		sys.exit()
	# set up globals
	for i in range(len(endVolumesInput)):
		endState.append(endVolumesInput[i])
		capacities.append(int(bucketCapacitiesInput[i]))
	# a bit more input checking
	for i in range(len(capacities)):
		if endState[i] != '*':
			if int(endState[i]) > capacities[i]:
				print("end volume higher than capacity")
				sys.exit()

	# set up heap
	initialState = [0] * len(endState)

	heap = []
	visitedStates = {}
	start = Node(initialState, None, 0)
	visitedStates[tuple(initialState)] = True
	pushToHeap(start, heap)
	# loop through until end is found or heap is empty (no solution)
	while len(heap) > 0:
		currNode = heapq.heappop(heap)
		print("checking state ", currNode.state)
		# if the heuristic is 0, this node is the solution
		if calculateHeuristic(currNode) == 0:
			printPath(currNode)
			sys.exit()
		else:
			visitedStates[tuple(currNode.state)] = True

		nextStates = getAllPossibleNextStates(currNode.state)
		for state in nextStates:
			try:
				visitedStates[tuple(state)]
			except KeyError:
				newNode = Node(state, currNode, currNode.steps + 1)
				pushToHeap(newNode, heap)
	print("no solution")



def printPath(node):
	if node.cameFrom == None:
		print(node.state)
		return
	else:
		printPath(node.cameFrom)
	print(node.state)

def pushToHeap(node, heap):
	node.score = calculateHeuristic(node)
	heapq.heappush(heap, node)	

def getAllPossibleNextStates(volumes):
	volumeStates = []

	# empty a single bucket and fill a single bucket
	for i in range(len(volumes)):
		# if bucket isn't empty, add state with this bucket empty
		if volumes[i] > 0:
			stateWithEmpty = []
			for j in range(len(volumes)):
				if i == j:
					stateWithEmpty.append(0)
				else:
					stateWithEmpty.append(volumes[j])
			volumeStates.append(stateWithEmpty)

		# if bucket isn't full, add state with this bucket filled
		if volumes[i] < capacities[i]:
			stateWithFill = []
			for j in range(len(volumes)):
				if i == j:
					stateWithFill.append(capacities[j])
				else:
					stateWithFill.append(volumes[j])	
			volumeStates.append(stateWithFill)

	# pour a bucket into another
	for i in range(len(volumes)):
		for j in range(len(volumes)):
			if i != j:
				newState = []
				pouringBucket = Bucket(capacities[i], volumes[i])
				acceptingBucket = Bucket(capacities[j], volumes[j])
				pouringBucket.pourIn(acceptingBucket)
				# if pouring the bucket resulted in a transfer of water, add new state
				if pouringBucket.volume != volumes[i]:
					for k in range(len(volumes)):
						if k == i:
							newState.append(pouringBucket.volume)
						elif k == j:
							newState.append(acceptingBucket.volume)
						else:
							newState.append(volumes[k])

					volumeStates.append(newState)

	return volumeStates

# calculate heuristic for a* search
def calculateHeuristic(node):
	heuristic = 0
	for i in range(len(node.state)):
		if endState[i] != '*':
			diff = 	math.fabs(node.state[i] - int(endState[i]))
			heuristic += diff
	# return 0 because this function is used to check termination condition as well
	if heuristic == 0:
		return heuristic
	# add distance travelled to heuristic
	heuristic += node.steps
	return heuristic

if __name__ == "__main__":
	main()
