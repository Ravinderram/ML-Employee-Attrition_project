import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import plotly.express as px
    from pca import pca
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    return pd, plt, sns


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
def _():
    import marimo as mo

    top_n = mo.ui.slider(5, 30, value=10, label="Select number of top countries")
    top_n

    return (top_n,)


@app.cell
def _(df, top_n):
    n = top_n.value

    top_countries = (
        df[['Country or region', 'Score']]
        .sort_values(by='Score', ascending=False)
        .head(n)
    )

    top_countries

    return n, top_countries


@app.cell
def _(n, plt, sns, top_countries):

    plt.figure(figsize=(10,6))
    sns.barplot(data=top_countries, x='Score', y='Country or region')
    plt.title(f'Top {n} Happiest Countries')
    plt.xlabel('Happiness Score')
    plt.ylabel('Country or region')
    plt.tight_layout()
    plt.show()

    return


if __name__ == "__main__":
    app.run()
