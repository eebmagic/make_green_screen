from PIL import Image
from ast import literal_eval

# GET FILE PATH
PATH = input("\n\tDrag file here:").strip()
print("\n")

# Get name
filename = PATH.split('/')[-1].split('.')[0]
container_path = '/'.join(PATH.split('/')[:-1]) + '/'

# GET FULL RGB FROM PATH FILE
im = Image.open(PATH, 'r')
pixelValues = list(im.getdata())
originalData = []
# Remove transparent band
for point in pixelValues:
	originalData.append(point[:3])


# LOOP THROUGH RESOLUTION OPTIONS
tolOptions = [50, 70, 120, 150, 180, 210]
for index, TOLERANCE in enumerate(tolOptions):

	# CONVERT TO LOWER COLOR RESOLUTION
	lowResData = []
	for point in originalData:
		newSet = []
		for num in point:
			newSet.append(num - (num % TOLERANCE))
		newTuple = (newSet[0], newSet[1], newSet[2])
		lowResData.append(newTuple)

	# HANDLE DATA
	most_frequent = max(set(lowResData), key=lowResData.count)

	outputData = []
	for i in range(len(originalData)):
		if lowResData[i] == most_frequent:
			outputData.append((1, 255, 2))
		else:
			outputData.append(originalData[i])

	# GENERATE NEW IMAGE FILE
	newIm = Image.new("RGB", im.size)
	newIm.putdata(outputData)
	newIm.save(container_path + filename + "_" + str(TOLERANCE) + ".png")

	total = str(len(tolOptions))
	print(f"Finished writing file [{index} of {total}]")

print(f"\nOutput images were dumped to {container_path}")
