import unreal


def GenerateBuilding(asset_package, asset_name):
  
    parent = unreal.EditorAssetLibrary.load_blueprint_class("/Game/BP_Items/Items/BP_ItemBase")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class",parent)

    unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name,asset_package,None,factory)
    
def Generate():
     GenerateBuilding("/Game/Assets","teda")


def printBlueprint():
    for sel in unreal.EditorUtilityLibrary().get_selected_assets():
        print (sel.get_class())
        print (sel.get_class().get_name())

        path_gen = str(sel.get_path_name()) + '_C'
        bp_gc = unreal.load_object(None, path_gen)
        bcd = unreal.get_default_object(bp_gc)

        print (bcd.get_class())
        print (bcd.get_class().get_name())


