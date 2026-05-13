import logging
from uuid import UUID

from actions import ActionResult
from actions.entity_service_action import EntityServiceAction

log = logging.getLogger(__name__)


class DeleteEntityAction(EntityServiceAction):
    def get_name(self) -> str:
        return f"Delete {self.entity_name}"

    def get_description(self) -> str:
        return f"Delete {self.entity_name} by id."

    def execute(self) -> ActionResult:
        print(f"Delete {self.entity_name} by id")
        entity_id = input(f"Enter {self.entity_name} id: ")

        try:
            entity_id = UUID(entity_id)
        except ValueError:
            log.error(
                f"Invalid UUID %s, didn't delete anything",
                entity_id
            )
            print(f"Invalid UUID {entity_id}, didn't delete anything")
            return ActionResult(error=True)

        entity = self.service.get_by_id(entity_id)
        if not entity:
            log.error(f"Entity %s not found", entity_id)
            print(f"\nEntity {entity_id} not found")
            return ActionResult(error=True)
        confirm = input(f"Are you sure you want to delete this entity {entity}? (Y/N): ")
        if confirm.casefold() != "y":
            log.warning("Deletion aborted")
            print("\nCancelled\n")
            return ActionResult()

        self.service.delete(entity.id)
        print(f"\nDeleted {entity_id}\n")
        return ActionResult()
