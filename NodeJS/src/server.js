import express from 'express';
import bodyParser from 'body-parser';
import promClient from 'prom-client';
import winston from 'winston';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Initialize Express
const app = express();
const port = process.env.PORT || 3000;

// Prometheus metrics
const collectDefaultMetrics = promClient.collectDefaultMetrics;
const Registry = promClient.Registry;
const register = new Registry();
collectDefaultMetrics({ register });

// Custom metrics
const httpRequestDurationMicroseconds = new promClient.Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route', 'status_code'],
    buckets: [0.1, 0.5, 1, 5]
});
register.registerMetric(httpRequestDurationMicroseconds);

// Configure Winston logger
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
    ),
    transports: [
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' }),
        new winston.transports.Console({
            format: winston.format.combine(
                winston.format.colorize(),
                winston.format.simple()
            )
        })
    ]
});

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

// Metrics middleware
app.use((req, res, next) => {
    const start = Date.now();
    res.on('finish', () => {
        const duration = Date.now() - start;
        httpRequestDurationMicroseconds
            .labels(req.method, req.route?.path || req.path, res.statusCode)
            .observe(duration / 1000);
    });
    next();
});

// Routes
app.get('/', (req, res) => {
    logger.info('Home page accessed');
    res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Metrics endpoint for Prometheus
app.get('/metrics', async (req, res) => {
    try {
        res.set('Content-Type', register.contentType);
        res.end(await register.metrics());
    } catch (err) {
        logger.error('Error generating metrics', { error: err });
        res.status(500).end(err);
    }
});

// Start server
app.listen(port, () => {
    logger.info(`Server is running on port ${port}`);
    console.log(`Server is running on http://localhost:${port}`);
}); 