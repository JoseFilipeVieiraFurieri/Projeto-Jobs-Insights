from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    job_data = read(path)

    return max(
        [
            int(job["max_salary"])
            for job in job_data
            if job["max_salary"].isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    job_data = read(path)

    return min(
        [
            int(job["min_salary"])
            for job in job_data
            if job["min_salary"].isdigit()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    min_salary = job.get("min_salary", None)
    max_salary = job.get("max_salary", None)

    if min_salary is None or max_salary is None:
        raise ValueError
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError
    if int(job["min_salary"]) >= int(job["max_salary"]):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) and int(
        job["max_salary"]
    ) >= int(salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    list_valid_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                list_valid_salary.append(job)
        except ValueError:
            continue
    return list_valid_salary
