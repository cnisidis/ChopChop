import bpy


class KYKEON_PT_SETTINGS(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "KYKEON_PT_settings"
    bl_category = "KYKEON"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.operator("kykeon.file_selector", icon="FILE_FOLDER", text="")
        row.prop(context.scene.kykeon, 'string_file_with_instructions', text="Instructions File")
        
        row = layout.row()
        row.prop(context.scene.kykeon, 'bool_save_copy', text='Auto Save To New Copy')
        row = layout.row()
        row.prop(context.scene.kykeon,'bool_single_range', text="Bake Single")
        
        box = layout.box()
        row = box.row()
        row.prop(context.scene.kykeon, 'str_part')
        row = box.row()
        row.prop(context.scene.kykeon, 'str_name')
        row = box.row()
        row.prop(context.scene.kykeon, 'int_start_frame')
        row = box.row()
        row.prop(context.scene.kykeon, 'int_end_frame')
        row = box.row()
        row.prop(context.scene.kykeon, 'float_speed')

        box.enabled = context.scene.kykeon.bool_single_range

        row = layout.row()
        row.operator('kykeon.bake_to_strip', text='Bake&Strips')
        




