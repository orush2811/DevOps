const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Validate number
const isValidNumber = (value) => {
  return typeof value === 'number' && !isNaN(value) && value >= 0;
};

// Calculate budget
app.post('/api/calculate', (req, res) => {
  try {
    const {
      salary,
      rent,
      electricity,
      water,
      councilTax,
      houseCommittee,
      shopping,
      carPayment
    } = req.body;

    // Validate all inputs
    const inputs = { salary, rent, electricity, water, councilTax, houseCommittee, shopping, carPayment };
    for (const [key, value] of Object.entries(inputs)) {
      if (!isValidNumber(value)) {
        throw new Error(`Invalid value for ${key}. Please enter a valid number.`);
      }
    }

    const totalFixedExpenses = rent + electricity + water + councilTax + houseCommittee + shopping + carPayment;
    const availableAfterBills = salary - totalFixedExpenses;
    
    // Calculate recommended savings (20% of income is a common financial advice)
    const recommendedSavings = salary * 0.2;
    const savingsPercentage = 20; // 20% of income

    res.json({
      totalFixedExpenses,
      availableAfterBills,
      recommendedSavings,
      savingsPercentage,
      expenseBreakdown: {
        housing: rent + houseCommittee,
        utilities: electricity + water,
        taxes: councilTax,
        shopping: shopping,
        carPayment: carPayment
      }
    });
  } catch (error) {
    console.error('Error calculating budget:', error);
    res.status(400).json({ message: error.message });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

// Serve the main page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
}); 