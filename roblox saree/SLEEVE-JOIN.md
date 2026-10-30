# Sleeved sari shoulder join

For a sari worn with a matching short-sleeve Classic Shirt, close the upper armhole openings in the Classic Pants torso side faces.

On the 585×559 atlas, fill torso RIGHT [165,74,64,34] and LEFT [361,74,64,34] with matching blouse cloth and alpha 255. Preserve existing opaque pixels. Leave the neckline, front/back artwork, open midriff and lower side cutouts unchanged.

The sleeve Shirt keeps all six mapped torso faces at alpha 0; both arm top caps are opaque. This connects the blouse to the sleeves without covering the sari pallu or waist.

Validation: both upper-side rectangles must be fully opaque; all pixels outside those rectangles must match the original Pants. The Shirt file does not need modification for this correction.
