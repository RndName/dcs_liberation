import random

from dcs.vehicles import AirDefence, Unarmed

from gen.sam.airdefensegroupgenerator import (
    AirDefenseRange,
    AirDefenseGroupGenerator,
)


class ZSU23Generator(AirDefenseGroupGenerator):
    """
    This generate a ZSU 23 group
    """

    name = "ZSU-23 Group"
    price = 50

    def generate(self):
        num_launchers = 4

        positions = self.get_circular_position(
            num_launchers, launcher_distance=120, coverage=180
        )
        for i, position in enumerate(positions):
            self.add_unit(
                AirDefence.ZSU_23_4_Shilka,
                "SPAA#" + str(i),
                position[0],
                position[1],
                position[2],
            )
        self.add_unit(
            Unarmed.M_818,
            "TRUCK",
            self.position.x + 80,
            self.position.y,
            self.heading,
        )

    @classmethod
    def range(cls) -> AirDefenseRange:
        return AirDefenseRange.AAA
