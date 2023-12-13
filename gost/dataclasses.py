from dataclasses import dataclass


@dataclass
class Gost33259Request:
    type_fl: str
    surface: str
    dn_passage: str
    pn: str
    row: str


@dataclass
class Gost28759Request:
    execution: str
    dn_passage: str
    pn: str


@dataclass
class Atk261813Request:
    execution: str
    pn: str
    dn_passage: str


@dataclass
class Gost6533Request:
    drawing: str
    diameter: str
    thickness: str


@dataclass
class Atk24200FlangeStoppersRequest:
    execution: str
    pn: str
    dn_passage: str


@dataclass
class Atk26185FlangeStoppersRequest:
    execution: str
    pn: str
    dn_passage: str
