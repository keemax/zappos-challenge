class Bucket:
	def __init__(self, capacity, volume):
		self.capacity = capacity
		self.volume = volume

	def fill(self):
		self.volume = self.capacity

	def empty(self):
		self.volume = 0

	def pourIn(self, bucket):
		bucket.volume += self.volume
		if bucket.volume > bucket.capacity:
			self.volume = bucket.volume - bucket.capacity
			bucket.volume = bucket.capacity
		else:
			self.volume = 0

	def __str__(self):
		return "volume: {0}\ncapacity: {1}\n".format(self.volume, self.capacity)