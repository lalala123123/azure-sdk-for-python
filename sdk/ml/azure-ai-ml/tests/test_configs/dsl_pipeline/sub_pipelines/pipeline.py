"""
Sub pipelines
"""
from pathlib import Path

from azure.ai.ml import dsl, load_component
from azure.ai.ml.entities import PipelineJob

parent_dir = str(Path(__file__).parent)
component_func = load_component(source=parent_dir + "/component.yml")

@dsl.pipeline(
    compute="cpu-cluster",
)
def sub_pipeline():
    component_job = component_func()
    component_job.illegal_settings = "illegal_value"
    print(component_job)


@dsl.pipeline(
    compute="cpu-cluster",
)
def parent_pipeline():
    sub_pipeline()

def generate_dsl_pipeline() -> PipelineJob:
    return parent_pipeline()