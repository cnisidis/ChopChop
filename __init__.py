import bpy

bl_info = {
    "name": "KYKEON Toolkit",
    "author" : "Constantine Nisidis",
    "descritpion": "KYKEON Tools for animation",
    "version":(1,0),
    "blender": (2, 80, 0),
    "location":"",
    "warning":"WIP - ",
    "support": "TESTING",
    "category" : "Tools"
}

from . operators    import KykeonBakeToStrip_OT_Operator, WMFileSelector, KykeonAutoSave_OT_Operator
from . properties   import KykeonSettings
from . ui           import KYKEON_PT_SETTINGS

classes = (KykeonBakeToStrip_OT_Operator, KykeonSettings, KYKEON_PT_SETTINGS, WMFileSelector, KykeonAutoSave_OT_Operator)
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
    register_classes()
    bpy.types.Scene.kykeon =  bpy.props.PointerProperty(type=KykeonSettings)
    

def unregister():
    del bpy.types.Scene.kykeon
    unregister_classes()


