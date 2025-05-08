# 🎵 Spotify Pop Analytics Dashboard

A **data-driven**, **interactive** dashboard for exploring pop genre metrics, built with [Preswald](https://github.com/StructuredLabs/preswald). This app showcases how to work with real-world datasets, perform data cleaning and SQL-like queries, and build minimal, end-user-facing data-driven UIs using the Preswald SDK.

---

## 🚀 Table of Contents

1. [Features](#-features)
2. [Demo](#-demo)
3. [Tech Stack](#-tech-stack)
4. [Installation](#-installation)
5. [Project Structure](#-project-structure)
6. [Usage](#-usage)
7. [Customization](#-customization)
8. [Contributing](#-contributing)
9. [License](#-license)

---

## ✨ Features

* **Key Metrics**: Total artists, average followers, top artist & top track with release dates.
* **Correlation Analysis**: Heatmap of audio features (danceability, energy, loudness, tempo) vs. popularity.
* **Interactive Scatter Plot**: Danceability vs. popularity (size = energy, color = loudness).
* **Bar Charts**:

  * All pop artists ranked by follower count.
  * Top 10 pop tracks by popularity.
* **Interactive Tables**: Fully sortable, filterable tables for artists and tracks.
* **Research Narratives**: Contextual descriptions and next-step suggestions for each visualization.

---

## 🛠️ Tech Stack

* **Language**: Python
* **UI Framework**: [Preswald](https://github.com/preswald/preswald)
* **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)
* **Data Storage**: In-memory SQLite for SQL-like queries via Pandas

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/rl4658/spotify-pop-analytics.git
   cd spotify-pop-analytics
   ```
2. **(Optional) Create & activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .\.venv\\Scripts\\activate  # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install preswald
   ```
4. **Place your data**

   * Rename your Spotify CSV to `data/sample.csv`
5. **Run the app**

   ```bash
   preswald run
   ```
6. **Open in browser**
   Navigate to `http://localhost:8501`

---

## 🗂️ Project Structure

```
spotify-pop-analytics/
├── data/
│   └── sample.csv           # Your Spotify dataset
├── images/
│   ├── logo.png             # App logo
│   └── favicon.ico          # App favicon
├── screenshots/             # Example visuals for README
├── hello.py                 # Main preswald script
├── preswald.toml            # Configuration file
└── README.md                # This file
```

---

## ⚙️ Usage

* **Modify Queries**: Edit `hello.py` SQL strings to filter by other genres or add conditions.
* **Add Visualizations**: Leverage Plotly Express to create new charts—just import `px` and call `plotly(fig)`.
* **Customize Branding**: Change `branding.primaryColor`, `logo`, and `favicon` in `preswald.toml`.

---

## 🔧 Customization

* **Theme**: Adjust the `template` parameter in Plotly calls (e.g., `plotly_dark`) and tweak `labels` and `colors`.
* **Narratives**: Update `text()` blocks in `hello.py` to refine descriptions and calls to action.
* **Data Sources**: Add new `[data.<name>]` sections in `preswald.toml` to pull from multiple CSVs or other sources.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-chart`)
3. Commit your changes (`git commit -m "Add radial bar chart"`)
4. Push to the branch (`git push origin feature/new-chart`)
5. Open a Pull Request

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
