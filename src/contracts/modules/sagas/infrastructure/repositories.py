from uuid import uuid4
from datetime import datetime

from contracts.config.db import db
from contracts.seedwork.application.sagas import Step, End, Start, Transaction
from contracts.modules.sagas.infrastructure.dto import Saga


class SagaRepository():

    def create(self, step: Step):
        saga = Saga()
        saga.id = str(uuid4())
        saga.created_at = datetime.now()
        saga.index = step.index

        if isinstance(step, End): saga.is_last = True
        if isinstance(step, Start): saga.is_first = True
        if isinstance(step, Transaction):
            saga.event = step.event.__name__
            saga.command = step.command.__name__

        db.session.add(saga)
        db.session.commit()

