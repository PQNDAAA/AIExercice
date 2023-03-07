import unreal 

def createGenericAsset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
    if unique_name:
        asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')
        

    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
        path = asset_path.rsplit('/', 1)[0]
        name = asset_path.rsplit('/', 1)[1]
        return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
    return unreal.load_asset(asset_path)

def createGenericAsset_EXAMPLE():
    base_path = '/Game/Assets/'
    generic_assets = [
        [base_path + 'actor',        unreal.Blueprint,       unreal.BlueprintFactory],
        [base_path + 'material',        unreal.Material,       unreal.MaterialFactoryNew()],
        [base_path + 'world',           unreal.World,          unreal.WorldFactory()],
        [base_path + 'particle_system', unreal.ParticleSystem, unreal.ParticleSystemFactoryNew()],
        [base_path + 'paper_flipbook',  unreal.PaperFlipbook,  unreal.PaperFlipbookFactory()],
    ]
    for asset in generic_assets:
        print (createGenericAsset(asset[0], True, asset[1], None))
        
def spawnActor1():

    make_blueprint_small("zada")
    


def spawnActor():

    unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.EditorAssetLibrary.load_blueprint_class('/Game/Assets/actor1'),unreal.Vector(0.0,0.0,0.0),unreal.Rotator(0.0,0.0,0.0))
    unreal.Actor.attach_to_actor('/Game/BP_Items/Items/BP_ItemBase')

def make_blueprint_small(asset_name):

    package_path = "/Game/Assets"
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Actor)
    # make the blueprint
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    blueprint = asset_tools.create_asset(asset_name, package_path, None, factory)

    # get the root data handle
    subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
    root_data_handle = subsystem.k2_gather_subobject_data_for_blueprint(blueprint)[0]
    
    # add 3 static mesh components
    for i in range(3):
        # add sub object
        sub_handle, fail_reason = subsystem.add_new_subobject(
            unreal.AddNewSubobjectParams(
                parent_handle=root_data_handle,
                new_class=unreal.StaticMeshComponent,
                blueprint_context=blueprint))

        if not fail_reason.is_empty():
            raise Exception("ERROR from sub_object_subsystem.add_new_subobject: {fail_reason}" )

        subsystem.attach_subobject( root_data_handle, sub_handle )
    

        

