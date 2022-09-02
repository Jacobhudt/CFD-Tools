import meshio
import sys

""" Script for converting Salome .med files to .xdmf files readable by FEniCS.
    Mesh gets separated into two files as FEniCS cannot work with mixed cells. (triangles and tetrahedrons)
    The predefined boundaries in the mesh gets assigned an index starting with 6,7,...
    To ensure correct boundary definitions, *_boundary.xdmf should be inspected visually in Paraview.
"""


## Run with: python convertMEDtoXDMF.py mesh_name.med

mesh = meshio.read(sys.argv[1])

mesh.cell_data_dict["cell_tags"]["tetra"] *= -1


meshio.write_points_cells(sys.argv[1].replace('.med', '') + "_boundary.xdmf",
    mesh.points,
    [mesh.cells[1]],
    cell_data={"f": [mesh.cell_data["cell_tags"][1][:]*(-1)]}, 
)


meshio.write_points_cells(sys.argv[1].replace('.med', '') + "_domain.xdmf",
    mesh.points,
    [mesh.cells[0]],
    cell_data={"f": [mesh.cell_data["cell_tags"][0]]},
)
