"""
Prompt Evaluation System

A simple Python script that:
1. Compares two AI-generated outputs
2. Scores them using a lightweight rubric
3. Selects the better response
"""

from typing import Dict


KEYWORDS = {"system", "process", "result", "data", "output", "input"}


def score_response(response: str) -> Dict[str, int]:
    """
    Score a response using simple heuristics:
    - clarity
    - completeness
    - relevance
    """
    score = {
        "clarity": 0,
        "completeness": 0,
        "relevance": 0,
    }

    words = response.split()
    word_count = len(words)
    lowered = response.lower()

    if 8 <= word_count <= 40:
        score["clarity"] += 1

    if word_count > 15:
        score["completeness"] += 1

    if any(keyword in lowered for keyword in KEYWORDS):
        score["relevance"] += 1

    return score


def total_score(score_dict: Dict[str, int]) -> int:
    """Return total score from rubric dictionary."""
    return sum(score_dict.values())


def evaluate_outputs(output_a: str, output_b: str) -> Dict[str, object]:
    """Compare two outputs and determine the better one."""
    score_a = score_response(output_a)
    score_b = score_response(output_b)

    total_a = total_score(score_a)
    total_b = total_score(score_b)

    if total_a > total_b:
        winner = "A"
    elif total_b > total_a:
        winner = "B"
    else:
        winner = "Tie"

    return {
        "output_a_score": score_a,
        "output_b_score": score_b,
        "total_a": total_a,
        "total_b": total_b,
        "winner": winner,
    }


if __name__ == "__main__":
    response_a = "This system processes input data and produces a result."
    response_b = (
        "This process evaluates structured input data, applies logic, "
        "and returns a more complete result for the user."
    )

    result = evaluate_outputs(response_a, response_b)
    print("Evaluation Result:")
    print(result)
