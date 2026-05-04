from actions.actions import Action, ActionResult


class ExitAction(Action):
    def get_name(self) -> str:
        return "exit"

    def get_description(self) -> str:
        return "Exit this app"

    def execute(self) -> ActionResult:
        print("Exiting action")
        return ActionResult(stop=True)