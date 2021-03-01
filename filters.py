from vkwave.bots.core.dispatching.filters.base import BaseFilter, FilterResult, BaseEvent
from all_json import SETTINGS


class NotGroupMemberFilter(BaseFilter):
    async def check(self, event: BaseEvent) -> FilterResult:
        user_id = event.object.object.message.from_id
        response = await event.api_ctx.groups.is_member(
            group_id=str(SETTINGS["group_id"]), user_id=user_id, return_raw_response=True
        )
        result = not bool(response["response"])
        return FilterResult(result)
