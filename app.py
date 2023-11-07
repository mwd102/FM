from flask import (
    Flask, request, render_template,
    redirect, make_response, url_for,
    flash
    )
import os
import pandas as pd

if os.path.exists("env.py"):
    import env

from calculate_functions import *

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
                flash('No file part.', 'error')
                return redirect(url_for('index'))

        file = request.files['file']

        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('index'))

        if file:
            try:
                form_data = request.form.to_dict()

                selected_options = [form_data[key] for key in form_data.keys() if key.startswith('option')]
                if not selected_options:
                    flash('At least one checkbox must be selected.', 'error')
                    return redirect(url_for('index'))
                # Read the uploaded HTML file using Pandas
                # This assumes the HTML file contains tables
                squad_rawdata_list = pd.read_html(
                    file, header=0, encoding='utf-8')

                squad_rawdata = squad_rawdata_list[0]

                #Calculate Speed & Workrate Score
                speed = int(request.form['speed'])
                workrate = int(request.form['workrate'])
                setp = int(request.form['setp'])
                squad_rawdata = calculate_speed_workrate_score(squad_rawdata, speed, workrate, setp)

                #Calculate GK Score
                gk_essential = int(request.form['gk_essential'])
                gk_core = int(request.form['gk_core'])
                gk_secondary = int(request.form['gk_secondary'])
                squad_rawdata = calculate_gk_score(squad_rawdata, gk_essential, gk_core, gk_secondary)

                #Calculate FB Score
                fb_essential = int(request.form['fb_essential'])
                fb_core = int(request.form['fb_core'])
                fb_secondary = int(request.form['fb_secondary'])
                squad_rawdata = calculate_fb_score(squad_rawdata, fb_essential, fb_core, fb_secondary)

                #Calculate CB Score
                cb_core = int(request.form['cb_core'])
                cb_secondary = int(request.form['cb_secondary'])
                squad_rawdata = calculate_cb_score(squad_rawdata, cb_core, cb_secondary)

                #Calculate DM Score
                dm_core = int(request.form['dm_core'])
                squad_rawdata = calculate_dm_score(squad_rawdata, dm_core)

                #Calculate SV Score
                sv_core = int(request.form['sv_core'])
                squad_rawdata = calculate_segundo_volante_score(squad_rawdata, sv_core)

                #Calculate B2B Score
                b2b_core = int(request.form['b2b_core'])
                squad_rawdata = calculate_box2box_score(squad_rawdata, b2b_core)
                
                #Calculate W Score
                wing_core = int(request.form['wing_core'])
                wing_secondary = int(request.form['wing_secondary'])
                squad_rawdata = calculate_winger_score(squad_rawdata, wing_core, wing_secondary)

                #Calculate IW Score
                iw_core = int(request.form['iw_core'])
                squad_rawdata = calculate_inverted_winger_score(squad_rawdata, iw_core)

                #Calculate AMC Score
                amc_core = int(request.form['amc_core'])
                squad_rawdata = calculate_amc_score(squad_rawdata, amc_core)

                #Calculate STR Score
                str_core = int(request.form['str_core'])
                str_secondary = int(request.form['str_secondary'])
                squad_rawdata = calculate_striker_score(squad_rawdata, str_core, str_secondary)

                # Builds Squad Dataframe using only columns
                # that will be exported to HTML
                squad = squad_rawdata[[
                    'Inf', 'Name', 'Age', 'Club', 'Transfer Value', 'Wage',
                    'Nat', 'Position', 'Personality', 'Media Handling',
                    'Left Foot', 'Right Foot', 'Spd', 'Jum', 'Str', 'Work',
                    'Height'] + selected_options]

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
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
        <title>Processed FM Data</title>
    </header>
    <body>
        <button id="downloadButton">Download HTML</button>
        {table_html}
        <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js"
            integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI="
            crossorigin="anonymous"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script>
            $(document).ready(function () {{
                $('#table').DataTable({{
                    paging: false,
                    order: [[12, 'desc']],
                    // scrollY: 400,
                }});

                // Add click event listener to the download button
                document.getElementById('downloadButton').addEventListener('click', function () {{
                    // Create a Blob containing the HTML content
                    var blob = new Blob(['<!DOCTYPE html><html>' +
                    document.documentElement.outerHTML + '</html>'], {{ type: 'text/html' }});
                    // Create a temporary URL for the Blob
                    var url = URL.createObjectURL(blob);
                    // Create a download link and trigger a click event to download the file
                    var a = document.createElement('a');
                    a.href = url;
                    a.download = 'processed_data.html';
                    document.body.appendChild(a);
                    a.click();
                    // Clean up the temporary URL and remove the download link
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);
                }});
            }});
        </script>
    </body>
    </html>
    """
    # Return the HTML as bytes
    return html.encode('utf-8')



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
