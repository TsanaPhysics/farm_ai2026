<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farm AI Dashboard | xAI 2026</title>
    <link rel="stylesheet" href="../css/dashboard.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <aside class="sidebar">
        <div class="logo">
            <i class="fas fa-seedling"></i>
            <span>Farm AI Hub</span>
        </div>
        <nav class="nav-links">
            <div class="nav-item">
                <a href="#" class="nav-link active">
                    <i class="fas fa-th-large"></i>
                    <span>Dashboard</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="#" class="nav-link">
                    <i class="fas fa-flask"></i>
                    <span>Soil Models</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="#" class="nav-link">
                    <i class="fas fa-cloud-sun"></i>
                    <span>Weather AI</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="../admin/" class="nav-link">
                    <i class="fas fa-user-shield"></i>
                    <span>Admin Panel</span>
                </a>
            </div>
        </nav>
    </aside>

    <main class="main-content">
        <header class="header">
            <h1>Overview <span class="status-badge"><span class="status-dot"></span> System Live</span></h1>
            <div class="user-profile">
                <img src="../images/profile.png" alt="Profile" style="width: 40px; border-radius: 50%; border: 2px solid var(--primary);">
            </div>
        </header>

        <section class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Model Accuracy</div>
                <div class="stat-value" style="color: var(--primary);">99.3%</div>
                <div style="font-size: 0.8rem; color: #00ff00; margin-top: 5px;">+2.1% from last month</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Active Sensors</div>
                <div class="stat-value">1,248</div>
                <div style="font-size: 0.8rem; color: #888; margin-top: 5px;">Geospatial Nodes</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Datasets Managed</div>
                <div class="stat-value">42.8 GB</div>
                <div style="font-size: 0.8rem; color: var(--accent); margin-top: 5px;">Multi-modal Data</div>
            </div>
        </section>

        <section class="dashboard-grid">
            <div class="chart-container">
                <h3>Real-time Soil Nutrient Analysis</h3>
                <canvas id="soilChart" height="200"></canvas>
            </div>
            <div class="chart-container" style="background: rgba(0,0,0,0.2);">
                <h3>Quick Prediction</h3>
                <form id="predictForm" style="display: flex; flex-direction: column; gap: 10px; margin-top: 1rem;">
                    <input type="number" placeholder="pH Value" step="0.1" style="padding: 10px; border-radius: 8px; border: none; background: rgba(255,255,255,0.1); color: white;">
                    <input type="number" placeholder="Moisture (%)" style="padding: 10px; border-radius: 8px; border: none; background: rgba(255,255,255,0.1); color: white;">
                    <button type="submit" style="padding: 12px; border-radius: 8px; border: none; background: var(--primary); color: black; font-weight: bold; cursor: pointer;">Run xAI Analysis</button>
                </form>
                <div id="predictionResult" style="margin-top: 1rem; padding: 1rem; border-radius: 12px; background: rgba(0,242,254,0.1); border: 1px dashed var(--primary); display: none;">
                    Prediction: <span id="resText" style="font-weight: bold; color: var(--primary);">Loading...</span>
                </div>
            </div>
        </section>

        <section class="chart-container" style="margin-top: 1.5rem;">
            <h3>Recent Datasets</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Source</th>
                        <th>Type</th>
                        <th>Date Added</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>NASA POWER</td>
                        <td>Weather</td>
                        <td>20 Apr 2026</td>
                        <td><span style="color: #00ff00;">Processed</span></td>
                    </tr>
                    <tr>
                        <td>GitHub / CropRec</td>
                        <td>Soil</td>
                        <td>19 Apr 2026</td>
                        <td><span style="color: #00ff00;">Processed</span></td>
                    </tr>
                    <tr>
                        <td>Local Sensor A1</td>
                        <td>Live Stream</td>
                        <td>Just Now</td>
                        <td><span style="color: var(--primary);">Analysing...</span></td>
                    </tr>
                </tbody>
            </table>
        </section>
    </main>

    <script>
        // Chart Initialization
        const ctx = document.getElementById('soilChart').getContext('2d');
        const soilChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00'],
                datasets: [{
                    label: 'Nitrogen Levels',
                    data: [45, 52, 48, 60, 55, 58],
                    borderColor: '#00f2fe',
                    tension: 0.4,
                    fill: true,
                    backgroundColor: 'rgba(0, 242, 254, 0.1)'
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.05)' } },
                    x: { grid: { display: false } }
                }
            }
        });

        // Simple Prediction Simulation
        document.getElementById('predictForm').addEventListener('submit', (e) => {
            e.preventDefault();
            const res = document.getElementById('predictionResult');
            const resText = document.getElementById('resText');
            res.style.display = 'block';
            resText.innerText = 'Calculating...';
            setTimeout(() => {
                resText.innerText = 'Nitrogen (N) Predicted: 48.2 mg/kg';
            }, 1500);
        });
    </script>
</body>
</html>
