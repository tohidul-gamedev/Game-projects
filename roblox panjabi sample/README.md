# Roblox Panjabi samples

## Current: Sample 03

[Download the actual shirt PNG](panjabi-magenta-sample-03.png)

![Current shirt](panjabi-magenta-sample-03.png)

585 × 559 RGBA PNG with a white unused background and a `2.94` wordmark. Magenta-purple fabric with a smaller pale-silver chest placket and four small buttons.

The neck and sleeve/hand transparency is transferred directly from the user's approved red Panjabi example (image 71.png), resized to 585 × 559. The exported PNG alpha channel matches that reference mask pixel-for-pixel. The fully transparent neckline spans x273–316, y29–84, crossing the UP/FRONT seam. It uses real PNG alpha, not a checkerboard picture. Garment panels fill the standard layout with a small bleed and no black outlines. Chest embroidery is reduced compared with the previous drafts.

Verification:
- 585 × 559 RGBA dimensions.
- Pixel-for-pixel alpha equality with the resized approved demo mask.
- White opaque background.
- Transparent openings show the colored background in the alpha proof.
- Fixed template overlay used for panel alignment inspection.

### Verification previews — not wearable textures

[Alpha proof](previews/sample-03-alpha-proof.png): cyan is placed behind the actual PNG, so cyan visible through the neck and sleeve ends proves their transparency. This preview is flattened; use the main PNG above for Roblox.

[Template overlay check](previews/sample-03-overlay-check.png): black guide rectangles are added only for inspecting panel positions. These black lines are absent from the main PNG.

Not yet tested on an avatar in Roblox Studio.

## Earlier drafts

- [Sample 01](panjabi-magenta-sample-01.png): original generated atlas; superseded after layout and background feedback.
- [Sample 02](panjabi-magenta-sample-02.png): prior fixed-size revision; superseded by the reference-mask-based Sample 03.

Keep future samples in this folder with sequential filenames. Do not upload the flattened previews as clothing textures.
