# M1-01 — Python + uv

Goal: create a venv and install dependencies without help, and understand what each command actually does.

## Files in this repo

- `pyproject.toml` — project metadata + two dependency groups: default (`requests`) and `dev` (`pytest`, `ruff`)
- `main.py` — tiny script that uses the installed dependency, so "it works" is provable, not assumed
- `test_main.py` — tiny test that uses the `dev` group, to prove that group installs separately

## Steps to do yourself (no need to copy commands blindly — understand each one)

1. **Install uv** (if not already installed)
   Check the official install instructions for your OS. Confirm with `uv --version`.

2. **Create a virtual environment**
   `uv venv`
   This creates a `.venv/` folder — an isolated Python interpreter + package directory, so this project's dependencies don't leak into or clash with other projects on your machine.

3. **Activate the virtual environment**
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
   Activating just changes your shell's `PATH` so `python`/`pip` point inside `.venv/` instead of the system Python.

4. **Install dependencies, including the dev group**
   `uv sync --group dev`
   `uv sync` reads `pyproject.toml` (and the lockfile `uv.lock`, generated automatically) and installs exact pinned versions. `--group dev` additionally installs the `dev` extras (pytest, ruff) — these aren't needed to *run* the app, only to *develop* it.

5. **Run the demo without activating (uv's shortcut)**
   `uv run main.py`
   `uv run` finds/creates the venv, syncs it if needed, then runs the command inside it — you don't have to activate manually.

6. **Run the tests**
   `uv run pytest`

7. **Lint (uses the dev group)**
   `uv run ruff check .`

8. **Inspect the lockfile**
   Open `uv.lock` after step 4 and note it pins exact versions + hashes — this is what makes installs reproducible across machines.