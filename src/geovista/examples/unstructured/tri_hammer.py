#!/usr/bin/env python3
# Copyright (c) 2021, GeoVista Contributors.
#
# This file is part of GeoVista and is distributed under the 3-Clause BSD license.
# See the LICENSE file in the package root directory for licensing details.

"""
WW3 Triangular Mesh (Projected)
-------------------------------

This example demonstrates how to render a projected unstructured triangular mesh.

📋 Summary
^^^^^^^^^^

Creates a mesh from 1-D latitude and longitude unstructured cell points.

The resulting mesh contains triangular cells. The connectivity is required to
construct the cells from the unstructured points.

It uses a WAVEWATCH III (WW3) unstructured triangular mesh sea surface
wave significant height data located on mesh nodes/points.

Note that, a threshold is also applied to remove land ``NaN`` cells, and a
Natural Earth base layer is rendered along with Natural Earth coastlines. The mesh
is also transformed to the Hammer & Eckert-Greifendorff azimuthal projection.
As data is located on the mesh nodes/points, these values are interpolated
across the mesh faces/cells.

----

"""  # noqa: D205,D212,D400
from __future__ import annotations

import geovista as gv
from geovista.pantry.data import ww3_global_tri
import geovista.theme


def main() -> None:
    """Plot a projected WW3 unstructured triangular mesh.

    Notes
    -----
    .. versionadded:: 0.1.0

    """
    # Load the sample data.
    sample = ww3_global_tri()

    # Create the mesh from the sample data.
    mesh = gv.Transform.from_unstructured(
        sample.lons,
        sample.lats,
        connectivity=sample.connectivity,
        data=sample.data,
        name=sample.name,
    )
    # sphinx_gallery_start_ignore
    # Provide mesh diagnostics via logging.
    gv.logger.info("%s", mesh)
    # sphinx_gallery_end_ignore

    # Plot the unstructured mesh.
    crs = "+proj=hammer"
    plotter = gv.GeoPlotter(crs=crs)
    sargs = {"title": f"{sample.name} / {sample.units}", "shadow": True}
    plotter.add_mesh(mesh, scalar_bar_args=sargs, scalars=sample.name)
    plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
    plotter.add_coastlines()
    plotter.add_axes()
    plotter.add_text(
        f"WW3 Triangular Mesh ({crs})",
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    plotter.view_xy()
    plotter.camera.zoom(1.5)
    plotter.show()


if __name__ == "__main__":
    main()
