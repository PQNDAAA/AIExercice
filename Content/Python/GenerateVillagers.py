import unreal
from unreal import DataTable


def GenerateVillagers(asset_package, asset_name):
  
    parent = unreal.EditorAssetLibrary.load_blueprint_class("/Game/BP_Villagers/Villagers/BP_VillagerCharacter")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class",parent)
    unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name,asset_package,None,factory)

    dt = unreal.load_object(None,'/Game/Resources/DT_Resources')
    

    for row in dt:
        row.ItemInt = 42

    dt.save_package('/Game/Resources/DT_Resources')

    
def Generate(villagername,villagerpath):
     GenerateVillagers(villagerpath,villagername)

"""
def printBlueprint():
    for sel in unreal.EditorUtilityLibrary().get_selected_assets():
        print (sel.get_class())
        print (sel.get_class().get_name())

        path_gen = str(sel.get_path_name()) + '_C'
        bp_gc = unreal.load_object(None, path_gen)
        bcd = unreal.get_default_object(bp_gc)

        print (bcd.get_class())
        print (bcd.get_class().get_name())

@unreal.ustruct()
class BasicStruct(unreal.StructBase):
    some_health = unreal.uproperty(float)
    some_attack = unreal.uproperty(float)
    some_defense = unreal.uproperty(float)  


@unreal.uclass()
class PythonTestClass(unreal.BlueprintFunctionLibrary):
 
    @unreal.ufunction(static = True, params = [str], ret = BasicStruct)
    def editVariables(pathbuilding):

    # get the generated class of the Blueprint (note the _C)
        bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
        bp_cdo = unreal.get_default_object(bp_gc)

        health = bp_cdo.get_editor_property("Health")
        attack = bp_cdo.get_editor_property("Attack")
        defense = bp_cdo.get_editor_property("Defense")

        struct = BasicStruct()

        struct.some_health = health
        struct.some_attack = attack
        struct.some_defense = defense

        return struct
        # set the default property values
    #bp_cdo.set_editor_property("villagersMax", 1)
"""

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


def SetStaticMesh(pathbuilding,sm):
    # get the generated class of the Blueprint (note the _C)
    bp_gc = unreal.load_object(None, pathbuilding)
    # get the Class Default Object (CDO) of the generated class
    bp_cdo = unreal.get_default_object(bp_gc)
    bp_cdo.set_editor_property("Static_Mesh_Reference", sm)


