# Quantum CI/CD demo

An example Qiskit project that runs Quantum CI/CD in GitHub Actions on every pull request.

- `circuits.py`: entry points of the checked circuits.
- `quantum-ci.toml`: circuits and rules, that is structural rules, a gate budget and a depth regression rule.
- `quantum-ci-baseline.json`: the accepted metrics used by the regression rule.
- `.github/workflows/quantum-ci.yml`: the workflow.

This repository contains no code of the tool. The workflow checks out the private repository of the tool at a pinned
commit with a read-only token from the secret `QUANTUM_CI_TOOL_TOKEN`, installs it with pip together with the exact
Qiskit version recorded in the baseline (`qiskit==2.5.2`) and runs `quantum-ci analyze --format json`. A FAIL result
or an analysis error ends the job with a non-zero exit code. When the job is a required status check, the pull request
cannot be merged until it passes. The JSON report is printed in the log of the analysis step and kept as the artifact
`quantum-ci-report` for 14 days. Pull requests from forks do not receive the secret, so their analysis cannot run.

A baseline is compatible only with the Qiskit version that created it. To move to another Qiskit version, change the
pinned version in the workflow and recreate the baseline with that version in the same pull request.

To accept a change of the metrics, run `quantum-ci create-baseline --overwrite`, review the change of the baseline
together with the change of the circuits in the pull request, and commit it deliberately.
