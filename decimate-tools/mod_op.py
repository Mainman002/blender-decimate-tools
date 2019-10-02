import bpy
	
#### Object Mode ###################################################################

class MOD_Spin_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_spin_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):
        bpy.ops.object.modifier_add(type='SCREW')
        bpy.context.object.modifiers["Screw"].axis = 'Y'
        bpy.context.object.modifiers["Screw"].use_normal_calculate = True
        bpy.context.object.modifiers["Screw"].show_expanded = False
        bpy.context.object.modifiers["Screw"].use_merge_vertices = True
        #bpy.context.object.modifiers["Screw"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.12
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        #bpy.context.object.modifiers["Solidify"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].width = 0.035
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        #bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}


class MOD_Solidify_Plane_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_solidify_plane_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):
        bpy.ops.object.shade_smooth()
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].offset = 1
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].thickness = 0.25
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        bpy.context.object.modifiers["Solidify"].show_on_cage = True
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 2
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].width = 0.04
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}

#### Edit Mode ###################################################################


class MOD_Spin_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_spin_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):
        bpy.ops.object.modifier_add(type='SCREW')
        bpy.context.object.modifiers["Screw"].axis = 'Y'
        bpy.context.object.modifiers["Screw"].use_normal_calculate = True
        bpy.context.object.modifiers["Screw"].show_expanded = False
        bpy.context.object.modifiers["Screw"].use_merge_vertices = True
        #bpy.context.object.modifiers["Screw"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.12
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        #bpy.context.object.modifiers["Solidify"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].width = 0.035
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        #bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}


class MOD_Solidify_Plane_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_solidify_plane_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].offset = 1
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].thickness = 0.25
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        bpy.context.object.modifiers["Solidify"].show_on_cage = True
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 2
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].width = 0.04
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}
