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
    try:
        min_salary = job.get("min_salary", None)
        max_salary = job.get("max_salary", None)

        if min_salary is None or max_salary is None:
            raise ValueError("Dados não podem ser nulos")
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError("Salario minimo não pode ser maior que o maximo")
        if (
            salary is None
            or isinstance(salary, (list, dict))
            or callable(salary)
        ):
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    list_valid_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_valid_salary.append(job)
        except (ValueError, TypeError):
            continue

    return list_valid_salary


##

# print(filter_by_salary_range(jobs, 4000))
