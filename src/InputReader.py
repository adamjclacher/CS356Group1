import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import pickle

with open('resources/InputConfigJSONTemplate.json', 'r') as file:
    data = json.load(file)


class EncoderType:
    name: str
    id: int
    code: str
    active: bool
    active_codecs: List[int]


@dataclass
class Codec:
    name: str
    id: int
    code: str
    max_layers: int
    active_encoder_modes: List[int]
    active_scalability: Optional[List[int]]


@dataclass
class EncoderMode:
    name: str
    id: int
    code: str


@dataclass
class RawFile:
    id: int
    name: str
    code: str
    times: List[str]
    spatials: List[str]
    temporals: List[str]
    depths: List[str]
    metadata: Dict[str, Any]


@dataclass
class PreEncodedFile:
    id: int
    code: str
    duration: str


@dataclass
class Time:
    id: int
    name: str
    code: str
    duration: str


@dataclass
class ScalabilityType:
    id: int
    name: str
    order: int
    code: str
    value: str


@dataclass
class Scalability:
    name: str
    id: int
    code: str
    types: List[ScalabilityType]


@dataclass
class TopologyType:
    name: str
    id: int
    code: str
    image_url: str
    active: bool


@dataclass
class Topology:
    name: str
    types: List[TopologyType]


@dataclass
class Impairment:
    name: str
    id: int
    code: str
    active: bool
    active_impairment_values: List[int]


@dataclass
class ImpairmentValue:
    name: str
    id: int
    code: int
    active: bool
    value: int


@dataclass
class Config:
    Metadata: Dict[str, str]
    Encoder: List[Dict[str, Any]]
    Network: List[Dict[str, Any]]
    Metrics: List[Dict[str, Any]]
    Output: Dict[str, Any]


# Parse the JSON into the Config dataclass
config = Config(**data)
#THIS IS TO SAVE THE PICKLE
with open("resources/config.pkl", 'wb') as file:
    pickle.dump(config, file)
#THIS IS TO READ THE PICKLE
with open("resources/config.pkl", "rb") as file:
    loaded_config = pickle.load(file)

print(loaded_config.Metadata)
print(loaded_config.Encoder)
print(loaded_config.Network)
print(loaded_config.Metrics)
print(loaded_config.Output)
