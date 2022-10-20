from fenics import *
import sys

# Read volumetric mesh
mesh = Mesh()

# Read tags for volume elements
mvc = MeshValueCollection("size_t", mesh, mesh.topology().dim())
with XDMFFile(MPI.comm_world, "YOUR_MESH_DOMAIN.xdmf") as infile:
   infile.read(mesh)
   infile.read(mvc, "name_to_read")

# Read tags for surface elements (can also be used for applying DirichletBC)

mvc = MeshValueCollection("size_t", mesh, mesh.topology().dim()-1)
with XDMFFile(MPI.comm_world, "YOUR_MESH_BOUNDARY.xdmf") as infile:
    infile.read(mvc, "name_to_read")

mf = cpp.mesh.MeshFunctionSizet(mesh, mvc)
dx = Measure("dx")(subdomain_data=mf)



##Example boundary conditions, inspect boundary tags visiually for example in paraview
"""
inlet = DirichletBC(V, Constant(1), boundaries, 1) #6 is the key for the inlet-boundary
outlet = DirichletBC(V, Constant(-1), boundaries, 2)
wall = DirichletBC(V, Constant(0), boundaries, 3)

"""

