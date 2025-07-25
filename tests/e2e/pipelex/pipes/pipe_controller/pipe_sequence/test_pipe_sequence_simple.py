"""Test simple pipe sequence functionality without batching."""

import pytest

from pipelex import pretty_print
from pipelex.core.pipe_run_params import PipeRunMode
from pipelex.core.pipe_run_params_factory import PipeRunParamsFactory
from pipelex.core.stuff_content import TextContent
from pipelex.core.stuff_factory import StuffFactory
from pipelex.core.working_memory_factory import WorkingMemoryFactory
from pipelex.hub import get_required_pipe
from pipelex.pipeline.job_metadata import JobMetadata


@pytest.mark.dry_runnable
@pytest.mark.inference
@pytest.mark.asyncio
async def test_simple_text_sequence(pipe_run_mode: PipeRunMode):
    """Test simple text processing sequence without batching."""
    # Create test input
    raw_text_stuff = StuffFactory.make_stuff(
        name="raw_text",
        concept_str="simple_text_processing.RawText",
        content=TextContent(text="This is  some  messy    text with bad spacing."),
    )

    if pipe_run_mode == PipeRunMode.DRY:
        # Create working memory with the required input for dry run
        working_memory = WorkingMemoryFactory.make_from_multiple_stuffs([raw_text_stuff])

        pipe = get_required_pipe(pipe_code="simple_text_sequence")
        pipe_output = await pipe.run_pipe(
            job_metadata=JobMetadata(job_name="test_simple_text_sequence"),
            working_memory=working_memory,
            pipe_run_params=PipeRunParamsFactory.make_run_params(pipe_run_mode=pipe_run_mode),
        )

        pretty_print(pipe_output)
        assert pipe_output is not None
        assert pipe_output.working_memory is not None
        assert pipe_output.main_stuff is not None
        assert pipe_output.main_stuff.concept_code == "simple_text_processing.SummaryText"
