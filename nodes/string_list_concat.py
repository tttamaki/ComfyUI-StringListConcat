from typing_extensions import override
from comfy_api.latest import ComfyExtension, io


class StringListConcat(io.ComfyNode):
    """Concatenates multiple string inputs into one string."""

    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.Autogrow.TemplatePrefix(
            input=io.String.Input("string", multiline=True),
            prefix="string",
            min=2,
            max=32,
        )
        return io.Schema(
            node_id="StringListConcat",
            display_name="String List Concat",
            category="tttamaki/string-list",
            description="Concatenates multiple string inputs into one string",
            inputs=[
                io.Autogrow.Input("inputs", template=template),
                io.String.Input("delimiter", multiline=False, default=""),
            ],
            outputs=[
                io.String.Output(),
            ],
        )

    @classmethod
    def execute(
        cls, inputs: io.Autogrow.Type, delimiter: str
    ) -> io.NodeOutput:
        values = list(inputs.values())
        result = delimiter.join(values)
        return io.NodeOutput(result)


class StringListConcatExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [StringListConcat]


async def comfy_entrypoint() -> StringListConcatExtension:
    return StringListConcatExtension()
