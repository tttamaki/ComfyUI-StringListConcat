from typing_extensions import override
from comfy_api.latest import ComfyExtension, io

from .nodes.cleaning_string import CleaningString
from .nodes.string_list_concat import StringListConcat


class StringListConcatExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [StringListConcat, CleaningString]


async def comfy_entrypoint() -> StringListConcatExtension:
    return StringListConcatExtension()

__all__ = [
    "StringListConcat",
    "CleaningString",
    "comfy_entrypoint"
]
