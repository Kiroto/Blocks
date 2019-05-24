# Blocks

POSITIVE Z = NORTH
POSITIVE X = EAST
NEGATIVE Z = SOUTH
NEGATIVE X = WEST

0 - Top,
1 - North,
2 - East,
3 - South,
4 - West,
5 - Bottom

** Block Information

Stored in blocks.json
Blocks have 3 properties:
 - Name: Name of the block (currently unused)
 - Texture: Texture of the block (required)
 - Model: Model of the block (required)

Origin of blocks is (Currently) South East Bottom

** Current Models:

 - Block: 6 sides
 - Wedge: 5 Sides, with a slope at the top


** Stages:
 - Have a scale (to which it is generated)
 - Have a name (Currently unused)
 - Have a description (Currently unused)
 - Have a map (3D array with block IDs. These blocks will be placed in the same order the world was made)

The map
 - each 2d array inside the 3d array is a height
 - each array inside the 2d array is a depth
 - each item in the array is a block or length

# Textures

Texture Packing:

Textures are packed on lists and those lists, named: texturePacks.json
Blocks are saved in an array, index being their ID, with their information: blocks.json
Blocks are modelled by using their information and textured by taking textures with the help of texturePacks.json


** Block Rules

If only one texture, texture for the whole block.
If two textures, first is top and bottom, second is sides.
If three textures, first is top, second is sides, third is bottom.
If four textures, first is top, second is north and south, third is east and west, fourth is bottom.
If six textures, top, north, east, south, west and bottom.
If five, less than one or more than six, except.