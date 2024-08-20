import time
from datetime import timedelta
from typing import Any

from airflow.configuration import conf
from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.temporal import TimeDeltaTrigger
from airflow.utils.context import Context


class DeferrableHelloOperator(BaseSensorOperator):
    def __init__(
        self, deferrable: bool = conf.getboolean("operators", "default_deferrable", fallback=False), **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.deferrable = deferrable

    def execute(self, context: Context) -> None:
        print("Work about to start")
        self.defer(
            trigger=TimeDeltaTrigger(timedelta(minutes=5)),
            method_name="execute_complete",
        )

    def execute_complete(
        self,
        context: Context,
        event: dict[str, Any] | None = None,
    ) -> None:
        print("Work complete")
        return