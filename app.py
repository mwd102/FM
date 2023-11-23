from flask import (
    Flask, request, render_template,
    redirect, make_response, session, url_for,
    flash, jsonify
    )
from function_names import function_names
import os
import pandas as pd
from werkzeug.utils import secure_filename

if os.path.exists("env.py"):
    import env


from calculate_functions import *

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

data_list = []

def count_html_table_rows(file):
    file.seek(0)
    content = file.read() 
    if isinstance(content, bytes):
        content = content.decode('utf-8')
        print("decoded")
    row_count = content.count('<tr')
    file.seek(0)
    return row_count

@app.route('/')
def index():
    selected_options = session.get('selected_options', [])
    return render_template(
        'index.html',
        function_names=function_names,
        selected_options=selected_options)


@app.route('/get_data')
def get_data():
    return jsonify(data_list)


@app.route('/clear_data')
def clear_data():
    data_list.clear()
    return jsonify({'message': 'Data list cleared successfully'})


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            flash('No file part.', 'error')
            return redirect(url_for('index'))

        file = request.files['file']

        row_count = count_html_table_rows(file)
        max_row_count = 1000
        if row_count > max_row_count:
            flash(f'Sorry, our application currently supports processing files with up to {max_row_count} rows. Please use a smaller data set or clone https://github.com/Fatheed7/FM/ to run locally.', 'error')
            return redirect(url_for('index'))

        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('index'))
        
        if file.content_length > 2 * 1024 * 1024:
            flash('File is too large (maximum 2 MB).', 'error')
            return redirect(url_for('index'))

        if not os.path.splitext(secure_filename(file.filename))[1].lower() == '.html':
            flash('Invalid file format, only HTML files are allowed.', 'error')
            return redirect(url_for('index'))

        if file:
            try:
                form_data = request.form.to_dict()

                selected_options = []
                data_calc_values = []

                for key, value in form_data.items():
                    data_calc_values.append(key)
                    selected_options.append(value)

                if not data_calc_values:
                    flash('At least one checkbox must be selected.', 'error')
                    return redirect(url_for('index'))

                # List containing selected functions to be run
                calculation_functions = [
                    calculate_speed_workrate_score
                ]

                # Iterate over selected function names
                # and dynamically add them to the list
                for option in selected_options:
                    try:
                        function_name = option
                        # Fetch the function by name and add it to the list
                        calculation_functions.append(
                            getattr(__import__(
                                'calculate_functions'), function_name))
                    except AttributeError:
                        flash(f'Function not found: {function_name}', 'error')
                        return redirect(url_for('index'))

                # Read the uploaded HTML file using Pandas
                # This assumes the HTML file contains tables
                squad_rawdata_list = pd.read_html(
                    file, header=0, encoding='utf-8')
                squad_rawdata = squad_rawdata_list[0]

                
                # List of columns to include in the check for hyphens
                included_columns = [
                     "1v1",  "Acc",  "Aer",  "Agg",  "Agi",  "Ant",  "Bal",  
                     "Bra",  "Cmd",  "Cnt",  "Cmp",  "Cro",  "Dec",  "Det",  
                     "Dri",  "Fin",  "Fir",  "Fla",  "Han",  "Hea",  "Jum",  
                     "Kic",  "Ldr",  "Lon",  "Mar",  "OtB",  "Pac",  "Pas",  
                     "Pos",  "Ref",  "Sta",  "Str",  "Tck",  "Tea",  "Tec",  
                     "Thr",  "TRO",  "Vis",  "Wor",  "Cor",  "Com",  "Ecc",  
                     "Fre",  "L Th",  "Nat",  "Pen",  "Pun"
                ]

                # Function to check for hyphens in non-excluded columns
                def check_for_hyphens(row, included_columns):
                    for col in row.index:
                        if col in included_columns and '-' in str(row[col]):
                            return True
                    return False
                
                squad_rawdata['masked_attributes'] = squad_rawdata.apply(check_for_hyphens, axis=1, included_columns=included_columns)

                # Check if any row returns True
                if squad_rawdata['masked_attributes'].any():
                    flash('At least one row has an attribute range. Please fully scout the player(s) or disable attribute masking.', 'error')
                    return redirect(url_for('index'))


                # Run the selected functions on the data
                for calculation_function in calculation_functions:
                    squad_rawdata = calculation_function(squad_rawdata)
                
                # Determine earning column
                earnings_columns = ['Wage', 'Salary']
                valid_earnings_columns = squad_rawdata.columns[squad_rawdata.columns.isin(earnings_columns)]

                # Add 'Earnings' to the DataFrame if a valid earnings column is present
                if len(valid_earnings_columns) > 0:
                    squad_rawdata['Wage'] = squad_rawdata[valid_earnings_columns[0]]
                else:
                    # If neither Wage nor Salary is present, create an 'Earnings' column with NaN values
                    squad_rawdata['Wage'] = None

                # Columns to export to HTML
                columns_to_export = [
                    'Inf', 'Name', 'Age', 'Club', 'Transfer Value', 'Wage',
                    'Nat', 'Position', 'Personality', 'Media Handling',
                    'Left Foot', 'Right Foot', 'Spd', 'Jum', 'Str', 'Work', 'Height'
                ] + data_calc_values

                # Builds Squad DataFrame using only specified columns
                squad = squad_rawdata[columns_to_export]


                global data_list
                data_list = squad.fillna('').to_dict(orient='records')

                session['selected_options'] = selected_options

                return redirect(url_for('index'))

            except ValueError as ve:
                return render_template("error.html", error=ve)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


@app.route('/<path:invalid_route>')
def invalid_route(invalid_route):
    # Route back to index page on invalid route
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
