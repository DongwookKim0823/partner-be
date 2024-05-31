from abc import ABC, abstractmethod
from typing import Optional

from django.db.models.query import QuerySet

from mung_manager.errors.exceptions import NotImplementedException
from mung_manager.reservations.models import (
    DailyReservation,
    DayOff,
    KoreaSpecialDay,
    Reservation,
)


class AbstractReservationSelector(ABC):
    @abstractmethod
    def get_reservation_list(self, pet_kindergarden_id: int, reserved_at: str) -> dict[str, list[Reservation]]:
        raise NotImplementedException()

    @abstractmethod
    def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        raise NotImplementedException()

    @abstractmethod
    def check_is_exists_reservation_by_customer_pet_id_and_reserved_at(
        self, customer_pet_id: int, reserved_at: str
    ) -> bool:
        raise NotImplementedException()


class AbstractDailyReservationSelector(ABC):
    @abstractmethod
    def get_daily_reservations_queryset_by_year_and_month_and_pet_kindergarden_id(
        self, year: int, month: int, pet_kindergarden_id: int
    ) -> QuerySet[DailyReservation]:
        raise NotImplementedException()


class AbstractDayOffSelector(ABC):
    @abstractmethod
    def get_day_off_queryset_by_pet_kindergarden_id_and_day_off_at(
        self, pet_kindergarden_id: int, year: int, month: int
    ) -> QuerySet[DayOff]:
        raise NotImplementedException()

    @abstractmethod
    def get_day_off_by_id(self, day_off_id: int) -> Optional[DayOff]:
        raise NotImplementedException()

    @abstractmethod
    def check_is_exists_day_off_by_day_off_at_and_pet_kindergarden_id(
        self, day_off_at: str, pet_kindergarden_id: int
    ) -> bool:
        raise NotImplementedException()


class AbstractKoreaSpecialDaySelector(ABC):
    @abstractmethod
    def get_korea_special_day_queryset_by_year_and_month(self, year: int, month: int) -> QuerySet[KoreaSpecialDay]:
        raise NotImplementedException()
