from dataclasses import dataclass

from classes.SequenceSourceData import SequenceSourceData


@dataclass
class DataSourceParameters:
    labels: dict[str, str]
    feature_source_filename: dict[str, str]
    target_feature_type: dict[str, str]
    sequence_source: SequenceSourceData