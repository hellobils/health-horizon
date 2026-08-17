"""
user_profile.py

Defines user background and health information to be used by models

"""

from dataclasses import dataclass
from enum import Enum


class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class Ethnicity(str, Enum):
    WHITE = "White or not stated"
    INDIAN = "Indian"
    PAKISTANI = "Pakistani"
    BANGLADESHI = "Bangladeshi"
    CHINESE = "Chinese"
    OTHER_ASIAN = "Other Asian"
    BLACK_CARIBBEAN = "Black Caribbean"
    BLACK_AFRICAN = "Black African"
    OTHER = "Other"

class Smoking(str, Enum):
    NON_SMOKER = "Non Smoker"
    EX_SMOKER = "Ex Smoker"
    LIGHT_SMOKER = "Light Smoker"
    MODERATE_SMOKER = "Moderate Smoker"
    HEAVY_SMOKER = "Heavy Smoker"

class Diabetes(str, Enum):
    NOT_DIABETIC = "None"
    TYPE_1 = "Type 1"
    TYPE_2 = "Type 2"

class EducationLevel(str, Enum):
    MORE_THAN_10_YEARS = "More than 10 years"
    SEVEN_TO_NINE_YEARS = "7-9 years"
    LESS_THAN_7_YEARS = "Less than 7 years"

@dataclass
class UserProfile:
    age: int
    sex: Sex
    ethnicity: Ethnicity
    cholesterol_hdl_ratio: float
    fasting_blood_glucose: float
    hba1c: float
    height_cm: float
    weight_kg: float
    education_level: EducationLevel
    systolic_bp: int
    smoking_status: Smoking = Smoking.NON_SMOKER
    diabetes_status: Diabetes = Diabetes.NOT_DIABETIC
    history_of_cvd: bool = False
    learning_disability: bool = False
    family_history_diabetes: bool = False
    steroid_meds: bool = False
    erectile_dysfunction: bool = False
    family_history_cvd: bool = False
    kidney_disease: bool = False
    atrial_fibrillation: bool = False
    bp_treatment: bool = False
    migraines: bool = False
    rheumatoid_arthritis: bool = False
    lupus: bool = False
    statin_meds: bool = False
    severe_mental_illness: bool = False
    bipolar_schizo_status: bool = False
    antipsychotic_meds: bool = False
    pcos: bool = False
    gestational_diabetes: bool = False

    @property
    def bmi(self) -> float:
        height_m = self.height_cm / 100
        return round(self.weight_kg / (height_m ** 2), 1)


