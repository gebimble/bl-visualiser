from sqlalchemy.orm import Session

from bl_visualiser import models, schemas


def get_climber_by_name(db: Session, climber_name: str):
    return db.query(models.Climber).filter(models.Climber.name == climber_name).first()  # noqa: ignore


def get_climber(db: Session, climber_id: int):
    return db.query(models.Climber).filter(models.Climber.id == climber_id).first()  # noqa: ignore


def create_climber(db: Session, climber: schemas.ClimberCreate):
    db_climber = models.Climber(
        name=climber.name,
        sex=climber.sex,
        date_of_birth=climber.date_of_birth,
    )
    db.add(db_climber)
    db.commit()
    db.refresh(db_climber)
    return db_climber
