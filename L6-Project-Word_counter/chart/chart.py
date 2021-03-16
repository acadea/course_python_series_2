from bokeh.plotting import figure, output_file, show


def plot_word_count(data: dict, limit: int = 30):
    # prepare some data
    x = list(data.keys())[:limit]
    y = list(data.values())[:limit]

    p = figure(x_range=x, plot_height=750, plot_width=1000, title="Word Counts",
               toolbar_location=None, tools="")

    p.vbar(x=x, top=y, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)
