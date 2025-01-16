import pytest
import subprocess
import os
from typing import List

@pytest.mark.parametrize("arguments", [
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0", "-n", "10000", "--fast"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0", "--num_monte_carlo_samples", "10000", "--fast"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0", "--fast"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0", "-n", "1000"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0", "--num_monte_carlo_samples", "1000"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "2.0"]
])
def test_average_annual_hurricane_loss_terminates(arguments: List[str]) -> None:
    log_file_path = os.path.join(os.path.dirname(__file__), '../simulation.log')
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as log_file:
            initial_log_content = log_file.read()
    else:
        initial_log_content = ""

    subprocess.run(arguments, capture_output=True, text=True)

    with open(log_file_path, "r") as log_file:
        updated_log_content = log_file.read()

    assert updated_log_content != initial_log_content
    new_content = updated_log_content[len(initial_log_content):]
    assert "Average annual hurricane loss" in new_content

@pytest.mark.parametrize("arguments", [
    ["python", "gethurricaneloss.py", "2"],
    ["python", "gethurricaneloss.py", "2", "1"],
    ["python", "gethurricaneloss.py", "2", "1", "3"],
    ["python", "gethurricaneloss.py", "2", "1", "3", "5"],
    ["python", "gethurricaneloss.py", "2", "1", "3", "5", "7"],
    ["python", "gethurricaneloss.py", "a", "1.0", "3.0", "5.0", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "-1", "1.0", "3.0", "5.0", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "a", "3.0", "5.0", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "a", "5.0", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "-1", "5.0", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "a", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "-1", "7.0", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "a", "2.0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "a"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "-n", "a"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "-n"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "-n", "10.4"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "-n", "-1"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "-n", "0"],
    ["python", "gethurricaneloss.py", "2.0", "1.0", "3.0", "5.0", "7.0", "-1", "--FAKEINPUT"]
])
def test_bad_inputs_fail(arguments: List[str]) -> None:
    result = subprocess.run(arguments, capture_output=True, text=True)
    assert result.returncode != 0

@pytest.mark.parametrize("arguments", [
    ["python", "gethurricaneloss.py", "2", "1", "3", "5", "7", "2"],
    ["python", "gethurricaneloss.py", "2", "-1", "3", "5", "-7", "2"],
    ["python", "gethurricaneloss.py", "2", "1", "3", "5", "7", "2", "--num_monte_carlo_samples", "17"],
    ["python", "gethurricaneloss.py", "2.7", "1.31", "3.69", "5.5", "7", "12.3", "--num_monte_carlo_samples", "17", "--fast"],
    ["python", "gethurricaneloss.py", "-n", "289", "--fast", "2", "1", "3", "5", "7", "2"],
    ["python", "gethurricaneloss.py", "--num_monte_carlo_samples", "27", "1.27", "3.72", "5.3", "0.0", "0", "7.1"],
    ["python", "gethurricaneloss.py", "0", "0", "0", "0", "0", "0"]
])
def test_good_inputs_succeed(arguments: List[str]) -> None:
    result = subprocess.run(arguments, capture_output=True, text=True)
    assert result.returncode == 0
