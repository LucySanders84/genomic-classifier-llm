from dataclasses import dataclass

from classes.Sequence import Sequence


@dataclass
class PipelineInputParameters:
    label: str
    sequence_source: list[Sequence]
    feature_source_filename: str
    target_type: str
    contig_length: int
    stride: int