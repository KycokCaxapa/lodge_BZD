from fastapi import APIRouter
from typing import List

from app.schedule.schemas import SSubject
from app.schedule.dao import SubjectDAO


router = APIRouter(tags=['Schedule'])


@router.post('/create_subject')
async def create_subject(subject: SSubject) -> None:
    await SubjectDAO.create(subject=subject.subject,
                         group=subject.group,
                         day=subject.day,
                         place=subject.place,
                         week=subject.week,
                         teacher=subject.teacher)
    return subject


@router.get('/schedule')
async def get_schedule(group: int) -> List[SSubject]:
    schedule = await SubjectDAO.get_by_filter(group=group)
    return schedule


@router.put('/update')
async def update_subject(id: int, subject: SSubject) -> None:
    await SubjectDAO.update(id,
                            subject=subject.subject,
                            group=subject.group,
                            day=subject.day,
                            place=subject.place,
                            week=subject.week,
                            teacher=subject.teacher)


@router.delete('/delete_subject')
async def delete_subject(id: int) -> None:
    await SubjectDAO.delete_by_filter(id=id)
