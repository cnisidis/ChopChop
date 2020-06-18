import bpy

def Map(value ,in_min, in_max, out_min, out_max):
    return out_min+((value-in_min)*(out_max-out_min) / (in_max - in_min))


def ToBakeToAction(instruction):
    

    ob = bpy.context.object
    #add Dancer name to the Actions
    dancer_name = ob.name 

    try:
        tracks = ob.animation_data.nla_tracks
    except:
        return False


    part    = instruction['part']
    name    = instruction['name']
    act     = instruction['action']
    frame_start = instruction['start']
    frame_end =  instruction['end']
    speed = float(instruction['speed'])
    scale = 1/(speed/100)
    duration = frame_end - frame_start


    op_bake = bpy.ops.nla.bake(frame_start=frame_start, frame_end=frame_end, step=1, only_selected=True, visual_keying=False, clear_constraints=False, clear_parents=False, bake_types={'POSE'})
    
    if op_bake == {'FINISHED'}:
        
        action = ob.animation_data.action
        
        if action is not None:
            #new_action = bpy.data.actions[0]
            action.name = dancer_name+'_'+part+'_'+name 
            
            track = tracks.new()
            track.name = 'Tk_'+dancer_name+'_'+part+'_'+name 
            strip = track.strips.new( action.name, action.frame_range[0], action)
            strip.frame_start = 1
            strip.frame_end = duration
            strip.scale = scale
            track.mute = True
            
            ob.animation_data.action = None
    
    #print(instruction)
    return True

    