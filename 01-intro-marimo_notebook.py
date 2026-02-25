import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <br>

    # <font size=6 color=lightblue>**Introduction to the Marino Notebook**</font>

    ---
    """)
    return


@app.cell
def _():
    print('Hello, World!!!')
    return


@app.cell
def _():
    first_name = 'Fernando'
    last_name = 'Galvao'

    print(f'Full name: {first_name} {last_name}')
    return


@app.cell
def _():
    a = 15
    b = -3
    return a, b


@app.cell
def _(a, b):
    total = a + b
    print(total)
    return


@app.cell
def _():
    def _():
        def hello():
            print('Hello, World!!!')
            print('Welcome to Marino Notebook ; )')
        if __name__ == '__main__':
            return hello()

    _()
    return


@app.cell
def _():
    def _():
        def hello_guy(your_name:str):
            print(f'Hello, {your_name}!!!')
            print(f'Welcome to Marino Notebook ; )')
        if __name__ == '__main__':
            return hello_guy('Fernando')

    _()
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(start=0, stop=100, label='Choose a value:')
    slider
    return (slider,)


@app.cell
def _(slider):
    print(f'Double the selected value is: {slider.value * 2}')
    return


@app.function
def print_name(your_name):
    print(your_name)


@app.cell
def _():
    print_name('Fernando')
    return


@app.cell
def _():
    list_names = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Linus Torvalds', 
                  'Hedy Lamarr', 'Margaret Hamilton', 'Mary Kenneth Keller', 'Radia Perlman', 'Carol Shaw',
                  'Bjarne Stroustrup', 'Guido van Rossum', 'Fei-Fei Li', 'Yann LeCun', 'Ian Goodfellow', 
                  'Geoffrey Hinton', 'John Hopfield']

    def _():
        for name in list_names:
            print(name)

    _()
    return (list_names,)


@app.cell
def _(list_names):
    def _():
        print('\tNAMES')
        print('='*30)
        for idx, name in enumerate(list_names):
            print(f'{idx+1}: {name}')

    _()
    return


@app.cell
def _():
    def _():
        def print_names(names:list) -> list:
            print(names)
        
        if __name__ == '__main__':
            list_names = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Linus Torvalds', 
                     'Hedy Lamarr', 'Margaret Hamilton', 'Mary Kenneth Keller', 'Radia Perlman', 'Carol Shaw',
                     'Bjarne Stroustrup', 'Guido van Rossum', 'Fei-Fei Li', 'Yann LeCun', 'Ian Goodfellow', 
                     'Geoffrey Hinton', 'John Hopfield']
            return print_names(list_names)


    _()
    return


@app.cell
def _():
    def _():
        def print_names(names:list) -> list:
            print(names)
        
        if __name__ == '__main__':
            list_names = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Linus Torvalds', 
                     'Hedy Lamarr', 'Margaret Hamilton', 'Mary Kenneth Keller', 'Radia Perlman', 'Carol Shaw',
                     'Bjarne Stroustrup', 'Guido van Rossum', 'Fei-Fei Li', 'Yann LeCun', 'Ian Goodfellow', 
                     'Geoffrey Hinton', 'John Hopfield']
            for name in list_names:
                print(name)
        return None


    _()
    return


@app.cell
def _():
    def _():
        def print_names(names:list) -> list:
            print(names)
        
        if __name__ == '__main__':
            list_names = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Linus Torvalds', 
                     'Hedy Lamarr', 'Margaret Hamilton', 'Mary Kenneth Keller', 'Radia Perlman', 'Carol Shaw',
                     'Bjarne Stroustrup', 'Guido van Rossum', 'Fei-Fei Li', 'Yann LeCun', 'Ian Goodfellow', 
                     'Geoffrey Hinton', 'John Hopfield']
            for idx, name in enumerate(list_names):
                print(f'{idx+1}: {name}')
        return None


    _()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
