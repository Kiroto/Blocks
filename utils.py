import os
import json
import pyglet
import pyglet.gl as gl
import modeller

def getBlockList(**kwargs):
    verbose = kwargs.get('verbose', False)
    blocksFile = open('blocks.json', 'r')
    blocksJson = blocksFile.read()
    blocksFile.close()
    blocksList = json.loads(blocksJson)
    if verbose:
        print('BlockList Loaded!')
    return blocksList["blocklist"]

def getStagelist(**kwargs):
    verbose = kwargs.get('verbose', False)
    stages = {}
    print('Loading Stages...')
    for filename in os.listdir('./stages'):
        if filename.endswith('.json'):
            stages.update({filename[:-5]: './stages/%s' % filename})
            if verbose:
                print('Loaded %s!' % filename)
    print('All Stages Loaded!')
    return stages

def getStage(stage, **kwargs):
    verbose = kwargs.get('verbose', False)
    stageList = getStagelist(verbose=verbose)
    if stage not in stageList:
        print("The stage %s isn't on the stage list" % stage)
    else:
        stageFile = open(('./stages/%s.json' % stage), 'r')
        stageJson = stageFile.read()
        stageFile.close()
        stage = json.loads(stageJson)
        return stage

# Load Textures // Modeler

def findTextureFiles(**kwargs):
    verbose = kwargs.get('verbose', False)
    textureList = {}
    print('Finding Textures...')
    for filename in os.listdir('./textures'):
        if filename.endswith('.png'):
            textureList.update({filename: './textures/%s' % filename})
            if verbose:
                print('Found %s!' % filename)
    print('All Textures Found!')
    return textureList

def findTexturePacks(**kwargs):
    verbose = kwargs.get('verbose', False)

    foundTexturePacks = {}
    textureList = findTextureFiles(**kwargs)

    texturePackListFile = open('./textures/texturePacks.json', 'r')
    texturePackListJson = texturePackListFile.read()
    texturePackListFile.close()
    texturePackList = json.loads(texturePackListJson)

    print('Finding Texture Packs...')

    for texturePack in texturePackList:
        foundTexturePacks.update({texturePack: []})
        if verbose:
            print('Looking for Texture pack %s' % texturePack)
        for texture in texturePackList[texturePack]:
            if texture in textureList:
                foundTexturePacks[texturePack].append('./textures/' + texture)
                if verbose:
                    print(' - Texture %s found' % texture)
            else:
                print(' - Texture %s not found' % texture)
                del foundTexturePacks[texturePack]
                print(' - Texture Pack %s unlisted' % texturePack)
    
    print('All Texture Packs Found!')

    return foundTexturePacks

def pyPackTextures(**kwargs):
    verbose = kwargs.get('verbose', False)
    print('Pygletting images')
    textures = {}
    texturePacks = findTexturePacks(**kwargs)
    for texturePack in texturePacks:
        textures.update({texturePack: []})
        if verbose:
            print(' - Pygletting pack %s' % texturePack)
        for texture in texturePacks[texturePack]:
            if verbose:
                print(' -- Pygletting image %s' % texture)
            tex = pyglet.image.load(texture).texture
            gl.glTexParameterf(gl.GL_TEXTURE_2D,gl.GL_TEXTURE_MIN_FILTER,gl.GL_NEAREST)
            gl.glTexParameterf(gl.GL_TEXTURE_2D,gl.GL_TEXTURE_MAG_FILTER,gl.GL_NEAREST)
            textures[texturePack].append(pyglet.graphics.TextureGroup(tex))
    return textures

blockList = getBlockList()
pyTextures = pyPackTextures()

def getBlockTexture(blockID):
    return pyTextures[blockList[blockID]['textures']]
# def makeBlockTypes(**kwargs):
#     verbose = kwargs.get('verbose', False)
    
#     blockList = getBlockList(**kwargs)
#     blockTypes = []
#     for block in blockList:
#         if block["model"] == 'Block':
#             blockTypes.append(modeller.Model(pyTextures[block['textures']], modeller.Block))
#     return blockTypes

    