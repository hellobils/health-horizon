"""
user_profile.py

Defines user background and health profile to be used by models

"""


from dataclasses import dataclass
from enum import Enum


class Sex(str, Enum):
    Male = "Male"
    Female = "Female"


@dataclass
class UserProfile:
    age: int
    sex: Sex
    ethnicity: str
    postcode: str
    systolic_bp: int
    smoking_status: str
    diabetes_status: str
    heart_attack: bool
    chronic_kidney_disease: bool
    atrial_fib: bool
    bp_treament: bool
    migraines: bool
    rheum_arthritis: bool
    lupus: bool
    sever_mh: bool
    atyp_antipsychotic_med: bool
    steroid_meds: bool
    erectile_dys: bool
    cholesterol_hdl_ratio: int
    height: int
    weight: int




