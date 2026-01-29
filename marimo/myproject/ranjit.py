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
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("../marimo/myproject/happy.csv")
    return


if __name__ == "__main__":
    app.run()
