# Data Science Project Structure

This project follows a standard, professional folder structure to ensure clarity, reproducibility, and ease of collaboration.

## Folder Overview

- `data/` — Store all raw and processed datasets here. **Do not modify raw data.**
- `notebooks/` — Jupyter notebooks for exploration, analysis, and reporting.
- `scripts/` — Standalone Python scripts for data processing, modeling, or automation.
- `outputs/` — Generated results, figures, and model outputs. Never overwrite raw data.

## Best Practices
- Keep code, data, and outputs separate.
- Use clear, consistent folder names.
- Avoid deeply nested folders.
- Make paths predictable for easy collaboration.

This structure helps your project scale, remain organized, and be easy for others to understand and review.

## Milestone: Data Organization

To satisfy the assignment requirements, the following steps have been completed:

1. **Separated data stages** into `data/raw/` (original datasets) and
   `data/processed/` (cleaned or derived tables). Each folder contains a
   `.gitkeep` placeholder to track empty directories.
2. **Added a sample raw file** (`example_raw.csv`) to demonstrate immutability.
3. **Created a demonstration script** (`scripts/organize_data_demo.py`) that
   reads from raw, writes processed output, and saves an artifact in `outputs/`.
4. **Updated this README** to explain the reasoning and point users at the
   example script and folder layout.

### Key principles illustrated

- Raw data is never modified; scripts only read from `data/raw`.
- Processed datasets are written to `data/processed` with clear names.
- Output artifacts (reports, plots, models) belong in `outputs/`.
- Workflows should be one-directional: raw → processed → outputs.

By following this organization, you avoid accidental overwrites, maintain
reproducibility, and make it easier for others (or future you) to follow
your work.