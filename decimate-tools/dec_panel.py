import bpy

class DEC_PT_Edit_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_edit_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):
        sel_mode = context.tool_settings.mesh_select_mode
        layout = self.layout

        if sel_mode[1]: # edge

            row_smooth = layout.row()
            col_smooth_lbl = row_smooth.column()
            col_smooth_lbl.label(text="Decimate Tools")

            row = layout.column()
            row.operator('wm.dec_edge_ot_operator', text='Decimate Edges')
        elif sel_mode[0]: # vertex
            row_smooth = layout.row()
            col_smooth_lbl = row_smooth.column()
            col_smooth_lbl.label(text="Decimate Tools")

            row = layout.column()
            row.operator('wm.dec_verts_ot_operator', text='Decimate Verts')

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Modifier Tools")

        row = layout.column()
        row.operator('wm.mod_spin_ot_operator', text='Modifier Spin Edge')

class DEC_PT_Object_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_object_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):
        layout = self.layout

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Modifier Tools")

        row = layout.column()
        row.operator('wm.mod_spin_ot_operator', text='Modifier Spin Edge')



            #sel_mode = context.tool_settings.mesh_select_mode
            #if sel_mode[0]: # vertex
            #    bpy.ops.mesh.select_mode(type='EDGE')
            #elif sel_mode[1]: # edge
            #    bpy.ops.mesh.select_mode(type='FACE')
            #else: # face
            #    bpy.ops.mesh.select_mode(type='VERT')


    #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
    #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
    #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')



    #objectmode
    #mesh_edit
    #curve_edit
    #surface_edit
    #text_edit
    #armature_edit
    #mball_edit
    #lattice_edit
    #pose_mode
    #imagepaint
    #weightpaint
    #vertexpaint
    #particlemode
