from questions.q15 import solve


def test_question_15_results():
    result = solve()
    assert abs(result["total_head"] - 1.282110) < 1e-5
    assert abs(result["upstream_depth"] - 1.240169) < 1e-5
    assert abs(result["upstream_velocity"] - 0.907135) < 1e-5
    assert abs(result["downstream_velocity"] - 4.5) < 1e-12
    assert abs(result["upstream_froude"] - 0.260074) < 1e-5
    assert abs(result["downstream_froude"] - 2.873479) < 1e-5
    assert abs(result["gate_force"] - 2556.354) < 0.01
