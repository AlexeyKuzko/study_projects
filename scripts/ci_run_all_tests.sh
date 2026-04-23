#!/usr/bin/env bash
set -euo pipefail

# Root of the repository (where this script lives is assumed to be in repo root under scripts/)
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
echo "Root: ${ROOT_DIR}"

SUMMARY=()
EXIT_CODE=0

echo "Starting multi-subproject test run..."

for subdir in "$ROOT_DIR"/*/; do
  # Only consider directories
  [ -d "$subdir" ] || continue
  basename_sub=$(basename "$subdir")

  # Heuristics: skip hidden dirs and non-project folders
  if [[ "$basename_sub" == ".*" ]]; then
    continue
  fi

  if [[ -f "$subdir/requirements.txt" || -f "$subdir/pyproject.toml" || -f "$subdir/setup.py" ]]; then
    echo "\n=== Subproject: ${basename_sub} ==="

    VENV_DIR="$ROOT_DIR/.venvs/${basename_sub}"
    mkdir -p "$VENV_DIR"
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"

    # Prefer requirements.txt if present
    if [[ -f "$subdir/requirements.txt" ]]; then
      pip install --upgrade pip setuptools wheel >/dev/null 2>&1 || true
      echo "Installing dependencies from $subdir/requirements.txt"
      if ! pip install -r "$subdir/requirements.txt"; then
        echo "[ERR] Failed to install dependencies for ${basename_sub}"
        EXIT_CODE=1
      fi
    elif [[ -f "$subdir/pyproject.toml" ]]; then
      echo "Detected pyproject.toml; attempting pip install ."
      if ! pip install --upgrade pip setuptools wheel >/dev/null 2>&1; then
        echo "[WARN] Could not upgrade packaging tools"
      fi
      if ! (cd "$subdir" && pip install -e .); then
        echo "[ERR] Failed to install ${basename_sub} in editable mode"
        EXIT_CODE=1
      fi
    elif [[ -f "$subdir/setup.py" ]]; then
      echo "Installing via setup.py for ${basename_sub}"
      if ! (cd "$subdir" && pip install -e .); then
        echo "[ERR] Failed to install ${basename_sub} via setup.py"
        EXIT_CODE=1
      fi
    fi

    TESTS_DIR="$subdir/tests"
    if [[ -d "$TESTS_DIR" ]]; then
      echo "Running tests in ${basename_sub}..."
      if ! pytest -q "$TESTS_DIR"; then
        echo "[ERR] Tests failed for ${basename_sub}"
        EXIT_CODE=1
      fi
    else
      echo "No tests directory found in ${basename_sub}; skipping tests."
    fi

    deactivate
  else
    echo "Skipping ${basename_sub}: no known project file."
  fi
done

echo "\nTest run complete."
if [[ $EXIT_CODE -eq 0 ]]; then
  echo "ALL SUBPROJECT TESTS PASSED"
else
  echo "SOME SUBPROJECT TESTS FAILED"
fi
exit $EXIT_CODE
