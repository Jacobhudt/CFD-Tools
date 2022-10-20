import meshio
import sys
import numpy as np
""" Script for converting Salome .med files to .xdmf files readable by FEniCS.
    Mesh gets separated into two files as FEniCS cannot work with mixed cells. (triangles and tetrahedrons)
    The predefined boundaries in the mesh gets assigned an index starting with 6,7,...
    To ensure correct boundary definitions, *_boundary.xdmf should be inspected visually in Paraview.
"""

## Run with: python convertMEDtoXDMF.py mesh_name.med

mesh = meshio.read(sys.argv[1])

print(len(mesh.cell_data["cell_tags"][2]))

temp_b = np.copy(mesh.cell_data["cell_tags"][2])

temp_d = np.copy(mesh.cell_data["cell_tags"][1])

## Convert the negative boundary tags (which usually starts with 6), to 1,2,...

for i in range(len(temp_b)):
    if temp_b[i] == -6:
        temp_b[i] = 3
    if temp_b[i] == -7:
        temp_b[i] = 2
    if temp_b[i] == -8:
        temp_b[i] = 1

## Convert cells tagged by 0 to 1. Only valid for meshes with one region.

for i in range(len(temp_d)):
    temp_d[i] = 1


meshio.write_points_cells(sys.argv[1].replace('.med', '') + "_boundary.xdmf",
    mesh.points,
    [mesh.cells[2]],
    cell_data={"name_to_read": [temp_b]}, # "name_to_read" is an arbitrary name for the tags used in most FEniCS tutorials
)


meshio.write_points_cells(sys.argv[1].replace('.med', '') + "_domain.xdmf",
    mesh.points,
    [mesh.cells[1]],
    cell_data={"name_to_read": [temp_d]}, # "name_to_read" is an arbitrary name for the tags used in most FEniCS tutorials
)


