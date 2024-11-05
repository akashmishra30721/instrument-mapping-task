from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the DataFrame (replace with your actual data loading logic)
final_df = pd.read_csv('temp.csv')  # Replace with your data source

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_by_broker_symbol')
def search_by_broker_symbol():
    broker = request.args.get('broker', '').strip().lower()
    symbol = request.args.get('symbol', '').strip().lower()

    # Check if broker is selected
    if broker:
        # Map broker to corresponding column in final_df for filtering
        if broker == 'kotak':
            filtered_df = final_df[final_df['Kotak Symbol_kotak'].str.lower().str.contains(symbol)]
        elif broker == 'fyers':
            filtered_df = final_df[final_df['Symbol ticker_fyers'].str.lower().str.contains(symbol)]
        elif broker == 'angel':
            filtered_df = final_df[final_df['Angel One Symbol_angel'].str.lower().str.contains(symbol)]
        elif broker == 'zerodha':
            filtered_df = final_df[final_df['Zerodha Symbol_zerodha'].str.lower().str.contains(symbol)]
        
    else:
        # If no broker is selected, return an empty DataFrame
        filtered_df = pd.DataFrame(columns=final_df.columns)

    # Render the result page with the filtered DataFrame as a table
    result_html = filtered_df.to_html(classes='table table-striped', index=False)
    return render_template('result.html', result=result_html)

@app.route('/search_by_instrument_name')
def search_by_instrument_name():
    instrument_name = request.args.get('instrumentName', '').strip().lower()

    # Filter based on instrument name across all relevant columns
    filtered_df = final_df[
        (
            final_df['Instrument Name_Kotak'].str.lower().str.contains(instrument_name) | 
            final_df['Instrument Name_Fyers'].str.lower().str.contains(instrument_name) |
            final_df['Instrument Name_angel'].str.lower().str.contains(instrument_name) |
            final_df['Instrument Name_zerodha'].str.lower().str.contains(instrument_name) |
            (instrument_name == '')
        )
    ]

    # Render the result page with the filtered DataFrame as a table
    result_html = filtered_df.to_html(classes='table table-striped', index=False)
    return render_template('result.html', result=result_html)

if __name__ == '__main__':
    app.run(debug=True)
