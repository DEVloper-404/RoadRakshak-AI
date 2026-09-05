# Violation images

Filename encodes everything:

```
<PLATE>__<VIOLATION>__<CAMERA>__<VEHICLE>.jpg

UP39T9319__OVER_SPEEDING__CAM-02__GOODS.jpg
CG15E5157__NO_HELMET__CAM-01__BIKE.jpg
UNKNOWN__WRONG_WAY__CAM-03__BIKE.jpg
```

Rename a file and reload the page — no rebuild.

| segment | values | if omitted |
|---|---|---|
| plate | `UP39T9319`, or `UNKNOWN` when it could not be read | filename used as-is |
| violation | `NO_HELMET` `TRIPLE_RIDING` `WRONG_WAY` `OVER_SPEEDING` | cycles |
| camera | `CAM-01` … `CAM-06` | dealt round-robin |
| vehicle | `BIKE` `CAR` `AUTO` `GOODS` `TRUCK` `BUS` | inferred from violation |

**`UNKNOWN` is not a dropped violation.** The record still appears, shows a
dashed `NOT READ` plate, and **refuses to generate a challan** until an officer
supplies the plate with *Re-enter plate*. That is the whole point of the PENDING
state — a plate is never guessed onto a fine.

Images are scheduled at staggered points in their camera's clip, so they surface
one at a time as the videos play. Two stills pinned to the same camera are spaced
apart rather than firing at the same second. Keep the set small.

## Source footage is traced automatically

The still is pinned to a camera, and the camera is pinned to a clip, so the
footage a still came from follows from that — no extra configuration. The UI and
the challan both show the clip name, when the clip was recorded (from the
QuickTime creation date), and the offence time, which is the clip start plus the
offset into it.

Only the highlight ring and violation caption are burned into the picture;
camera and location are drawn by the page, so a renamed file can never carry a
stale camera caption.

To add one: drop the photo in `data/Violations/`, add a row to `SUPPLIED` in
`demo/build_demo.py`, and re-run it. EXIF rotation and downscaling are handled.
