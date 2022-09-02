from fenics import *
import sys


# Read volumetric mesh
mesh = Mesh()
XDMFFile("YOURMESH_domain.xdmf").read(mesh)

# Read tags for volume elements
cell_markers = MeshFunction("size_t", mesh, mesh.topology().dim())
XDMFFile("YOURMESH_domain.xdmf").read(cell_markers)
with XDMFFile("cell_markers.xdmf") as f:
    f.write(cell_markers)

# Read tags for surface elements (can also be used for applying DirichletBC)
boundaries = MeshValueCollection("size_t", mesh, mesh.topology().dim() - 1)
XDMFFile("YOURMESH_boundary.xdmf").read(boundaries)
boundaries = MeshFunction("size_t", mesh, boundaries)

##Example boundary conditions
"""
inlet = DirichletBC(V, Constant(1), boundaries, 6) #6 is the key for the inlet-boundary
outlet = DirichletBC(V, Constant(-1), boundaries, 7)
wall = DirichletBC(V, Constant(0), boundaries, 8)

"""

