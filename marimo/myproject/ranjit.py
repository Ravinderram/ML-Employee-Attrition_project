import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import marimo as mo
    import seaborn as sns
    import plotly.express as px
    from pca import pca
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    return mo, pd, plt, sns


@app.cell
def _(pd):
    df = pd.read_csv("../myproject/happy.csv")
    return (df,)


@app.cell
def _(df):
    # Show the first rows
    df.head()
    return


@app.cell
def _(mo):
    n_slider = mo.ui.slider(start=1, stop=20, step=1, value=10, label="Number of Countries")

    # 2. Display the slider
    n_slider
    return (n_slider,)


@app.cell
def _(df, n_slider, plt, sns):

    def plot_happiness(n):
        # Filter your data based on the slider value
        top_countries = df.nlargest(n, 'Score')
    
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_countries, x='Score', y='Country or region', ax=ax)
    
        ax.set_title(f'Top {n} Happiest Countries')
        ax.set_xlabel('Happiness Score')
        ax.set_ylabel('Country or region')
        plt.tight_layout()
    
        # Return the figure so Marimo can render it
        return fig

    # This will update instantly as you move the slider
    plot_happiness(n_slider.value)
    return


if __name__ == "__main__":
    app.run()
