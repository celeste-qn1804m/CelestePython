class CalUtils:
	names = []
	heights = []
	totalStudentHeight = 0
	totalStudentCount = 0
	def calAvgHeight(self):
		self.totalStudentHeight = 0 #re-init to 0
		for height in self.heights: #loop through all the heights
			self.totalStudentHeight += height #add all together
		self.totalStudentCount = len(self.names)
		return self.totalStudentHeight / self.totalStudentCount

cal = CalUtils() #define new object
file = open("listOfStudentHeight.txt", 'r') #open file
for line in file: #read each line
	data = line.split("\t") #split name and height since format is <name>\t<height>
	name = data[0]
	height = float(data[1])
	cal.names.append(name) #append into current list
	cal.heights.append(height)
	#cal.totalStudentHeight += height;
file.close() #close file
cal.totalStudentCount = len(cal.names)
print ("Student average height is %.2f m for %d students." % (cal.calAvgHeight() , cal.totalStudentCount));
new_name = input("Enter new student name: ")

while True:
	try:
		new_height = input("Enter new student height(in meters): ")
		new_height = float(new_height)
	except ValueError:
		print ("Please enter a number for height!")
	else:
		break
cal.names.append(new_name)
cal.heights.append(new_height)
print ("Student average height is %.2f m for %d students." % (cal.calAvgHeight() , cal.totalStudentCount));
