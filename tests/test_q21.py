from questions.q21 import solve


def test_question_21_results():
    result = solve()
    assert abs(result["discharge"] - 5.257243) < 1e-5
    assert abs(result["normal_depth"] - 1.064141) < 1e-5
    assert abs(result["force_on_blocks"] - 6713.142) < 0.01
