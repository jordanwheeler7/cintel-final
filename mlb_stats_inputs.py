"""
Purpose: Provide user interaction options for MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui
import randfacts
# Define the UI inputs and include our new selection options

def get_team_data_inputs():
    return ui.panel_sidebar(
        ui.h2("Here is a random fact for you to enjoy!"),
        ui.h5(randfacts.getFact()),
        ui.hr(),
        ui.h2("MLB Teams Interaction"),
        ui.tags.hr(),
        ui.input_select(
            id="TEAM_SELECT",
            label="Choose a team",
            choices=["All Teams", "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles", "Boston Red Sox", "Chicago Cubs", "Chicago White Sox", "Cincinnati Reds", "Cleveland Indians", "Colorado Rockies", "Detroit Tigers", "Houston Astros", "Kansas City Royals", "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins", "Milwaukee Brewers", "Minnesota Twins", "New York Mets", "New York Yankees", "Oakland Athletics", "Philadelphia Phillies", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants", "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays", "Texas Rangers", "Toronto Blue Jays", "Washington Nationals"],
            selected="Kansas City Royals",
        ),         
        ui.tags.hr(),    
        ui.tags.section(
            ui.h3("Team Data Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("From: The year the team was founded"),
                ui.tags.li("To: The year the team was disbanded"),
                ui.tags.li("G: Number of games played"),
                ui.tags.li("W: Number of games won"),
                ui.tags.li("L: Number of games lost"),
                ui.tags.li("W-L%: Percentage of games won"),
                ui.tags.li("G>.500: Number of games won when the team's W-L% was greater or less than .500"),
                ui.tags.li("Divs: Number of division titles won"),
                ui.tags.li("Pnnts: Number of pennants won"),
                ui.tags.li("WS: Number of World Series won"),
                ui.tags.li("Playoffs: Number of playoff appearances"),
                ui.tags.li("Players: Number of players who played for the team"),
                ui.tags.li("HOF#: Number of players who played for the team and are in the Hall of Fame"),
                ui.tags.li("R: Number of runs scored"),
                ui.tags.li("AB: Number of at bats"),
                ui.tags.li("H: Number of hits"),
                ui.tags.li("HR: Number of Home Runs"),
                ui.tags.li("BA: Batting Average"),
                ui.tags.li("RA: Runs Allowed"),
                ui.tags.li("ERA: Earned Run Average"),
        
            ),
            ui.output_table("team_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
