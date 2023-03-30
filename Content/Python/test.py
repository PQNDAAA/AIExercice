import unreal
from unreal import DataTable

"""
@unreal.ustruct()
class PythonUnrealStruct(unreal.StructBase):
    some_string = unreal.uproperty(str)
    some_number = unreal.uproperty(float)
    array_of_string = unreal.uproperty(unreal.Array(str))

@unreal.uclass()
class PythonTestClass(unreal.BlueprintFunctionLibrary):

    @unreal.ufunction(static = True, params = [int], ret = PythonUnrealStruct)
    def MyPythonFunction(integer_argument1):
        struct = PythonUnrealStruct()
        struct.some_string = "5"
        struct.some_number = integer_argument1 + 1
        struct.array_of_string = ["a", "b", "c"]
        return struct
    """
def editDT():
    dt_path = "/Game/Resources/DT_Resources"
    my_dt = DataTable.load(dt_path)

    row = my_dt.find_row_by_name('Row1')
    row.value1 = 'new_value3'

    new_row = my_dt.add_row('Row3')
    new_row.value1 = 'value3'

    my_dt.save()