import unreal


def GenerateBuilding(asset_package, asset_name):
  
    parent = unreal.EditorAssetLibrary.load_blueprint_class("/Game/Building/StorageBuilding/BP_StorageBuildingBase")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class",parent)
    unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name,asset_package,None,factory)
    
def Generate(buildingname,buildingpath):
     GenerateBuilding(buildingpath,buildingname)


def printBlueprint():
    for sel in unreal.EditorUtilityLibrary().get_selected_assets():
        print (sel.get_class())
        print (sel.get_class().get_name())

        path_gen = str(sel.get_path_name()) + '_C'
        bp_gc = unreal.load_object(None, path_gen)
        bcd = unreal.get_default_object(bp_gc)

        print (bcd.get_class())
        print (bcd.get_class().get_name())

def editVariables(pathbuilding):

    # get the generated class of the Blueprint (note the _C)
    bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
    bp_cdo = unreal.get_default_object(bp_gc)

    return bp_cdo.get_editor_property("villagersMax")
        # set the default property values
    #bp_cdo.set_editor_property("villagersMax", 1)


def SetVillagersMax(pathbuilding,villagers):
     # get the generated class of the Blueprint (note the _C)
    bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("villagersMax", villagers)

def SetStaticMesh(pathbuilding,sm):
    # get the generated class of the Blueprint (note the _C)
    bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Static_Mesh_Reference", sm)

def SetMaxResources(path, resources):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("maxResources", resources)

def SetName(path, name):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("buildingName", name)

def SetSearchArea(path, searcharea):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("searchArea", searcharea)

def SetPlacementArea(path, placementarea):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("placementArea", placementarea)

def SetDurability(path, durability):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("durability", durability)

def SetJobs(path, jobs):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("TargetJobs", jobs)

def SetUnlockingLevel(path, unlockingLevel):
    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("unlockingLevel", unlockingLevel)

def GetStaticMesh(pathbuilding):

# get the generated class of the Blueprint (note the _C)
    bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Static_Mesh_Reference")

def GetMaxResources(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("maxResources")

def GetPlacementArea(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("placementArea")

def GetSearchArea(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("searchArea")

def GetName(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("buildingName")

def GetDurability(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("durability")

def GetJobs(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("TargetJobs")

def GetUnlockingLevel(path):

    bp_gc = unreal.load_object(None, path)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("unlockingLevel")


