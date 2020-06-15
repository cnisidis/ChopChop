import bpy
import os
from bpy_extras.io_utils import ExportHelper
import csv
from . utils import ToBakeToAction, Map





class KykeonBakeToStrip_OT_Operator(bpy.types.Operator):
    bl_idname = "kykeon.bake_to_strip"
    #bl_context_mode = 'OBJECT'
    bl_label = "Kykeon Bake To Strip"
    bl_description = "Bake actions to object and then create strips automatically"
    bl_options = {'REGISTER'}

    from_file = False
    file_with_instructions = ''

    current_instructions =[]


    @classmethod
    def poll(self, context):
        #self.from_file = bpy.context.scene.kykeon.bool_from_file
        #if self.from_file:
        self.file_with_instructions = bpy.context.scene.kykeon.string_file_with_instructions
        return context
        


    def execute(self, context):
        if (self.file_with_instructions != None or self.file_with_instructions != '') and context.scene.kykeon.bool_single_range == False:
            instr_filepath = os.path.normpath(self.file_with_instructions)
            path_exist = os.path.exists(instr_filepath)
            is_file = os.path.isfile(instr_filepath)

            instructions = []               
            if path_exist and is_file:
                instructions_file = open(instr_filepath, 'r')
                instructions_csv = instructions_file.read()
                instructions_csv_lines = instructions_csv.split('\n')
                instruction = {'part':'','name':'', 'start':0, 'end':0, 'speed':100}
                
                for line in instructions_csv_lines:
                    print(line)
                    if len(line)>0 or line !='' :
                        fields = line.split(';')
                        field_per_line = 5
                        for i, field in enumerate(fields):
                            if i%field_per_line == 0:
                                instruction['part'] = field
                            if i%field_per_line == 1:
                                instruction['name'] = field
                            if i%field_per_line == 2:
                                instruction['start'] = int(field)
                            if i%field_per_line == 3:
                                instruction['end'] = int(field)
                            if i%field_per_line == 4:
                                instruction['speed'] = int(field)
                        instructions.append(instruction)
                        #---//TODO---------#
                        #---CREATE STRIPS--#        
                        self.report({'INFO'}, 'Creating New Action ...')        
                        Bake = ToBakeToAction(instruction)
                        if not Bake:
                            self.report({'WARNING'}, 'Your Object doesnt have NLA Track info')
                            return {'CANCELLED'}
                        self.report({'INFO'}, 'Action' + instruction['name'] +' Created')        
                        
                    
                self.report({'INFO'}, 'Creating New Actions ...')        
                
                
                
                #print(instructions)
            else:
                self.report({'INFO'}, 'No File Selected')
                return {'CANCELLED'}
                

        elif context.scene.kykeon.bool_single_range == True:
                print('Single Bake Range')
                kykeon_prop =   context.scene.kykeon       
                #print(instructions_csv_lines)
                instruction = {'part':kykeon_prop.str_part,'name':kykeon_prop.str_name, 'start':kykeon_prop.int_start_frame, 'end':kykeon_prop.int_end_frame, 'speed':kykeon_prop.float_speed}
                print(instruction)
                print('Operator Executed')

        return {'FINISHED'}


class WMFileSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "kykeon.file_selector"
    bl_label = "Import CSV"

    filename_ext = ""

    def execute(self, context):
        fdir = self.properties.filepath
        context.scene.kykeon.string_file_with_instructions = fdir
        return{'FINISHED'}


class KykeonAutoSave_OT_Operator(bpy.types.Operator):
    bl_idname = "kykeon.auto_save"
    #bl_context_mode = 'OBJECT'
    bl_label = "Auto Save File to Copy"
    bl_description = "Auto Save File to Copy, keep only needful actions"
    bl_options = {'REGISTER'}

    def execute(self, context):
        print('WIP - Saved To ..')
        self.report({'WARNING'}, 'This operator has no functionality yet')
        return {'FINISHED'}
