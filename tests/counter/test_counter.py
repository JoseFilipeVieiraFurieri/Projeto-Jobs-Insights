from src.pre_built.counter import count_ocurrences


def test_counter():
    world_count = count_ocurrences("data/jobs.csv", "nurse")

    assert world_count == 276
