from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_tax():
    if request.method == 'POST':
        income = float(request.form.get('income'))

        # Calculate MPF contribution
        if income <= 85200:  # If annual income is below $85,200, no MPF contributions are required
            MPF_contribution = 0
        else:
            MPF_contribution = min(0.05 * income, 18000)

        net_income = income - MPF_contribution - 132000  # Deduct the tax-free allowance HKD 132,000 in 2023/2024

        if net_income <= 0:  # If the net income is not positive, no tax is payable
            tax_payable = 0
        elif net_income > 2500000:
            # For extremely high annual income (e.g. over HKD2.5M), the actual amount is HKD2.022M in 2023/2024
            # apply a standard tax rate of 15%, the actual standard tax rate, by the calculation from IRD tax calculator, it is not exactly 15%, it is slightly higher.
            tax_payable = net_income * 0.15
        else:
            # Apply the progressive tax calculation
            bands = [(50000, 0.02), (50000, 0.06), (50000, 0.10), (50000, 0.14), (None, 0.17)]
            remaining_income = net_income
            tax_payable = 0
            for band in bands:
                if band[0] is None or remaining_income <= band[0]:
                    tax_payable += remaining_income * band[1]
                    break
                else:
                    tax_payable += band[0] * band[1]
                    remaining_income -= band[0]

        return render_template('result.html', MPF_contribution=MPF_contribution, tax_payable=tax_payable)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)