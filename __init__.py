# Important plugin info for Blender
bl_info = {
    'name': 'Rokoko Studio Live for Blender',
    'author': 'Rokoko Electronics ApS',
    'category': 'Animation',
    'location': 'View 3D > Tool Shelf > Rokoko',
    'description': 'Stream your Rokoko Studio animations directly into Blender',
    'version': (1, 2, 1),
    'blender': (2, 80, 0),
    'wiki_url': 'https://rokoko.freshdesk.com/support/solutions/folders/47000761699',
}

beta_branch = False

# If first startup of this plugin, load all modules normally
# If reloading the plugin, use importlib to reload modules
# This lets you do adjustments to the plugin on the fly without having to restart Blender
import sys
if "bpy" not in locals():
    import bpy
    from . import core
    from . import panels
    from . import operators
    from . import properties
else:
    import importlib
    importlib.reload(core)
    importlib.reload(panels)
    importlib.reload(operators)
    importlib.reload(properties)


# List of all buttons and panels
classes = [  # These panels will only be loaded when the user is logged in
    panels.objects.ObjectsPanel,
    panels.retargeting.RetargetingPanel,
    panels.info.InfoPanel,
]
classes_always_enable = [  # These non-panels will always be loaded, all non-panel ui should go in here
    operators.detector.DetectFaceShapes,
    operators.detector.DetectActorBones,
    operators.detector.SaveCustomShapes,
    operators.detector.SaveCustomBones,
    operators.detector.SaveCustomBonesRetargeting,
    operators.detector.ImportCustomBones,
    operators.detector.ExportCustomBones,
    operators.detector.ClearCustomBones,
    operators.detector.ClearCustomShapes,
    operators.actor.InitTPose,
    operators.actor.ResetTPose,
    operators.actor.PrintCurrentPose,
    operators.retargeting.BuildBoneList,
    operators.retargeting.ClearBoneList,
    operators.retargeting.RetargetAnimation,
    panels.retargeting.RSL_UL_BoneList,
    panels.retargeting.BoneListItem,
    operators.info.LicenseButton,
]


# register and unregister all classes
def register():
    print("\n### Loading Rokoko Studio Live for Blender...")

    # Register classes
    for cls in classes:
        bpy.utils.register_class(cls)
    for cls in classes_always_enable:
        bpy.utils.register_class(cls)

    # Register all custom properties
    properties.register()

    # Load custom icons
    core.icon_manager.load_icons()

    # Load bone detection list
    core.detection_manager.load_detection_lists()

    print("### Loaded Rokoko Studio Live for Blender successfully!\n")


def unregister():
    print("### Unloading Rokoko Studio Live for Blender...")

    # Unregister all classes
    for cls in reversed(classes + classes_always_enable):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

    # Unload all custom icons
    core.icon_manager.unload_icons()

    print("### Unloaded Rokoko Studio Live for Blender successfully!\n")


if __name__ == '__main__':
    register()
