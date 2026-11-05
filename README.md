# AI / Machine Learning Lab Programs

Beginner-friendly Python programs arranged lab-wise from the supplied experiment list.

## Setup
Use Python 3.10 or newer. From this folder, create a virtual environment if you want:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Run a program from the project root, for example:

```bash
python lab1/01_environment_check.py
python lab2/01_bfs_dfs.py
```

Some programs use small sample data created inside the script, so no dataset download is needed.
The Grad-CAM and FGSM examples train a small CNN on generated synthetic images; they are demonstrations
of the ideas, not production-grade image classifiers.

## Lab index

- Lab 1: environment check, production system, water jug
- Lab 2: BFS/DFS, hill climbing, best-first search, A*
- Lab 3: preprocessing, EDA, NumPy/Pandas, visualization
- Lab 4: knowledge representation, rule-based system, semantic network
- Lab 5: decision tree classifier and model evaluation
- Lab 6: PyTorch basics, linear regression, neural network fundamentals
- Lab 7: Grad-CAM, FGSM, PCA/SVD, mini project

For a GitHub submission, include the source files and this README. Do not commit `.venv/`, cache files,
or private credentials.
