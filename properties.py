import bpy


class KykeonSettings(bpy.types.PropertyGroup):
    # #tags
    bool_from_file : bpy.props.BoolProperty(name='from_file', default=True)
    bool_single_range : bpy.props.BoolProperty(name='single', default=False)

    str_part : bpy.props.StringProperty(name='Part Name', default='NewPart')
    str_name : bpy.props.StringProperty(name='Strip Name', default='NewAction')
    int_start_frame : bpy.props.IntProperty(name='Start Frame', default=0)
    int_end_frame : bpy.props.IntProperty(name='End Frame', default=100)
    float_speed : bpy.props.FloatProperty(name='speed', default=100)

    bool_save_copy : bpy.props.BoolProperty(name='bool_save_copy', default=False)

    string_file_with_instructions : bpy.props.StringProperty(name="file_with_instructions", default="")
    