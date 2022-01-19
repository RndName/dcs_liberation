# Statics
from dcs import unittype
from game.modsupport import fortificationmod


@fortificationmod
class ERO_Hesco_Barrier_Tower2(unittype.StaticType):
    id = "ERO_Hesco_Barrier_Tower2"
    name = "ERO Hesco Barrier Tower (stackable)"
    shape_name = "ERO_Hesco_Barrier_Tower2"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM11(unittype.StaticType):
    id = "ERO_Revetment_SAM11"
    name = "ERO Revetment O5"
    shape_name = "ERO_Revetment_SAM11"
    rate = 10


@fortificationmod
class ERO_Revetment_D(unittype.StaticType):
    id = "ERO_Revetment_D"
    name = "ERO Revetment D"
    shape_name = "ERO_Revetment_D"
    rate = 10


@fortificationmod
class ERO_Revetment_Platform1(unittype.StaticType):
    id = "ERO_Revetment_Platform1"
    name = "ERO Revetment Platform A"
    shape_name = "ERO_Revetment_Platform1"
    rate = 10


@fortificationmod
class ERO_Revetment_Platform2(unittype.StaticType):
    id = "ERO_Revetment_Platform2"
    name = "ERO Revetment Platform B"
    shape_name = "ERO_Revetment_Platform2"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_D_elevated(unittype.StaticType):
    id = "ERO_Revetment_SAM_D_elevated"
    name = "ERO Revetment D Elevated"
    shape_name = "ERO_Revetment_SAM_D_elevated"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_O(unittype.StaticType):
    id = "ERO_Revetment_SAM_O"
    name = "ERO Revetment O"
    shape_name = "ERO_Revetment_SAM_O"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_O2(unittype.StaticType):
    id = "ERO_Revetment_SAM_O2"
    name = "ERO Revetment O2"
    shape_name = "ERO_Revetment_SAM_O2"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_O3(unittype.StaticType):
    id = "ERO_Revetment_SAM_O3"
    name = "ERO Revetment O3"
    shape_name = "ERO_Revetment_SAM_O3"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_O4(unittype.StaticType):
    id = "ERO_Revetment_SAM_O4"
    name = "ERO Revetment O4"
    shape_name = "ERO_Revetment_SAM_O4"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_OC_elevated(unittype.StaticType):
    id = "ERO_Revetment_SAM_OC_elevated"
    name = "ERO Revetment O Elevated"
    shape_name = "ERO_Revetment_SAM_OC_elevated"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_OC2_elevated(unittype.StaticType):
    id = "ERO_Revetment_SAM_OC2_elevated"
    name = "ERO Revetment SA-2 Elevated"
    shape_name = "ERO_Revetment_SAM_OC2_elevated"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_U(unittype.StaticType):
    id = "ERO_Revetment_SAM_U"
    name = "ERO Revetment U2"
    shape_name = "ERO_Revetment_SAM_U"
    rate = 10


@fortificationmod
class ERO_Revetment_SAM_UC(unittype.StaticType):
    id = "ERO_Revetment_SAM_UC"
    name = "ERO Revetment U3"
    shape_name = "ERO_Revetment_SAM_UC"
    rate = 10


@fortificationmod
class ERO_Revetment_Tank_U(unittype.StaticType):
    id = "ERO_Revetment_Tank_U"
    name = "ERO Revetment Tank U2"
    shape_name = "ERO_Revetment_Tank_U"
    rate = 10


@fortificationmod
class ERO_Revetment_Tank_U1(unittype.StaticType):
    id = "ERO_Revetment_Tank_U1"
    name = "ERO Revetment Tank U1"
    shape_name = "ERO_Revetment_Tank_U1"
    rate = 10


ssap_statics_map = {
    "ERO_Hesco_Barrier_Tower2": ERO_Hesco_Barrier_Tower2,
    "ERO_Revetment_SAM11": ERO_Revetment_SAM11,
    "ERO_Revetment_D": ERO_Revetment_D,
    "ERO_Revetment_Platform1": ERO_Revetment_Platform1,
    "ERO_Revetment_Platform2": ERO_Revetment_Platform2,
    "ERO_Revetment_SAM_D_elevated": ERO_Revetment_SAM_D_elevated,
    "ERO_Revetment_SAM_O": ERO_Revetment_SAM_O,
    "ERO_Revetment_SAM_O2": ERO_Revetment_SAM_O2,
    "ERO_Revetment_SAM_O3": ERO_Revetment_SAM_O3,
    "ERO_Revetment_SAM_O4": ERO_Revetment_SAM_O4,
    "ERO_Revetment_SAM_OC_elevated": ERO_Revetment_SAM_OC_elevated,
    "ERO_Revetment_SAM_OC2_elevated": ERO_Revetment_SAM_OC2_elevated,
    "ERO_Revetment_SAM_U": ERO_Revetment_SAM_U,
    "ERO_Revetment_SAM_UC": ERO_Revetment_SAM_UC,
    "ERO_Revetment_Tank_U": ERO_Revetment_Tank_U,
    "ERO_Revetment_Tank_U1": ERO_Revetment_Tank_U1,
}
