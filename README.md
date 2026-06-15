# GMO Safety Evidence Dashboard

An interactive data dashboard analyzing GMO product safety across countries — approval status, use cases, and risk assessments.

## Tech Stack
- **Python** — data collection, cleaning, Plotly Dash dashboard
- **R** — statistical comparison (ANOVA, ggplot2, R Markdown)

## Features
- 🗺️ Country-level GMO approval world map
- 📊 Risk score analysis by crop type
- 🔬 Statistical analysis report (R Markdown + ANOVA)
- 🔍 Interactive filters by crop type and approval status
- 📋 Full data table with 20 GMO products

## Project Structure 
gmo-safety-dashboard/
├── data/           # Raw and cleaned datasets

├── dashboard/      # Python Dash application

├── analysis/       # R scripts and R Markdown report

├── notebooks/      # Jupyter notebooks

└── assets/         # Screenshots
## Screenshots

## Screenshots

![Bar Chart](assets/Screenshot%202026-06-15%20131903.png)
![Scatter Plot](assets/Screenshot%202026-06-15%20131927.png)
![Data Table](assets/Screenshot%202026-06-15%20131958.png)
![Dashboard Filter](assets/Screenshot%202026-06-15%20134624.png)
![Scatter New](assets/Screenshot%202026-06-15%20134646.png)
![World Map](assets/Screenshot%202026-06-15%20135945.png)

## How to Run

### Python Dashboard
```bash
conda activate gmo_dash
cd dashboard
python app.py
```
Open `http://127.0.0.1:8050/` in your browser.

### R Analysis
Open `analysis/gmo_analysis.Rmd` in RStudio and click **Knit**.

## Author
**Nazrin Shahpalangova** — Biology/Genetics (BSc, Baku State University)  
Data analyst with domain expertise in GMO safety and risk assessment.
