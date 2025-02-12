# EV Charging Optimization Project

## Project Structure

```
EV_Charging_Optimization/
│── data/                     # Stores raw and processed datasets
│   ├── raw/                  # Unprocessed datasets
│   ├── processed/            # Cleaned and preprocessed data
│   ├── maps/                 # GIS data and maps
│
│── notebooks/                # Jupyter notebooks for data analysis & visualization
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_monte_carlo_simulation.ipynb
│   ├── 04_vector_space_optimization.ipynb
│   ├── 05_q_learning_model.ipynb
│   ├── 06_evaluation_metrics.ipynb
│
│── src/                      # Source code for the project
│   ├── data_processing.py    # Data cleaning & preprocessing
│   ├── monte_carlo.py        # Monte Carlo simulation implementation
│   ├── vector_space.py       # Gradient-based spatial optimization
│   ├── rl_model.py           # Reinforcement learning (Q-learning) model
│   ├── evaluation.py         # Evaluation metrics calculation
│   ├── utils.py              # Helper functions
│
│── models/                   # Trained models and saved checkpoints
│   ├── q_learning_model.pkl
│   ├── monte_carlo_candidates.npy
│
│── config/                   # Configuration files
│   ├── settings.yaml         # Hyperparameters and settings
│
│── results/                  # Outputs, plots, and visualizations
│   ├── candidate_scores.csv  # Final optimized locations
│   ├── plots/                # Graphs and visualizations
│
│── scripts/                  # Standalone scripts for running experiments
│   ├── run_monte_carlo.py    
│   ├── run_rl_training.py    
│   ├── run_evaluation.py     
│
│── requirements.txt          # Required Python libraries
│── README.md                 # Project overview and setup instructions
│── report/                   # Research paper and documentation
│   ├── draft.pdf
│   ├── figures/
```

## Getting Started
### Installation
```bash
  git clone https://github.com/yourusername/EV_Charging_Optimization.git
  cd EV_Charging_Optimization
  pip install -r requirements.txt
```

### Usage
Run Monte Carlo simulation:
```bash
  python scripts/run_monte_carlo.py
```
Train RL model:
```bash
  python scripts/run_rl_training.py
```
Evaluate results:
```bash
  python scripts/run_evaluation.py
```

## License
MIT License.

