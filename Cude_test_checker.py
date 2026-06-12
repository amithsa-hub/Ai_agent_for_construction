def cube_test_result(grade, strength):

    grades = {
        "M20":20,
        "M25":25,
        "M30":30,
        "M35":35,
        "M40":40
    }

    target = grades[grade]

    if strength >= target:
        return "PASS ✅ Concrete satisfies grade requirement."
    else:
        return "FAIL ❌ Concrete does not satisfy grade requirement."
