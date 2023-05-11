def GenerateVillagers(asset_package, asset_name):
  
    parent = unreal.EditorAssetLibrary.load_blueprint_class("/Game/Tools/CharactersTool/Characters/BP/BP_VillagerCharacter")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class",parent)
    unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name,asset_package,None,factory)

    
def Generate(villagername,villagerpath):
     GenerateVillagers(villagerpath,villagername)

def SetName(pathbuilding,name):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Name", name)
def SetHealth(pathbuilding,health):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Health", health)
def SetDefense(pathbuilding,defense):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Defense", defense)
def SetAttack(pathbuilding,attack):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Attack", attack)
def SetJobs(pathbuilding,jobs):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Jobs", jobs)
def SetDurationForBreak(pathbuilding,duration):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("DurationForBreak", duration)
def SetUnlockingLevel(pathbuilding,unlockingLevel):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("unlockingLevel", unlockingLevel)    

def GetName(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Name")
def GetHealth(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Health")
def GetDefense(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Defense")
def GetAttack(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Attack")
def GetJobs(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("Jobs")
def GetDurationForBreak(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("DurationForBreak")
def GetUnlockingLevel(pathbuilding):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    return bp_cdo.get_editor_property("unlockingLevel")


def SetStaticMesh(pathbuilding,sm):
    bp_gc = unreal.load_object(None, pathbuilding)
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Static_Mesh_Reference", sm)


