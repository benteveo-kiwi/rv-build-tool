from rv import commands, rvtypes
from rv.commands import NeutralMenuState


class Package_SamplePlugin(rvtypes.MinorMode):

    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        globalBindings = None #[("Event-Name", self.eventCallback, "DescriptionOfBinding")]
        localBindings = None

        menu = [
            ("Example", [
                    ("Run Example", self.runExample, None, lambda: NeutralMenuState),
            ])
        ]

        self.init("Package_SamplePlugin", globalBindings, localBindings, menu)

    def runExample(self, event):
        print("DEBUG: Example Ran.")


def createMode():
    return Package_SamplePlugin()
