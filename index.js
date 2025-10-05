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
      carPayment,
      kindergartenPayment
    } = req.body;

    // Validate all inputs and provide defaults for undefined values
    const inputs = { 
      salary: salary !== undefined && salary !== null ? salary : 0, 
      rent: rent !== undefined && rent !== null ? rent : 0, 
      electricity: electricity !== undefined && electricity !== null ? electricity : 0, 
      water: water !== undefined && water !== null ? water : 0, 
      councilTax: councilTax !== undefined && councilTax !== null ? councilTax : 0, 
      houseCommittee: houseCommittee !== undefined && houseCommittee !== null ? houseCommittee : 0, 
      shopping: shopping !== undefined && shopping !== null ? shopping : 0, 
      carPayment: carPayment !== undefined && carPayment !== null ? carPayment : 0, 
      kindergartenPayment: kindergartenPayment !== undefined && kindergartenPayment !== null ? kindergartenPayment : 0 
    };
    
    // Debug log to see what values we're receiving
    console.log('Received values:', { salary, rent, electricity, water, councilTax, houseCommittee, shopping, carPayment, kindergartenPayment });
    console.log('Kindergarten payment specifically:', kindergartenPayment, typeof kindergartenPayment);
    console.log('Processed inputs:', inputs);
    console.log('Final kindergarten payment in inputs:', inputs.kindergartenPayment);

    for (const [key, value] of Object.entries(inputs)) {
      if (!isValidNumber(value)) {
        throw new Error(`Invalid value for ${key}. Please enter a valid number.`);
      }
    }

    const totalFixedExpenses = inputs.rent + inputs.electricity + inputs.water + inputs.councilTax + inputs.houseCommittee + inputs.shopping + inputs.carPayment + inputs.kindergartenPayment;
    const availableAfterBills = inputs.salary - totalFixedExpenses;
    
    // Calculate recommended savings (20% of income is a common financial advice)
    const recommendedSavings = inputs.salary * 0.2;
    const savingsPercentage = 20; // 20% of income

    res.json({
      totalFixedExpenses,
      availableAfterBills,
      recommendedSavings,
      savingsPercentage,
      expenseBreakdown: {
        housing: inputs.rent + inputs.houseCommittee,
        utilities: inputs.electricity + inputs.water,
        taxes: inputs.councilTax,
        shopping: inputs.shopping,
        carPayment: inputs.carPayment,
        kindergartenPayment: inputs.kindergartenPayment
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