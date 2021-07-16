import yt

import yt_idv
from yt_idv.scene_components.sph_particles import SPHRendering
from yt_idv.scene_data.particle_positions import ParticlePositions


@yt.derived_field(name=("gas", "prefactor"), sampling_type="particle", units="g/cm**2")
def _field(field, data):
    rv = (
        data["gas", "mass"]
        / data["gas", "density"]
        / data["gas", "smoothing_length"] ** 2
    )
    rv *= data["gas", "density"]
    return rv


ds = yt.load_sample("snapshot_033")
dd = ds.all_data()

rc = yt_idv.render_context(height=800, width=800, gui=True)
sg = rc.add_scene(ds, None, no_ghost=True)

pos = ParticlePositions(
    data_source=dd,
    radius_field="smoothing_length",
    particle_type="gas",
    color_field="prefactor",
    position_field="position",
)
pren = SPHRendering(data=pos, scale=1.0, max_particle_size=1.0)

sg.data_objects.append(pos)
sg.components.append(pren)

print(sg.camera.near_plane, sg.camera.far_plane)
# sg.camera.far_plane = 0.1
rc.run()
