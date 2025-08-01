from pydantic import Field

from pipelex.core.stuff_content import StructuredContent


class CategoryInput(StructuredContent):
    category: str = Field(..., description="The category of the input")
