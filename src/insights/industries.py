from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_jobs = read(path)
    result = [jobs for jobs in list_jobs]
    industry_types = set()
    for job in result:
        if job["industry"] != "":
            industry_types.add(job["industry"])
    return industry_types


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    return [job for job in jobs if job["industry"] == industry]
