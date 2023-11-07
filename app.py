from flask import (
    Flask, request, render_template,
    redirect, make_response, url_for
    )
import os
import pandas as pd

from calculate_functions import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            try:
                # Read the uploaded HTML file using Pandas
                # This assumes the HTML file contains tables
                squad_rawdata_list = pd.read_html(
                    file, header=0, encoding='utf-8')

                squad_rawdata = squad_rawdata_list[0]

                # List containing all functions to be ran
                calculation_functions = [
                    calculate_speed_workrate_score,
                    calculate_gk_score,
                    calculate_fb_score,
                    calculate_cb_score,
                    calculate_dm_score,
                    calculate_segundo_volante_score,
                    calculate_box2box_score,
                    calculate_winger_score,
                    calculate_inverted_winger_score,
                    calculate_amc_score,
                    calculate_striker_score
                ]

                # Each function is called as the list is looped over.
                for calculation_function in calculation_functions:
                    squad_rawdata = calculation_function(squad_rawdata)

                # Builds Squad Dataframe using only columns
                # that will be exported to HTML
                squad = squad_rawdata[[
                    'Inf', 'Name', 'Age', 'Club', 'Transfer Value', 'Wage',
                    'Nat', 'Position', 'Personality', 'Media Handling',
                    'Left Foot', 'Right Foot', 'Spd', 'Jum', 'Str', 'Work',
                    'Height', 'gk', 'fb', 'cb', 'vol', 'str']]

                html = generate_html(squad)

                response = make_response(html)
                response.headers['Content-Type'] = 'text/html'
                return response
            except ValueError as ve:
                return render_template("error.html", error=ve)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


@app.route('/<path:invalid_route>')
def invalid_route(invalid_route):
    # Route back to index page on invalid route
    return redirect(url_for('index'))


def generate_html(dataframe: pd.DataFrame):

    # Get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table", index=False, na_rep='')
    # Construct the HTML with jQuery Data tables
    html = f"""
    <html>
    <header>
        <meta charset="utf-8">
        <link
         href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css"
         rel="stylesheet">
        <title>Processed FM Data</title>
    </header>
    <body>
    <a onclick="this.href='data:text/html;charset=UTF-8,
    '+encodeURIComponent(document.documentElement.outerHTML)"
     href="#" download="processed_data.html"">
        <button>Download HTML</button>
    </a>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js"
    integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI="
    crossorigin="anonymous"></script>
    <script type="text/javascript"
    src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js">
    </script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                paging: false,
                order: [[12, 'desc']],
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # Return the HTML as bytes
    return html.encode('utf-8')


if __name__ == '__main__':
    app.run(debug=True)
