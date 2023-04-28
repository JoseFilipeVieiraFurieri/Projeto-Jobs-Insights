from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as jobs:
        jobs_list = csv.DictReader(jobs)
        result = [job for job in jobs_list]

    return result


def get_unique_job_types(path: str) -> List[str]:
    job_data = read(path)
    result = [jobs for jobs in job_data]
    job_types = set()
    for job in result:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    list_jobs = [job for job in jobs if job["job_type"] == job_type]

    return list_jobs
