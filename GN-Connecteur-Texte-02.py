import bpy
import mathutils
import os
import typing


def gn_connecteur_texte_02_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize GN-CONNECTEUR-TEXTE-02 node group"""
    gn_connecteur_texte_02_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="GN-CONNECTEUR-TEXTE-02")

    gn_connecteur_texte_02_1.color_tag = 'NONE'
    gn_connecteur_texte_02_1.description = ""
    gn_connecteur_texte_02_1.is_modifier = True

    # gn_connecteur_texte_02_1 interface

    # Socket Geometry
    geometry_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'

    # Socket Geometry
    geometry_socket_1 = gn_connecteur_texte_02_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'

    # Socket String
    string_socket = gn_connecteur_texte_02_1.interface.new_socket(name="String", in_out='INPUT', socket_type='NodeSocketString')
    string_socket.default_value = ""
    string_socket.attribute_domain = 'POINT'

    # Socket Radius
    radius_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 0.10000000149011612
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'

    # Socket MargesBox
    margesbox_socket = gn_connecteur_texte_02_1.interface.new_socket(name="MargesBox", in_out='INPUT', socket_type='NodeSocketFloat')
    margesbox_socket.default_value = 0.5
    margesbox_socket.min_value = -10000.0
    margesbox_socket.max_value = 10000.0
    margesbox_socket.subtype = 'NONE'
    margesbox_socket.attribute_domain = 'POINT'

    # Socket connector line offset x
    connector_line_offset_x_socket = gn_connecteur_texte_02_1.interface.new_socket(name="connector line offset x", in_out='INPUT', socket_type='NodeSocketFloat')
    connector_line_offset_x_socket.default_value = 0.0
    connector_line_offset_x_socket.min_value = -10000.0
    connector_line_offset_x_socket.max_value = 10000.0
    connector_line_offset_x_socket.subtype = 'NONE'
    connector_line_offset_x_socket.attribute_domain = 'POINT'

    # Socket connector line offset down
    connector_line_offset_down_socket = gn_connecteur_texte_02_1.interface.new_socket(name="connector line offset down", in_out='INPUT', socket_type='NodeSocketFloat')
    connector_line_offset_down_socket.default_value = 0.0
    connector_line_offset_down_socket.min_value = -10000.0
    connector_line_offset_down_socket.max_value = 10000.0
    connector_line_offset_down_socket.subtype = 'NONE'
    connector_line_offset_down_socket.attribute_domain = 'POINT'

    # Socket Suivi Camera
    suivi_camera_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Suivi Camera", in_out='INPUT', socket_type='NodeSocketBool')
    suivi_camera_socket.default_value = False
    suivi_camera_socket.attribute_domain = 'POINT'

    # Socket Scale global
    scale_global_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Scale global", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_global_socket.default_value = 1.0
    scale_global_socket.min_value = -10000.0
    scale_global_socket.max_value = 10000.0
    scale_global_socket.subtype = 'NONE'
    scale_global_socket.attribute_domain = 'POINT'

    # Socket distance
    distance_socket = gn_connecteur_texte_02_1.interface.new_socket(name="distance", in_out='INPUT', socket_type='NodeSocketVector')
    distance_socket.default_value = (1.0, 1.0, 0.0)
    distance_socket.min_value = -3.4028234663852886e+38
    distance_socket.max_value = 3.4028234663852886e+38
    distance_socket.subtype = 'TRANSLATION'
    distance_socket.attribute_domain = 'POINT'

    # Socket Rotation Manuel
    rotation_manuel_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Rotation Manuel", in_out='INPUT', socket_type='NodeSocketRotation')
    rotation_manuel_socket.default_value = (0.0, 0.0, 0.0)
    rotation_manuel_socket.attribute_domain = 'POINT'

    # Socket Cartouche ronde
    cartouche_ronde_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Cartouche ronde", in_out='INPUT', socket_type='NodeSocketBool')
    cartouche_ronde_socket.default_value = False
    cartouche_ronde_socket.attribute_domain = 'POINT'

    # Socket Cartouche Radius
    cartouche_radius_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Cartouche Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    cartouche_radius_socket.default_value = 3.5999999046325684
    cartouche_radius_socket.min_value = 0.0
    cartouche_radius_socket.max_value = 3.4028234663852886e+38
    cartouche_radius_socket.subtype = 'DISTANCE'
    cartouche_radius_socket.attribute_domain = 'POINT'

    # Socket Cartouche Res
    cartouche_res_socket = gn_connecteur_texte_02_1.interface.new_socket(name="Cartouche Res", in_out='INPUT', socket_type='NodeSocketInt')
    cartouche_res_socket.default_value = 8
    cartouche_res_socket.min_value = 1
    cartouche_res_socket.max_value = 1000
    cartouche_res_socket.subtype = 'NONE'
    cartouche_res_socket.attribute_domain = 'POINT'

    # Initialize gn_connecteur_texte_02_1 nodes

    # Node Group Input
    group_input = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Object Info
    object_info = gn_connecteur_texte_02_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'ORIGINAL'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Active Camera
    active_camera = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputActiveCamera")
    active_camera.name = "Active Camera"
    active_camera.show_options = True

    # Node Align Rotation to Vector
    align_rotation_to_vector = gn_connecteur_texte_02_1.nodes.new("FunctionNodeAlignRotationToVector")
    align_rotation_to_vector.name = "Align Rotation to Vector"
    align_rotation_to_vector.show_options = True
    align_rotation_to_vector.axis = 'Z'
    align_rotation_to_vector.pivot_axis = 'AUTO'
    # Factor
    align_rotation_to_vector.inputs[1].default_value = 1.0

    # Node String to Curves
    string_to_curves = gn_connecteur_texte_02_1.nodes.new("GeometryNodeStringToCurves")
    string_to_curves.name = "String to Curves"
    string_to_curves.show_options = True
    string_to_curves.align_x = 'LEFT'
    string_to_curves.align_y = 'MIDDLE'
    string_to_curves.overflow = 'OVERFLOW'
    string_to_curves.pivot_mode = 'BOTTOM_LEFT'
    # Size
    string_to_curves.inputs[1].default_value = 1.0
    # Character Spacing
    string_to_curves.inputs[2].default_value = 1.0
    # Word Spacing
    string_to_curves.inputs[3].default_value = 1.0
    # Line Spacing
    string_to_curves.inputs[4].default_value = 1.0
    # Text Box Width
    string_to_curves.inputs[5].default_value = 0.0

    # Node Instance on Points
    instance_on_points = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Fill Curve
    fill_curve = gn_connecteur_texte_02_1.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.show_options = True
    fill_curve.mode = 'TRIANGLES'
    # Group ID
    fill_curve.inputs[1].default_value = 0

    # Node Curve Line
    curve_line = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.show_options = True
    curve_line.mode = 'POINTS'

    # Node Compare
    compare = gn_connecteur_texte_02_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    # B_INT
    compare.inputs[3].default_value = 2

    # Node Object Info.001
    object_info_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.show_options = True
    object_info_001.transform_space = 'RELATIVE'
    if "Empty" in bpy.data.objects:
        object_info_001.inputs[0].default_value = bpy.data.objects["Empty"]
    # As Instance
    object_info_001.inputs[1].default_value = False

    # Node Curve Circle
    curve_circle = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.show_options = True
    curve_circle.mode = 'RADIUS'
    # Resolution
    curve_circle.inputs[0].default_value = 6

    # Node Join Geometry
    join_geometry = gn_connecteur_texte_02_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Reroute
    reroute = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    # Node Reroute.001
    reroute_001 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    # Node Reroute.003
    reroute_003 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    # Node Index.001
    index_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.hide = True
    index_001.show_options = True

    # Node Reroute.002
    reroute_002 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    # Node Reroute.005
    reroute_005 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    # Node Reroute.006
    reroute_006 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    # Node Reroute.008
    reroute_008 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    # Node Set Material
    set_material = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True
    if "Connector-Color" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["Connector-Color"]

    # Node Bounding Box
    bounding_box = gn_connecteur_texte_02_1.nodes.new("GeometryNodeBoundBox")
    bounding_box.name = "Bounding Box"
    bounding_box.show_options = True

    # Node Grid
    grid = gn_connecteur_texte_02_1.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.hide = True
    grid.show_options = True
    # Size X
    grid.inputs[0].default_value = 1.0
    # Size Y
    grid.inputs[1].default_value = 1.0
    # Vertices X
    grid.inputs[2].default_value = 3
    # Vertices Y
    grid.inputs[3].default_value = 3

    # Node Join Geometry.001
    join_geometry_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Curve to Mesh.001
    curve_to_mesh_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    curve_to_mesh_001.show_options = True
    # Fill Caps
    curve_to_mesh_001.inputs[2].default_value = False

    # Node Group Output.001
    group_output_001 = gn_connecteur_texte_02_1.nodes.new("NodeGroupOutput")
    group_output_001.name = "Group Output.001"
    group_output_001.show_options = True
    group_output_001.is_active_output = True

    # Node Join Geometry.002
    join_geometry_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"
    join_geometry_002.show_options = True

    # Node Separate XYZ
    separate_xyz = gn_connecteur_texte_02_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Separate XYZ.001
    separate_xyz_001 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.show_options = True

    # Node Math
    math = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False

    # Node Math.001
    math_001 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'ADD'
    math_001.use_clamp = False

    # Node Math.002
    math_002 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'SUBTRACT'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'SUBTRACT'
    math_003.use_clamp = False

    # Node Combine XYZ
    combine_xyz = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Transform Geometry
    transform_geometry = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.show_options = True
    transform_geometry.mode = 'COMPONENTS'
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry.001
    transform_geometry_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.show_options = True
    transform_geometry_001.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Mesh to Points
    mesh_to_points = gn_connecteur_texte_02_1.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.name = "Mesh to Points"
    mesh_to_points.show_options = True
    mesh_to_points.mode = 'EDGES'
    # Position
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Realize Instances
    realize_instances = gn_connecteur_texte_02_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Instance on Points.002
    instance_on_points_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.show_options = True
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0
    # Scale
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Compare.001
    compare_001 = gn_connecteur_texte_02_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    # B_INT
    compare_001.inputs[3].default_value = 1

    # Node Index.002
    index_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"
    index_002.hide = True
    index_002.show_options = True

    # Node Reroute.013
    reroute_013 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    # Node Math.004
    math_004 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = -1.0

    # Node Set Material.003
    set_material_003 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSetMaterial")
    set_material_003.name = "Set Material.003"
    set_material_003.show_options = True
    # Selection
    set_material_003.inputs[1].default_value = True
    if "BOX-Color" in bpy.data.materials:
        set_material_003.inputs[2].default_value = bpy.data.materials["BOX-Color"]

    # Node Set Material.004
    set_material_004 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSetMaterial")
    set_material_004.name = "Set Material.004"
    set_material_004.show_options = True
    # Selection
    set_material_004.inputs[1].default_value = True
    if "Texte-Color" in bpy.data.materials:
        set_material_004.inputs[2].default_value = bpy.data.materials["Texte-Color"]

    # Node Math.005
    math_005 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'ADD'
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = 0.0

    # Node Combine XYZ.001
    combine_xyz_001 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0
    # Z
    combine_xyz_001.inputs[2].default_value = 0.0

    # Node Reroute.014
    reroute_014 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    # Node Reroute.015
    reroute_015 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    # Node Math.006
    math_006 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 0.5

    # Node Reroute.016
    reroute_016 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    # Node Reroute.017
    reroute_017 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    # Node Frame
    frame = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame.label = "Cartouche"
    frame.name = "Frame"
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_001.label = "TEXTE"
    frame_001.name = "Frame.001"
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Combine XYZ.002
    combine_xyz_002 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.show_options = True
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0
    # Z
    combine_xyz_002.inputs[2].default_value = 0.0

    # Node Group Input.001
    group_input_001 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Combine XYZ.003
    combine_xyz_003 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.show_options = True
    # Y
    combine_xyz_003.inputs[1].default_value = 0.0
    # Z
    combine_xyz_003.inputs[2].default_value = 0.0

    # Node Math.007
    math_007 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = -0.5

    # Node Math.008
    math_008 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'ADD'
    math_008.use_clamp = False

    # Node Math.009
    math_009 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.hide = True
    math_009.show_options = True
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 0.5

    # Node Mesh to Points.001
    mesh_to_points_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_001.name = "Mesh to Points.001"
    mesh_to_points_001.show_options = True
    mesh_to_points_001.mode = 'VERTICES'
    # Position
    mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points_001.inputs[3].default_value = 0.05000000074505806

    # Node Compare.002
    compare_002 = gn_connecteur_texte_02_1.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.show_options = True
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    # B_INT
    compare_002.inputs[3].default_value = 7

    # Node Index.003
    index_003 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Sample Index
    sample_index = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'
    # Index
    sample_index.inputs[2].default_value = 6

    # Node Position
    position = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Realize Instances.001
    realize_instances_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.show_options = True
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Vector Math
    vector_math = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'ADD'

    # Node Curve Line.002
    curve_line_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_002.name = "Curve Line.002"
    curve_line_002.show_options = True
    curve_line_002.mode = 'POINTS'

    # Node Curve to Mesh.002
    curve_to_mesh_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_002.name = "Curve to Mesh.002"
    curve_to_mesh_002.show_options = True
    # Fill Caps
    curve_to_mesh_002.inputs[2].default_value = False

    # Node Sample Index.001
    sample_index_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'
    # Index
    sample_index_001.inputs[2].default_value = 8

    # Node Position.001
    position_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Vector Math.001
    vector_math_001 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'ADD'

    # Node Group Input.002
    group_input_002 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Combine XYZ.004
    combine_xyz_004 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.show_options = True
    # Z
    combine_xyz_004.inputs[2].default_value = 0.0

    # Node Combine XYZ.005
    combine_xyz_005 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.show_options = True
    # Y
    combine_xyz_005.inputs[1].default_value = 0.0
    # Z
    combine_xyz_005.inputs[2].default_value = 0.0

    # Node Frame.002
    frame_002 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_002.label = "CONNECTOR LINE"
    frame_002.name = "Frame.002"
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = False

    # Node Reroute.009
    reroute_009 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    # Node Reroute.018
    reroute_018 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    # Node Reroute.019
    reroute_019 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    # Node Reroute.010
    reroute_010 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    # Node Reroute.011
    reroute_011 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    # Node Reroute.020
    reroute_020 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    # Node Reroute.021
    reroute_021 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.show_options = True
    # Node Switch
    switch = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'ROTATION'

    # Node Group Input.003
    group_input_003 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Transform Geometry.002
    transform_geometry_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.show_options = True
    transform_geometry_002.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Vector Math.002
    vector_math_002 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'SCALE'
    # Vector
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)

    # Node Points
    points = gn_connecteur_texte_02_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True
    # Count
    points.inputs[0].default_value = 1
    # Position
    points.inputs[1].default_value = (0.0, -1.399999976158142, 0.0)
    # Radius
    points.inputs[2].default_value = 0.10000000149011612

    # Node Sample Index.002
    sample_index_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'
    # Index
    sample_index_002.inputs[2].default_value = 0

    # Node Position.002
    position_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Group Input.004
    group_input_004 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Group Input.005
    group_input_005 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Vector Math.003
    vector_math_003 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'MULTIPLY'
    # Vector_001
    vector_math_003.inputs[1].default_value = (-1.0, -1.0, -1.0)

    # Node Transform Geometry.003
    transform_geometry_003 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.show_options = True
    transform_geometry_003.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.004
    transform_geometry_004 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.show_options = True
    transform_geometry_004.mode = 'COMPONENTS'
    # Translation
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.009999999776482582)
    # Rotation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Bounding Box.001
    bounding_box_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeBoundBox")
    bounding_box_001.name = "Bounding Box.001"
    bounding_box_001.show_options = True

    # Node Vector Math.004
    vector_math_004 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.show_options = True
    vector_math_004.operation = 'ADD'

    # Node Transform Geometry.005
    transform_geometry_005 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.show_options = True
    transform_geometry_005.mode = 'COMPONENTS'
    # Translation
    transform_geometry_005.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math.007
    vector_math_007 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.show_options = True
    vector_math_007.operation = 'MULTIPLY'
    # Vector_001
    vector_math_007.inputs[1].default_value = (-1.0, -1.0, -1.0)

    # Node Realize Instances.002
    realize_instances_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    realize_instances_002.show_options = True
    # Selection
    realize_instances_002.inputs[1].default_value = True
    # Realize All
    realize_instances_002.inputs[2].default_value = True
    # Depth
    realize_instances_002.inputs[3].default_value = 0

    # Node Reroute.004
    reroute_004 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    # Node Transform Geometry.006
    transform_geometry_006 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_006.name = "Transform Geometry.006"
    transform_geometry_006.show_options = True
    transform_geometry_006.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_006.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Frame.004
    frame_004 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_005.label = "deplacement du tout au pivot"
    frame_005.name = "Frame.005"
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.006
    frame_006 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_006.label = "trouve centre pour revenir en arrière"
    frame_006.name = "Frame.006"
    frame_006.show_options = True
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Vector Math.008
    vector_math_008 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.show_options = True
    vector_math_008.operation = 'MULTIPLY'
    # Vector_001
    vector_math_008.inputs[1].default_value = (0.5, 0.5, 0.5)

    # Node Vector Math.009
    vector_math_009 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorMath")
    vector_math_009.name = "Vector Math.009"
    vector_math_009.show_options = True
    vector_math_009.operation = 'MULTIPLY'

    # Node Reroute.022
    reroute_022 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.show_options = True
    # Node Frame.007
    frame_007 = gn_connecteur_texte_02_1.nodes.new("NodeFrame")
    frame_007.label = "1. decentre par la moitier 2.Scale 3.repositionne + la scale"
    frame_007.name = "Frame.007"
    frame_007.show_options = True
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Reroute.023
    reroute_023 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.show_options = True
    # Node Reroute.024
    reroute_024 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    # Node Quadrilateral
    quadrilateral = gn_connecteur_texte_02_1.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    quadrilateral.name = "Quadrilateral"
    quadrilateral.show_options = True
    quadrilateral.mode = 'RECTANGLE'

    # Node Fillet Curve
    fillet_curve = gn_connecteur_texte_02_1.nodes.new("GeometryNodeFilletCurve")
    fillet_curve.name = "Fillet Curve"
    fillet_curve.show_options = True
    fillet_curve.mode = 'POLY'
    # Limit Radius
    fillet_curve.inputs[3].default_value = True

    # Node Fill Curve.001
    fill_curve_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeFillCurve")
    fill_curve_001.name = "Fill Curve.001"
    fill_curve_001.show_options = True
    fill_curve_001.mode = 'NGONS'
    # Group ID
    fill_curve_001.inputs[1].default_value = 0

    # Node Math.010
    math_010 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False
    # Value_001
    math_010.inputs[1].default_value = -1.0

    # Node Math.011
    math_011 = gn_connecteur_texte_02_1.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.show_options = True
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False
    # Value_001
    math_011.inputs[1].default_value = -1.0

    # Node Bounding Box.002
    bounding_box_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeBoundBox")
    bounding_box_002.name = "Bounding Box.002"
    bounding_box_002.mute = True
    bounding_box_002.show_options = True

    # Node Reroute.007
    reroute_007 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    # Node Instance on Points.003
    instance_on_points_003 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_003.name = "Instance on Points.003"
    instance_on_points_003.show_options = True
    # Selection
    instance_on_points_003.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_003.inputs[3].default_value = False
    # Instance Index
    instance_on_points_003.inputs[4].default_value = 0
    # Scale
    instance_on_points_003.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Reroute.012
    reroute_012 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    # Node Reroute.025
    reroute_025 = gn_connecteur_texte_02_1.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.show_options = True
    # Node Transform Geometry.007
    transform_geometry_007 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeTransform")
    transform_geometry_007.name = "Transform Geometry.007"
    transform_geometry_007.show_options = True
    transform_geometry_007.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_007.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Switch.001
    switch_001 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.show_options = True
    switch_001.input_type = 'GEOMETRY'

    # Node Group Input.006
    group_input_006 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True

    # Node Group Input.007
    group_input_007 = gn_connecteur_texte_02_1.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    group_input_007.outputs[13].hide = True

    # Node Mesh to Points.002
    mesh_to_points_002 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_002.name = "Mesh to Points.002"
    mesh_to_points_002.show_options = True
    mesh_to_points_002.mode = 'EDGES'
    # Position
    mesh_to_points_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points_002.inputs[3].default_value = 0.05000000074505806

    # Node Compare.003
    compare_003 = gn_connecteur_texte_02_1.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.show_options = True
    compare_003.data_type = 'INT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'EQUAL'
    # B_INT
    compare_003.inputs[3].default_value = 4

    # Node Join Geometry.003
    join_geometry_003 = gn_connecteur_texte_02_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"
    join_geometry_003.show_options = True

    # Node Vector Rotate
    vector_rotate = gn_connecteur_texte_02_1.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.show_options = True
    vector_rotate.invert = False
    vector_rotate.rotation_type = 'AXIS_ANGLE'
    # Vector
    vector_rotate.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Center
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Axis
    vector_rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
    # Angle
    vector_rotate.inputs[3].default_value = 0.0

    # Node Viewer
    viewer = gn_connecteur_texte_02_1.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.show_options = True
    viewer.data_type = 'FLOAT'
    viewer.domain = 'AUTO'
    # Value
    viewer.inputs[1].default_value = 0.0

    # Set parents
    gn_connecteur_texte_02_1.nodes["String to Curves"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Fill Curve"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Curve Line"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Curve Circle"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Reroute.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Bounding Box"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Grid"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Separate XYZ"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Mesh to Points"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Realize Instances"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Instance on Points.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Compare.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Index.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Reroute.013"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.004"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Set Material.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Set Material.004"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Math.005"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Reroute.015"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Math.006"].parent = gn_connecteur_texte_02_1.nodes["Frame.001"]
    gn_connecteur_texte_02_1.nodes["Reroute.016"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Reroute.017"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Group Input.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.007"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.008"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.009"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Sample Index"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Position"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Realize Instances.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Vector Math"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Curve Line.002"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Sample Index.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Position.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Vector Math.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Group Input.002"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Reroute.009"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].parent = gn_connecteur_texte_02_1.nodes["Frame.007"]
    gn_connecteur_texte_02_1.nodes["Group Input.004"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Vector Math.003"].parent = gn_connecteur_texte_02_1.nodes["Frame.002"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].parent = gn_connecteur_texte_02_1.nodes["Frame.007"]
    gn_connecteur_texte_02_1.nodes["Bounding Box.001"].parent = gn_connecteur_texte_02_1.nodes["Frame.006"]
    gn_connecteur_texte_02_1.nodes["Vector Math.004"].parent = gn_connecteur_texte_02_1.nodes["Frame.006"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].parent = gn_connecteur_texte_02_1.nodes["Frame.007"]
    gn_connecteur_texte_02_1.nodes["Vector Math.007"].parent = gn_connecteur_texte_02_1.nodes["Frame.006"]
    gn_connecteur_texte_02_1.nodes["Vector Math.008"].parent = gn_connecteur_texte_02_1.nodes["Frame.006"]
    gn_connecteur_texte_02_1.nodes["Vector Math.009"].parent = gn_connecteur_texte_02_1.nodes["Frame.006"]
    gn_connecteur_texte_02_1.nodes["Quadrilateral"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.010"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Math.011"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Bounding Box.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Instance on Points.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Reroute.012"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Reroute.025"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Switch.001"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Group Input.006"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Group Input.007"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Compare.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]
    gn_connecteur_texte_02_1.nodes["Join Geometry.003"].parent = gn_connecteur_texte_02_1.nodes["Frame"]

    # Set locations
    gn_connecteur_texte_02_1.nodes["Group Input"].location = (-1756.0589599609375, 1200.74658203125)
    gn_connecteur_texte_02_1.nodes["Object Info"].location = (-224.0371551513672, 428.14178466796875)
    gn_connecteur_texte_02_1.nodes["Active Camera"].location = (-434.19940185546875, 328.52294921875)
    gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].location = (12.04483413696289, 395.6163330078125)
    gn_connecteur_texte_02_1.nodes["String to Curves"].location = (-1103.6937255859375, 1514.0018310546875)
    gn_connecteur_texte_02_1.nodes["Instance on Points"].location = (341.29461669921875, 1962.920166015625)
    gn_connecteur_texte_02_1.nodes["Fill Curve"].location = (-513.8580932617188, 1602.147705078125)
    gn_connecteur_texte_02_1.nodes["Curve Line"].location = (2072.37548828125, -44.259063720703125)
    gn_connecteur_texte_02_1.nodes["Compare"].location = (152.68746948242188, 150.51275634765625)
    gn_connecteur_texte_02_1.nodes["Object Info.001"].location = (1220.423828125, -800.2595825195312)
    gn_connecteur_texte_02_1.nodes["Curve Circle"].location = (2001.8238525390625, -833.661376953125)
    gn_connecteur_texte_02_1.nodes["Join Geometry"].location = (4658.0302734375, 584.8904418945312)
    gn_connecteur_texte_02_1.nodes["Reroute"].location = (-1516.233154296875, 1167.7452392578125)
    gn_connecteur_texte_02_1.nodes["Reroute.001"].location = (-492.4835205078125, 1209.686767578125)
    gn_connecteur_texte_02_1.nodes["Reroute.003"].location = (2676.70947265625, 1958.14990234375)
    gn_connecteur_texte_02_1.nodes["Index.001"].location = (-2.7266387939453125, 86.92660522460938)
    gn_connecteur_texte_02_1.nodes["Reroute.002"].location = (4717.30859375, 69.03759765625)
    gn_connecteur_texte_02_1.nodes["Reroute.005"].location = (4481.30859375, -237.6932373046875)
    gn_connecteur_texte_02_1.nodes["Reroute.006"].location = (498.3876953125, 539.7015380859375)
    gn_connecteur_texte_02_1.nodes["Reroute.008"].location = (482.733642578125, 416.07470703125)
    gn_connecteur_texte_02_1.nodes["Set Material"].location = (4529.30859375, -84.94964599609375)
    gn_connecteur_texte_02_1.nodes["Bounding Box"].location = (-138.6651611328125, 1058.2889404296875)
    gn_connecteur_texte_02_1.nodes["Grid"].location = (770.5399780273438, 1235.346923828125)
    gn_connecteur_texte_02_1.nodes["Join Geometry.001"].location = (4383.44482421875, -428.34356689453125)
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].location = (2322.324462890625, -82.70557403564453)
    gn_connecteur_texte_02_1.nodes["Group Output.001"].location = (8637.01171875, 1406.0733642578125)
    gn_connecteur_texte_02_1.nodes["Join Geometry.002"].location = (3500.3603515625, 782.384033203125)
    gn_connecteur_texte_02_1.nodes["Separate XYZ"].location = (35.652069091796875, 1078.657470703125)
    gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].location = (18.946914672851562, 910.025634765625)
    gn_connecteur_texte_02_1.nodes["Math"].location = (353.9988098144531, 1147.36962890625)
    gn_connecteur_texte_02_1.nodes["Math.001"].location = (351.0389709472656, 891.0986328125)
    gn_connecteur_texte_02_1.nodes["Math.002"].location = (198.66397094726562, 1120.5391845703125)
    gn_connecteur_texte_02_1.nodes["Math.003"].location = (190.692626953125, 872.6550903320312)
    gn_connecteur_texte_02_1.nodes["Combine XYZ"].location = (551.7832641601562, 960.3905029296875)
    gn_connecteur_texte_02_1.nodes["Transform Geometry"].location = (1099.55419921875, 1242.1903076171875)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].location = (-695.0996704101562, 1550.945068359375)
    gn_connecteur_texte_02_1.nodes["Mesh to Points"].location = (756.0238647460938, 688.4938354492188)
    gn_connecteur_texte_02_1.nodes["Realize Instances"].location = (-885.2017211914062, 1530.23583984375)
    gn_connecteur_texte_02_1.nodes["Instance on Points.002"].location = (1081.1378173828125, 776.878662109375)
    gn_connecteur_texte_02_1.nodes["Compare.001"].location = (409.80120849609375, 383.5198974609375)
    gn_connecteur_texte_02_1.nodes["Index.002"].location = (246.40753173828125, 177.44924926757812)
    gn_connecteur_texte_02_1.nodes["Reroute.013"].location = (56.39666748046875, 686.2181396484375)
    gn_connecteur_texte_02_1.nodes["Math.004"].location = (-1046.363037109375, 1012.2216796875)
    gn_connecteur_texte_02_1.nodes["Set Material.003"].location = (1771.72216796875, 819.5880126953125)
    gn_connecteur_texte_02_1.nodes["Set Material.004"].location = (-344.81884765625, 1629.5921630859375)
    gn_connecteur_texte_02_1.nodes["Math.005"].location = (-857.4955444335938, 1204.4342041015625)
    gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].location = (-889.965087890625, 1334.315673828125)
    gn_connecteur_texte_02_1.nodes["Reroute.014"].location = (-1301.0535888671875, 950.5928344726562)
    gn_connecteur_texte_02_1.nodes["Reroute.015"].location = (-1082.611572265625, 1092.722900390625)
    gn_connecteur_texte_02_1.nodes["Math.006"].location = (-1037.2783203125, 1181.0555419921875)
    gn_connecteur_texte_02_1.nodes["Reroute.016"].location = (47.76275634765625, 621.75)
    gn_connecteur_texte_02_1.nodes["Reroute.017"].location = (706.1586303710938, 556.419677734375)
    gn_connecteur_texte_02_1.nodes["Frame"].location = (668.7723999023438, 273.9205322265625)
    gn_connecteur_texte_02_1.nodes["Frame.001"].location = (0.0, 0.0)
    gn_connecteur_texte_02_1.nodes["Combine XYZ.002"].location = (589.8512573242188, 791.4240112304688)
    gn_connecteur_texte_02_1.nodes["Group Input.001"].location = (-88.17613220214844, 562.98974609375)
    gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].location = (914.1609497070312, 1152.0032958984375)
    gn_connecteur_texte_02_1.nodes["Math.007"].location = (561.0441284179688, 1200.8114013671875)
    gn_connecteur_texte_02_1.nodes["Math.008"].location = (744.4204711914062, 1185.2850341796875)
    gn_connecteur_texte_02_1.nodes["Math.009"].location = (562.6062622070312, 1028.8497314453125)
    gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].location = (114.1783447265625, 1933.317626953125)
    gn_connecteur_texte_02_1.nodes["Compare.002"].location = (-81.72406005859375, 1949.49365234375)
    gn_connecteur_texte_02_1.nodes["Index.003"].location = (-263.96563720703125, 1891.7781982421875)
    gn_connecteur_texte_02_1.nodes["Sample Index"].location = (1379.629638671875, 75.375)
    gn_connecteur_texte_02_1.nodes["Position"].location = (1228.2994384765625, -29.152740478515625)
    gn_connecteur_texte_02_1.nodes["Realize Instances.001"].location = (1249.625244140625, 662.60888671875)
    gn_connecteur_texte_02_1.nodes["Vector Math"].location = (1626.891357421875, 17.19342041015625)
    gn_connecteur_texte_02_1.nodes["Curve Line.002"].location = (2074.06103515625, -425.2611389160156)
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].location = (2469.5615234375, -743.8351440429688)
    gn_connecteur_texte_02_1.nodes["Sample Index.001"].location = (1404.4761962890625, -249.90859985351562)
    gn_connecteur_texte_02_1.nodes["Position.001"].location = (1185.8658447265625, -391.32861328125)
    gn_connecteur_texte_02_1.nodes["Vector Math.001"].location = (1647.61865234375, -264.9219970703125)
    gn_connecteur_texte_02_1.nodes["Group Input.002"].location = (909.866455078125, -370.461669921875)
    gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].location = (1500.2281494140625, -477.39593505859375)
    gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].location = (1480.3433837890625, -119.44186401367188)
    gn_connecteur_texte_02_1.nodes["Frame.002"].location = (1489.6253662109375, -36.996826171875)
    gn_connecteur_texte_02_1.nodes["Reroute.009"].location = (980.87255859375, -43.48597717285156)
    gn_connecteur_texte_02_1.nodes["Reroute.018"].location = (2478.300537109375, 95.42762756347656)
    gn_connecteur_texte_02_1.nodes["Reroute.019"].location = (2242.30029296875, 726.93701171875)
    gn_connecteur_texte_02_1.nodes["Reroute.010"].location = (58.64158630371094, 1750.173095703125)
    gn_connecteur_texte_02_1.nodes["Reroute.011"].location = (68.34578704833984, 895.5408935546875)
    gn_connecteur_texte_02_1.nodes["Reroute.020"].location = (221.83203125, 548.5606079101562)
    gn_connecteur_texte_02_1.nodes["Reroute.021"].location = (246.58554077148438, 1654.3275146484375)
    gn_connecteur_texte_02_1.nodes["Switch"].location = (223.05673217773438, 516.80517578125)
    gn_connecteur_texte_02_1.nodes["Group Input.003"].location = (-18.680545806884766, 769.6381225585938)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].location = (6976.23193359375, 914.272705078125)
    gn_connecteur_texte_02_1.nodes["Vector Math.002"].location = (5192.9443359375, 690.3019409179688)
    gn_connecteur_texte_02_1.nodes["Points"].location = (1854.4007568359375, -1282.5164794921875)
    gn_connecteur_texte_02_1.nodes["Sample Index.002"].location = (2329.7001953125, -1249.3797607421875)
    gn_connecteur_texte_02_1.nodes["Position.002"].location = (2128.4775390625, -1408.1461181640625)
    gn_connecteur_texte_02_1.nodes["Group Input.004"].location = (1327.9869384765625, -779.3353271484375)
    gn_connecteur_texte_02_1.nodes["Group Input.005"].location = (4751.4091796875, 1045.51318359375)
    gn_connecteur_texte_02_1.nodes["Vector Math.003"].location = (1595.033203125, -923.25146484375)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].location = (7669.16357421875, 869.2117309570312)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.004"].location = (-143.54461669921875, 1669.7489013671875)
    gn_connecteur_texte_02_1.nodes["Bounding Box.001"].location = (-17.68115234375, -34.84130859375)
    gn_connecteur_texte_02_1.nodes["Vector Math.004"].location = (175.49609375, -9.26171875)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].location = (7423.27294921875, 909.8168334960938)
    gn_connecteur_texte_02_1.nodes["Vector Math.007"].location = (509.39306640625, -187.46484375)
    gn_connecteur_texte_02_1.nodes["Realize Instances.002"].location = (6165.31689453125, 1017.2500610351562)
    gn_connecteur_texte_02_1.nodes["Reroute.004"].location = (5807.65625, 896.0787353515625)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].location = (5954.27880859375, 1046.4378662109375)
    gn_connecteur_texte_02_1.nodes["Frame.004"].location = (0.0, 0.0)
    gn_connecteur_texte_02_1.nodes["Frame.005"].location = (5117.67626953125, 1011.523681640625)
    gn_connecteur_texte_02_1.nodes["Frame.006"].location = (7180.31640625, 1454.90283203125)
    gn_connecteur_texte_02_1.nodes["Vector Math.008"].location = (344.0810546875, -62.4627685546875)
    gn_connecteur_texte_02_1.nodes["Vector Math.009"].location = (899.6640625, -86.66796875)
    gn_connecteur_texte_02_1.nodes["Reroute.022"].location = (6826.37109375, 616.3657836914062)
    gn_connecteur_texte_02_1.nodes["Frame.007"].location = (897.9790649414062, -14.28594970703125)
    gn_connecteur_texte_02_1.nodes["Reroute.023"].location = (6889.90380859375, 956.3050537109375)
    gn_connecteur_texte_02_1.nodes["Reroute.024"].location = (7209.337890625, 985.2894287109375)
    gn_connecteur_texte_02_1.nodes["Quadrilateral"].location = (715.8599243164062, 1492.0462646484375)
    gn_connecteur_texte_02_1.nodes["Fillet Curve"].location = (1594.316162109375, 1729.82861328125)
    gn_connecteur_texte_02_1.nodes["Fill Curve.001"].location = (1750.193603515625, 1777.195556640625)
    gn_connecteur_texte_02_1.nodes["Math.010"].location = (421.77484130859375, 1515.1942138671875)
    gn_connecteur_texte_02_1.nodes["Math.011"].location = (538.1503295898438, 1363.5384521484375)
    gn_connecteur_texte_02_1.nodes["Bounding Box.002"].location = (1295.543701171875, 359.652099609375)
    gn_connecteur_texte_02_1.nodes["Reroute.007"].location = (2729.6357421875, 1062.045166015625)
    gn_connecteur_texte_02_1.nodes["Instance on Points.003"].location = (1421.4296875, 1124.6385498046875)
    gn_connecteur_texte_02_1.nodes["Reroute.012"].location = (1010.5314331054688, 601.7672119140625)
    gn_connecteur_texte_02_1.nodes["Reroute.025"].location = (985.8270874023438, 879.1331787109375)
    gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].location = (1273.2275390625, 1481.64453125)
    gn_connecteur_texte_02_1.nodes["Switch.001"].location = (1604.33837890625, 833.25634765625)
    gn_connecteur_texte_02_1.nodes["Group Input.006"].location = (1410.848388671875, 801.8582763671875)
    gn_connecteur_texte_02_1.nodes["Group Input.007"].location = (720.5108032226562, 1348.3233642578125)
    gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].location = (739.2125854492188, 314.1221923828125)
    gn_connecteur_texte_02_1.nodes["Compare.003"].location = (506.08428955078125, 195.570068359375)
    gn_connecteur_texte_02_1.nodes["Join Geometry.003"].location = (924.2742309570312, 362.64593505859375)
    gn_connecteur_texte_02_1.nodes["Vector Rotate"].location = (403.561767578125, 322.00445556640625)
    gn_connecteur_texte_02_1.nodes["Viewer"].location = (294.0, 2043.0)

    # Set dimensions
    gn_connecteur_texte_02_1.nodes["Group Input"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Object Info"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Object Info"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Active Camera"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Active Camera"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].height = 100.0

    gn_connecteur_texte_02_1.nodes["String to Curves"].width  = 190.0
    gn_connecteur_texte_02_1.nodes["String to Curves"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Instance on Points"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Instance on Points"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Fill Curve"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Fill Curve"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Curve Line"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Curve Line"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Compare"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Compare"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Object Info.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Object Info.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Curve Circle"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Curve Circle"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Join Geometry"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Join Geometry"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.001"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.003"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Index.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Index.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.002"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.005"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.005"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.006"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.006"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.008"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.008"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Set Material"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Set Material"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Bounding Box"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Bounding Box"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Grid"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Grid"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Join Geometry.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Join Geometry.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Output.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Output.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Join Geometry.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Join Geometry.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Separate XYZ"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Separate XYZ"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Mesh to Points"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Mesh to Points"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Realize Instances"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Realize Instances"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Instance on Points.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Instance on Points.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Compare.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Compare.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Index.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Index.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.013"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.013"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Set Material.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Set Material.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Set Material.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Set Material.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.005"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.005"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.014"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.014"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.015"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.015"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.006"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.006"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.016"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.016"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.017"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.017"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Frame"].width  = 2110.0
    gn_connecteur_texte_02_1.nodes["Frame"].height = 1538.0

    gn_connecteur_texte_02_1.nodes["Frame.001"].width  = 959.0
    gn_connecteur_texte_02_1.nodes["Frame.001"].height = 836.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.007"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.007"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.008"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.008"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.009"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.009"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Compare.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Compare.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Index.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Index.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Sample Index"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Sample Index"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Position"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Position"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Realize Instances.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Realize Instances.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Curve Line.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Curve Line.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Sample Index.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Sample Index.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Position.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Position.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Frame.002"].width  = 1863.2969970703125
    gn_connecteur_texte_02_1.nodes["Frame.002"].height = 1416.38623046875

    gn_connecteur_texte_02_1.nodes["Reroute.009"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.009"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.018"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.018"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.019"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.019"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.010"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.010"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.011"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.011"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.020"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.020"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.021"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.021"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Switch"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Switch"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Points"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Points"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Sample Index.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Sample Index.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Position.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Position.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.005"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.005"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Bounding Box.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Bounding Box.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.004"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.007"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.007"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Realize Instances.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Realize Instances.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.004"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Frame.004"].width  = 150.0
    gn_connecteur_texte_02_1.nodes["Frame.004"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Frame.005"].width  = 150.0
    gn_connecteur_texte_02_1.nodes["Frame.005"].height = 353.1337890625

    gn_connecteur_texte_02_1.nodes["Frame.006"].width  = 1117.0
    gn_connecteur_texte_02_1.nodes["Frame.006"].height = 434.0

    gn_connecteur_texte_02_1.nodes["Vector Math.008"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.008"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Math.009"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Math.009"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.022"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.022"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Frame.007"].width  = 893.0
    gn_connecteur_texte_02_1.nodes["Frame.007"].height = 402.0

    gn_connecteur_texte_02_1.nodes["Reroute.023"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.023"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.024"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.024"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Quadrilateral"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Quadrilateral"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Fillet Curve"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Fillet Curve"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Fill Curve.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Fill Curve.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.010"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.010"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Math.011"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Math.011"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Bounding Box.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Bounding Box.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.007"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.007"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Instance on Points.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Instance on Points.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.012"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.012"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Reroute.025"].width  = 16.0
    gn_connecteur_texte_02_1.nodes["Reroute.025"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Switch.001"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Switch.001"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.006"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.006"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Group Input.007"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Group Input.007"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Compare.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Compare.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Join Geometry.003"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Join Geometry.003"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Vector Rotate"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Vector Rotate"].height = 100.0

    gn_connecteur_texte_02_1.nodes["Viewer"].width  = 140.0
    gn_connecteur_texte_02_1.nodes["Viewer"].height = 100.0


    # Initialize gn_connecteur_texte_02_1 links

    # active_camera.Active Camera -> object_info.Object
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Active Camera"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Object Info"].inputs[0]
    )
    # object_info.Rotation -> align_rotation_to_vector.Rotation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Object Info"].outputs[2],
        gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].inputs[0]
    )
    # object_info.Location -> align_rotation_to_vector.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Object Info"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].inputs[2]
    )
    # reroute.Output -> string_to_curves.String
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute"].outputs[0],
        gn_connecteur_texte_02_1.nodes["String to Curves"].inputs[0]
    )
    # reroute_021.Output -> instance_on_points.Rotation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.021"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points"].inputs[5]
    )
    # transform_geometry_001.Geometry -> reroute_001.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.001"].inputs[0]
    )
    # index_001.Index -> compare.A
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Index.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Compare"].inputs[2]
    )
    # set_material.Geometry -> reroute_002.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Set Material"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_008.Output -> reroute_006.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.008"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_005.Output -> set_material.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.005"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Set Material"].inputs[0]
    )
    # join_geometry_001.Geometry -> reroute_005.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Join Geometry.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.005"].inputs[0]
    )
    # curve_line.Curve -> curve_to_mesh_001.Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve Line"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].inputs[0]
    )
    # curve_circle.Curve -> curve_to_mesh_001.Profile Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve Circle"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].inputs[1]
    )
    # bounding_box.Min -> separate_xyz.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Separate XYZ"].inputs[0]
    )
    # bounding_box.Max -> separate_xyz_001.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box"].outputs[2],
        gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].inputs[0]
    )
    # math_002.Value -> math.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math"].inputs[0]
    )
    # math_003.Value -> math_001.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.001"].inputs[0]
    )
    # reroute_013.Output -> math.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.013"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math"].inputs[1]
    )
    # reroute_013.Output -> math_001.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.013"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.001"].inputs[1]
    )
    # math.Value -> combine_xyz.X
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Combine XYZ"].inputs[0]
    )
    # math_001.Value -> combine_xyz.Y
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Combine XYZ"].inputs[1]
    )
    # separate_xyz.X -> math_002.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Separate XYZ"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.002"].inputs[0]
    )
    # separate_xyz_001.X -> math_002.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.002"].inputs[1]
    )
    # separate_xyz.Y -> math_003.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Separate XYZ"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Math.003"].inputs[0]
    )
    # separate_xyz_001.Y -> math_003.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Separate XYZ.001"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Math.003"].inputs[1]
    )
    # set_material_003.Geometry -> join_geometry_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Set Material.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.002"].inputs[0]
    )
    # reroute_017.Output -> mesh_to_points.Mesh
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.017"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points"].inputs[0]
    )
    # reroute_001.Output -> bounding_box.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Bounding Box"].inputs[0]
    )
    # string_to_curves.Curve Instances -> realize_instances.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["String to Curves"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Realize Instances"].inputs[0]
    )
    # mesh_to_points.Points -> instance_on_points_002.Points
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Mesh to Points"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.002"].inputs[0]
    )
    # index_002.Index -> compare_001.A
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Index.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Compare.001"].inputs[2]
    )
    # transform_geometry.Geometry -> instance_on_points_002.Instance
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.002"].inputs[2]
    )
    # math_004.Value -> reroute_013.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.013"].inputs[0]
    )
    # reroute_014.Output -> math_004.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.014"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.004"].inputs[0]
    )
    # realize_instances.Geometry -> transform_geometry_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Realize Instances"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # math_005.Value -> combine_xyz_001.X
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.005"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].inputs[0]
    )
    # combine_xyz_001.Vector -> transform_geometry_001.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].inputs[1]
    )
    # group_input.MargesBox -> reroute_014.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input"].outputs[3],
        gn_connecteur_texte_02_1.nodes["Reroute.014"].inputs[0]
    )
    # math_006.Value -> math_005.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.006"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.005"].inputs[0]
    )
    # reroute_014.Output -> reroute_015.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.014"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.015"].inputs[0]
    )
    # reroute_015.Output -> math_006.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.015"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.006"].inputs[0]
    )
    # group_input.String -> reroute.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Reroute"].inputs[0]
    )
    # bounding_box.Bounding Box -> reroute_016.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.016"].inputs[0]
    )
    # reroute_016.Output -> reroute_017.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.016"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.017"].inputs[0]
    )
    # compare_001.Result -> mesh_to_points.Selection
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Compare.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points"].inputs[1]
    )
    # transform_geometry_001.Geometry -> fill_curve.Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Fill Curve"].inputs[0]
    )
    # fill_curve.Mesh -> set_material_004.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Fill Curve"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Set Material.004"].inputs[0]
    )
    # math.Value -> math_007.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.007"].inputs[0]
    )
    # math_008.Value -> combine_xyz_003.X
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.008"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].inputs[0]
    )
    # math_007.Value -> math_008.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.007"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.008"].inputs[0]
    )
    # math_009.Value -> math_008.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.009"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.008"].inputs[1]
    )
    # reroute_013.Output -> math_009.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.013"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.009"].inputs[0]
    )
    # reroute_012.Output -> instance_on_points_002.Rotation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.012"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.002"].inputs[5]
    )
    # index_003.Index -> compare_002.A
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Index.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Compare.002"].inputs[2]
    )
    # position.Position -> sample_index.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Position"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index"].inputs[1]
    )
    # compare_002.Result -> mesh_to_points_001.Selection
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Compare.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].inputs[1]
    )
    # vector_math.Vector -> curve_line.Start
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve Line"].inputs[0]
    )
    # instance_on_points_002.Instances -> realize_instances_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Instance on Points.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Realize Instances.001"].inputs[0]
    )
    # reroute_009.Output -> sample_index.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.009"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index"].inputs[0]
    )
    # sample_index.Value -> vector_math.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Sample Index"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math"].inputs[0]
    )
    # curve_line_002.Curve -> curve_to_mesh_002.Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve Line.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].inputs[0]
    )
    # position_001.Position -> sample_index_001.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Position.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_index_001.Value -> vector_math_001.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Sample Index.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math_001.Vector -> curve_line.End
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve Line"].inputs[1]
    )
    # reroute_009.Output -> sample_index_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.009"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index.001"].inputs[0]
    )
    # vector_math_001.Vector -> curve_line_002.Start
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve Line.002"].inputs[0]
    )
    # curve_to_mesh_002.Mesh -> join_geometry_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.001"].inputs[0]
    )
    # curve_circle.Curve -> curve_to_mesh_002.Profile Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve Circle"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.002"].inputs[1]
    )
    # group_input_002.Radius -> curve_circle.Radius
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.002"].outputs[2],
        gn_connecteur_texte_02_1.nodes["Curve Circle"].inputs[4]
    )
    # combine_xyz_004.Vector -> vector_math_001.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.001"].inputs[1]
    )
    # combine_xyz_005.Vector -> vector_math.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math"].inputs[1]
    )
    # group_input_002.connector line offset x -> combine_xyz_004.X
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.002"].outputs[4],
        gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].inputs[0]
    )
    # group_input_002.connector line offset x -> combine_xyz_005.X
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.002"].outputs[4],
        gn_connecteur_texte_02_1.nodes["Combine XYZ.005"].inputs[0]
    )
    # group_input_002.connector line offset down -> combine_xyz_004.Y
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.002"].outputs[5],
        gn_connecteur_texte_02_1.nodes["Combine XYZ.004"].inputs[1]
    )
    # reroute_018.Output -> reroute_009.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.018"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.009"].inputs[0]
    )
    # realize_instances_001.Geometry -> reroute_019.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Realize Instances.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.019"].inputs[0]
    )
    # instance_on_points.Instances -> reroute_003.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Instance on Points"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.003"].inputs[0]
    )
    # transform_geometry_004.Geometry -> instance_on_points.Instance
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points"].inputs[2]
    )
    # reroute_010.Output -> mesh_to_points_001.Mesh
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.010"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].inputs[0]
    )
    # reroute_011.Output -> reroute_010.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.011"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_006.Output -> reroute_020.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.006"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.020"].inputs[0]
    )
    # reroute_020.Output -> reroute_021.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.020"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.021"].inputs[0]
    )
    # group_input_003.Suivi Camera -> switch.Switch
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.003"].outputs[6],
        gn_connecteur_texte_02_1.nodes["Switch"].inputs[0]
    )
    # switch.Output -> reroute_008.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Switch"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.008"].inputs[0]
    )
    # position_002.Position -> sample_index_002.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Position.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index.002"].inputs[1]
    )
    # group_input_004.Geometry -> sample_index_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Sample Index.002"].inputs[0]
    )
    # group_input_005.Scale global -> vector_math_002.Scale
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.005"].outputs[7],
        gn_connecteur_texte_02_1.nodes["Vector Math.002"].inputs[3]
    )
    # group_input_004.distance -> vector_math_003.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.004"].outputs[8],
        gn_connecteur_texte_02_1.nodes["Vector Math.003"].inputs[0]
    )
    # vector_math_003.Vector -> curve_line_002.End
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Curve Line.002"].inputs[1]
    )
    # transform_geometry_005.Geometry -> transform_geometry_003.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].inputs[0]
    )
    # mesh_to_points_001.Points -> instance_on_points.Points
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points"].inputs[0]
    )
    # set_material_004.Geometry -> transform_geometry_004.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Set Material.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.004"].inputs[0]
    )
    # realize_instances_002.Geometry -> bounding_box_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Realize Instances.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Bounding Box.001"].inputs[0]
    )
    # transform_geometry_002.Geometry -> transform_geometry_005.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].inputs[0]
    )
    # reroute_022.Output -> transform_geometry_005.Scale
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.022"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.005"].inputs[3]
    )
    # reroute_004.Output -> transform_geometry_006.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].inputs[0]
    )
    # group_input_005.distance -> transform_geometry_006.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.005"].outputs[8],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].inputs[1]
    )
    # transform_geometry_006.Geometry -> realize_instances_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.006"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Realize Instances.002"].inputs[0]
    )
    # transform_geometry_003.Geometry -> group_output_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Group Output.001"].inputs[0]
    )
    # bounding_box_001.Min -> vector_math_004.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box.001"].outputs[1],
        gn_connecteur_texte_02_1.nodes["Vector Math.004"].inputs[0]
    )
    # bounding_box_001.Max -> vector_math_004.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box.001"].outputs[2],
        gn_connecteur_texte_02_1.nodes["Vector Math.004"].inputs[1]
    )
    # vector_math_008.Vector -> vector_math_007.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.008"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.007"].inputs[0]
    )
    # vector_math_007.Vector -> transform_geometry_002.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.007"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].inputs[1]
    )
    # vector_math_009.Vector -> transform_geometry_003.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.009"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.003"].inputs[1]
    )
    # realize_instances_002.Geometry -> transform_geometry_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Realize Instances.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.002"].inputs[0]
    )
    # vector_math_004.Vector -> vector_math_008.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.004"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.008"].inputs[0]
    )
    # vector_math_002.Vector -> reroute_022.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.022"].inputs[0]
    )
    # reroute_024.Output -> vector_math_009.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.024"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.009"].inputs[1]
    )
    # vector_math_008.Vector -> vector_math_009.Vector
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Vector Math.008"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Vector Math.009"].inputs[0]
    )
    # reroute_022.Output -> reroute_023.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.022"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.023"].inputs[0]
    )
    # reroute_023.Output -> reroute_024.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.023"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.024"].inputs[0]
    )
    # join_geometry.Geometry -> reroute_004.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Join Geometry"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.004"].inputs[0]
    )
    # join_geometry_002.Geometry -> join_geometry.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Join Geometry.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry"].inputs[0]
    )
    # align_rotation_to_vector.Rotation -> switch.True
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Align Rotation to Vector"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Switch"].inputs[2]
    )
    # group_input_003.Rotation Manuel -> switch.False
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.003"].outputs[9],
        gn_connecteur_texte_02_1.nodes["Switch"].inputs[1]
    )
    # quadrilateral.Curve -> fillet_curve.Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Quadrilateral"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Fillet Curve"].inputs[0]
    )
    # fillet_curve.Curve -> fill_curve_001.Curve
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Fillet Curve"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Fill Curve.001"].inputs[0]
    )
    # combine_xyz_003.Vector -> transform_geometry.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry"].inputs[1]
    )
    # math_011.Value -> quadrilateral.Height
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.011"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Quadrilateral"].inputs[1]
    )
    # math_010.Value -> quadrilateral.Width
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.010"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Quadrilateral"].inputs[0]
    )
    # math.Value -> math_010.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.010"].inputs[0]
    )
    # math_001.Value -> math_011.Value
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Math.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Math.011"].inputs[0]
    )
    # reroute_019.Output -> bounding_box_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.019"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Bounding Box.002"].inputs[0]
    )
    # grid.Mesh -> transform_geometry.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Grid"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry"].inputs[0]
    )
    # combine_xyz.Vector -> transform_geometry.Scale
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry"].inputs[3]
    )
    # mesh_to_points.Points -> instance_on_points_003.Points
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Mesh to Points"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.003"].inputs[0]
    )
    # transform_geometry_007.Geometry -> instance_on_points_003.Instance
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.003"].inputs[2]
    )
    # reroute_003.Output -> reroute_007.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_008.Output -> reroute_012.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.008"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_025.Output -> instance_on_points_003.Rotation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.025"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Instance on Points.003"].inputs[5]
    )
    # reroute_012.Output -> reroute_025.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.012"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.025"].inputs[0]
    )
    # fill_curve_001.Mesh -> transform_geometry_007.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Fill Curve.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].inputs[0]
    )
    # combine_xyz_003.Vector -> transform_geometry_007.Translation
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Combine XYZ.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Transform Geometry.007"].inputs[1]
    )
    # instance_on_points_002.Instances -> switch_001.False
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Instance on Points.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Switch.001"].inputs[1]
    )
    # instance_on_points_003.Instances -> switch_001.True
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Instance on Points.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Switch.001"].inputs[2]
    )
    # switch_001.Output -> set_material_003.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Switch.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Set Material.003"].inputs[0]
    )
    # group_input_006.Cartouche ronde -> switch_001.Switch
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.006"].outputs[10],
        gn_connecteur_texte_02_1.nodes["Switch.001"].inputs[0]
    )
    # group_input_007.Cartouche Radius -> fillet_curve.Radius
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.007"].outputs[11],
        gn_connecteur_texte_02_1.nodes["Fillet Curve"].inputs[2]
    )
    # group_input_007.Cartouche Res -> fillet_curve.Count
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Group Input.007"].outputs[12],
        gn_connecteur_texte_02_1.nodes["Fillet Curve"].inputs[1]
    )
    # reroute_017.Output -> mesh_to_points_002.Mesh
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.017"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].inputs[0]
    )
    # compare_003.Result -> mesh_to_points_002.Selection
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Compare.003"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].inputs[1]
    )
    # index_002.Index -> compare_003.A
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Index.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Compare.003"].inputs[2]
    )
    # bounding_box.Bounding Box -> join_geometry_003.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.003"].inputs[0]
    )
    # mesh_to_points_001.Points -> viewer.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Mesh to Points.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Viewer"].inputs[0]
    )
    # reroute_019.Output -> reroute_018.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.019"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.018"].inputs[0]
    )
    # bounding_box_002.Bounding Box -> reroute_011.Input
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Bounding Box.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Reroute.011"].inputs[0]
    )
    # reroute_002.Output -> join_geometry.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry"].inputs[0]
    )
    # curve_to_mesh_001.Mesh -> join_geometry_001.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Curve to Mesh.001"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.001"].inputs[0]
    )
    # reroute_007.Output -> join_geometry_002.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Reroute.007"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.002"].inputs[0]
    )
    # mesh_to_points_002.Points -> join_geometry_003.Geometry
    gn_connecteur_texte_02_1.links.new(
        gn_connecteur_texte_02_1.nodes["Mesh to Points.002"].outputs[0],
        gn_connecteur_texte_02_1.nodes["Join Geometry.003"].inputs[0]
    )

    return gn_connecteur_texte_02_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    gn_connecteur_texte_02 = gn_connecteur_texte_02_1_node_group(node_tree_names)
    node_tree_names[gn_connecteur_texte_02_1_node_group] = gn_connecteur_texte_02.name

