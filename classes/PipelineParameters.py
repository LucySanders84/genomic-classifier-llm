from dataclasses import dataclass

from classes.Sequence import Sequence


@dataclass
class PipelineParameters:
    label: str
    sequence_source: list[Sequence]
    feature_source_filename: str
    target_type: str
    fragment_length: int
    stride: int