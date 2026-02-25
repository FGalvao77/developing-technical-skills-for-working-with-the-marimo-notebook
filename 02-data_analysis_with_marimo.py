import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import polars as pl
    import io

    return io, mo, pd, pl


@app.cell
def _():
    csv_data = '''
        id,product,sales,sector
        1,notebook,1500,electronic
        2,keyboard,200,electronic
        3,monitor,900,electronic
        4,ergonomic chair,1200,furniture
        5,table,800,furniture
        6,usb drive,7, others
    '''
    return (csv_data,)


@app.cell
def _(csv_data, io, mo, pd):
    df_pandas = pd.read_csv(filepath_or_buffer=io.StringIO(initial_value=csv_data))
    mo.md(text='##Data loaded successfully using the **`Pandas`** library.!!!')
    return (df_pandas,)


@app.cell
def _(df_pandas):
    df_pandas
    return


@app.cell
def _(csv_data, io, mo, pl):
    df_polars = pl.read_csv(source=io.StringIO(initial_value=csv_data))
    mo.md(text='##Data loaded successfully using the **`Polars`** library.!!!')
    return (df_polars,)


@app.cell
def _(df_polars):
    df_polars
    return


@app.cell
def _(df_pandas, mo):
    my_table = mo.ui.table(data=df_pandas, 
                           label='My sales spreadsheet', 
                           selection='multi')

    mo.vstack([
        mo.md(text='Explore the data below:'),
        my_table
    ])
    return


@app.cell
def _(df_polars, mo):
    my_table2 = mo.ui.table(data=df_polars, 
                           label='My sales spreadsheet', 
                           selection=None)

    mo.vstack([
        mo.md(text='Explore the data below:'),
        my_table2
    ])
    return


@app.cell
def _(df_pandas, mo):
    sectors = list(df_pandas['sector'].unique())
    sector_filter = mo.ui.dropdown(
        options=sectors, label='Filter by sector:'
    )

    sector_filter
    return (sector_filter,)


@app.cell
def _(df_pandas, mo, sector_filter):
    df_filtered = df_pandas[df_pandas['sector'] == sector_filter.value]
    mo.ui.table(data=df_filtered)
    return


@app.cell
def _(df_pandas, mo, sector_filter):
    def _():
        df_filtered = df_pandas[df_pandas['sector'] == sector_filter.value]
        return mo.ui.table(data=df_filtered)

    _()
    return


@app.cell
def _(df_polars):
    list(df_polars['sector'].unique())
    return


@app.cell
def _(df_polars):
    df_polars['sector'].unique().sort().to_list()
    return


@app.cell
def _(df_polars):
    sectors2 = df_polars['sector'].unique().sort().to_list()
    sectors2
    return (sectors2,)


@app.cell
def _(mo, sectors2):
    sector_filter2 = mo.ui.dropdown(
        options=sectors2, 
        label='Filter by sector:',
        value=sectors2[0] if sectors2 else None
    )

    # Exibe o widget no notebook
    sector_filter2
    return


@app.cell
def _(df_polars, mo):
    sectors3 = df_polars['sector'].unique().sort().to_list()

    sector_filter3 = mo.ui.dropdown(
        options=sectors3, 
        label='Filter by sector:',
        value=sectors3[0] if sectors3 else None
    )

    # Exibe o widget no notebook
    sector_filter3
    return


@app.cell
def _(df_polars, mo):
    # CÉLULA 1: Definição do Widget (Escopo Global)
    sectors4 = df_polars['sector'].unique().sort().to_list()

    sector_filter4 = mo.ui.dropdown(
        options=sectors4, 
        label='Filter by sector:',
        value=sectors4[0] if sectors4 else None
    )

    # Exibe o widget no notebook
    sector_filter4
    return (sector_filter4,)


@app.cell
def _(df_polars, mo, pl, sector_filter4):
    # CÉLULA 2: Lógica de Filtragem (Reativa)
    # O marimo executará esta célula automaticamente toda vez que sector_filter mudar
    def _(selection):
        if selection is None:
            return 

        df_filtered4 = df_polars.filter(pl.col(name='sector') == selection)
        return mo.ui.table(data=df_filtered4)

    # Chamamos a função passando o valor ATUAL do widget
    _(sector_filter4.value)
    return


@app.cell
def _(df_polars, mo, pl, sector_filter4):
    # CÉLULA 2: Lógica de Filtragem (Reativa)
    # O marimo executará esta célula automaticamente toda vez que sector_filter mudar
    def _(selection):
        if selection is None:
            return mo.md("Selecione um setor para visualizar os dados.")

        df_filtered4 = df_polars.filter(pl.col(name='sector') == selection)
        return mo.ui.table(data=df_filtered4)

    # Chamamos a função passando o valor ATUAL do widget
    _(sector_filter4.value)
    return


@app.cell
def _(df_polars, mo, pl, sector_filter4):
    # CÉLULA 2: Lógica de Filtragem (Reativa)
    # O marimo executará esta célula automaticamente toda vez que sector_filter mudar
    def _(selection):
        if selection is None:
            print(mo.md(text='Selecione um setor para visualizar os dados.'))

        df_filtered4 = df_polars.filter(pl.col(name='sector') == selection)
        return mo.ui.table(data=df_filtered4)

    # Chamamos a função passando o valor ATUAL do widget
    _(sector_filter4.value)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
