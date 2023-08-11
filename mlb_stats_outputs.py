"""
Purpose: Display output for Mlb Stats dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_team_data_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3('MLB Stats Dashboard'),
            ui.tags.br(),
            ui.output_text('team_select_string'),
            ui.tags.br(),
            ui.output_table('team_data_table'),
            ui.tags.br(),
            ui.h3('Filtered Summary Table'),
            output_widget('team_data_chart'),
            ui.tags.br(),
            output_widget('total_team_count'),
            ui.tags.br(),
            output_widget('avg_wins_losses'),
            ui.tags.br(),
            output_widget('team_win_loss_scatter'),
            ui.tags.br(),
            output_widget('wins_percentage_by_team'),
            ui.tags.br(),
        ),
    )
