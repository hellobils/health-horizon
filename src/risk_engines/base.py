"""
base.py

Defines the shared "contract" that every risk engine (QRISK3, QDiabetes,
CAIDE, etc.) must follow. This means the app can call any engine the
same way, without needing to know how each one works internally.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class RiskCategory(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    VERY_HIGH = "Very High"


@dataclass
class RiskResult:
    """What every engine hands back after scoring a person."""
    condition: str          # e.g. "Cardiovascular Disease"
    score: float             # raw % risk (e.g. 7.3 means 7.3%)
    category: RiskCategory   # bucketed Low/Moderate/High/Very High
    detail: str = ""         # optional note, e.g. which algorithm/version


class RiskEngine(ABC):
    """
    Every risk engine (qrisk3.py, qdiabetes.py, caide.py) must inherit
    from this and implement `assess`. That's the only rule.
    """

    @abstractmethod
    def assess(self, profile) -> RiskResult:
        """
        Takes a UserProfile, returns a RiskResult.
        `profile` type isn't hinted here to avoid a circular import
        with user_profile.py — that's fine, Python won't complain.
        """
        raise NotImplementedError