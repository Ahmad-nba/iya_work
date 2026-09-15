from questions.q10 import solve
from open_channel import CircularSection, TrapezoidalSection, normal_depth


def test_question_10_results():
    result = solve()
    assert abs(result["normal_depth"] - 1.069) < 0.002
    assert abs(result["depth_over_weir"] - 0.441) < 0.002
    assert abs(result["downstream_depth_of_jump"] - result["normal_depth"]) < 1e-12
    assert 0.04 < result["upstream_depth_of_jump"] < 0.06
    assert result["jump_distance_downstream_of_weir"] > 0.0


def test_other_section_shapes_support_manning_normal_depth():
    trapezoid_depth = normal_depth(
        TrapezoidalSection(bottom_width=4.0, side_slope=1.0),
        discharge=8.0,
        roughness=0.03,
        slope=0.001,
    )
    circular_depth = normal_depth(
        CircularSection(diameter=3.0),
        discharge=4.0,
        roughness=0.02,
        slope=0.001,
    )
    assert 0.0 < trapezoid_depth < 3.0
    assert 0.0 < circular_depth < 3.0
