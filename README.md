Here’s the updated `README.md` file for the provided script:

```markdown
# P/E Ratio Plotting Script for Small Cap 100 and Nifty 100

This Python script fetches and plots the ratio of P/E (Price to Earnings) values between two stock indices: `Small Cap 100` and `Nifty 100`, over a specified number of days. The data is fetched from the `screener.in` API, and the results are visualized using `matplotlib`.

## Prerequisites

Ensure that Python is installed on your system. The script also requires the following Python packages:

- `requests`
- `matplotlib`

To install these dependencies, run the following command:

```bash
pip install requests matplotlib
```

## Usage

This script accepts a command-line argument for the number of days of data to fetch. You can specify the number of days to see how the P/E ratio changes over time.

### Running the Script

1. **Download the Script**: Save the Python script as `plot_pe_ratio.py`.

2. **Run the Script**: Use the following command to run the script, replacing `<days>` with the number of days you want:

```bash
python plot_pe_ratio.py <days>
```

For example, to fetch data for the past 365 days, use:

```bash
python plot_pe_ratio.py 365
```

### Parameters

- **days**: The number of days for which you want to fetch the P/E ratio data (e.g., 30, 180, 365, etc.).

### Output

- **X-axis**: The date range for the specified number of days.
- **Y-axis**: The ratio of `Small Cap 100 P/E` to `Nifty 100 P/E`.
- The output will be a line plot showing the trend of the P/E ratio over time.

### Example

When you run the script for 365 days, the plot will display the ratio of `Small Cap 100` P/E to `Nifty 100` P/E for the past year.

```bash
python plot_pe_ratio.py 365
```

The graph will have:
- **X-axis**: Date
- **Y-axis**: Ratio of `Small Cap 100` P/E to `Nifty 100` P/E

## Script Details

- The script takes two pre-configured stock indices: `Small Cap 100` and `Nifty 100`.
- It retrieves P/E data from `screener.in` for both indices over the specified period.
- The P/E ratio is calculated for each matching date, and the result is plotted in a graph.
- **Error Handling**: If the company names provided do not match, or if there is an issue with the API, the script will raise a `ValueError`.

## Dependencies

This script requires the following Python libraries:
- `requests`: To fetch data from the API.
- `matplotlib`: To plot the graph.

You can install these libraries using the following command:

```bash
pip install requests matplotlib
```

## License

This project is open-source and available under the MIT License.
```

### Key Points:
- **Script Execution**: Instructions on how to run the script with the `days` parameter as a command-line argument.
- **Dependencies**: Lists required Python packages and how to install them.
- **Error Handling**: Mentions the error cases such as invalid company names or API issues.
- **Usage Example**: Shows how to run the script with a specific number of days.

This `README.md` provides clear instructions for using and understanding the script. Let me know if you'd like to make further adjustments!