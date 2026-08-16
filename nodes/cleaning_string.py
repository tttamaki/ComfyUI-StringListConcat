import re

from typing_extensions import override
from comfy_api.latest import ComfyExtension, io


class CleaningString(io.ComfyNode):
    """Cleans a string by normalizing line breaks, commas, and spaces."""

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="CleaningString",
            display_name="Cleaning String",
            category="tttamaki/string-list",
            description="Cleans line breaks, empty comma-separated values, and repeated spaces",
            inputs=[
                        io.String.Input("string", multiline=True),
            ],
            outputs=[
                io.String.Output(),
            ],
        )

    @classmethod
    def execute(cls, string: str) -> io.NodeOutput:
        result = re.sub(r"[\r\n]+", " ", string)
        result = re.sub(r" +,", ",", result)
        result = re.sub(r",(?:[ \t]*,)+", ",", result)
        result = re.sub(r" {2,}", " ", result)
        return io.NodeOutput(result)


class CleaningStringExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [CleaningString]


async def comfy_entrypoint() -> CleaningStringExtension:
    return CleaningStringExtension()
