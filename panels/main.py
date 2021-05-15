import bpy
import datetime

from ..core import animations
from ..core.icon_manager import Icons

row_scale = 0.75
paired_inputs = {}


# Initializes the Rokoko panel in the toolbar
class ToolPanel(object):
    bl_label = 'Pose Transfer'
    bl_idname = 'VIEW3D_TS_pose_transfer'
    bl_category = 'Pose Transfer'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


def separator(layout, scale=1):
    # Add small separator
    row = layout.row(align=True)
    row.scale_y = scale
    row.label(text='')


# Main panel of the Rokoko panel
class ReceiverPanel(ToolPanel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_rsl_receiver_v2'
    bl_label = 'Pose Transfer'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = False

        col = layout.column()

        row = col.row(align=True)
        row.label(text='Scene Scale:')
        row.prop(context.scene, 'rsl_scene_scaling', text='')

        layout.separator()

        row = layout.row(align=True)
        row.prop(context.scene, 'rsl_reset_scene_on_stop')

        row = layout.row(align=True)
        row.prop(context.scene, 'rsl_hide_mesh_during_play')


def add_indent(split, empty=False):
    row = split.row(align=True)
    row.alignment = 'LEFT'
    if empty:
        row.label(text="", icon='BLANK1')
    else:
        row.label(text="", icon_value=Icons.PAIRED.get_icon())


def show_actor(layout, actor, scale=False):
    row = layout.row(align=True)
    if scale:
        row.scale_y = row_scale

    actor_id = animations.live_data.get_actor_id(actor)
    if paired_inputs.get(actor_id):
        row.label(text=actor_id + '  --> ' + ', '.join(paired_inputs.get(actor_id)), icon_value=Icons.SUIT.get_icon())
    else:
        row.enabled = False
        row.label(text=actor_id, icon_value=Icons.SUIT.get_icon())


def show_glove(layout, glove, scale=False):
    row = layout.row(align=True)
    if scale:
        row.scale_y = row_scale

    if paired_inputs.get(glove['gloveID']):
        row.label(text=glove['gloveID'] + '  --> ' + ', '.join(paired_inputs.get(glove['gloveID'])), icon='VIEW_PAN')
    else:
        row.enabled = False
        row.label(text=glove['gloveID'], icon='VIEW_PAN')


def show_face(layout, face, scale=False):
    row = layout.row(align=True)
    if scale:
        row.scale_y = row_scale

    face_id = animations.live_data.get_face_id(face)
    if paired_inputs.get(face_id):
        row.label(text=face_id + '  --> ' + ', '.join(paired_inputs.get(face_id)), icon_value=Icons.FACE.get_icon())
    else:
        row.enabled = False
        row.label(text=face_id, icon_value=Icons.FACE.get_icon())


def show_tracker(layout, tracker, scale=False):
    row = layout.row(align=True)
    if scale:
        row.scale_y = row_scale

    if paired_inputs.get(tracker['name']):
        row.label(text=tracker['name'] + '  --> ' + ', '.join(paired_inputs.get(tracker['name'])), icon_value=Icons.VP.get_icon())
    else:
        row.enabled = False
        row.label(text=tracker['name'], icon_value=Icons.VP.get_icon())


def show_prop(layout, prop, scale=False):
    row = layout.row(align=True)
    if scale:
        row.scale_y = row_scale

    prop_id = animations.live_data.get_prop_name_raw(prop)
    if paired_inputs.get(prop_id):
        row.label(text=prop_id + '  --> ' + ', '.join(paired_inputs.get(prop_id)), icon='FILE_3D')
    else:
        row.enabled = False
        row.label(text=prop_id, icon='FILE_3D')
