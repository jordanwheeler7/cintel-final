import pandas as pd
from shiny import render, reactive
from shinywidgets import render_widget
import plotly.express as px
import pathlib
from util_logger import setup_logger

logger, logname = setup_logger(__name__)

def get_team_data_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("team_data.csv")
    original_df = pd.read_csv(p)
    print(original_df.head())
    total_count = len(original_df)

    # Create a reactive value to hold the selected team and the filtered pandas dataframe
    reactive_team = reactive.Value("All Teams")
    reactive_df = reactive.Value()

    # Create a reactive effect to set the reactive value when inputs change

    @reactive.Effect
    @reactive.event(
        input.TEAM_WINS_RANGE,
        input.TEAM_LOSSES_RANGE,
        input.TEAM_DIVISIONS,
        input.TEAM_SELECT,
    )
    def update_filtered_df():
        selected_team = input.TEAM_SELECT()
        df = original_df.copy()

        # Filter by selected team
        if selected_team != "All Teams":
            df = df[df["Franchise"] == selected_team]

        # Wins and Losses are ranges
        input_wins_range = input.TEAM_WINS_RANGE()
        input_losses_range = input.TEAM_LOSSES_RANGE()
        wins_filter = (df["W"] >= input_wins_range[0]) & (df["W"] <= input_wins_range[1])
        losses_filter = (df["L"] >= input_losses_range[0]) & (df["L"] <= input_losses_range[1])
        df = df[wins_filter & losses_filter]

        # Division is a list of checkboxes
        show_divisions_list = []
        if input.TEAM_DIVISIONS_AL():
            show_divisions_list.append("AL")
        if input.TEAM_DIVISIONS_NL():
            show_divisions_list.append("NL")
        show_divisions_list = show_divisions_list or ["AL", "NL"]
        division_filter = df["Divs"].isin(show_divisions_list)
        df = df[division_filter]

        reactive_df.set(df)

    @output
    @render.text
    def total_team_count():
        filtered_count = len(reactive_df.get())
        message = f"Showing {filtered_count} of {total_count} teams"
        return message

    @output
    @render.table
    def team_data_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def team_win_loss_scatter():
        df = reactive_df.get()
        scatter_plot = px.scatter(
            df,
            x="W",
            y="L",
            color="Franchise",
            title="Team Win-Loss Scatter Plot",
            labels={"W": "Wins", "L": "Losses"},
            size_max=10,
        )
        return scatter_plot

    @output
    @render.text
    def avg_wins_losses():
        df = reactive_df.get()
        avg_wins = df["W"].mean()
        avg_losses = df["L"].mean()
        message = f"Average Wins: {avg_wins:.2f}, Average Losses: {avg_losses:.2f}"
        return message

    @output
    @render_widget
    def wins_percentage_by_team():
        df = reactive_df.get()
        win_percentage_histogram = px.histogram(
            df,
            x="W-L%",
            title="Win Percentage by Team Histogram",
            labels={"W-L%": "Win-Loss Percentage"},
            nbins=20,
        )
        return win_percentage_histogram

    @output
    @render.table
    def team_data_chart():
        filtered_df = reactive_df.get()
        return filtered_df

    # Return a list of function names for use in reactive outputs
    return [
        total_team_count,
        team_data_table,
        team_win_loss_scatter,
        avg_wins_losses,
        wins_percentage_by_team,
        team_data_chart,
    ]
