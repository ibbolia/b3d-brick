import bpy, random

class Brick:
	def __init__(self, length=4, width = 4, height = 2):
		self.lwh = (length, width, height)

	def genMeshData(self):
		verts = []
		edges = []
		faces = []

		#Vertexes
		verts.append((self.lwh[0], self.lwh[1], self.lwh[2]))	#0
		verts.append((self.lwh[0], self.lwh[1], -self.lwh[2]))	#1
		verts.append((self.lwh[0], -self.lwh[1], self.lwh[2]))	#2
		verts.append((self.lwh[0], -self.lwh[1], -self.lwh[2]))	#3
		verts.append((-self.lwh[0], self.lwh[1], self.lwh[2]))	#4
		verts.append((-self.lwh[0], self.lwh[1], -self.lwh[2]))	#5
		verts.append((-self.lwh[0], -self.lwh[1], self.lwh[2]))	#6
		verts.append((-self.lwh[0], -self.lwh[1], -self.lwh[2]))#7

		#Faces
		#Blender determines normals by vertices in a face clockwise
		faces.append((2,3,7,6)) #-Y (Front)
		faces.append((0,4,5,1)) #+Y (Back)
		faces.append((0,1,3,2)) #+X (Right)
		faces.append((5,4,6,7))	#-X (Left)
		faces.append((0,2,6,4))	#+Z (Top)
		faces.append((1,5,7,3))	#-Z (Bottom)

		self.verts = verts
		self.edges = edges
		self.faces = faces

	def randomizeVerts(self, min = -.5, max = .5):
		verts = []

		for vtx in self.verts:
			tup = []
			for xyz in vtx:
				rnd = random.uniform(min, max)
				tup.append(xyz + rnd)
			verts.append((tup[0], tup[1], tup[2]))
			

		pass

def getMin(points = []):
	minX = 0
	minY = 0
	for tp in points:
		minX = min(minX, tp[0])
		minY = min(minY, tp[1])

	return {'X':minX, 'Y':minY}

def getMax(points= []):
	minX = 0
	minY = 0
	for tp in points:
		minX = max(minX, tp[0])
		minY = max(minY, tp[1])

	return {'X':minX, 'Y':minY}

class BrickGeneratorOperator(bpy.types.Operator):
	bl_idname = "object.brick"
	bl_label = "Brick"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		#Create mesh data
		mesh_data = bpy.data.meshes.new("brick_mesh_data")
		samp_brick = Brick()
		samp_brick.genMeshData()
		mesh_data.from_pydata(samp_brick.verts, samp_brick.edges, samp_brick.faces)
		mesh_data.update()

		#create blender object
		obj = bpy.data.objects.new("Brick", mesh_data)
		obj.location = bpy.context.scene.cursor_location

		#Link object to mesh data
		scene = bpy.context.scene
		scene.objects.link(obj)

		return {'FINISHED'}

if __name__ == "__main__":
	points = [
	(1,1),
	(0,0),
	(0,1),
	(13,-4)]

	mini = getMin(points)
	maxi = getMax(points)
	bSize = .5

	index = mini['X']
	print(index)
	
	lsX = []
	lsY = []

	while(index <= maxi['X']):
		lsX.append(index)
		index = float(index) + bSize

	index = mini['Y']
	while(index <= maxi['Y']):
		lsY.append(index)
		index = index + bSize

	print(lsX)
	print(lsY)